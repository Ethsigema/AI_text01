#!/usr/bin/env python3
"""Verify the pinned Golden Banshee candidate increment (full Game validation remains blocked) and independently restore it.

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

COMMIT = 'c6e62f2af2277b43b139b8049936008772df979d'
REPO_PATH = 'battlegrounds-backup/pending/20261109-hopebringer-banshee-golden-candidate'
BASE_URL = f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
ARCHIVE_SHA = 'a20b6c427a1219903df1d4a927693d3e553a337236f509408eff651318297433'
MANIFEST_SHA = '1491acec3776557780a76aa0b5e88c9e6a356adf21f31bd6c4de3f1ccdd92a38'
BASE_MAP_SHA = '32cd814943a82a4ee79fb05de8a3f4d24d7f74d7b609dd6247aebcd5a4cc7449'
TARGET_MAP_SHA = '45dcd76fe50c5e2e03cea65032189b15cca35894cac08b2e704c17139b7fd6a8'
BASE_RECEIPT_SHA = '95a9eea6be3b1e309e535aabd3936705d7f4d69a27569ab1f357a5a4dea3880d'
BASE_RECEIPT_URL = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/a71d3e4ea64dc52264a3f789a48ddae2e4a043cd/battlegrounds-backup/pending/20261109-hopebringer-summoner-golden/HOPEBRINGER_SUMMONER_GOLDEN_REMOTE_CHAIN_VERIFICATION.json'
PACKAGE = 'hopebringer_banshee_golden_20261109'


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
    parser.add_argument('--baseline-dir', required=True, type=Path)
    parser.add_argument('--baseline-source-map', required=True, type=Path)
    parser.add_argument('--baseline-receipt', type=Path)
    parser.add_argument('--download-dir', type=Path)
    parser.add_argument('--output', required=True, type=Path, help='New directory; must not exist')
    args = parser.parse_args()
    baseline = args.baseline_dir.resolve()
    output = args.output.resolve()
    require(not output.exists(), 'Output already exists; retain it and use another directory')
    require(output != baseline and baseline not in output.parents, 'Output cannot be inside the baseline')
    output.mkdir(parents=True)
    downloads = args.download_dir.resolve() if args.download_dir else output / 'downloaded'
    freshly_downloaded_by_helper = args.download_dir is None
    if freshly_downloaded_by_helper:
        downloads.mkdir()
        get(BASE_URL + 'MANIFEST.json', downloads / 'MANIFEST.json')
    manifest_bytes = (downloads / 'MANIFEST.json').read_bytes()
    require(sha(manifest_bytes) == MANIFEST_SHA, 'Pinned manifest hash mismatch')
    manifest = json.loads(manifest_bytes)
    require(manifest['sha256'] == ARCHIVE_SHA and manifest['bytes'] == 1182008, 'Archive metadata mismatch')
    require(len(manifest['parts']) == 5 and len(manifest['files']) == 109, 'Package count mismatch')
    required_names = ['CHANGES.json', 'REMOVALS.json', 'SHA256SUMS.txt', 'README.md', 'RECOVERY.md']
    required_names += [part['name'] for part in manifest['parts']]
    require(len(required_names) == len(set(required_names)), 'Duplicate download names')
    for name in required_names:
        require(safe(name) and '/' not in name, 'Unsafe download name')
        if freshly_downloaded_by_helper:
            get(BASE_URL + name, downloads / name)
    for name, expected in manifest['companion_files'].items():
        require(safe(name) and '/' not in name, 'Unsafe companion name')
        require(file_meta(downloads / name) == expected, f'Companion mismatch: {name}')
    changes = read_json(downloads / 'CHANGES.json')
    removals = read_json(downloads / 'REMOVALS.json')
    require(removals == manifest['removed_source_files'] == [], 'Unexpected removals')
    require((downloads / 'SHA256SUMS.txt').read_text().strip() == f'{ARCHIVE_SHA}  {manifest["archive"]}', 'SHA256SUMS mismatch')
    blocks = []
    for part in manifest['parts']:
        data = (downloads / part['name']).read_bytes()
        require(len(data) == part['bytes'] and sha(data) == part['sha256'], f'Part mismatch: {part["name"]}')
        blocks.append(data)
    archive_bytes = b''.join(blocks)
    require(len(archive_bytes) == manifest['bytes'] and sha(archive_bytes) == ARCHIVE_SHA, 'Archive mismatch')
    require(safe(manifest['archive']) and '/' not in manifest['archive'], 'Unsafe archive name')
    archive = output / manifest['archive']
    archive.write_bytes(archive_bytes)
    extracted = output / 'extracted'
    extracted.mkdir()
    members = {}
    seen = set()
    with tarfile.open(archive, mode='r:xz') as tar:
        for entry in tar:
            require(safe(entry.name), f'Unsafe member: {entry.name}')
            name = entry.name.rstrip('/')
            require(name not in seen, f'Duplicate member: {name}')
            seen.add(name)
            require(entry.isfile() or entry.isdir(), f'Non-regular member rejected: {name}')
            target = extracted / name
            if entry.isdir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            require(name in manifest['files'], f'Unlisted member: {name}')
            body = tar.extractfile(entry).read()
            meta = {'bytes': len(body), 'sha256': sha(body)}
            require(meta == manifest['files'][name], f'Member mismatch: {name}')
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as handle:
                handle.write(body)
            members[name] = meta
    require(members == manifest['files'], 'Incomplete package members')
    print('PASS: 5 remote parts, assembled archive and all 109 members', flush=True)
    package = extracted / PACKAGE
    validation = read_json(package / 'VALIDATION.json')
    require(manifest['status'] == 'candidate_pending_full_game_validation' and manifest['promote_over_verified_baseline'] is False, 'Candidate marker missing')
    require(validation['status'] == 'PARTIAL_ISOLATED_PASS_FULL_GAME_BLOCKED' and validation['promote_over_verified_baseline'] is False, 'Incorrect validation status')
    require(len(validation['full_attempts']) == 4 and all(attempt['status'] == 'SIGKILL_NO_GAMEPLAY_RESULT' and attempt['process']['exit'] == -9 and attempt['gameplay_report_present'] is False for attempt in validation['full_attempts']), 'Full Game failures not preserved')
    require(validation['passed']['source_and_isolated_combat_checks'] == 20 and validation['passed']['actual_combat_resolutions'] == 2, 'Isolated validation scope mismatch')
    internal_manifest = read_json(package / 'PACKAGE_MANIFEST.json')
    internal_actual = {name.removeprefix(PACKAGE + '/'): value for name, value in members.items() if name != PACKAGE + '/PACKAGE_MANIFEST.json'}
    require(internal_manifest == internal_actual, 'Internal package manifest mismatch')
    baseline_map_bytes = args.baseline_source_map.read_bytes()
    require(sha(baseline_map_bytes) == BASE_MAP_SHA, 'Baseline source map mismatch')
    require(baseline_map_bytes == (package / 'BASE_MAP.json').read_bytes(), 'Baseline map continuity mismatch')
    target_map_bytes = (package / 'SOURCE_MAP.json').read_bytes()
    require(sha(target_map_bytes) == TARGET_MAP_SHA, 'Target source map mismatch')
    base_map = json.loads(baseline_map_bytes)
    target_map = json.loads(target_map_bytes)
    require(len(base_map) == 27889 and len(target_map) == 27892, 'Source file counts mismatch')
    if args.baseline_receipt:
        receipt_bytes = args.baseline_receipt.read_bytes()
    else:
        receipt_bytes = get(BASE_RECEIPT_URL, output / 'PINNED_BASELINE_RECEIPT.json')
    require(sha(receipt_bytes) == BASE_RECEIPT_SHA, 'Pinned baseline receipt mismatch')
    prior = json.loads(receipt_bytes)
    require(prior['status'] == 'PASS_EXACT_SOURCE_ONLY', 'Prior receipt not PASS')
    require(prior['source_map_sha256'] == BASE_MAP_SHA, 'Prior receipt map mismatch')
    require(prior['prior_chain_to_golden_tycoon_to_golden_summoner_map_continuity'] is True, 'Prior chain continuity missing')
    baseline_before = inventory(baseline)
    compare(baseline_before, base_map, 'baseline before restore')
    print('PASS: all 27,889 reused baseline files independently rehashed', flush=True)
    delta = inventory(package / 'delta')
    require(delta == read_json(package / 'SOURCE_DELTA.json')['changes'], 'Delta map mismatch')
    actual_delta = {name: meta for name, meta in target_map.items() if base_map.get(name) != meta}
    require(delta == actual_delta and len(delta) == 8, 'Delta is not the exact source difference')
    expected_changes = {
        'added': sorted(set(target_map) - set(base_map)),
        'modified': sorted(name for name in set(base_map) & set(target_map) if base_map[name] != target_map[name]),
        'removed': sorted(set(base_map) - set(target_map)),
    }
    require(changes == expected_changes, 'Change lists mismatch')
    packed_changes = read_json(package / 'CHANGES.json')
    require(packed_changes['added'] == expected_changes['added'] and packed_changes['modified'] == expected_changes['modified'] and packed_changes['deleted'] == expected_changes['removed'], 'Archived change lists mismatch')
    require(read_json(package / 'REMOVALS.json') == removals, 'Archived removal lists mismatch')
    require(packed_changes['details'] == {name: {'before': base_map.get(name), 'after': target_map.get(name)} for name in sorted(set(delta) | set(removals))}, 'Archived change detail hashes mismatch')

    require(changes['removed'] == removals, 'Removal mismatch')
    require(len(changes['added']) == 3 and len(changes['modified']) == 5, 'Change counts mismatch')
    require({**base_map, **delta} == target_map, 'Baseline plus delta does not equal target')
    restored = output / 'restored_hopebringer_banshee_golden_candidate_runtime'
    restored.mkdir()
    for name in target_map:
        require(safe(name), f'Unsafe source path: {name}')
        source = package / 'delta' / name if name in delta else baseline / name
        target = restored / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        require(target.stat().st_nlink == 1, f'Hardlink found: {name}')
        require((target.stat().st_dev, target.stat().st_ino) != (source.stat().st_dev, source.stat().st_ino), f'Non-independent copy: {name}')
    compare(inventory(restored), target_map, 'restored target')
    compare(inventory(baseline), baseline_before, 'baseline after restore')
    receipt = {
        'status': 'PASS_EXACT_SOURCE_ONLY',
        'candidate_status': 'candidate_pending_full_game_validation',
        'promote_over_verified_baseline': False,
        'full_game_validation_passed': False,
        'preserved_full_game_sigkill_attempts': 4,
        'preserved_source_and_isolated_combat_checks_passed': 20,

        'archive_commit': COMMIT,
        'repository_path': REPO_PATH,
        'manifest_sha256': MANIFEST_SHA,
        'archive': manifest['archive'],
        'archive_sha256': ARCHIVE_SHA,
        'archive_bytes': len(archive_bytes),
        'parts_verified': 5,
        'members_verified': 109,
        'increment_bytes_freshly_downloaded_by_this_helper': freshly_downloaded_by_helper,
        'increment_input_mode': 'fresh immutable GitHub URLs' if freshly_downloaded_by_helper else 'pre-fetched pinned remote bytes; see FETCH_PROVENANCE.json',
        'baseline_files_rehashed': len(base_map),
        'baseline_bytes': sum(meta['bytes'] for meta in base_map.values()),
        'baseline_source_map_sha256': BASE_MAP_SHA,
        'source_map_sha256': TARGET_MAP_SHA,
        'change_lists': changes,
        'new_files': 3,
        'modified_files': 5,
        'removed_files': 0,
        'delta_files': 8,
        'restored_files': len(target_map),
        'restored_bytes': sum(meta['bytes'] for meta in target_map.values()),
        'missing_files': [],
        'mismatched_files': [],
        'unexpected_files': [],
        'baseline_unchanged_after_restore': True,
        'independent_copy_no_hardlinks': True,
        'historical_baseline_freshly_downloaded_this_round': False,
        'historical_baseline_provenance': 'Reused previously restored Golden Eternal Summoner baseline, with every file rehashed before and after this independent copy. Earlier whole-chain download verification is reused, not rerun.',
        'supporting_hopebringer_summoner_golden_receipt_sha256': BASE_RECEIPT_SHA,
        'supporting_prior_fresh_whole_chain_receipt_sha256': prior['supporting_prior_fresh_whole_chain_receipt_sha256'],
        'prior_chain_to_golden_summoner_to_banshee_candidate_map_continuity': True,
        'implementation_scope': 'Exact source-byte recovery only. Not gameplay acceptance.',
        'gameplay_test_run': False,
        'lost_november6_work_recovered': False,
        'all_prior_backups_preserved': True,
        'no_deletion_performed': True,
        'verified_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (output / 'HOPEBRINGER_BANSHEE_GOLDEN_CANDIDATE_REMOTE_VERIFICATION.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2), flush=True)


if __name__ == '__main__':
    main()
