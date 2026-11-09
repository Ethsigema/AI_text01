#!/usr/bin/env python3
"""Verify combined read-only diagnostics and 41 selected input files without executing probes.
The historical base and input archive are reused; this is not a full runtime rehash.

The default downloads are public immutable GitHub URLs. --download-dir accepts
bytes separately fetched from the same pinned commit (for connector-only hosts).
No existing backups, source trees, or downloads are modified. No gameplay runs.
"""
from pathlib import Path, PurePosixPath
import argparse
import datetime
import hashlib
import json
import shutil
import tarfile
import urllib.request

COMMIT = '3bc00aebf6ae235d819c2f9ad9fb0a71fcd2b1eb'
REPO_PATH = 'battlegrounds-backup/pending/20261109-combined-leaf-readonly-diagnostic'
BASE_URL = f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
ARCHIVE_SHA = '41d8059e6a5db3e1c7de4f9acc7396537dc7f9b6a5902dea75cd7988ed5978c3'
MANIFEST_SHA = 'ab1f60ba0f392253c8105fbe33780abe79896c29da375d0437128dad339a1159'
INPUT_MAP_SHA = '9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111'
INPUT_ARCHIVE_SHA = '46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7'
INPUT_MANIFEST_SHA = 'c10934e5554eec684c1ceb287cea81073a1dae45b7195905bb8211d86d6fd06a'
INPUT_RECEIPT_SHA = 'ba73c82db88ceaedbb57f395da246433deb89d55ddd3ff6296a871c9d03b3cda'
INPUT_URL = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/1288c092b970edaa6a75c2be89809354eed19405/battlegrounds-backup/pending/20261109-native-spell-listener-leaf-partial-candidate/'
PACKAGE = 'combined_leaf_readonly_diagnostic_20261109'
INPUT_PACKAGE = 'native_spell_listener_leaf_partial_candidate_20261109'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_meta(path):
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return {'bytes': path.stat().st_size, 'sha256': digest.hexdigest()}


def safe(name):
    p = PurePosixPath(name)
    return bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name and str(p) == name.rstrip('/')


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def inventory(root):
    require(root.is_dir() and not root.is_symlink(), 'Invalid tree root')
    result = {}
    for path in sorted(root.rglob('*')):
        require(not path.is_symlink(), f'Symlink rejected: {path}')
        if path.is_file():
            result[path.relative_to(root).as_posix()] = file_meta(path)
        else:
            require(path.is_dir(), f'Special file rejected: {path}')
    return result


def compare(actual, expected, label):
    missing = sorted(set(expected) - set(actual))
    unexpected = sorted(set(actual) - set(expected))
    mismatched = sorted(name for name in set(actual) & set(expected) if actual[name] != expected[name])
    require(not missing and not unexpected and not mismatched,
            json.dumps({'tree': label, 'missing': missing, 'unexpected': unexpected, 'mismatched': mismatched}))


def get(url, target):
    with urllib.request.urlopen(url, timeout=120) as response:
        body = response.read()
    with target.open('xb') as handle:
        handle.write(body)
    return body


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--historical-baseline', required=True, type=Path, help='Previously verified complete Harbinger runtime')
    parser.add_argument('--input-archive', required=True, type=Path, help='Previously downloaded native listener candidate archive')
    parser.add_argument('--input-manifest', type=Path)
    parser.add_argument('--input-receipt', type=Path)
    parser.add_argument('--download-dir', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    output, baseline = args.output.resolve(), args.historical_baseline.resolve()
    require(not output.exists() and output != baseline and baseline not in output.parents, 'New output must be outside baseline')
    require(baseline.is_dir() and not args.historical_baseline.is_symlink(), 'Invalid baseline')
    output.mkdir(parents=True)
    fresh = args.download_dir is None
    downloads = args.download_dir.resolve() if args.download_dir else output / 'downloaded'
    if fresh:
        downloads.mkdir()
        get(BASE_URL + 'MANIFEST.json', downloads / 'MANIFEST.json')
    manifest_bytes = (downloads / 'MANIFEST.json').read_bytes()
    require(sha(manifest_bytes) == MANIFEST_SHA, 'Pinned diagnostic manifest mismatch')
    manifest = json.loads(manifest_bytes)
    require(manifest['sha256'] == ARCHIVE_SHA and manifest['bytes'] == 78984 and len(manifest['parts']) == 1 and len(manifest['files']) == 38, 'Diagnostic metadata mismatch')
    require(manifest['kind'] == 'diagnostic-evidence-only' and manifest['is_runtime_increment'] is False, 'Evidence-only marker missing')
    names = list(manifest['companion_files']) + [part['name'] for part in manifest['parts']]
    require(len(names) == len(set(names)) == 6, 'Download list mismatch')
    for name in names:
        require(safe(name) and '/' not in name, 'Unsafe download name')
        if fresh:
            get(BASE_URL + name, downloads / name)
    for name, metadata in manifest['companion_files'].items():
        require(file_meta(downloads / name) == metadata, 'Companion mismatch: ' + name)
    changes = read_json(downloads / 'CHANGES.json')
    require(changes == manifest['runtime_changes'] == {'added': [], 'modified': [], 'removed': []}, 'Runtime changes mismatch')
    require(read_json(downloads / 'REMOVALS.json') == manifest['removed_source_files'] == [], 'Unexpected removals')
    require((downloads / 'SHA256SUMS.txt').read_text().strip() == f'{ARCHIVE_SHA}  {manifest["archive"]}', 'SHA256SUMS mismatch')
    part = manifest['parts'][0]
    archive = (downloads / part['name']).read_bytes()
    require(len(archive) == part['bytes'] == 78984 and sha(archive) == part['sha256'] == ARCHIVE_SHA, 'Archive/part mismatch')
    require(safe(manifest['archive']) and '/' not in manifest['archive'], 'Unsafe archive name')
    archive_path = output / manifest['archive']
    archive_path.write_bytes(archive)
    extracted = output / 'extracted'
    extracted.mkdir()
    actual, payload = {}, {}
    with tarfile.open(archive_path) as tar:
        for entry in tar:
            require(safe(entry.name) and entry.isfile() and entry.name not in actual, 'Unsafe or duplicate member')
            require(entry.name in manifest['files'], 'Unlisted member')
            body = tar.extractfile(entry).read()
            metadata = {'bytes': len(body), 'sha256': sha(body)}
            require(metadata == manifest['files'][entry.name], 'Member mismatch: ' + entry.name)
            target = extracted / entry.name
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as handle:
                handle.write(body)
            actual[entry.name], payload[entry.name] = metadata, body
    require(actual == manifest['files'], 'Missing archive members')
    package = extracted / PACKAGE
    internal = read_json(package / 'PACKAGE_MANIFEST.json')
    require(internal == {name.removeprefix(PACKAGE + '/'): metadata for name, metadata in actual.items() if name != PACKAGE + '/PACKAGE_MANIFEST.json'} and len(internal) == 37, 'Internal manifest mismatch')
    require(not any(name.startswith(PACKAGE + '/' + part + '/') for name in actual for part in ['delta', 'patch', 'runtime', 'core']), 'Unexpected runtime payload')
    result = read_json(package / 'RESULT.json')
    require(result['status'] == 'PASS_SCOPED_COMBINED_ENTRY_DIAGNOSTICS_ONLY' and result['input_commit'] == '1288c092b970edaa6a75c2be89809354eed19405', 'Result input/status mismatch')
    require(result['runtime_added'] == result['runtime_modified'] == result['runtime_deleted'] == 0 and result['input_source_map_sha256'] == INPUT_MAP_SHA, 'Zero-change or input map mismatch')
    require(result['full_catalog_or_Game_run'] is result['heavy_hosts_loaded'] is result['previous_partial_acceptance_status_upgraded'] is result['whole_program_memory_reduction_proven'] is False, 'Diagnostic scope mismatch')
    print('PASS: pinned diagnostic archive and all 38 members; runtime changes 0', flush=True)
    dep_bytes = args.input_manifest.read_bytes() if args.input_manifest else get(INPUT_URL + 'MANIFEST.json', output / 'PINNED_INPUT_MANIFEST.json')
    receipt_bytes = args.input_receipt.read_bytes() if args.input_receipt else get(INPUT_URL + 'NATIVE_LISTENER_LEAF_PARTIAL_STREAM_VERIFICATION.json', output / 'PINNED_INPUT_RECEIPT.json')
    require(sha(dep_bytes) == INPUT_MANIFEST_SHA and sha(receipt_bytes) == INPUT_RECEIPT_SHA, 'Pinned dependency metadata mismatch')
    dependency, prior = json.loads(dep_bytes), json.loads(receipt_bytes)
    require(dependency['sha256'] == prior['archive_sha256'] == INPUT_ARCHIVE_SHA and prior['source_map_sha256'] == INPUT_MAP_SHA, 'Dependency linkage mismatch')
    require(prior['status'] == 'PASS_EXACT_STREAMED_SOURCE_ONLY' and prior['full_game_validation_passed'] is False and prior['complete_runtime_directory_created'] is False, 'Prior receipt scope mismatch')
    require(file_meta(args.input_archive)['sha256'] == INPUT_ARCHIVE_SHA, 'Reused input archive mismatch')
    dep_actual, dep_payload = {}, {}
    with tarfile.open(args.input_archive) as tar:
        for entry in tar:
            require(safe(entry.name) and entry.isfile() and entry.name not in dep_actual and entry.name in dependency['files'], 'Unsafe dependency member')
            body = tar.extractfile(entry).read()
            dep_actual[entry.name] = {'bytes': len(body), 'sha256': sha(body)}
            require(dep_actual[entry.name] == dependency['files'][entry.name], 'Dependency member mismatch')
            if entry.name.startswith(INPUT_PACKAGE + '/delta/') or entry.name in [INPUT_PACKAGE + '/SOURCE_MAP.json', INPUT_PACKAGE + '/BASE_MAP.json']:
                dep_payload[entry.name] = body
    require(dep_actual == dependency['files'], 'Missing dependency members')
    source_bytes = dep_payload[INPUT_PACKAGE + '/SOURCE_MAP.json']
    require(sha(source_bytes) == INPUT_MAP_SHA, 'Input source map mismatch')
    source_map = json.loads(source_bytes)
    old_map = json.loads(dep_payload[INPUT_PACKAGE + '/BASE_MAP.json'])
    selected = read_json(package / 'TEST_INPUT_MAP.json')
    require(len(selected) == 41 and sum(v['bytes'] for v in selected.values()) == 366179, 'Selected input counts mismatch')
    selected_actual, origins = {}, {}
    for name, expected in selected.items():
        require(safe(name) and source_map.get(name) == expected, 'Diagnostic input not pinned: ' + name)
        delta_name = INPUT_PACKAGE + '/delta/' + name
        if delta_name in dep_payload:
            body, origin = dep_payload[delta_name], 'reused pinned native listener archive delta'
        else:
            require(old_map.get(name) == expected, 'Baseline input does not match dependency base map')
            source = baseline / name
            cursor = source
            while cursor != baseline:
                require(not cursor.is_symlink(), 'Symlink in selected baseline input')
                cursor = cursor.parent
            require(source.is_file(), 'Missing selected baseline input')
            body, origin = source.read_bytes(), 'reused previously independently restored Harbinger baseline'
        actual_meta = {'bytes': len(body), 'sha256': sha(body)}
        require(actual_meta == expected, 'Actual selected input mismatch: ' + name)
        selected_actual[name], origins[name] = actual_meta, origin
    compare(selected_actual, selected, 'selected actual input bytes')
    reports, count = {}, 0
    for mode, record in result['fresh_processes'].items():
        report_bytes = (package / mode / 'report.json').read_bytes()
        require(sha(report_bytes) == record['report_sha256'], 'Archived report hash mismatch')
        report = json.loads(report_bytes)
        process = read_json(package / mode / 'PROCESS.json')
        launch = read_json(package / mode / 'LAUNCH.json')
        require(process['exit'] == 0 and process['mode'] == mode and process['maxrss_kib'] == record['maxrss_kib'], 'Archived process mismatch')
        require(len(report['checks']) == record['checks'] and all(c['passed'] is True for c in report['checks']), 'Archived checks mismatch')
        require(process['test_input_map_sha256'] == launch['test_input_map_sha256'] == file_meta(package / 'TEST_INPUT_MAP.json')['sha256'], 'Process input pin mismatch')
        require(process['gate_sha256'] == launch['gate_sha256'] == file_meta(package / mode / 'gate_executed.gd')['sha256'] == file_meta(package / 'gate.gd')['sha256'], 'Process script pin mismatch')
        require(process['fixture_sha256'] == launch['fixture_sha256'] == file_meta(package / 'STOCK_FIXTURE.json')['sha256'], 'Process fixture pin mismatch')
        count += len(report['checks'])
        reports[mode] = report
    require(len(reports) == 4 and count == result['total_checks'] == 47, 'Archived run/check counts mismatch')
    for mode in ['harbinger_then_stock', 'stock_then_harbinger']:
        require(reports[mode]['results']['harbinger'] == reports['harbinger_only']['results']['harbinger'] and reports[mode]['results']['stock'] == reports['stock_only']['results']['stock'], 'Archived order comparison mismatch')
    for name, origin in origins.items():
        if origin.startswith('reused previously'):
            require(file_meta(baseline / name) == selected[name], 'Selected historical input changed during verification')
    require(file_meta(args.input_archive)['sha256'] == INPUT_ARCHIVE_SHA, 'Reused input archive changed')
    (output / 'SELECTED_INPUT_VERIFICATION.json').write_text(json.dumps({name: {**selected_actual[name], 'origin': origins[name]} for name in sorted(selected)}, indent=2) + '\n')
    receipt = {
        'status': 'PASS_DIAGNOSTIC_BYTES_AND_SELECTED_INPUTS', 'diagnostic_only': True,
        'archive_commit': COMMIT, 'repository_path': REPO_PATH, 'archive_sha256': ARCHIVE_SHA,
        'archive_bytes': len(archive), 'manifest_sha256': MANIFEST_SHA,
        'parts_verified': 1, 'members_verified': 38, 'internal_manifest_members_verified': 37,
        'runtime_changes': changes, 'input_verified_commit': '1288c092b970edaa6a75c2be89809354eed19405',
        'input_archive_sha256': INPUT_ARCHIVE_SHA, 'input_archive_rehashed': True,
        'reused_input_archive_members_verified': len(dep_actual),
        'input_manifest_sha256': INPUT_MANIFEST_SHA, 'input_receipt_sha256': INPUT_RECEIPT_SHA,
        'input_source_map_sha256': INPUT_MAP_SHA, 'selected_input_files_rehashed': 41,
        'selected_input_bytes_rehashed': 366179,
        'selected_inputs_from_archive_delta': sum('archive delta' in origin for origin in origins.values()),
        'selected_inputs_from_historical_baseline': sum('Harbinger baseline' in origin for origin in origins.values()),
        'selected_baseline_inputs_and_input_archive_unchanged': True,
        'archived_report_process_script_fixture_consistency_verified': True,
        'archived_processes_checked': 4, 'archived_passed_checks_checked': 47,
        'diagnostic_download_by_this_helper': fresh,
        'download_mode': 'fresh immutable URLs' if fresh else 'pre-fetched pinned bytes; see FETCH_PROVENANCE.json',
        'historical_chain_freshly_downloaded_this_round': False,
        'entire_runtime_rehashed_this_round': False, 'new_runtime_directory_created': False,
        'diagnostic_probes_run_by_verifier': False, 'gameplay_test_run': False,
        'full_game_acceptance': False, 'previous_partial_acceptance_upgraded': False,
        'missing_or_mismatched_selected_inputs': [], 'all_prior_backups_preserved': True,
        'no_deletion_performed': True, 'verified_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (output / 'COMBINED_DIAGNOSTIC_REMOTE_VERIFICATION.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2), flush=True)

if __name__ == '__main__':
    main()
