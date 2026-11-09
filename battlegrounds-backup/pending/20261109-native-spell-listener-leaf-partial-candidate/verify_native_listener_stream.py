#!/usr/bin/env python3
"""Verify the pinned partially validated native spell listener leaf candidate by streaming every reconstructed source file. No complete runtime directory is written.

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

COMMIT = '8056893fcb4181431e1bbd8a8866dfb2b2932df3'
REPO_PATH = 'battlegrounds-backup/pending/20261109-native-spell-listener-leaf-partial-candidate'
BASE_URL = f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
ARCHIVE_SHA = '46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7'
MANIFEST_SHA = 'c10934e5554eec684c1ceb287cea81073a1dae45b7195905bb8211d86d6fd06a'
BASE_MAP_SHA = 'e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe'
TARGET_MAP_SHA = '9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111'
BASE_RECEIPT_SHA = 'a6d29ead3af28eb40c81bcc7b7a23a56ea5fb0f85c38125262e5b717c2bd14dc'
BASE_RECEIPT_URL = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/26679da39e12f73907a9d15c325ca4028daf8474/battlegrounds-backup/pending/20261109-harbinger-identity-leaf-candidate/HARBINGER_IDENTITY_LEAF_CANDIDATE_REMOTE_VERIFICATION.json'
PACKAGE = 'native_spell_listener_leaf_partial_candidate_20261109'


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



BASE_MANIFEST_SHA = '180d5ebba796ffa9cde4a4afe2814604cba823a9bd5856f09bbf45cc8ca8ce1c'
BASE_ARCHIVE_SHA = 'b666e972100a402ae3b9fa92ab2126e5324f4327842ac88fecebcc204c6f4ee4'
STATUS = 'PARTIAL_PURE_VALIDATION_AND_CANDIDATE_STOCK_PASS_ORIGINAL_HOST_BLOCKED'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-dir', required=True, type=Path)
    parser.add_argument('--baseline-source-map', required=True, type=Path)
    parser.add_argument('--baseline-receipt', type=Path)
    parser.add_argument('--baseline-manifest', type=Path)
    parser.add_argument('--baseline-archive', type=Path)
    parser.add_argument('--download-dir', type=Path)
    parser.add_argument('--output', required=True, type=Path, help='New directory; must not exist')
    args = parser.parse_args()
    baseline, output = args.baseline_dir.resolve(), args.output.resolve()
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
    require(manifest['sha256'] == ARCHIVE_SHA and manifest['bytes'] == 1155064, 'Archive metadata mismatch')
    require(len(manifest['parts']) == 5 and len(manifest['files']) == 247, 'Package counts mismatch')
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
    require(read_json(package / 'PACKAGE_MANIFEST.json') == internal_actual and len(internal_actual) == 246, 'Internal manifest mismatch')
    print('PASS: 5 pinned archive parts, assembled archive and all 247 members', flush=True)
    packed = read_json(package / 'CHANGES.json')
    result = read_json(package / 'RESULT.json')
    require(manifest['status'] == packed['status'] == result['status'] == STATUS, 'Experimental scope missing')
    require(manifest['promote_over_verified_baseline'] is packed['promote_over_verified_baseline'] is False, 'Candidate may not replace accepted baseline')
    require(result['full_catalog_or_Game_verified'] is result['full_host_compilation_verified'] is result['promote_over_verified_baseline'] is result['memory_savings_percentage_claimed'] is False, 'Partial validation markers mismatch')
    require(result['original_full_stock_attempt']['exit'] == -9 and result['original_full_stock_attempt']['completed'] is False, 'Original entry SIGKILL disclosure mismatch')
    require(packed['input_commit'] == manifest['depends_on']['recovery_commit'] == '26679da39e12f73907a9d15c325ca4028daf8474', 'Input commit mismatch')
    require(packed['immediate_base_archive_sha256'] == manifest['depends_on']['archive_sha256'] == BASE_ARCHIVE_SHA, 'Input archive mismatch')
    base_bytes = args.baseline_source_map.read_bytes()
    require(sha(base_bytes) == BASE_MAP_SHA and base_bytes == (package / 'BASE_MAP.json').read_bytes(), 'Baseline map continuity mismatch')
    target_bytes = (package / 'SOURCE_MAP.json').read_bytes()
    require(sha(target_bytes) == TARGET_MAP_SHA, 'Target map mismatch')
    base_map, target_map = json.loads(base_bytes), json.loads(target_bytes)
    require(len(base_map) == 27893 and len(target_map) == 27895, 'Source counts mismatch')
    for name in set(base_map) | set(target_map):
        require(safe(name), 'Unsafe source path: ' + name)
    receipt_bytes = args.baseline_receipt.read_bytes() if args.baseline_receipt else get(BASE_RECEIPT_URL, output / 'PINNED_BASELINE_RECEIPT.json')
    dep_bytes = args.baseline_manifest.read_bytes() if args.baseline_manifest else get(BASE_RECEIPT_URL.rsplit('/', 1)[0] + '/MANIFEST.json', output / 'PINNED_BASELINE_MANIFEST.json')
    require(sha(receipt_bytes) == BASE_RECEIPT_SHA and sha(dep_bytes) == BASE_MANIFEST_SHA, 'Pinned baseline metadata mismatch')
    prior, dependency = json.loads(receipt_bytes), json.loads(dep_bytes)
    require(prior['status'] == 'PASS_EXACT_SOURCE_ONLY' and prior['source_map_sha256'] == BASE_MAP_SHA and prior['archive_sha256'] == BASE_ARCHIVE_SHA, 'Baseline receipt mismatch')
    require(prior['prior_chain_to_catalog_memory_to_harbinger_leaf_map_continuity'] is True and prior['full_game_validation_passed'] is False, 'Baseline continuity or scope mismatch')
    require(dependency['sha256'] == BASE_ARCHIVE_SHA and dependency['files']['harbinger_identity_leaf_candidate_20261109/SOURCE_MAP.json'] == {'bytes': len(base_bytes), 'sha256': BASE_MAP_SHA}, 'Dependency archive/map linkage mismatch')
    if args.baseline_archive:
        require(file_meta(args.baseline_archive)['sha256'] == BASE_ARCHIVE_SHA, 'Baseline archive mismatch')
    baseline_before = inventory(baseline)
    compare(baseline_before, base_map, 'baseline before restore')
    print('PASS: all 27,893 reused baseline files independently rehashed', flush=True)
    delta = inventory(package / 'delta')
    actual_delta = {name: meta for name, meta in target_map.items() if base_map.get(name) != meta}
    require(delta == actual_delta and len(delta) == 5, 'Delta not exact source difference')
    expected = {'added': sorted(set(target_map) - set(base_map)), 'modified': sorted(name for name in set(base_map) & set(target_map) if base_map[name] != target_map[name]), 'removed': sorted(set(base_map) - set(target_map))}
    require(changes == expected == {'added': ['core/spell_listener_source_proof.gd', 'research/spell_listener_source_leaf/provider_revision.json'], 'modified': ['core/native_spell_listener_stock.gd', 'core/patch_3702_azerite_sources.gd', 'core/spell_cast_listeners.gd'], 'removed': []}, 'Change lists mismatch')
    require(packed['added'] == [{'path': name, 'after': target_map[name]} for name in changes['added']], 'Added details mismatch')
    require(packed['modified'] == [{'path': name, 'before': base_map[name], 'after': target_map[name]} for name in changes['modified']], 'Modified details mismatch')
    require(packed['deleted'] == removals == read_json(package / 'REMOVALS.json') == [], 'Removal lists mismatch')
    require({**base_map, **delta} == target_map, 'Baseline plus delta not target')
    require(sum(v['bytes'] for v in target_map.values()) == 1548719055 and sum(v['bytes'] for v in target_map.values()) - sum(v['bytes'] for v in base_map.values()) == 4533, 'Source bytes mismatch')
    disk_before = shutil.disk_usage(output).free
    reconstructed = {}
    aggregate = hashlib.sha256()
    baseline_origins = delta_origins = 0
    for name in sorted(target_map):
        source = package / 'delta' / name if name in delta else baseline / name
        require(source.is_file() and not source.is_symlink(), 'Invalid stream input: ' + name)
        digest, count = hashlib.sha256(), 0
        aggregate.update(name.encode('utf-8') + b'\0' + str(target_map[name]['bytes']).encode('ascii') + b'\0')
        with source.open('rb') as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b''):
                digest.update(chunk)
                aggregate.update(chunk)
                count += len(chunk)
        reconstructed[name] = {'bytes': count, 'sha256': digest.hexdigest()}
        require(reconstructed[name] == target_map[name], 'Reconstructed actual byte mismatch: ' + name)
        if name in delta:
            delta_origins += 1
        else:
            baseline_origins += 1
    compare(reconstructed, target_map, 'independently streamed target file bytes')
    require(delta_origins == 5 and baseline_origins == 27890, 'Source origin counts mismatch')
    compare(inventory(baseline), baseline_before, 'baseline after stream reconstruction')
    (output / 'STREAM_RECONSTRUCTED_SOURCE_MAP.json').write_text(json.dumps(reconstructed, indent=2, sort_keys=True) + '\n')
    receipt = {
        'status': 'PASS_EXACT_STREAMED_SOURCE_ONLY', 'candidate_status': STATUS,
        'partial_validation_only': True, 'promote_over_verified_baseline': False,
        'full_game_validation_passed': False, 'full_host_compilation_verified': False,
        'original_stock_probe_exit': -9, 'gameplay_test_run_by_verifier': False,
        'archive_commit': COMMIT, 'repository_path': REPO_PATH, 'manifest_sha256': MANIFEST_SHA,
        'archive': manifest['archive'], 'archive_sha256': ARCHIVE_SHA, 'archive_bytes': len(archive_bytes),
        'parts_verified': 5, 'members_verified': 247, 'internal_manifest_members_verified': 246,
        'increment_bytes_freshly_downloaded_by_this_helper': fresh,
        'increment_input_mode': 'fresh immutable GitHub URLs' if fresh else 'pre-fetched pinned bytes; see FETCH_PROVENANCE.json for actual download evidence',
        'baseline_verified_commit': '26679da39e12f73907a9d15c325ca4028daf8474',
        'baseline_archive_sha256': BASE_ARCHIVE_SHA, 'baseline_archive_rehashed': args.baseline_archive is not None,
        'baseline_manifest_sha256': BASE_MANIFEST_SHA, 'baseline_receipt_sha256': BASE_RECEIPT_SHA,
        'baseline_files_rehashed': len(base_map), 'baseline_bytes': sum(v['bytes'] for v in base_map.values()),
        'baseline_source_map_sha256': BASE_MAP_SHA, 'source_map_sha256': TARGET_MAP_SHA,
        'change_lists': changes, 'new_files': 2, 'modified_files': 3, 'removed_files': 0, 'delta_files': 5,
        'actual_source_bytes_streamed': sum(v['bytes'] for v in reconstructed.values()),
        'target_files_streamed_and_verified': len(reconstructed),
        'stream_sources_from_reused_baseline': baseline_origins,
        'stream_sources_from_fresh_remote_delta': delta_origins,
        'aggregate_stream_sha256': aggregate.hexdigest(),
        'aggregate_stream_format': 'For each target path in sorted order: UTF-8 path, NUL, ASCII byte count, NUL, then all actual file bytes.',
        'reconstructed_map_sha256': file_meta(output / 'STREAM_RECONSTRUCTED_SOURCE_MAP.json')['sha256'],
        'complete_runtime_directory_created': False, 'source_file_copy_performed': False,
        'verification_mode': 'Actual per-file bytes streamed independently from pinned baseline plus freshly downloaded delta; no second full runtime written.',
        'free_disk_bytes_before_stream': disk_before, 'free_disk_bytes_after_stream': shutil.disk_usage(output).free,
        'missing_files': [], 'mismatched_files': [], 'unexpected_files': [],
        'baseline_unchanged_after_stream': True,
        'historical_baseline_freshly_downloaded_this_round': False,
        'historical_baseline_provenance': 'Reused previously independently restored Harbinger identity leaf candidate; every file rehashed before and after byte-stream reconstruction. Historical archive chain is reused, not downloaded again.',
        'prior_chain_to_harbinger_leaf_to_native_listener_map_continuity': True,
        'implementation_scope': 'Exact streamed source-byte recovery only. No complete runtime directory, gameplay acceptance or rerun of archived probes.',
        'all_prior_backups_preserved': True, 'no_deletion_performed': True,
        'verified_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (output / 'NATIVE_LISTENER_LEAF_PARTIAL_STREAM_VERIFICATION.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2), flush=True)

if __name__ == '__main__':
    main()
