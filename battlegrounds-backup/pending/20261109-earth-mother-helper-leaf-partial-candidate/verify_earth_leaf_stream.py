#!/usr/bin/env python3
"""Verify the pinned partially validated EarthMother helper leaf candidate by streaming every reconstructed source file. No complete runtime directory is written.

The default downloads are public immutable GitHub URLs. --download-dir accepts
bytes separately fetched from the same pinned commit (for connector-only hosts).
No existing backups, source trees, or downloads are modified. No gameplay runs.
"""
from pathlib import Path, PurePosixPath
import argparse
import io
import datetime
import hashlib
import json
import shutil
import tarfile
import urllib.request

COMMIT = '851466e4964562e8cf172bd40d37a389386fcfdf'
REPO_PATH = 'battlegrounds-backup/pending/20261109-earth-mother-helper-leaf-partial-candidate'
BASE_URL = f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
ARCHIVE_SHA = '333aad27ba8ed0d0699c97cd4a33be5494310247a8350993532cd725f26e753c'
MANIFEST_SHA = 'e6f5562344c7c5ddee0b0cdd6c31684a4b32f570c68e834d9d00145402eb69f7'
BASE_MAP_SHA = '9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111'
TARGET_MAP_SHA = 'd758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960'
BASE_RECEIPT_SHA = 'ba73c82db88ceaedbb57f395da246433deb89d55ddd3ff6296a871c9d03b3cda'
BASE_RECEIPT_URL = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/1288c092b970edaa6a75c2be89809354eed19405/battlegrounds-backup/pending/20261109-native-spell-listener-leaf-partial-candidate/NATIVE_LISTENER_LEAF_PARTIAL_STREAM_VERIFICATION.json'
PACKAGE = 'earth_mother_helper_leaf_partial_candidate_20261109'


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



BASE_MANIFEST_SHA = 'c10934e5554eec684c1ceb287cea81073a1dae45b7195905bb8211d86d6fd06a'
BASE_ARCHIVE_SHA = '46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7'
STATUS = 'PARTIAL_PURE_HELPER_AND_LIGHT_ENTRY_PASS_FULL_HOST_UNVERIFIED'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--historical-baseline', required=True, type=Path, help='Verified complete Harbinger runtime')
    parser.add_argument('--baseline-receipt', type=Path)
    parser.add_argument('--baseline-manifest', type=Path)
    parser.add_argument('--prior-archive', required=True, type=Path, help='Pinned native listener candidate archive')
    parser.add_argument('--download-dir', type=Path)
    parser.add_argument('--output', required=True, type=Path, help='New directory; must not exist')
    args = parser.parse_args()
    baseline, output = args.historical_baseline.resolve(), args.output.resolve()
    require(not output.exists(), 'Output exists; retain it and use a new directory')
    require(output != baseline and baseline not in output.parents, 'Output cannot be in baseline')
    output.mkdir(parents=True)
    fresh = args.download_dir is None
    downloads = args.download_dir.resolve() if args.download_dir else output / 'downloaded'
    if fresh:
        downloads.mkdir()
        get(BASE_URL + 'MANIFEST.json', downloads / 'MANIFEST.json')
    manifest_bytes = (downloads / 'MANIFEST.json').read_bytes()
    require(sha(manifest_bytes) == MANIFEST_SHA, 'Pinned manifest hash mismatch')
    manifest = json.loads(manifest_bytes)
    require(manifest['sha256'] == ARCHIVE_SHA and manifest['bytes'] == 1169808, 'Archive metadata mismatch')
    require(len(manifest['parts']) == 5 and len(manifest['files']) == 79, 'Package counts mismatch')
    names = ['CHANGES.json', 'REMOVALS.json', 'SHA256SUMS.txt', 'README.md', 'RECOVERY.md'] + [p['name'] for p in manifest['parts']]
    require(len(names) == len(set(names)), 'Duplicate download names')
    for name in names:
        require(safe(name) and '/' not in name, 'Unsafe download name')
        if fresh:
            get(BASE_URL + name, downloads / name)
    for name, expected in manifest['companion_files'].items():
        require(safe(name) and '/' not in name, 'Unsafe companion name')
        require(file_meta(downloads / name) == expected, 'Companion mismatch: ' + name)
    changes = read_json(downloads / 'CHANGES.json')
    removals = read_json(downloads / 'REMOVALS.json')
    require(removals == manifest['removed_source_files'] == [], 'Unexpected removals')
    require((downloads / 'SHA256SUMS.txt').read_text().strip() == f'{ARCHIVE_SHA}  {manifest["archive"]}', 'SHA256SUMS mismatch')
    blocks = []
    for part in manifest['parts']:
        body = (downloads / part['name']).read_bytes()
        require(len(body) == part['bytes'] and sha(body) == part['sha256'], 'Part mismatch: ' + part['name'])
        blocks.append(body)
    archive_bytes = b''.join(blocks)
    require(len(archive_bytes) == manifest['bytes'] and sha(archive_bytes) == ARCHIVE_SHA, 'Archive mismatch')
    require(safe(manifest['archive']) and '/' not in manifest['archive'], 'Unsafe archive name')
    archive = output / manifest['archive']
    archive.write_bytes(archive_bytes)
    extracted = output / 'extracted'
    extracted.mkdir()
    members = {}
    with tarfile.open(archive, mode='r:xz') as tar:
        for entry in tar:
            name = entry.name
            require(safe(name) and entry.isfile() and name not in members, 'Unsafe or duplicate member: ' + name)
            require(name in manifest['files'], 'Unlisted member: ' + name)
            body = tar.extractfile(entry).read()
            meta = {'bytes': len(body), 'sha256': sha(body)}
            require(meta == manifest['files'][name], 'Member mismatch: ' + name)
            target = extracted / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as handle:
                handle.write(body)
            members[name] = meta
    require(members == manifest['files'], 'Incomplete package members')
    package = extracted / PACKAGE
    internal_actual = {name.removeprefix(PACKAGE + '/'): value for name, value in members.items() if name != PACKAGE + '/PACKAGE_MANIFEST.json'}
    require(read_json(package / 'PACKAGE_MANIFEST.json') == internal_actual and len(internal_actual) == 78, 'Internal manifest mismatch')
    print('PASS: 5 pinned archive parts, assembled archive and all 79 members', flush=True)
    packed = read_json(package / 'CHANGES.json')
    result = read_json(package / 'RESULT.json')
    require(manifest['status'] == result['status'] == STATUS and manifest['partial_validation_only'] is True, 'Partial scope marker mismatch')
    require(manifest['promote_over_verified_baseline'] is result['verified_gameplay_baseline_promoted'] is False, 'Candidate cannot promote baseline')
    require(result['full_Game_run'] is result['full_catalog_compiled'] is result['full_EndTurn_host_compiled'] is result['save_or_replay_run'] is result['old_save_fingerprint_compatibility_preserved'] is False, 'Game/save unverified markers missing')
    require(result['failed_harness_runs_excluded'] == ['earth'], 'Invalid failed report not excluded')
    require(result['input_commit'] == manifest['depends_on']['recovery_commit'] == '1288c092b970edaa6a75c2be89809354eed19405', 'Input commit mismatch')
    require(manifest['depends_on']['archive_sha256'] == BASE_ARCHIVE_SHA, 'Input archive mismatch')
    base_bytes = (package / 'BASE_MAP.json').read_bytes()
    target_bytes = (package / 'SOURCE_MAP.json').read_bytes()
    require(sha(base_bytes) == BASE_MAP_SHA and sha(target_bytes) == TARGET_MAP_SHA, 'Pinned map mismatch')
    base_map, target_map = json.loads(base_bytes), json.loads(target_bytes)
    require(len(base_map) == 27895 and len(target_map) == 27896, 'Source counts mismatch')
    for name in set(base_map) | set(target_map):
        require(safe(name), 'Unsafe source path: ' + name)
    receipt_bytes = args.baseline_receipt.read_bytes() if args.baseline_receipt else get(BASE_RECEIPT_URL, output / 'PINNED_INPUT_RECEIPT.json')
    dep_bytes = args.baseline_manifest.read_bytes() if args.baseline_manifest else get(BASE_RECEIPT_URL.rsplit('/', 1)[0] + '/MANIFEST.json', output / 'PINNED_INPUT_MANIFEST.json')
    require(sha(receipt_bytes) == BASE_RECEIPT_SHA and sha(dep_bytes) == BASE_MANIFEST_SHA, 'Pinned dependency metadata mismatch')
    prior, dependency = json.loads(receipt_bytes), json.loads(dep_bytes)
    require(prior['status'] == 'PASS_EXACT_STREAMED_SOURCE_ONLY' and prior['source_map_sha256'] == BASE_MAP_SHA and prior['archive_sha256'] == BASE_ARCHIVE_SHA, 'Prior input receipt mismatch')
    require(prior['prior_chain_to_harbinger_leaf_to_native_listener_map_continuity'] is True and prior['full_game_validation_passed'] is False and prior['complete_runtime_directory_created'] is False, 'Input continuity/scope mismatch')
    require(dependency['sha256'] == BASE_ARCHIVE_SHA and dependency['removed_source_files'] == [], 'Input metadata mismatch')
    require(file_meta(args.prior_archive)['sha256'] == BASE_ARCHIVE_SHA, 'Reused input archive mismatch')
    prior_package = 'native_spell_listener_leaf_partial_candidate_20261109'
    prior_members, prior_payload = {}, {}
    with tarfile.open(args.prior_archive) as tar:
        for entry in tar:
            require(safe(entry.name) and entry.isfile() and entry.name not in prior_members and entry.name in dependency['files'], 'Unsafe prior member')
            body = tar.extractfile(entry).read()
            prior_members[entry.name] = {'bytes': len(body), 'sha256': sha(body)}
            require(prior_members[entry.name] == dependency['files'][entry.name], 'Prior member mismatch')
            if entry.name.startswith(prior_package + '/delta/') or entry.name in [prior_package + '/BASE_MAP.json', prior_package + '/SOURCE_MAP.json']:
                prior_payload[entry.name] = body
    require(prior_members == dependency['files'] and len(prior_members) == 247, 'Incomplete prior archive')
    require(prior_payload[prior_package + '/SOURCE_MAP.json'] == base_bytes, 'Direct input map discontinuity')
    historical_map_bytes = prior_payload[prior_package + '/BASE_MAP.json']
    require(sha(historical_map_bytes) == 'e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe', 'Historical Harbinger map mismatch')
    historical_map = json.loads(historical_map_bytes)
    prior_delta = {name.removeprefix(prior_package + '/delta/'): body for name, body in prior_payload.items() if name.startswith(prior_package + '/delta/')}
    prior_delta_meta = {name: {'bytes': len(body), 'sha256': sha(body)} for name, body in prior_delta.items()}
    require(len(prior_delta) == 5 and {**historical_map, **prior_delta_meta} == base_map, 'Prior delta composition mismatch')
    baseline_before = inventory(baseline)
    compare(baseline_before, historical_map, 'historical Harbinger baseline before')
    compare({**baseline_before, **prior_delta_meta}, base_map, 'composed direct input actual byte hashes')
    print('PASS: 27,893 historical files plus 5 prior delta payloads, composing exact 27,895-file input', flush=True)
    delta = inventory(package / 'delta')
    actual_delta = {name: meta for name, meta in target_map.items() if base_map.get(name) != meta}
    require(delta == actual_delta and len(delta) == 4, 'New delta not exact source difference')
    expected = {'added': sorted(set(target_map) - set(base_map)), 'modified': sorted(name for name in set(base_map) & set(target_map) if base_map[name] != target_map[name]), 'removed': sorted(set(base_map) - set(target_map))}
    require(changes == expected == {'added': ['core/exact_value_identity.gd'], 'modified': ['core/catalog.gd', 'core/earth_mother_sources.gd', 'core/end_turn_repeats.gd'], 'removed': []}, 'Change list mismatch')
    expected_packed = [{'path': name, 'status': 'added' if name in changes['added'] else 'modified', 'before': base_map.get(name), 'after': target_map[name]} for name in delta]
    require(sorted(packed, key=lambda row: row['path']) == sorted(expected_packed, key=lambda row: row['path']), 'Archived change details mismatch')
    require(removals == read_json(package / 'REMOVALS.json') == [], 'Removal mismatch')
    require({**base_map, **delta} == target_map, 'Input plus new delta not target')
    require(sum(v['bytes'] for v in target_map.values()) == 1548719422 and sum(v['bytes'] for v in target_map.values()) - sum(v['bytes'] for v in base_map.values()) == 367, 'Source bytes mismatch')
    for name in changes['modified']:
        require(file_meta(package / 'before' / name) == base_map[name], 'Archived before file mismatch')
    disk_before = shutil.disk_usage(output).free
    reconstructed, origins = {}, {'historical_tree': 0, 'prior_archive_delta': 0, 'fresh_new_delta': 0}
    aggregate = hashlib.sha256()
    for name in sorted(target_map):
        if name in delta:
            source = package / 'delta' / name
            handle, origin = source.open('rb'), 'fresh_new_delta'
        elif name in prior_delta:
            handle, origin = io.BytesIO(prior_delta[name]), 'prior_archive_delta'
        else:
            source = baseline / name
            require(source.is_file() and not source.is_symlink(), 'Invalid historical source')
            handle, origin = source.open('rb'), 'historical_tree'
        digest, count = hashlib.sha256(), 0
        aggregate.update(name.encode('utf-8') + b'\0' + str(target_map[name]['bytes']).encode('ascii') + b'\0')
        with handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b''):
                digest.update(chunk)
                aggregate.update(chunk)
                count += len(chunk)
        reconstructed[name] = {'bytes': count, 'sha256': digest.hexdigest()}
        require(reconstructed[name] == target_map[name], 'Actual reconstructed bytes mismatch: ' + name)
        origins[origin] += 1
    compare(reconstructed, target_map, 'complete streamed target')
    require(origins == {'historical_tree': 27887, 'prior_archive_delta': 5, 'fresh_new_delta': 4}, 'Source origins mismatch')
    compare(inventory(baseline), baseline_before, 'historical baseline after stream')
    require(file_meta(args.prior_archive)['sha256'] == BASE_ARCHIVE_SHA, 'Prior archive changed during stream')
    (output / 'STREAM_RECONSTRUCTED_SOURCE_MAP.json').write_text(json.dumps(reconstructed, indent=2, sort_keys=True) + '\n')
    receipt = {
        'status': 'PASS_EXACT_STREAMED_SOURCE_ONLY', 'candidate_status': STATUS,
        'partial_validation_only': True, 'promote_over_verified_baseline': False,
        'full_game_validation_passed': False, 'full_host_compilation_verified': False,
        'save_compatibility_verified': False, 'old_save_fingerprint_compatibility_preserved': False,
        'gameplay_test_run_by_verifier': False,
        'archive_commit': COMMIT, 'repository_path': REPO_PATH, 'manifest_sha256': MANIFEST_SHA,
        'archive': manifest['archive'], 'archive_sha256': ARCHIVE_SHA, 'archive_bytes': len(archive_bytes),
        'parts_verified': 5, 'members_verified': 79, 'internal_manifest_members_verified': 78,
        'increment_bytes_freshly_downloaded_by_this_helper': fresh,
        'increment_input_mode': 'fresh immutable GitHub URLs' if fresh else 'pre-fetched pinned bytes; see FETCH_PROVENANCE.json for actual download evidence',
        'input_verified_commit': '1288c092b970edaa6a75c2be89809354eed19405',
        'input_archive_sha256': BASE_ARCHIVE_SHA, 'input_archive_rehashed': True,
        'input_archive_members_reverified': 247,
        'input_manifest_sha256': BASE_MANIFEST_SHA, 'input_receipt_sha256': BASE_RECEIPT_SHA,
        'historical_full_tree_files_rehashed': len(historical_map),
        'historical_full_tree_source_map_sha256': sha(historical_map_bytes),
        'direct_input_files_verified_by_actual_byte_hashes': len(base_map),
        'direct_input_bytes': sum(v['bytes'] for v in base_map.values()),
        'input_source_map_sha256': BASE_MAP_SHA, 'source_map_sha256': TARGET_MAP_SHA,
        'change_lists': changes, 'new_files': 1, 'modified_files': 3, 'removed_files': 0, 'new_delta_files': 4,
        'actual_target_bytes_streamed': sum(v['bytes'] for v in reconstructed.values()),
        'target_files_streamed_and_verified': len(reconstructed), 'stream_source_origins': origins,
        'aggregate_stream_sha256': aggregate.hexdigest(),
        'aggregate_stream_format': 'Sorted UTF-8 target path, NUL, ASCII file byte count, NUL, actual file bytes; repeat for every target file.',
        'reconstructed_map_sha256': file_meta(output / 'STREAM_RECONSTRUCTED_SOURCE_MAP.json')['sha256'],
        'complete_runtime_directory_created': False, 'source_file_copy_performed': False,
        'verification_mode': 'Actual per-file byte reconstruction from reused verified Harbinger tree, reused pinned native listener archive delta, and freshly downloaded EarthMother delta.',
        'free_disk_bytes_before_stream': disk_before, 'free_disk_bytes_after_stream': shutil.disk_usage(output).free,
        'missing_files': [], 'mismatched_files': [], 'unexpected_files': [],
        'historical_baseline_and_prior_archive_unchanged': True,
        'historical_chain_freshly_downloaded_this_round': False,
        'prior_chain_to_native_listener_to_earth_helper_map_continuity': True,
        'implementation_scope': 'Source bytes only. No full runtime directory, new gameplay tests, save compatibility, replay or acceptance upgrade.',
        'all_prior_backups_preserved': True, 'no_deletion_performed': True,
        'verified_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (output / 'EARTH_MOTHER_HELPER_PARTIAL_STREAM_VERIFICATION.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2), flush=True)

if __name__ == '__main__':
    main()
