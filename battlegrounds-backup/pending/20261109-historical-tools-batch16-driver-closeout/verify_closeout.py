"""Read-only byte verifier for the separate driver-closeout evidence archive."""
from pathlib import Path, PurePosixPath
import argparse, concurrent.futures, hashlib, io, json, lzma, re, tarfile, urllib.request

PIN = '58518fbc71c1af43e609e2f4b1ab3fd42dcb96491d156864dceec2ed3d799990'
FORBIDDEN = {'.git', '.aws', '.ssh', '.codex', 'sessions', 'cookies', 'chats', 'messages', '__pycache__', '.godot', 'cache', 'node_modules'}
PATTERNS = [rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', rb'gh[pousr]_[A-Za-z0-9]{30,}', rb'github_pat_[A-Za-z0-9_]{30,}', rb'AKIA[0-9A-Z]{16}', rb'xox[baprs]-[A-Za-z0-9-]{20,}', rb'sk-[A-Za-z0-9]{32,}']

def require(ok, detail):
    if not ok:
        raise ValueError(detail)

def meta(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def dump(p, v):
    p.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')

def safe(name):
    p = PurePosixPath(name)
    require(str(p) == name and not p.is_absolute() and '..' not in p.parts, 'unsafe path')
    require(not {x.lower() for x in p.parts} & FORBIDDEN and p.suffix not in {'.pyc', '.pyo'}, 'excluded path')

def archive_check(data, manifest):
    require(meta(data) == {k: manifest[k] for k in ('bytes', 'sha256')}, 'archive mismatch')
    decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    raw = decoder.decompress(data)
    require(decoder.eof and not decoder.unused_data, 'truncated or multiple XZ streams')
    prefix = manifest['archive'].removesuffix('.tar.xz')
    members, contents, seen, dirs = {}, {}, set(), []
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:') as tf:
        for m in tf:
            safe(m.name)
            require(m.name not in seen, 'duplicate archive member')
            seen.add(m.name)
            require(m.name == prefix or m.name.startswith(prefix + '/'), 'wrong archive root')
            if m.isdir():
                dirs.append(m.name)
                continue
            require(m.isfile(), 'links and special files are forbidden')
            b = tf.extractfile(m).read()
            require(not any(re.search(p, b) for p in PATTERNS), 'credential signature found')
            members[m.name] = meta(b)
            contents[m.name[len(prefix) + 1:]] = b
    require(members == manifest['files'], 'archive member set/hash mismatch')
    if 'directories' in manifest:
        require(dirs == manifest['directories'], 'directory list mismatch')
    if 'FILES_SHA256.json' in contents:
        inside = json.loads(contents['FILES_SHA256.json'])
        if 'files' in inside:
            require(inside['count'] == len(inside['files']), 'internal count mismatch')
            inside = {x['path']: {k: x[k] for k in ('bytes', 'sha256')} for x in inside['files']}
        require(inside == {k: meta(v) for k, v in contents.items() if k != 'FILES_SHA256.json'}, 'internal manifest mismatch')
    else:
        inside = json.loads(contents['FILE_MANIFEST.json'])
        require(inside == {k: meta(v) for k, v in contents.items() if k != 'FILE_MANIFEST.json'}, 'source internal manifest mismatch')
        white = json.loads(contents['FILE_WHITELIST.json'])['files']
        require(len(white) == len(set(white)) and set(white) == set(inside), 'source whitelist mismatch')
    return contents, members

def local(folder):
    m = json.loads((folder / 'MANIFEST.json').read_bytes())
    require(m['sha256'] == PIN, 'original closeout archive changed')
    c, entries = archive_check((folder / m['archive']).read_bytes(), m)
    require(len(entries) == 34 and set(c) == set(m['file_whitelist']), 'exact 34-file whitelist mismatch')
    require(not any(k.startswith(('candidate/', 'delta/')) for k in c), 'unexpected source candidate')
    return m, c, {'status': 'PASS_EXACT_READONLY_CLOSEOUT_ARCHIVE', 'archive_sha256': PIN, 'archive_files_verified': len(entries), 'original_archive_unchanged': True, 'credential_signature_findings': [], 'private_or_cache_archive_paths': []}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--local', type=Path)
    p.add_argument('--commit')
    p.add_argument('--folder')
    p.add_argument('--manifest-sha256')
    p.add_argument('--out', type=Path)
    args = p.parse_args()
    if args.local:
        print(json.dumps(local(args.local)[2], indent=2))
        return
    require(all((args.commit, args.folder, args.manifest_sha256, args.out)), 'remote inputs missing')
    require(not args.out.exists(), 'use a new output directory')
    args.out.mkdir(parents=True)
    downloads = []
    def fetch(commit, folder, name, dest, expected=None):
        require(re.fullmatch('[0-9a-f]{40}', commit) is not None, 'fixed commit required')
        safe(folder)
        safe(name)
        u = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/' + commit + '/' + folder + '/' + name
        with urllib.request.urlopen(u, timeout=90) as response:
            b = response.read()
        if expected:
            require(meta(b) == {k: expected[k] for k in ('bytes', 'sha256')}, 'download mismatch: ' + name)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(b)
        downloads.append({'url': u, **meta(b)})
        return b
    raw = fetch(args.commit, args.folder, 'MANIFEST.json', args.out / 'closeout/MANIFEST.json')
    require(meta(raw)['sha256'] == args.manifest_sha256, 'closeout manifest pin mismatch')
    m = json.loads(raw)
    fetch(args.commit, args.folder, m['archive'], args.out / 'closeout' / m['archive'], m)
    _, closeout, result = local(args.out / 'closeout')
    restored = args.out / 'restored_evidence'
    restored.mkdir()
    for name, b in closeout.items():
        safe(name)
        dest = restored / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(b)
        require(dest.read_bytes() == b, 'evidence extraction readback mismatch')
    require(len([x for x in restored.rglob('*') if x.is_file()]) == 34, 'restored evidence count mismatch')
    print('PASS: fresh closeout archive and all 34 extracted evidence files', flush=True)
    dependencies = []
    for label in ('xml_candidate', 'source_batch14'):
        dep = m['dependencies'][label]
        dest = args.out / label
        b = fetch(dep['commit'], dep['folder'], 'MANIFEST.json', dest / 'MANIFEST.json')
        require(meta(b)['sha256'] == dep['manifest_sha256'], 'dependency manifest pin mismatch')
        dm = json.loads(b)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            parts = list(pool.map(lambda part: fetch(dep['commit'], dep['folder'], part['name'], dest / part['name'], part), dm['parts']))
        data = b''.join(parts)
        require(meta(data)['sha256'] == dep['archive_sha256'], 'dependency archive pin mismatch')
        c, files = archive_check(data, dm)
        dependencies.append({'role': label, 'commit': dep['commit'], 'archive_sha256': meta(data)['sha256'], 'parts': len(parts), 'members': len(files), 'freshly_downloaded': True})
        if label == 'xml_candidate':
            require(meta(c['candidate/evidence/portable_legacy/CardDefs.Bacon_latest.xml']) == {'bytes': 15824602, 'sha256': 'c385e3d67bfc2c52408059fbb0399b41164c8d1b78d3dd1619a6fb1882116690'}, 'XML identity mismatch')
        else:
            require(meta(c['SOURCE_MAP.json'])['sha256'] == dep['source_map_sha256'], 'source map pin mismatch')
            source = json.loads(c['SOURCE_MAP.json'])
            pins = json.loads(closeout['FINAL_STATE_PIN_CHECK.json'])
            for runtime in pins['runtimes']:
                for name, record in runtime['selected_source_hashes_match_prior_static_audit'].items():
                    require(source[name] == record, 'closeout source pin disagrees with fixed source map')
        print('PASS: fresh ' + label + ' archive and every member', flush=True)
    xml = m['dependencies']['xml_candidate']
    for f in xml['verified_reports']:
        fetch(xml['commit'], xml['folder'], f['name'], args.out / 'xml_candidate' / f['name'], f)
    prior = json.loads((args.out / 'xml_candidate/REMOTE_RESTORE_VERIFIED.json').read_bytes())
    require(prior['status'] == 'PASS_FRESH_DOWNLOAD_AND_ISOLATED_BYTE_RESTORE_ONLY' and prior['restored_tree']['files'] == 27921 and not prior['installed_in_existing_runtime'], 'unexpected prior XML verification state')
    result.update({'status': 'PASS_FRESH_CLOSEOUT_AND_PINNED_DEPENDENCY_ARCHIVES', 'commit': args.commit, 'folder': args.folder, 'manifest_sha256': args.manifest_sha256, 'evidence_files_actually_restored_and_read_back': 34, 'dependencies': dependencies, 'downloads': sorted(downloads, key=lambda x: x['url']), 'closeout_separate_from_xml_candidate': True, 'source_code_changes': {'added': [], 'modified': [], 'removed': []}, 'unique_current_driver_known': False, 'driver_restored': False, 'missing_source_contracts': 2, 'remaining_original_tool_reference_gaps': 345, 'prior_XML_tree_restoration_receipt_reused_not_rerun': True, 'historical_chain_rerun': False, 'historical_audit_scripts_rerun': False, 'runtime_tree_rehashed_this_closeout_backup': False, 'full_compiler_game_or_save_tests_run': False, 'full_game_verified': False, 'old_save_compatibility_verified': False, 'all_prior_backups_retained': True})
    dump(args.out / 'REMOTE_CLOSEOUT_VERIFIED.json', result)
    print(json.dumps({k: v for k, v in result.items() if k != 'downloads'}, indent=2))

if __name__ == '__main__':
    main()
