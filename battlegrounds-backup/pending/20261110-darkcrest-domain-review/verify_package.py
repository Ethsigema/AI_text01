"""Offline verification of this evidence package only. Never loads historical tools."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, io, json, lzma, re, tarfile

EXPECTED_SHA = 'f9c49deb53768cd618f94a202db364a78fa1afe793a9132427214110ec7df480'
FORBIDDEN = {'.git', '.aws', '.ssh', '.codex', 'sessions', 'cookies', 'chats', 'messages', '__pycache__', '.godot', 'cache', 'node_modules'}
SECRET_PATTERNS = [rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', rb'gh[pousr]_[A-Za-z0-9]{30,}', rb'github_pat_[A-Za-z0-9_]{30,}', rb'AKIA[0-9A-Z]{16}', rb'xox[baprs]-[A-Za-z0-9-]{20,}', rb'sk-[A-Za-z0-9]{32,}']

def meta(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def require(ok, why):
    if not ok:
        raise ValueError(why)

def inspect_archive(data):
    require(hashlib.sha256(data).hexdigest() == EXPECTED_SHA, 'original archive SHA256 differs')
    decoder = lzma.LZMADecompressor(memlimit=128 * 1024 * 1024)
    raw = decoder.decompress(data)
    require(decoder.eof and not decoder.unused_data, 'invalid XZ stream')
    root = 'darkcrest_domain_review_20261110T054142Z'
    files, payloads, seen = {}, {}, set()
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:') as tf:
        for m in tf:
            p = PurePosixPath(m.name)
            require(not p.is_absolute() and '..' not in p.parts and str(p) == m.name, 'unsafe path')
            require(m.name not in seen, 'duplicate archive path')
            seen.add(m.name)
            require(not {x.lower() for x in p.parts} & FORBIDDEN and p.suffix not in {'.pyc', '.pyo'}, 'excluded path')
            require(m.isfile() and m.name.startswith(root + '/'), 'only regular files under the fixed root are allowed')
            b = tf.extractfile(m).read()
            require(not any(re.search(pattern, b) for pattern in SECRET_PATTERNS), 'credential signature')
            name = m.name[len(root) + 1:]
            files[name], payloads[name] = meta(b), b
    declared = json.loads(payloads['MANIFEST.json'])
    require(declared == {k: v for k, v in files.items() if k != 'MANIFEST.json'}, 'member whitelist/hash mismatch')
    require(len(files) == 576, 'expected 576 regular files')
    recheck = json.loads(payloads['FINAL_VERIFICATION.json'])
    require(recheck['status'] == 'HELD_UNINSTALLED_SOURCE_AND_CONTENT_FIXTURE_PASS_GAME_NOT_RUN' and recheck['installed'] is False and recheck['assertions'] == 1130, 'gap status differs')
    require(recheck['Game_Waiting_Catalog_Combat_compiler_save_executed'] is False and recheck['prior_regression_assertions'] == 104 and recheck['new_assertions'] == 1026, 'historical execution boundary differs')
    candidate = json.loads(payloads['candidate/FINAL_MANIFEST.json'])['files']
    actual = {name.removeprefix('candidate/'): value for name, value in files.items() if name.startswith('candidate/') and name != 'candidate/FINAL_MANIFEST.json'}
    require(len(candidate) == 477 and candidate == actual, 'candidate technical whitelist differs')
    require(files['candidate/FINAL_MANIFEST.json']['sha256'] == recheck['candidate_manifest_sha256'], 'candidate manifest identity differs')
    require(files['independent_review/FINAL_MANIFEST.json']['sha256'] == recheck['review_manifest_sha256'], 'independent review manifest identity differs')
    return files

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('folder', type=Path)
    p.add_argument('--write-archive', action='store_true')
    p.add_argument('--report', type=Path)
    a = p.parse_args()
    m = json.loads((a.folder / 'MANIFEST.json').read_bytes())
    chunks = []
    for part in m['parts']:
        require(Path(part['name']).name == part['name'], 'unsafe part name')
        b = (a.folder / part['name']).read_bytes()
        require(meta(b) == {k: part[k] for k in ('bytes', 'sha256')}, 'part integrity mismatch')
        chunks.append(b)
    archive = b''.join(chunks)
    require(meta(archive) == {k: m[k] for k in ('bytes', 'sha256')}, 'archive integrity mismatch')
    files = inspect_archive(archive)
    require(files == m['files'], 'external manifest/member mismatch')
    if a.write_archive:
        require(Path(m['archive']).name == m['archive'], 'unsafe archive name')
        out = a.folder / m['archive']
        require(not out.exists(), 'archive output already exists; no overwrite')
        out.write_bytes(archive)
    result = {'status': 'PASS_ARCHIVE_INTEGRITY_ONLY_REAL_DOMAIN_GAME_UNVERIFIED', **meta(archive), 'archive_files': len(files), 'parts': len(chunks), 'all_members_match': True, 'credential_signature_findings': [], 'excluded_path_findings': [], 'dependencies_freshly_downloaded_or_reverified': False, 'prior_cancelled_dependency_download_retried': False, 'source_modified': False, 'historical_modules_executed': False, 'game_rerun': False, 'remaining_gaps': 345, 'candidate_installed': False, 'source_report_assertions': 1130, 'real_Game_Waiting_executed': False, 'complete_chain_recovery_claim': False}
    if a.report:
        a.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
