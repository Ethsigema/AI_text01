"""Verify only the Imperial Defender review archive; never execute its code."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, io, json, lzma, re, tarfile

ARCHIVE = 'imperial_defender_candidate_review_20261109T220940Z.tar.xz'
SHA = '19750c8aa7ad3117befab977d8dd338fbb934d5ed5c958cf373a52e71e54bde0'
FORBIDDEN = {'.git', '.aws', '.ssh', '.codex', 'sessions', 'cookies', 'chats', 'messages', '__pycache__', '.godot', 'cache', 'node_modules'}
SECRETS = [rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', rb'gh[pousr]_[A-Za-z0-9]{30,}', rb'github_pat_[A-Za-z0-9_]{30,}', rb'AKIA[0-9A-Z]{16}', rb'xox[baprs]-[A-Za-z0-9-]{20,}', rb'sk-[A-Za-z0-9]{32,}']

def meta(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def require(ok, why):
    if not ok:
        raise ValueError(why)

def inspect_archive(b):
    require(meta(b) == {'bytes': 104588, 'sha256': SHA}, 'original archive identity mismatch')
    decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    raw = decoder.decompress(b)
    require(decoder.eof and not decoder.unused_data, 'invalid XZ stream')
    root = ARCHIVE.removesuffix('.tar.xz')
    records, contents, seen = {}, {}, set()
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:') as tf:
        for m in tf:
            p = PurePosixPath(m.name)
            require(not p.is_absolute() and '..' not in p.parts and str(p) == m.name, 'unsafe archive path')
            require(m.name not in seen and m.isfile() and m.name.startswith(root + '/'), 'unexpected member type/path')
            seen.add(m.name)
            require(not {x.lower() for x in p.parts} & FORBIDDEN and p.suffix not in {'.pyc', '.pyo'}, 'excluded path')
            data = tf.extractfile(m).read()
            require(not any(re.search(pattern, data) for pattern in SECRETS), 'credential signature')
            name = m.name[len(root) + 1:]
            records[name], contents[name] = meta(data), data
    internal = json.loads(contents['PACKAGE_FILES_SHA256.json'])
    require(internal == {k: v for k, v in records.items() if k != 'PACKAGE_FILES_SHA256.json'}, 'internal whitelist/hash mismatch')
    require(len(records) == 57, 'expected 57 regular members')
    final = json.loads(contents['FINAL_VERIFICATION.json'])
    require(final['candidate_not_installed'] is True, 'candidate installation boundary differs')
    require(final['key_identity_counterexamples_to_universal_equivalence'] == 3, 'known mapping differences changed')
    require(final['game_full_catalog_save_tested'] is False, 'game acceptance boundary differs')
    require(records['candidate/tools/imperial_defender_patterns.py']['sha256'] == final['candidate_sha256'] == 'bf3fffeaa2efe948fda69fe88b829f07353713e753de6a7e21cc093748c86a3b', 'candidate pin differs')
    return records

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('folder', type=Path)
    p.add_argument('--report', type=Path)
    a = p.parse_args()
    b = (a.folder / ARCHIVE).read_bytes()
    records = inspect_archive(b)
    manifest = json.loads((a.folder / 'MANIFEST.json').read_bytes())
    require(records == manifest['files'], 'external manifest mismatch')
    result = {'status': 'PASS_EXACT_REVIEW_ARCHIVE_ONLY', 'archive': ARCHIVE, **meta(b), 'members_verified': len(records), 'candidate_installation_deferred': True, 'known_mapping_counterexamples': 3, 'remaining_reference_gaps': 345, 'source_tree_modified_in_backup': False, 'historical_tests_rerun_in_backup': False, 'game_or_save_accepted': False, 'dependencies_reverified': False, 'cancelled_dependency_download_retried': False, 'excluded_path_findings': [], 'common_credential_signature_findings': []}
    if a.report:
        a.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
