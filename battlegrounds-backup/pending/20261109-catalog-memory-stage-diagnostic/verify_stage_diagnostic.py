#!/usr/bin/env python3
"""Verify the diagnostic archive and its pinned runtime dependency without executing probes.

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

COMMIT = '54e5f406ef75bfe7864bbe4947d803de4b1a6525'
REPO_PATH = 'battlegrounds-backup/pending/20261109-catalog-memory-stage-diagnostic'
BASE_URL = f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
ARCHIVE_SHA = 'b5b03999c2cee2e995c56267cf2327786e3585187c061cf944a0088664a603a6'
MANIFEST_SHA = 'd026fb6cdb527cd96d9039c3c050d9cfb1332823dc88140d63dac790c9ec4857'
INPUT_MAP_SHA = 'e52121d24d2b21f75af73521362928a2da449f7f42915fb692cfcb3d425ab0a0'
INPUT_ARCHIVE_SHA = 'e5272cc3556bf626d353993b142a75d40ea26c4522eb94bcb2f5a55994f7f7d6'
INPUT_MANIFEST_SHA = '2218f998a299ee221fb31ee06c123737d8cc53c07d6a2c3eb6e122c744c87ad6'
INPUT_RECEIPT_SHA = '45d53273107a8411727d9d2e1462810ac6e685c4e1f62727eb55fdfd81a4d384'
INPUT_URL = 'https://raw.githubusercontent.com/Ethsigema/AI_text01/4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1/battlegrounds-backup/pending/20261109-catalog-memory-candidate/'
PACKAGE = 'catalog_memory_stage_diagnostic_20261109'


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
    parser.add_argument('--input-runtime', required=True, type=Path)
    parser.add_argument('--input-source-map', type=Path)
    parser.add_argument('--input-archive', type=Path)
    parser.add_argument('--input-manifest', type=Path)
    parser.add_argument('--input-receipt', type=Path)
    parser.add_argument('--download-dir', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    runtime = args.input_runtime.resolve()
    require(not output.exists() and output != runtime and runtime not in output.parents, 'Output must be a new directory outside runtime')
    output.mkdir(parents=True)
    fresh = args.download_dir is None
    downloads = args.download_dir.resolve() if args.download_dir else output / 'downloaded'
    if fresh:
        downloads.mkdir()
        get(BASE_URL + 'MANIFEST.json', downloads / 'MANIFEST.json')
    manifest_bytes = (downloads / 'MANIFEST.json').read_bytes()
    require(sha(manifest_bytes) == MANIFEST_SHA, 'Pinned diagnostic manifest mismatch')
    manifest = json.loads(manifest_bytes)
    require(manifest['sha256'] == ARCHIVE_SHA and manifest['bytes'] == 1101148 and len(manifest['parts']) == 5 and len(manifest['files']) == 67, 'Diagnostic package metadata mismatch')
    require(manifest['kind'] == 'diagnostic-evidence-only' and manifest['is_runtime_increment'] is False, 'Evidence-only marker missing')
    names = list(manifest['companion_files']) + [part['name'] for part in manifest['parts']]
    require(len(names) == len(set(names)) == 10, 'Download list mismatch')
    for name in names:
        require(safe(name) and '/' not in name, 'Unsafe download name')
        if fresh:
            get(BASE_URL + name, downloads / name)
    for name, metadata in manifest['companion_files'].items():
        require(file_meta(downloads / name) == metadata, 'Companion mismatch: ' + name)
    changes = read_json(downloads / 'CHANGES.json')
    require(changes == manifest['runtime_changes'] == {'added': [], 'modified': [], 'removed': []}, 'Runtime change claims mismatch')
    require(read_json(downloads / 'REMOVALS.json') == manifest['removed_source_files'] == [], 'Unexpected removals')
    require((downloads / 'SHA256SUMS.txt').read_text().strip() == f'{ARCHIVE_SHA}  {manifest["archive"]}', 'SHA256SUMS mismatch')
    blocks = []
    for part in manifest['parts']:
        body = (downloads / part['name']).read_bytes()
        require({'bytes': len(body), 'sha256': sha(body)} == {'bytes': part['bytes'], 'sha256': part['sha256']}, 'Part mismatch')
        blocks.append(body)
    archive = b''.join(blocks)
    require(len(archive) == manifest['bytes'] and sha(archive) == ARCHIVE_SHA, 'Archive mismatch')
    require(safe(manifest['archive']) and '/' not in manifest['archive'], 'Unsafe archive name')
    archive_path = output / manifest['archive']
    archive_path.write_bytes(archive)
    extracted = output / 'extracted'
    extracted.mkdir()
    actual = {}
    with tarfile.open(archive_path) as tar:
        for entry in tar:
            require(safe(entry.name) and entry.isfile() and entry.name not in actual, 'Unsafe or duplicate member: ' + entry.name)
            require(entry.name in manifest['files'], 'Unlisted member')
            body = tar.extractfile(entry).read()
            metadata = {'bytes': len(body), 'sha256': sha(body)}
            require(metadata == manifest['files'][entry.name], 'Member hash mismatch: ' + entry.name)
            target = extracted / entry.name
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as handle:
                handle.write(body)
            actual[entry.name] = metadata
    require(actual == manifest['files'], 'Missing archive members')
    package = extracted / PACKAGE
    internal = read_json(package / 'PACKAGE_MANIFEST.json')
    require(internal == {name.removeprefix(PACKAGE + '/'): metadata for name, metadata in actual.items() if name != PACKAGE + '/PACKAGE_MANIFEST.json'}, 'Internal manifest mismatch')
    require(not any(name.startswith(PACKAGE + '/' + part + '/') for name in actual for part in ['delta', 'patch', 'runtime', 'core']), 'Unexpected runtime payload')
    result = read_json(package / 'RESULT.json')
    require(result['verified_input_commit'] == '4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1' and result['runtime_added'] == result['runtime_modified'] == result['runtime_deleted'] == [], 'Diagnostic input or zero-change claim mismatch')
    require(result['preload']['exit'] == -9 and result['preload']['load_catalog_called'] is False and result['preload']['Game_loaded_by_gate'] is False, 'Diagnostic failure/scope markers mismatch')
    print('PASS: freshly fetched diagnostic archive, 5 parts and all 67 members', flush=True)
    source_bytes = (package / 'INPUT_SOURCE_MAP.json').read_bytes()
    require(sha(source_bytes) == INPUT_MAP_SHA, 'Input source map mismatch')
    if args.input_source_map:
        require(args.input_source_map.read_bytes() == source_bytes, 'Independent input map byte mismatch')
    source_map = json.loads(source_bytes)
    dep_manifest_bytes = args.input_manifest.read_bytes() if args.input_manifest else get(INPUT_URL + 'MANIFEST.json', output / 'PINNED_INPUT_MANIFEST.json')
    dep_receipt_bytes = args.input_receipt.read_bytes() if args.input_receipt else get(INPUT_URL + 'CATALOG_MEMORY_CANDIDATE_REMOTE_VERIFICATION.json', output / 'PINNED_INPUT_RECEIPT.json')
    require(sha(dep_manifest_bytes) == INPUT_MANIFEST_SHA and sha(dep_receipt_bytes) == INPUT_RECEIPT_SHA, 'Pinned dependency metadata mismatch')
    dependency = json.loads(dep_manifest_bytes)
    prior = json.loads(dep_receipt_bytes)
    require(dependency['sha256'] == INPUT_ARCHIVE_SHA and dependency['files']['catalog_memory_candidate_20261109/SOURCE_MAP.json'] == {'bytes': len(source_bytes), 'sha256': INPUT_MAP_SHA}, 'Dependency archive/map linkage mismatch')
    require(prior['status'] == 'PASS_EXACT_SOURCE_ONLY' and prior['source_map_sha256'] == INPUT_MAP_SHA and prior['archive_sha256'] == INPUT_ARCHIVE_SHA and prior['full_game_validation_passed'] is False, 'Input receipt scope mismatch')
    if args.input_archive:
        require(file_meta(args.input_archive)['sha256'] == INPUT_ARCHIVE_SHA, 'Input archive hash mismatch')
    before = inventory(runtime)
    compare(before, source_map, 'independent runtime input')
    require(len(before) == 27892 and sum(meta['bytes'] for meta in before.values()) == 1548714104, 'Input runtime counts mismatch')
    compare(inventory(runtime), before, 'runtime unchanged after diagnostic verification')
    receipt = {
        'status': 'PASS_DIAGNOSTIC_BYTES_AND_INPUT_DEPENDENCY',
        'archive_commit': COMMIT,
        'repository_path': REPO_PATH,
        'archive_sha256': ARCHIVE_SHA,
        'archive_bytes': len(archive),
        'manifest_sha256': MANIFEST_SHA,
        'parts_verified': 5,
        'members_verified': 67,
        'internal_manifest_members_verified': 66,
        'diagnostic_only': True,
        'runtime_changes': changes,
        'input_verified_commit': '4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1',
        'input_archive_sha256': INPUT_ARCHIVE_SHA,
        'input_manifest_sha256': INPUT_MANIFEST_SHA,
        'input_receipt_sha256': INPUT_RECEIPT_SHA,
        'input_archive_rehashed': args.input_archive is not None,
        'input_source_map_sha256': INPUT_MAP_SHA,
        'input_runtime_files_rehashed': len(before),
        'input_runtime_bytes': sum(meta['bytes'] for meta in before.values()),
        'input_runtime_unchanged': True,
        'missing_files': [], 'mismatched_files': [], 'unexpected_files': [],
        'diagnostic_download_by_this_python_helper': fresh,
        'download_mode': 'direct fixed URLs' if fresh else 'fresh pinned Git downloads; see FETCH_PROVENANCE.json',
        'historical_runtime_reused': True,
        'historical_chain_freshly_downloaded_this_round': False,
        'new_runtime_directory_created': False,
        'diagnostic_probes_run_by_verifier': False,
        'gameplay_test_run': False,
        'full_game_acceptance': False,
        'all_prior_backups_preserved': True,
        'no_deletion_performed': True,
        'verified_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (output / 'DIAGNOSTIC_REMOTE_VERIFICATION.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2), flush=True)

if __name__ == '__main__':
    main()
