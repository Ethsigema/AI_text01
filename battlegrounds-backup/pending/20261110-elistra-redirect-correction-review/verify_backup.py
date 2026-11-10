"""Offline byte verification only; never executes archived code or downloads dependencies."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, io, json, lzma, re, tarfile
ARCHIVE = 'elistra_redirect_correction_review_20261110T021700Z.tar.xz'
SHA = '0d743ad1e5c15305adccf46032276ab59dc09fb034d6ca3bc2525a6555c2da5f'
FORBIDDEN = {'.git', '.aws', '.ssh', '.codex', 'sessions', 'cookies', 'chats', 'messages', '__pycache__', '.godot', 'cache', 'node_modules'}
SECRETS = [rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', rb'gh[pousr]_[A-Za-z0-9]{30,}', rb'github_pat_[A-Za-z0-9_]{30,}', rb'AKIA[0-9A-Z]{16}', rb'xox[baprs]-[A-Za-z0-9-]{20,}', rb'sk-[A-Za-z0-9]{32,}']
def meta(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
def require(ok, why):
    if not ok:
        raise ValueError(why)
def inspect_archive(b):
    require(meta(b) == {'bytes': 182164, 'sha256': SHA}, 'archive identity mismatch')
    dec = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    raw = dec.decompress(b)
    require(dec.eof and not dec.unused_data, 'invalid XZ stream')
    root, records, contents, seen = ARCHIVE.removesuffix('.tar.xz'), {}, {}, set()
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:') as tf:
        for m in tf:
            p = PurePosixPath(m.name)
            require(not p.is_absolute() and '..' not in p.parts and str(p) == m.name, 'unsafe path')
            require(m.name not in seen and m.isfile() and m.name.startswith(root + '/'), 'unexpected member')
            seen.add(m.name)
            require(not {x.lower() for x in p.parts} & FORBIDDEN and p.suffix not in {'.pyc', '.pyo'}, 'excluded path')
            data = tf.extractfile(m).read()
            require(not any(re.search(s, data) for s in SECRETS), 'credential signature')
            name = m.name[len(root) + 1:]
            records[name], contents[name] = meta(data), data
    require(len(records) == 130, 'expected 130 members')
    require(json.loads(contents['FILES_SHA256.json'])['files'] == {k: v for k, v in records.items() if k != 'FILES_SHA256.json'}, 'internal whitelist/hash mismatch')
    r = json.loads(contents['FINAL_VERIFICATION.json'])
    require(r['remaining_tools_missing'] == 345 and r['new_candidate_installed'] is False and r['xml_candidate_not_installed'] is True and r['no_game_full_driver_combat_or_save_run'] is True, 'review boundary mismatch')
    result = json.loads(contents['VERIFIED_RESULTS.json'])
    require(result['unchanged_hook_pre_call_exceptions'] == 8 and result['installed'] is False and result['game_or_save_acceptance'] is False and result['candidate_sha256'] == '5117ad6bf7e755be6063d3538aa541e6633ca1091e163e247a5427a06c74e2ab', 'candidate/boundary mismatch')
    require(meta(contents['candidate/tools/elistra_redirect_patterns.py'])['sha256'] == result['candidate_sha256'], 'candidate bytes mismatch')
    return records
def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('folder', type=Path)
    p.add_argument('--report', type=Path)
    a = p.parse_args()
    b = (a.folder / ARCHIVE).read_bytes()
    records = inspect_archive(b)
    require(records == json.loads((a.folder / 'MANIFEST.json').read_bytes())['files'], 'external manifest mismatch')
    r = {'status': 'PASS_THIS_EXACT_ELISTRA_CORRECTION_REVIEW_ONLY', 'archive': ARCHIVE, **meta(b), 'members_verified': len(records), 'candidate_installation_deferred': True, 'remaining_reference_gaps': 345, 'source_tree_modified': False, 'archived_code_executed_in_backup': False, 'game_or_save_accepted': False, 'dependencies_reverified': False, 'cancelled_dependency_download_retried': False, 'excluded_path_findings': [], 'common_credential_signature_findings': []}
    if a.report:
        a.report.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(r, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
