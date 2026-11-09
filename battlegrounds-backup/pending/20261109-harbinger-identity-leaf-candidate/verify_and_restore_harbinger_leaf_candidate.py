#!/usr/bin/env python3
"""Verify the pinned experimental Harbinger identity leaf candidate (full Game remains untested) and independently restore it.

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

COMMIT = '9c6255899ed6fffc853c274c8f302d1af10c9764'
REPO_PATH = 'battlegrounds-backup/pending/20261109-harbinger-identity-leaf-candidate'
BASE_URL = f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
ARCHIVE_SHA = 'b666e972100a402ae3b9fa92ab2126e5324f4327842ac88fecebcc204c6f4ee4'
MANIFEST_SHA = '180d5ebba796ffa9cde4a4afe2814604cba823a9bd5856f09bbf45cc8ca8ce1c'
BASE_MAP_SHA = 'e52121d24d2b21f75af73521362928a2da449f7f42915fb692cfcb3d425ab0a0'
TARGET_MAP_SHA = 'e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe'
BASE_RECEIPT_SHA = '45d53273107a8411727d9d2e1462810ac6e685c4e1f62727eb55fdfd81a4d384'
BASE_RECEIPT_URL = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1/battlegrounds-backup/pending/20261109-catalog-memory-candidate/CATALOG_MEMORY_CANDIDATE_REMOTE_VERIFICATION.json'
PACKAGE = 'harbinger_identity_leaf_candidate_20261109'


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



BASE_MANIFEST_SHA = '2218f998a299ee221fb31ee06c123737d8cc53c07d6a2c3eb6e122c744c87ad6'
BASE_ARCHIVE_SHA = 'e5272cc3556bf626d353993b142a75d40ea26c4522eb94bcb2f5a55994f7f7d6'
STATUS = 'EXPERIMENTAL_SCOPED_EQUIVALENCE_AND_ENTRY_MEMORY_PASS_FULL_GAME_UNTESTED'

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
    require(manifest['sha256'] == ARCHIVE_SHA and manifest['bytes'] == 1092872, 'Archive metadata mismatch')
    require(len(manifest['parts']) == 5 and len(manifest['files']) == 126, 'Package counts mismatch')
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
    require(read_json(package / 'PACKAGE_MANIFEST.json') == internal_actual and len(internal_actual) == 125, 'Internal manifest mismatch')
    print('PASS: 5 pinned archive parts, assembled archive and all 126 members', flush=True)
    packed = read_json(package / 'CHANGES.json')
    result = read_json(package / 'RESULT.json')
    require(manifest['status'] == packed['status'] == result['status'] == STATUS, 'Experimental scope missing')
    require(manifest['promote_over_verified_baseline'] is packed['promote_over_verified_baseline'] is False, 'Candidate may not replace accepted baseline')
    require(result['Game_tested'] is result['full_catalog_tested'] is result['gameplay_baseline_promoted'] is False, 'Full Game untested marker mismatch')
    require(packed['input_commit'] == manifest['depends_on']['recovery_commit'] == '4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1', 'Input commit mismatch')
    require(packed['immediate_base_archive_sha256'] == manifest['depends_on']['archive_sha256'] == BASE_ARCHIVE_SHA, 'Input archive mismatch')
    base_bytes = args.baseline_source_map.read_bytes()
    require(sha(base_bytes) == BASE_MAP_SHA and base_bytes == (package / 'BASE_MAP.json').read_bytes(), 'Baseline map continuity mismatch')
    target_bytes = (package / 'SOURCE_MAP.json').read_bytes()
    require(sha(target_bytes) == TARGET_MAP_SHA, 'Target map mismatch')
    base_map, target_map = json.loads(base_bytes), json.loads(target_bytes)
    require(len(base_map) == 27892 and len(target_map) == 27893, 'Source counts mismatch')
    for name in set(base_map) | set(target_map):
        require(safe(name), 'Unsafe source path: ' + name)
    receipt_bytes = args.baseline_receipt.read_bytes() if args.baseline_receipt else get(BASE_RECEIPT_URL, output / 'PINNED_BASELINE_RECEIPT.json')
    dep_bytes = args.baseline_manifest.read_bytes() if args.baseline_manifest else get(BASE_RECEIPT_URL.rsplit('/', 1)[0] + '/MANIFEST.json', output / 'PINNED_BASELINE_MANIFEST.json')
    require(sha(receipt_bytes) == BASE_RECEIPT_SHA and sha(dep_bytes) == BASE_MANIFEST_SHA, 'Pinned baseline metadata mismatch')
    prior, dependency = json.loads(receipt_bytes), json.loads(dep_bytes)
    require(prior['status'] == 'PASS_EXACT_SOURCE_ONLY' and prior['source_map_sha256'] == BASE_MAP_SHA and prior['archive_sha256'] == BASE_ARCHIVE_SHA, 'Baseline receipt mismatch')
    require(prior['prior_chain_to_banshee_candidate_to_catalog_memory_map_continuity'] is True and prior['full_game_validation_passed'] is False, 'Baseline continuity or scope mismatch')
    require(dependency['sha256'] == BASE_ARCHIVE_SHA and dependency['files']['catalog_memory_candidate_20261109/SOURCE_MAP.json'] == {'bytes': len(base_bytes), 'sha256': BASE_MAP_SHA}, 'Dependency archive/map linkage mismatch')
    if args.baseline_archive:
        require(file_meta(args.baseline_archive)['sha256'] == BASE_ARCHIVE_SHA, 'Baseline archive mismatch')
    baseline_before = inventory(baseline)
    compare(baseline_before, base_map, 'baseline before restore')
    print('PASS: all 27,892 reused baseline files independently rehashed', flush=True)
    delta = inventory(package / 'delta')
    actual_delta = {name: meta for name, meta in target_map.items() if base_map.get(name) != meta}
    require(delta == actual_delta and len(delta) == 3, 'Delta not exact source difference')
    expected = {'added': sorted(set(target_map) - set(base_map)), 'modified': sorted(name for name in set(base_map) & set(target_map) if base_map[name] != target_map[name]), 'removed': sorted(set(base_map) - set(target_map))}
    require(changes == expected == {'added': ['core/eot_repeat_identity.gd'], 'modified': ['core/end_turn_repeats.gd', 'core/harbinger_eot_admission.gd'], 'removed': []}, 'Change lists mismatch')
    require(packed['added'] == [{'path': name, 'after': target_map[name]} for name in changes['added']], 'Added details mismatch')
    require(packed['modified'] == [{'path': name, 'before': base_map[name], 'after': target_map[name]} for name in changes['modified']], 'Modified details mismatch')
    require(packed['deleted'] == removals == read_json(package / 'REMOVALS.json') == [], 'Removal lists mismatch')
    require({**base_map, **delta} == target_map, 'Baseline plus delta not target')
    require(sum(v['bytes'] for v in target_map.values()) == 1548714522 and sum(v['bytes'] for v in target_map.values()) - sum(v['bytes'] for v in base_map.values()) == 418, 'Source bytes mismatch')
    restored = output / 'restored_harbinger_identity_leaf_candidate_runtime'
    restored.mkdir()
    for name in target_map:
        source = package / 'delta' / name if name in delta else baseline / name
        target = restored / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        require(target.stat().st_nlink == 1, 'Hardlink found: ' + name)
        require((target.stat().st_dev, target.stat().st_ino) != (source.stat().st_dev, source.stat().st_ino), 'Non-independent copy: ' + name)
    compare(inventory(restored), target_map, 'restored target')
    compare(inventory(baseline), baseline_before, 'baseline after restore')
    receipt = {
        'status': 'PASS_EXACT_SOURCE_ONLY', 'candidate_status': STATUS,
        'promote_over_verified_baseline': False, 'full_game_validation_passed': False,
        'full_game_attempted_for_this_experiment': False, 'gameplay_test_run': False,
        'archive_commit': COMMIT, 'repository_path': REPO_PATH, 'manifest_sha256': MANIFEST_SHA,
        'archive': manifest['archive'], 'archive_sha256': ARCHIVE_SHA, 'archive_bytes': len(archive_bytes),
        'parts_verified': 5, 'members_verified': 126, 'internal_manifest_members_verified': 125,
        'increment_bytes_freshly_downloaded_by_this_helper': fresh,
        'increment_input_mode': 'fresh immutable GitHub URLs' if fresh else 'pre-fetched pinned bytes; see FETCH_PROVENANCE.json for actual download evidence',
        'baseline_verified_commit': '4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1',
        'baseline_archive_sha256': BASE_ARCHIVE_SHA, 'baseline_archive_rehashed': args.baseline_archive is not None,
        'baseline_manifest_sha256': BASE_MANIFEST_SHA, 'baseline_receipt_sha256': BASE_RECEIPT_SHA,
        'baseline_files_rehashed': len(base_map), 'baseline_bytes': sum(v['bytes'] for v in base_map.values()),
        'baseline_source_map_sha256': BASE_MAP_SHA, 'source_map_sha256': TARGET_MAP_SHA,
        'change_lists': changes, 'new_files': 1, 'modified_files': 2, 'removed_files': 0, 'delta_files': 3,
        'restored_files': len(target_map), 'restored_bytes': sum(v['bytes'] for v in target_map.values()),
        'missing_files': [], 'mismatched_files': [], 'unexpected_files': [],
        'baseline_unchanged_after_restore': True, 'independent_copy_no_hardlinks': True,
        'historical_baseline_freshly_downloaded_this_round': False,
        'historical_baseline_provenance': 'Reused previously independently restored catalog memory candidate; every file rehashed before and after independent copy. Earlier whole-chain download audit is reused, not rerun.',
        'prior_chain_to_catalog_memory_to_harbinger_leaf_map_continuity': True,
        'implementation_scope': 'Exact source-byte recovery only. No gameplay acceptance or rerun of archived probes.',
        'all_prior_backups_preserved': True, 'no_deletion_performed': True,
        'verified_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (output / 'HARBINGER_IDENTITY_LEAF_CANDIDATE_REMOTE_VERIFICATION.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2), flush=True)

if __name__ == '__main__':
    main()
