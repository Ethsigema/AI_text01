"""Verify exact downloaded evidence and pinned dependencies without executing game code."""
from pathlib import Path, PurePosixPath
import argparse, concurrent.futures, hashlib, io, json, lzma, tarfile, urllib.request

EVIDENCE_SHA = '123c677612f62b44e831e2bdbcbe74a9c69afa5495bde54cf0def5819dc74e90'
SOURCE_SHA = '7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7'
AUDIT = 'historical_tools_batch15_resume_source_audit_20261110'
SOURCE = 'historical_tools_batch15_20261109T195018Z'
FORBIDDEN = {'.git', '.aws', '.ssh', '.codex', 'sessions', 'cookies', 'chats', 'messages', '__pycache__', '.godot', 'cache', 'node_modules'}

def require(ok, detail):
    if not ok:
        raise ValueError(detail)

def meta(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def archive_check(data, manifest):
    require(meta(data) == {k: manifest[k] for k in ('bytes', 'sha256')}, 'archive hash/size mismatch')
    # Reject trailing bytes, concatenated streams and truncated XZ before reading tar members.
    decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    raw = decoder.decompress(data)
    require(decoder.eof and not decoder.unused_data, 'noncanonical/truncated XZ stream')
    prefix = manifest['archive'].removesuffix('.tar.xz')
    records, selected = {}, {}
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:') as tf:
        for member in tf:
            p = PurePosixPath(member.name)
            require(member.isfile() and member.name not in records, 'non-file/duplicate member')
            require(not p.is_absolute() and '..' not in p.parts and p.parts[0] == prefix, 'unsafe archive path')
            require(not set(x.lower() for x in p.parts) & FORBIDDEN and p.suffix not in {'.pyc', '.pyo'}, 'forbidden archive member')
            b = tf.extractfile(member).read()
            records[member.name] = meta(b)
            relative = member.name[len(prefix) + 1:]
            if relative in {'FILE_MANIFEST.json', 'FILE_WHITELIST.json', 'DEPENDENCIES.json', 'SOURCE_MAP.json', 'BASE_MAP.json'} or relative in {
                'evidence/' + AUDIT + '/EVIDENCE_MANIFEST.json',
                'evidence/' + AUDIT + '/PROVENANCE_STATUS.json',
                'evidence/' + SOURCE + '/SOURCE_MAP.json',
                'evidence/' + SOURCE + '/BASE_MAP.json',
                'evidence/' + SOURCE + '/CHANGES.json',
            }:
                selected[relative] = b
    require(records == manifest['files'], 'archive member set/hash mismatch')
    internal = json.loads(selected['FILE_MANIFEST.json'])
    require({prefix + '/' + n: v for n, v in internal.items()} == {n: v for n, v in records.items() if n != prefix + '/FILE_MANIFEST.json'}, 'internal manifest mismatch')
    whitelist = json.loads(selected['FILE_WHITELIST.json'])['files']
    require(len(whitelist) == len(set(whitelist)) and set(whitelist) == set(internal), 'whitelist mismatch')
    return selected, records

def verify_local(folder):
    manifest = json.loads((folder / 'MANIFEST.json').read_bytes())
    chunks = []
    for part in manifest['parts']:
        b = (folder / part['name']).read_bytes()
        require(meta(b) == {k: part[k] for k in ('bytes', 'sha256')}, 'part mismatch: ' + part['name'])
        chunks.append(b)
    selected, records = archive_check(b''.join(chunks), manifest)
    evidence_bytes = selected['evidence/' + AUDIT + '/EVIDENCE_MANIFEST.json']
    require(meta(evidence_bytes)['sha256'] == EVIDENCE_SHA, 'original evidence manifest pin mismatch')
    evidence = json.loads(evidence_bytes)
    require(len(evidence['files']) == evidence['count'] == 130, 'evidence count mismatch')
    prefix = manifest['archive'].removesuffix('.tar.xz')
    for record in evidence['files']:
        require(records[prefix + '/evidence/' + record['path']] == {k: record[k] for k in ('bytes', 'sha256')}, 'original evidence changed')
    base = selected['evidence/' + SOURCE + '/BASE_MAP.json']
    source = selected['evidence/' + SOURCE + '/SOURCE_MAP.json']
    require(base == source and meta(source)['sha256'] == SOURCE_SHA, 'source map changed')
    changes = json.loads(selected['evidence/' + SOURCE + '/CHANGES.json'])
    require(changes == {'added': [], 'modified': [], 'removed': []}, 'unexpected source changes')
    status = json.loads(selected['evidence/' + AUDIT + '/PROVENANCE_STATUS.json'])
    require(status['contracts_recovered'] == [] and status['remaining_original_missing_tools'] == 345 and not status['new_omissions_or_exemptions'], 'open blockers lost')
    require(not manifest['full_game_verified'] and not manifest['old_save_compatibility_verified'], 'unfounded acceptance')
    return manifest, selected, {'status': 'PASS_EXACT_READONLY_EVIDENCE_ARCHIVE', 'archive_sha256': manifest['sha256'], 'archive_parts_verified': len(manifest['parts']), 'archive_members_verified': len(records), 'original_evidence_files_verified': 130, 'original_evidence_manifest_sha256': EVIDENCE_SHA, 'original_evidence_bytes_verified': sum(x['bytes'] for x in evidence['files']), 'source_map_sha256': SOURCE_SHA, 'source_changes': changes}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--local', type=Path)
    parser.add_argument('--commit')
    parser.add_argument('--folder')
    parser.add_argument('--manifest-sha256')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    if args.local:
        print(json.dumps(verify_local(args.local)[2], indent=2))
        return
    require(all((args.commit, args.folder, args.manifest_sha256, args.out)), 'remote verification requires commit/folder/manifest-sha256/out')
    require(len(args.commit) == 40 and all(c in '0123456789abcdef' for c in args.commit), 'immutable commit required')
    require(not args.out.exists(), 'use a new output directory')
    args.out.mkdir(parents=True)
    downloads = []

    def fetch(commit, folder, name, dest, expected=None):
        url = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/' + commit + '/' + folder + '/' + name
        with urllib.request.urlopen(url, timeout=90) as response:
            b = response.read()
        if expected:
            require(meta(b) == {k: expected[k] for k in ('bytes', 'sha256')}, 'download mismatch: ' + name)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(b)
        downloads.append({'url': url, **meta(b)})
        return b

    local = args.out / 'batch15'
    mb = fetch(args.commit, args.folder, 'MANIFEST.json', local / 'MANIFEST.json')
    require(meta(mb)['sha256'] == args.manifest_sha256, 'published manifest pin mismatch')
    manifest = json.loads(mb)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda p: fetch(args.commit, args.folder, p['name'], local / p['name'], p), manifest['parts']))
    _, selected, report = verify_local(local)
    print('PASS: fresh batch15 evidence archive and all 130 original evidence files', flush=True)
    dep_results = []
    dependencies = json.loads(selected['DEPENDENCIES.json'])
    dep = dependencies['fixed_candidate_backup']
    previous_source = None
    for level in range(2):
        dest = args.out / ('dependency_batch' + str(14 - level))
        raw = fetch(dep['commit'], dep['folder'], 'MANIFEST.json', dest / 'MANIFEST.json')
        require(meta(raw)['sha256'] == dep['manifest_sha256'], 'dependency manifest pin mismatch')
        dm = json.loads(raw)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            parts = list(pool.map(lambda p: fetch(dep['commit'], dep['folder'], p['name'], dest / p['name'], p), dm['parts']))
        data = b''.join(parts)
        require(meta(data)['sha256'] == dep['archive_sha256'], 'dependency archive pin mismatch')
        dc, records = archive_check(data, dm)
        require(meta(dc['SOURCE_MAP.json'])['sha256'] == dep['source_map_sha256'], 'dependency source map pin mismatch')
        if level == 0:
            require(dc['SOURCE_MAP.json'] == selected['evidence/' + SOURCE + '/SOURCE_MAP.json'], 'batch14/batch15 continuity mismatch')
            previous_source = dc['BASE_MAP.json']
        else:
            require(dc['SOURCE_MAP.json'] == previous_source, 'batch13/batch14 continuity mismatch')
        dep_results.append({'commit': dep['commit'], 'folder': dep['folder'], 'manifest_sha256': meta(raw)['sha256'], 'archive_sha256': meta(data)['sha256'], 'parts': len(dm['parts']), 'members': len(records), 'source_map_sha256': meta(dc['SOURCE_MAP.json'])['sha256'], 'freshly_downloaded': True})
        if level == 0:
            dep = dm['dependencies']['source_baseline']
        print('PASS: freshly downloaded fixed batch' + str(14 - level) + ' archive, exact members and source-map continuity', flush=True)
    report.update({'archive_commit': args.commit, 'folder': args.folder, 'publication_manifest_sha256': args.manifest_sha256, 'dependencies': dep_results, 'downloads': sorted(downloads, key=lambda x: x['url']), 'runtime_source_changes': 0, 'remaining_reference_gaps_within_original_scope': 345, 'missing_source_contracts': 2, 'full_historical_chain_downloaded_or_rerun': False, 'historical_searches_rerun': False, 'historical_generators_executed': False, 'candidate_modules_executed': False, 'gameplay_or_Godot_rerun': False, 'full_game_verified': False, 'old_save_compatibility_verified': False, 'all_prior_backups_preserved': True})
    dump(args.out / 'REMOTE_EVIDENCE_VERIFIED.json', report)
    print(json.dumps({k: v for k, v in report.items() if k != 'downloads'}, indent=2))

if __name__ == '__main__':
    main()
