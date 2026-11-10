"""Offline verification of this evidence package only. Never loads historical tools."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, io, json, lzma, re, tarfile

EXPECTED_SHA = '00097718164f6665867f6ee79d5f033cf99e112f921cfc6b2040ba6760d53a70'
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
    root = 'darkcrest_frost_seafloor_optional_review_20261110T093323Z'
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
    require(len(files) == 908, 'expected 908 regular files')
    recheck = json.loads(payloads['PRESERVATION_AND_OUTCOME.json'])
    require(recheck['status'] == 'NEW_OPTIONAL_HELPER_FIXTURE_PASS_OLD_FAILED_UNCHANGED' and recheck['new_runs'] == 1 and recheck['new_assertions'] == 2810, 'fixture outcome differs')
    require(not recheck['production_modified_or_installed'] and recheck['no_engine_by_sealer'] and not recheck['real_Game_real_delivery_saves_old_dependencies_accepted'], 'acceptance boundary differs')
    process_name = 'new_optional_fixture/tests_frost_seafloor/fixture_result/PROCESS.json'
    trial = json.loads(payloads[process_name])
    require(files[process_name]['sha256'] == recheck['new_process_sha256'], 'process evidence identity differs')
    require(trial['exit'] == 0 and trial['status'] == 'PASS_FROST_SEAFLOOR_OPTIONAL_FIELD_HELPERS_ONLY' and trial['success_marker_present'], 'new local helper status differs')
    require(trial['final_summary']['assertions'] == 2810 and trial['final_summary']['inherited_assertions'] == 1580 and trial['final_summary']['ok'] and trial['final_summary']['failures'] == [], 'new summary differs')
    require(not trial['full_Game_loaded'] and not trial['full_Catalog_loaded'] and not trial['gameplay_executed'], 'full runtime scope differs')
    old = json.loads(payloads['new_optional_fixture/evidence/previous_failed/fixture_result/PROCESS.json'])
    require(old['exit'] == -15 and old['status'] == 'FAILED_OR_CONTROLLED_STOP' and old['final_summary'] is None and not old['success_marker_present'] and old['expected_assertions'] == 2802, 'old failed trial overwritten')
    declared = json.loads(payloads['new_optional_fixture/POST_RUN_PUBLIC_MANIFEST.json'])['files']
    actual = {name.removeprefix('new_optional_fixture/'): value for name, value in files.items() if name.startswith('new_optional_fixture/') and name != 'new_optional_fixture/POST_RUN_PUBLIC_MANIFEST.json'}
    require(len(declared) == 893 and declared == actual, 'new fixture delivery whitelist differs')
    require(files['new_optional_fixture/POST_RUN_PUBLIC_MANIFEST.json']['sha256'] == recheck['new_postrun_manifest_sha256'], 'postrun manifest identity differs')
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
    result = {'status': 'PASS_ARCHIVE_INTEGRITY_ONLY_OPTIONAL_HELPERS_GAME_UNVERIFIED', **meta(archive), 'archive_files': len(files), 'parts': len(chunks), 'all_members_match': True, 'credential_signature_findings': [], 'excluded_path_findings': [], 'dependencies_freshly_downloaded_or_reverified': False, 'prior_cancelled_dependency_download_retried': False, 'source_modified': False, 'historical_modules_executed': False, 'game_rerun': False, 'remaining_gaps': 345, 'candidate_installed': False, 'source_report_assertions': 2810, 'inherited_assertions': 1580, 'old_fixture_failed_preserved': True, 'production_modified_by_new_fixture': False, 'real_Game_Waiting_executed': False, 'complete_chain_recovery_claim': False}
    if a.report:
        a.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
