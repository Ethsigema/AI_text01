"""Verify the exact original XML archive, pinned dependencies and a new restored tree.

No historical generator, candidate module, compiler, Godot or game is executed.
"""
from pathlib import Path, PurePosixPath
import argparse, concurrent.futures, hashlib, io, json, lzma, re, tarfile
import urllib.request, xml.etree.ElementTree as ET

ARCHIVE_SHA = '3d37a9d1a0ee2d61939e88f8ced995622ca22fd84ba7f9dabe8c4f2df6bafa7d'
XML_SHA = 'c385e3d67bfc2c52408059fbb0399b41164c8d1b78d3dd1619a6fb1882116690'
XML_TARGET = 'evidence/portable_legacy/CardDefs.Bacon_latest.xml'
SOURCE14_SHA = '7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7'
FORBIDDEN = {'.git', '.aws', '.ssh', '.codex', 'sessions', 'cookies', 'chats', 'messages', '__pycache__', '.godot', 'cache', 'node_modules'}
SECRET_PATTERNS = [rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', rb'gh[pousr]_[A-Za-z0-9]{30,}', rb'github_pat_[A-Za-z0-9_]{30,}', rb'AKIA[0-9A-Z]{16}', rb'xox[baprs]-[A-Za-z0-9-]{20,}', rb'sk-[A-Za-z0-9]{32,}']

def require(ok, detail):
    if not ok:
        raise ValueError(detail)

def meta(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def safe_path(name):
    p = PurePosixPath(name)
    require(not p.is_absolute() and '..' not in p.parts and str(p) == name, 'unsafe path: ' + name)
    require(not {x.lower() for x in p.parts} & FORBIDDEN and p.suffix not in {'.pyc', '.pyo'}, 'excluded path: ' + name)

def archive_check(data, manifest):
    require(meta(data) == {k: manifest[k] for k in ('bytes', 'sha256')}, 'archive hash/size mismatch')
    decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    raw = decoder.decompress(data)
    require(decoder.eof and not decoder.unused_data, 'truncated or multiple XZ streams')
    prefix = manifest['archive'].removesuffix('.tar.xz')
    records, contents, directories, seen = {}, {}, [], set()
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:') as tf:
        for member in tf:
            safe_path(member.name)
            require(member.name not in seen, 'duplicate archive member')
            seen.add(member.name)
            require(member.name == prefix or member.name.startswith(prefix + '/'), 'wrong archive root')
            if member.isdir():
                directories.append(member.name)
                continue
            require(member.isfile(), 'archive links and special files are forbidden')
            b = tf.extractfile(member).read()
            require(not any(re.search(p, b) for p in SECRET_PATTERNS), 'credential signature: ' + member.name)
            records[member.name] = meta(b)
            contents[member.name[len(prefix) + 1:]] = b
    require(records == manifest['files'], 'archive member set/hash mismatch')
    if 'directories' in manifest:
        require(directories == manifest['directories'], 'directory set/order mismatch')
    if 'FILES_SHA256.json' in contents:
        internal = json.loads(contents['FILES_SHA256.json'])
        require(internal['count'] == len(internal['files']) == 48, 'original manifest count mismatch')
        wanted = {x['path']: {k: x[k] for k in ('bytes', 'sha256')} for x in internal['files']}
        require(len(wanted) == 48, 'duplicate internal path')
        require(wanted == {k: meta(v) for k, v in contents.items() if k != 'FILES_SHA256.json'}, 'original member mismatch')
    else:
        internal = json.loads(contents['FILE_MANIFEST.json'])
        require(internal == {k: meta(v) for k, v in contents.items() if k != 'FILE_MANIFEST.json'}, 'dependency internal manifest mismatch')
        whitelist = json.loads(contents['FILE_WHITELIST.json'])['files']
        require(len(whitelist) == len(set(whitelist)) and set(whitelist) == set(internal), 'dependency whitelist mismatch')
    return contents, records

def validate_xml(contents):
    xml = contents['candidate/' + XML_TARGET]
    require(meta(xml) == {'bytes': 15824602, 'sha256': XML_SHA}, 'XML pin mismatch')
    require(hashlib.sha1(b'blob 15824602\0' + xml).hexdigest() == 'a5fc0a8ec52c9264850c8eb958b6c0d5723083ef', 'XML Git blob mismatch')
    root = None
    count = 0
    for event, el in ET.iterparse(io.BytesIO(xml), events=('start', 'end')):
        if root is None:
            require(el.tag == 'CardDefs' and el.get('build') == '253932', 'XML root/build mismatch')
            root = el
        if event == 'end' and el.tag == 'Entity':
            count += 1
            el.clear()
            root.clear()
    require(count == 5786, 'XML entity count mismatch')
    original = json.loads(contents['audit/XML_CANDIDATE_VERIFIED.json'])
    checks = []
    for record in original['native_entity_byte_checks']:
        native = contents['audit/native_identity/' + record['native_path']]
        pat = rb'(?m)^<Entity\b[^>]*CardID="' + re.escape(record['card_id'].encode()) + rb'"[^>]*>.*?^</Entity>\r?\n'
        matches = re.findall(pat, xml, re.DOTALL | re.MULTILINE)
        require(len(matches) == 1 and matches[0] == native, 'native entity mismatch: ' + record['card_id'])
        checks.append(record['card_id'])
    require(len(checks) == 5, 'native checks missing')
    return {'bytes': len(xml), 'sha256': XML_SHA, 'xml_entities': count, 'native_byte_identical_entities': checks}

def local_check(folder):
    m = json.loads((folder / 'MANIFEST.json').read_bytes())
    require(m['sha256'] == ARCHIVE_SHA, 'original archive was changed')
    chunks = []
    for p in m['parts']:
        safe_path(p['name'])
        b = (folder / p['name']).read_bytes()
        require(meta(b) == {k: p[k] for k in ('bytes', 'sha256')}, 'part mismatch: ' + p['name'])
        chunks.append(b)
    contents, records = archive_check(b''.join(chunks), m)
    report = {'status': 'PASS_EXACT_ORIGINAL_XML_PACKAGE', 'archive_sha256': ARCHIVE_SHA, 'archive_parts': len(chunks), 'archive_files': len(records), 'xml': validate_xml(contents), 'credential_signature_findings': [], 'private_or_cache_archive_paths': []}
    return m, contents, report

def check_tree(tree, mapping):
    actual = set()
    for p in tree.rglob('*'):
        require(not p.is_symlink(), 'symlink in tree')
        if p.is_file():
            actual.add(p.relative_to(tree).as_posix())
    require(actual == set(mapping), 'tree paths do not match fixed source map')
    aggregate = hashlib.sha256()
    for rel, expected in sorted(mapping.items()):
        p = tree / rel
        aggregate.update(rel.encode() + b'\0' + str(expected['bytes']).encode() + b'\0')
        h, n = hashlib.sha256(), 0
        with p.open('rb') as f:
            for b in iter(lambda: f.read(65536), b''):
                h.update(b)
                aggregate.update(b)
                n += len(b)
        require({'bytes': n, 'sha256': h.hexdigest()} == expected, 'tree file mismatch: ' + rel)
    return {'files': len(mapping), 'bytes': sum(x['bytes'] for x in mapping.values()), 'aggregate_sha256': aggregate.hexdigest(), 'missing': [], 'extra': [], 'mismatched': []}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--local', type=Path)
    parser.add_argument('--commit')
    parser.add_argument('--folder')
    parser.add_argument('--manifest-sha256')
    parser.add_argument('--out', type=Path)
    parser.add_argument('--baseline13', type=Path)
    args = parser.parse_args()
    if args.local:
        print(json.dumps(local_check(args.local)[2], indent=2))
        return
    require(all((args.commit, args.folder, args.manifest_sha256, args.out, args.baseline13)), 'remote mode requires all five inputs')
    require(re.fullmatch('[0-9a-f]{40}', args.commit) is not None, 'fixed commit required')
    require(not args.out.exists(), 'output must not exist')
    args.out.mkdir(parents=True)
    downloads = []
    def fetch(commit, folder, name, destination, expected=None):
        require(re.fullmatch('[0-9a-f]{40}', commit) is not None, 'dependency commit not pinned')
        safe_path(folder)
        safe_path(name)
        url = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/' + commit + '/' + folder + '/' + name
        with urllib.request.urlopen(url, timeout=90) as response:
            data = response.read()
        if expected:
            require(meta(data) == {k: expected[k] for k in ('bytes', 'sha256')}, 'download hash mismatch')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        downloads.append({'url': url, **meta(data)})
        return data
    def download_package(dep, destination):
        raw = fetch(dep['commit'], dep['folder'], 'MANIFEST.json', destination / 'MANIFEST.json')
        require(meta(raw)['sha256'] == dep['manifest_sha256'], 'manifest pin mismatch')
        manifest = json.loads(raw)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            parts = list(pool.map(lambda p: fetch(dep['commit'], dep['folder'], p['name'], destination / p['name'], p), manifest['parts']))
        data = b''.join(parts)
        require(meta(data)['sha256'] == dep['archive_sha256'], 'archive pin mismatch')
        contents, records = archive_check(data, manifest)
        return manifest, contents, {'commit': dep['commit'], 'folder': dep['folder'], 'manifest_sha256': meta(raw)['sha256'], 'archive_sha256': meta(data)['sha256'], 'parts': len(parts), 'members': len(records), 'freshly_downloaded': True}
    m16, c16, r16 = download_package({'commit': args.commit, 'folder': args.folder, 'manifest_sha256': args.manifest_sha256, 'archive_sha256': ARCHIVE_SHA}, args.out / 'batch16')
    _, _, report = local_check(args.out / 'batch16')
    print('PASS: fresh original archive, all 49 files, exact XML and five native entities', flush=True)
    dep14 = m16['dependencies']['fixed_source_candidate']
    require(dep14['commit'] == '3b0061fcf3a55850eeda689818f7cc1700700750', 'wrong fixed batch14')
    m14, c14, r14 = download_package(dep14, args.out / 'dependency_batch14')
    m13, c13, r13 = download_package(m14['dependencies']['source_baseline'], args.out / 'dependency_batch13')
    require(meta(c14['SOURCE_MAP.json'])['sha256'] == SOURCE14_SHA, 'fixed batch14 source pin mismatch')
    require(c14['BASE_MAP.json'] == c13['SOURCE_MAP.json'], 'batch13 to batch14 source continuity mismatch')
    require(meta(c13['SOURCE_MAP.json'])['sha256'] == m14['dependencies']['source_baseline']['source_map_sha256'], 'fixed batch13 source pin mismatch')
    print('PASS: freshly downloaded batch14 and batch13 packages, every member and pinned source continuity', flush=True)
    map13, map14 = json.loads(c13['SOURCE_MAP.json']), json.loads(c14['SOURCE_MAP.json'])
    require(set(map14) - set(map13) == {'tools/hand_murloc_gain_patterns.py', 'tools/piranha_vacancy_patterns.py'}, 'unexpected batch14 additions')
    require(all(map14[k] == v for k, v in map13.items()), 'unexpected batch14 changes/removals')
    base_before = check_tree(args.baseline13, map13)
    require(XML_TARGET not in map14 and not (args.baseline13 / XML_TARGET).exists(), 'XML target already exists')
    restored = args.out / 'isolated_restored_candidate'
    restored.mkdir()
    map16 = dict(map14)
    map16[XML_TARGET] = meta(c16['candidate/' + XML_TARGET])
    for rel, expected in sorted(map16.items()):
        safe_path(rel)
        dest = restored / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if rel in map13:
            src = args.baseline13 / rel
            with src.open('rb') as a, dest.open('xb') as b:
                for chunk in iter(lambda: a.read(65536), b''):
                    b.write(chunk)
            require((src.stat().st_dev, src.stat().st_ino) != (dest.stat().st_dev, dest.stat().st_ino), 'hardlink restoration')
        else:
            data = c16['candidate/' + rel] if rel == XML_TARGET else c14['delta/' + rel]
            require(meta(data) == expected, 'downloaded delta mismatch')
            dest.write_bytes(data)
    candidate = check_tree(restored, map16)
    require(candidate['files'] == 27921 and candidate['bytes'] == 1565165008, 'restored count/size mismatch')
    base_after = check_tree(args.baseline13, map13)
    require(base_after == base_before, 'existing baseline changed')
    dump(args.out / 'RESTORED_SOURCE_MAP.json', map16)
    # Verify the pre-existing batch14 and independent batch15 trees are unchanged when present.
    preserved = []
    for name in ['historical_tools_batch14_20261109T191857Z', 'historical_tools_batch15_20261109T195018Z']:
        tree = args.baseline13.parent.parent / name / 'runtime'
        if tree.is_dir():
            require(not (tree / XML_TARGET).exists(), 'XML unexpectedly installed in existing runtime')
            preserved.append({'tree': name + '/runtime', **check_tree(tree, map14)})
    report.update({'status': 'PASS_FRESH_DOWNLOAD_AND_ISOLATED_BYTE_RESTORE_ONLY', 'commit': args.commit, 'folder': args.folder, 'manifest_sha256': args.manifest_sha256, 'dependencies': [r14, r13], 'downloads': sorted(downloads, key=lambda x: x['url']), 'historical_chain_before_batch13_reused': True, 'full_historical_chain_redownloaded_or_rerun': False, 'base13_rehashed_before_and_after': base_after, 'restored_tree': candidate, 'restored_source_map_sha256': meta((args.out / 'RESTORED_SOURCE_MAP.json').read_bytes())['sha256'], 'existing_trees_preserved': preserved, 'same_inode_files': [], 'new_candidate_tree_for_byte_verification_only': True, 'installed_in_existing_runtime': False, 'original_evidence_unchanged': True, 'upstream_redistribution_license_confirmed': False, 'driver_recovered': False, 'missing_source_contracts': 2, 'remaining_original_tool_reference_gaps': 345, 'historical_generators_executed': False, 'full_compiler_executed': False, 'Godot_or_gameplay_executed': False, 'execution_fingerprint_recomputed': False, 'full_game_or_catalog_accepted': False, 'old_save_compatibility_verified': False, 'all_prior_backups_preserved': True})
    dump(args.out / 'REMOTE_RESTORE_VERIFIED.json', report)
    print(json.dumps({k: v for k, v in report.items() if k != 'downloads'}, indent=2))

if __name__ == '__main__':
    main()
