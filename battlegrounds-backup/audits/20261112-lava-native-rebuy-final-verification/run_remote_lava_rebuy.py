"""Fixed-commit single-runtime-tree Lava rebuy runner. No Game without --execute.

The only runtime is the NEW restored_snapshot; no run_tree is created. All
wrappers, logs, results, HOME/XDG folders are in sibling independent_tests.
Candidate and restored_snapshot are distinct source roots, both fully rehashed
at completion (also after failure). These are NOT two runtime copies.
New real-v3 / pure-v4 metadata is frozen; only explicit parent execution may run it.
"""
from pathlib import Path, PurePosixPath
import argparse
import datetime
import fcntl
import gzip
import hashlib
import json
import os
import re
import signal
import subprocess
import time

if not __debug__:
    raise RuntimeError("Optimized Python is forbidden: validation assertions must execute")

BASELINE = {'source_commit': '73ef3f42e2a52b71aacd29fac2d6392731015d9d',
            'empty_slot_v1_v2_v3_excluded': True}
RUNTIME_MODE = 'single_new_restored_snapshot_no_run_tree_copy'
FINAL_STATUS = 'PASS_FIXED_REMOTE_LAVA_REBUY_SINGLE_RUNTIME_AND_CONTRACTS_POST_TEST_DUAL_SOURCE_REHASH'
# Frozen after parent review and separately observed pure89/0; no full Game run by preparation.
NEW_TEST_METADATA = {'status': 'FROZEN_REVIEWED',
    'full_checks_mode': 'exact_PASS_count_and_JSON_checks_plus_one', 'pure_checks': 89,
    'scenario_file': 'DARKCREST_LAVA_REBUY_MATRIX_RESULT.json',
    'scope': 'ordinary mature shop-origin Darkcrest no-token Lava purchase sale different-original-UID rebuy only',
    'test_revision': 'real_v3_pure_v4_parent_reviewed', 'full_cases': 1,
    'active_purchase_count': 1, 'first_buy_before_source': True,
    'post_sale_new_offer_generation_tested': False}
FROZEN_SOURCE = {'source_files': 27978, 'source_bytes': 1550796458,
    'source_map_sha256': '9c79ddf64f3de4cfff3b9080b2a60b3408ff9e039cab2b215042d51718731a03',
    'aggregate_sha256': '65baa3dfa80eb642b7f36f516fa2d915e57980d6cb9ed2d987f627d97e286f92'}
T6 = ['BG31_035', 'BG32_837', 'BG36_622', 'BG36_640']
T5 = ['BG23_008', 'BG31_920', 'BG31_925', 'BG32_111', 'BG32_820', 'BG32_835']
PINNED_TESTS = {'tests/darkcrest_lava_sale_20261112/content_contract.gd': '18570c38bb5b3d52238aa6cadb84d515ef5d8caa886c86365e79fa9a88d140f6', 'tests/darkcrest_lava_20261112/content_contract.gd': '301a5c9e56618baf42ae6ccbd80eea92f3eadc27a3fcfa02030fb51052004beb', 'tests/darkcrest_tier6_20261112/content_contract.gd': '01e5874b444db4950cd9a3a08aec18a0bd4443c28c2a17500f59ee39f38eb787', 'tests/darkcrest_tier5_20261112/content_contract.gd': 'd039a22573d7340d0779e17adbbc70b0e2f3f958334fd7c742bdd4b6e3bd6248', 'tests/darkcrest_20261112/source_eot_contract.gd': '2d37ee1063792093a0fd1ad683c2e8786f196caad43abe0c82ea831caaaf7790', 'tests/darkcrest_20261112/hand_shape_contract.gd': '1577c66e9524b4db1875309104cf55cf67d254d1e024a41b9b094fff8331fa2e', 'tests/darkcrest_20261112/seafloor_annotation_contract.gd': 'c0e0046fa010ccfb83d87bedf87a4616b23fef5e1700e88438f27f9aca6dc4cb', 'tests/darkcrest_lava_rebuy_20261112/real_matrix.gd': 'b77d12b25f96d6a156452ee07df24f22af40b5db4e6b791349ec868a68efdea2', 'tests/darkcrest_lava_rebuy_20261112/content_contract.gd': 'e197cf58afdac7b751ab9056d3822152331416c3d1cf504f77b9177e7ede9f73'}
TESTS = [('lava_rebuy_real_matrix', 'tests/darkcrest_lava_rebuy_20261112/real_matrix.gd', 3600, None), ('lava_rebuy_content_contract', 'tests/darkcrest_lava_rebuy_20261112/content_contract.gd', 180, 89), ('lava_sale_content_contract', 'tests/darkcrest_lava_sale_20261112/content_contract.gd', 180, 140), ('lava_content_contract', 'tests/darkcrest_lava_20261112/content_contract.gd', 180, 211), ('tier6_content_contract', 'tests/darkcrest_tier6_20261112/content_contract.gd', 180, 966), ('tier5_content_contract', 'tests/darkcrest_tier5_20261112/content_contract.gd', 180, 810), ('source_eot_contract', 'tests/darkcrest_20261112/source_eot_contract.gd', 180, 68), ('hand_shape_contract', 'tests/darkcrest_20261112/hand_shape_contract.gd', 180, 166), ('seafloor_annotation_contract', 'tests/darkcrest_20261112/seafloor_annotation_contract.gd', 180, 267)]
FIXTURE = 'tests/darkcrest_20261112/darkcrest_sources_archived.gd'

def sha(data):
    return hashlib.sha256(data).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def dump(value):
    return (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()


def write_new(path, value):
    with path.open('xb') as stream:
        stream.write(dump(value))


def read_json(path):
    return json.loads(path.read_text())


def safe(name):
    return bool(name) and not PurePosixPath(name).is_absolute() and '..' not in PurePosixPath(name).parts and '\\' not in name and '\0' not in name


def stop(process):
    if process.poll() is not None:
        return
    try: os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError: return
    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        try: os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError: pass
        process.wait()


def rss_for_group(group):
    rss = 0
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():
            continue
        try:
            fields = (proc / 'stat').read_text().rsplit(')', 1)[1].split()
            if int(fields[2]) == group:
                rss += int((proc / 'statm').read_text().split()[1]) * os.sysconf('SC_PAGE_SIZE')
        except (OSError, ValueError, IndexError):
            pass
    return rss


def validate_old(label, log, expected_checks, evidence):
    scenario = None
    if label == 'lava_sale_content_contract':
        marker='DARKCREST_LAVA_SALE_CONTENT_CONTRACT '
        rows=[json.loads(line.removeprefix(marker)) for line in log.splitlines() if line.startswith(marker)]
        assert len(rows)==1
        summary=rows[0];count=summary['passed']
        assert count==expected_checks and summary['failed']==0 and summary['failures']==[]
        assert summary['scope']=='detached sale context and authority rejection observations only'
        assert all(summary[k] is False for k in ['real_game_run','live_capacity_tested','partial_failure_live_injection'])
    elif label == 'lava_content_contract':
        marker = 'DARKCREST_LAVA_CONTENT_CONTRACT '
        rows = [json.loads(line.removeprefix(marker)) for line in log.splitlines() if line.startswith(marker)]
        assert len(rows)==1
        summary=rows[0]; count=summary['passed']
        assert count==expected_checks and summary['failed']==0 and summary['failures']==[]
        assert summary['real_game_run'] is False
        assert summary['scope']=='detached untouched Lava shape and custody rejection contracts, not native play or birth provenance'
    elif label in ['tier6_content_contract', 'tier5_content_contract']:
        marker = 'DARKCREST_TIER6_CONTENT_CONTRACT ' if label == 'tier6_content_contract' else 'DARKCREST_TIER5_CONTENT_CONTRACT '
        rows = [json.loads(line.removeprefix(marker)) for line in log.splitlines() if line.startswith(marker)]
        assert len(rows) == 1
        summary = rows[0]; count = summary['passed']
        assert count == expected_checks and summary['failed'] == 0 and summary['failures'] == []
        assert summary['ids'] == (T6 if label == 'tier6_content_contract' else T5)
        assert summary['scope'] == 'pure fixture content and identity observations only, not actual acquisition or provenance'
        if label == 'tier6_content_contract': assert summary['real_game_run'] is False
    elif label == 'source_eot_contract':
        count = expected_checks
        assert log.splitlines().count('DARKCREST_SOURCE_EOT_CONTRACT passed=68 failed=0') == 1
    elif label == 'seafloor_annotation_contract':
        rows = [json.loads(line.removeprefix('SEAFLOOR_ANNOTATION_CONTRACT ')) for line in log.splitlines() if line.startswith('SEAFLOOR_ANNOTATION_CONTRACT ')]
        assert len(rows) == 1
        summary = rows[0]; count = summary['checks']
        assert count == expected_checks and summary['failures'] == 0 and summary['scope'] == 'source_contract_only_no_Game_or_Catalog'
    elif label == 'hand_shape_contract':
        rows = [json.loads(line) for line in log.splitlines() if line.startswith('{') and 'darkcrest_five_strict_hand_shapes' in line]
        assert len(rows) == 1
        summary = rows[0]; count = summary['passed']
        assert count == expected_checks and summary['failed'] == 0 and summary['failures'] == []
    else:
        raise ValueError('Unknown test label: ' + label)
    assert type(count) is int and count > 0
    assert sum(line.startswith('PASS ') for line in log.splitlines()) == count, (label, 'PASS count does not match summary')
    return count, scenario


def require(ok, detail):
    if not ok:
        raise ValueError(detail)


def require_frozen():
    require(NEW_TEST_METADATA.get('status') == 'FROZEN_REVIEWED', 'UNKNOWN new rebuy API/scenario metadata: not executable')
    require(NEW_TEST_METADATA.get('full_checks_mode') == 'exact_PASS_count_and_JSON_checks_plus_one', 'UNKNOWN full check-count contract')
    for field in ['pure_checks']:
        require(type(NEW_TEST_METADATA.get(field)) is int and NEW_TEST_METADATA[field] > 0, 'UNKNOWN ' + field)
    require(safe(NEW_TEST_METADATA.get('scenario_file')) and '/' not in NEW_TEST_METADATA['scenario_file'], 'UNKNOWN scenario filename')
    require(isinstance(NEW_TEST_METADATA.get('scope'), str) and NEW_TEST_METADATA['scope'] not in ['', 'UNKNOWN'], 'UNKNOWN scope')
    require(len(TESTS) == 9 and len(set(x[0] for x in TESTS)) == 9, 'Exact one new full Game + eight pure contracts required')
    for _, name, _, _ in TESTS:
        require(re.fullmatch(r'[0-9a-f]{64}', PINNED_TESTS.get(name, '')) is not None, 'UNKNOWN pinned test hash: ' + name)


def validate(label, log, expected_checks, evidence):
    require(label in [x[0] for x in TESTS], 'Unknown test label: ' + label)
    failures = [line for line in log.splitlines() if re.search(r'^\s*FAIL(?:\s|$)', line)
                or any(marker in line for marker in ['SCRIPT ERROR', 'Parse Error', 'ParseError', 'COMMAND_FAILURE', 'WARNING', 'ERROR:'])]
    require(not failures, {'failure_markers': failures})
    if label in ['lava_rebuy_real_matrix', 'lava_rebuy_content_contract']:
        require_frozen()
        if label == 'lava_rebuy_real_matrix': return validate_rebuy_full(log, evidence)
        return validate_rebuy_pure(log, expected_checks)
    return validate_old(label, log, expected_checks, evidence)


def exact_keys(row, keys, label):
    require(type(row) is dict and set(row) == set(keys), ('Unexpected schema', label, sorted(row) if isinstance(row, dict) else type(row).__name__))


def integer_fields(row, keys):
    for key in keys: require(type(row[key]) is int, ('Strict integer required', key))


def marker_counts(log, markers):
    lines = log.splitlines()
    for marker, count in markers.items():
        require(lines.count('PASS ' + marker) == count, ('Required PASS marker multiplicity', marker, count))


def validate_rebuy_full(log, evidence):
    rows = re.findall(r'^DARKCREST_LAVA_REBUY_REAL_MATRIX_PASS cases=1 checks=(\d+)$', log, re.M)
    require(len(rows) == 1, 'Exactly one new full-matrix completion required')
    count = int(rows[0]); require(count > 0, 'Positive exact count required')
    scenario = read_json(evidence / NEW_TEST_METADATA['scenario_file'])
    exact_keys(scenario, ['scope','checks','cases','coin_pre_source_fixture','entirely_natural_game','old_matrices_repeated','post_sale_new_offer_generation_tested','no_live_state_injection'], 'full scenario')
    require(scenario['scope'] == NEW_TEST_METADATA['scope'], 'New full scope mismatch')
    require(type(scenario['checks']) is int and scenario['checks'] + 1 == count, 'JSON/log count offset must be only output-file check')
    for key in ['coin_pre_source_fixture','no_live_state_injection']: require(scenario[key] is True, key)
    for key in ['entirely_natural_game','old_matrices_repeated','post_sale_new_offer_generation_tested']: require(scenario[key] is False, key)
    require(type(scenario['cases']) is list and len(scenario['cases']) == 1, 'Exactly one new lifecycle case required')
    row = scenario['cases'][0]
    exact_keys(row, ['kind','seed','pre_source_first_lava_rolls','pre_source_cooffer_rolls','offer_uids','source_uid','source_tier','final_round','first_buy_before_source','active_purchase_count','first_purchase','offer_created_after_first_sale','second_offer_created_before_source','post_sale_new_offer_generation_tested','retirement','purchases','sale_effects','holds'], 'rebuy case')
    require(row['kind'] == 'pre_source_lava_sale_mature_source_different_uid_rebuy', 'Wrong rebuy case')
    integer_fields(row, ['seed','pre_source_first_lava_rolls','pre_source_cooffer_rolls','source_tier','final_round','active_purchase_count'])
    require(row['seed'] == 20261120 and 0 <= row['pre_source_first_lava_rolls'] <= 100 and 0 <= row['pre_source_cooffer_rolls'] <= 240, 'Fixed bounded native search required')
    require(row['first_buy_before_source'] is True and row['active_purchase_count'] == 1, 'Exactly one active purchase after the pre-source purchase required')
    require(row['source_tier'] == row['final_round'] == 4, 'Real source4 / round4 completion required')
    require(row['offer_created_after_first_sale'] is False and row['second_offer_created_before_source'] is True and row['post_sale_new_offer_generation_tested'] is False, 'This tests a different preexisting offer, not post-sale factory generation')
    require(type(row['offer_uids']) is list and len(row['offer_uids']) == 2, 'Two original offer UIDs required')
    ids = row['offer_uids'] + [row['source_uid']]
    require(all(type(uid) is str and re.fullmatch(r'u[1-9][0-9]*', uid) for uid in ids) and len(set(ids)) == 3, 'Distinct original UID schema required')
    require(type(row['purchases']) is list and len(row['purchases']) == 1, 'Exactly one new active purchase required')
    require(type(row['sale_effects']) is list and len(row['sale_effects']) == 1, 'One actual sale required')
    require(type(row['holds']) is list and len(row['holds']) == 2, 'Token and second-body holds required')
    first_buy = row['first_purchase']
    exact_keys(first_buy, ['uid','gold_before','gold_after','source_owned','active_purchase'], 'old-supported pre-source purchase')
    integer_fields(first_buy, ['gold_before','gold_after'])
    require(first_buy['uid'] == row['offer_uids'][0] and first_buy['source_owned'] is False and first_buy['active_purchase'] is False, 'First buy is pre-source, not new active coverage')
    require(first_buy['gold_before'] >= 3 and first_buy['gold_after'] == first_buy['gold_before'] - 3, 'First native buy delta')
    purchase = row['purchases'][0]
    exact_keys(purchase, ['uid','source_uid','source_tier','round','gold_before','gold_after','bought_before','bought_after','next_uid_before','next_uid_after','rng_before','rng_after'], 'active purchase')
    require(purchase['uid'] == row['offer_uids'][1] and purchase['source_uid'] == row['source_uid'], 'Purchase original source/object mismatch')
    integer_fields(purchase, ['source_tier','round','gold_before','gold_after','bought_before','bought_after','next_uid_before','next_uid_after','rng_before','rng_after'])
    require(purchase['source_tier'] == purchase['round'] == 3, 'Active purchase must be mature source3 / round3')
    require(purchase['gold_before'] >= 3 and purchase['gold_after'] == purchase['gold_before'] - 3, 'Natural active buy funds mismatch')
    require(purchase['bought_after'] == purchase['bought_before'] + 1, 'Bought counter must advance exactly once')
    require(purchase['next_uid_before'] == purchase['next_uid_after'] and purchase['rng_before'] == purchase['rng_after'], 'Purchase cannot birth/re-roll')
    sale = row['sale_effects'][0]
    exact_keys(sale, ['uid','index','gold_before','gold_after','stock_before','stock_after','sold_before','sold_after','uid_before','uid_after','rng_before','rng_after','retirement'], 'sale')
    integer_fields(sale, ['index','gold_before','gold_after','stock_before','stock_after','sold_before','sold_after','uid_before','uid_after','rng_before','rng_after'])
    require(sale['uid'] == row['offer_uids'][0] and sale['index'] == 0, 'Actual front Lava sale required')
    require(sale['gold_before'] >= 0 and sale['gold_after'] == sale['gold_before'] + 1 and sale['gold_after'] == purchase['gold_before'], 'Sale income precedes the one active purchase')
    for field in ['stock','sold']: require(sale[field + '_after'] == sale[field + '_before'] + 1, 'Single sale delta: ' + field)
    require(sale['stock_before'] >= 0 and sale['sold_before'] >= 0, 'Nonnegative native stock/counter required')
    require(sale['uid_before'] == sale['uid_after'] and sale['rng_before'] == sale['rng_after'], 'Sale cannot allocate UID or draw RNG')
    # One intervening native tier3 cast allocates a generated card; do not pretend
    # sale and purchase are adjacent or require their RNG cursors to be equal.
    require(purchase['next_uid_before'] == sale['uid_after'] + 1, 'Intervening native cast must allocate one original generated body')
    retired = row['retirement']; exact_keys(retired, ['owner','round','sequence'], 'retirement'); integer_fields(retired, retired)
    require(retired == sale['retirement'] and retired['owner'] == 0 and retired['round'] == 3 and retired['sequence'] >= 0, 'Exact old entity retirement required')
    expected_holds = [('already_owned_lava_purchase','darkcrest_lava_purchase_second_body_held'), ('current_token_purchase','darkcrest_lava_purchase_token_or_waiting_held')]
    for index, hold in enumerate(row['holds']):
        exact_keys(hold, ['kind','error','uid','round'], 'public hold')
        require((hold['kind'],hold['error']) == expected_holds[index] and hold['uid'] == row['offer_uids'][1] and type(hold['round']) is int and hold['round'] == 3, 'Wrong exact public hold')
    logged = [json.loads(line.removeprefix('DARKCREST_LAVA_REBUY_CASE_PASS ')) for line in log.splitlines() if line.startswith('DARKCREST_LAVA_REBUY_CASE_PASS ')]
    require(logged == scenario['cases'], 'Case log/JSON mismatch')
    markers = {key:1 for key in ['complete_game_script','complete_catalog','bounded_native_first_lava_before_source_found','first_original_lava_buy_before_source','first_pre_source_buy_native_deltas','bounded_native_same_shop_source_single_lava_found','two_original_lava_objects_distinct_before_source','original_shop_darkcrest_purchase','original_lava_hand_and_shop_survive_real_recruit_2','original_lava_hand_and_shop_survive_real_recruit_3','natural_gold_covers_single_active_rebuy','native_detached_alias_fixture_stats','native_detached_alias_fixture_effects','shared_nested_shadow_bind_refused_before_install_stats','shared_nested_shadow_bind_refused_before_install_effects','shared_nested_refusal_preserves_live_originals_stats','shared_nested_refusal_preserves_live_originals_effects','native_detached_purchase_cursor','actual_lava_projection_bound_for_refusal_checks','shadow_does_not_copy_live_issuance_or_retirement','bound_shadow_direct_grant_refused','bound_shadow_direct_cast_refused','bound_shadow_direct_eot_refused','bound_shadow_cannot_authorize_lava_play_or_sale','bound_shadow_direct_generation_refused','bound_shadow_negative_calls_issue_no_receipts','bound_shadow_low_level_native_sale_refused','released_shadow_never_becomes_live_authority','all_bound_shadow_checks_leave_live_originals_unchanged','public_native_lava_sell','native_sale_gold_stock_sold_exact_deltas','sale_no_uid_rng_change_old_object_absent','exact_retirement_owner_round_native_sequence','sale_rejections_preserve_full_live_state','sale_retires_only_one_play_record','retirement_added_once','distinct_uid_new_play_record_old_retirement_preserved','actual_nonempty_enemy_combat','combat_copy_starts_original_lava_stats','next_recruit_original_lava_2_5_kept0_after_combat','actual_token_public_cast_tier3','matrix_result_file']}
    markers.update({key:1 for key in ['mature_original_shop_source_active','zero_owned_lava_no_current_token','actual_full_ownedpurchase_shadow_passes','purchase_projection_preserves_live_state_and_receipt_refs','natural_gold_available_for_native_lava_purchase','public_active_original_lava_buy','purchase_only_original_offer_hand_transfer','native_purchase_exact_gold_and_counters','purchase_no_second_stock_uid_rng_change','live_historical_receipts_preserved_projection_released']})
    markers.update({key:2 for key in ['public_original_lava_play_position_0','actual_completed_original_lava_board_custody','all_lava_transactions_clear_after_sale','retired_rejections_preserve_full_live_state']})
    for kind, _ in expected_holds:
        for suffix in ['_preflight_held','_preflight_read_only','_public_buy_held','_public_rejection_no_consumption']: markers[kind + suffix] = 1
    marker_counts(log, markers)
    require(any(line == 'PASS coin_fixture_only_before_darkcrest_owned' for line in log.splitlines()), 'Disclosed pre-source Coin fixture missing')
    acquisitions = [json.loads(line.removeprefix('ACQUIRED ')) for line in log.splitlines() if line.startswith('ACQUIRED ')]
    require(len(acquisitions) == 1, 'Exactly one tier3 native cast outcome required')
    acquisition = acquisitions[0]
    require(acquisition['tier'] == 3 and acquisition['source_uid'] == row['source_uid'] and acquisition['id'] in ['BG23_007','BG23_004'], 'Original full tier3 domain output required')
    require(acquisition['pool_after'] == acquisition['pool_before'] - 1 and acquisition['uid'] == 'u' + str(sale['uid_after']), 'Native cast stock/UID delta mismatch')
    growth = [json.loads(line.removeprefix('GROWTH ')) for line in log.splitlines() if line.startswith('GROWTH ')]
    # Inherited four-player next_round prints PASS markers, not GROWTH arrays.
    require(not growth, 'Unexpected old initializer/growth logger')
    marker_counts(log, {'native_growth_exact_once_' + str(turn):1 for turn in [1,2,3]})
    require(sum(line.startswith('PASS ') for line in log.splitlines()) == count, 'Exact full PASS count mismatch')
    return count, scenario


def validate_rebuy_pure(log, expected_checks):
    marker = 'DARKCREST_LAVA_REBUY_CONTENT_CONTRACT '
    rows = [json.loads(line.removeprefix(marker)) for line in log.splitlines() if line.startswith(marker)]
    require(len(rows) == 1, 'One pure summary required')
    row = rows[0]
    exact_keys(row, ['passed','failed','failures','real_game_run','scope','actual_purchase_proven'], 'pure summary')
    integer_fields(row, ['passed','failed'])
    require(row['passed'] == expected_checks == NEW_TEST_METADATA['pure_checks'] and row['failed'] == 0 and row['failures'] == [], 'Pure check summary mismatch')
    require(row['real_game_run'] is False and row['actual_purchase_proven'] is False, 'Pure contract must not claim live purchase')
    require(row['scope'] == 'detached typed purchase snapshots and projection authority refusal only', 'Pure scope mismatch')
    require(sum(line.startswith('PASS ') for line in log.splitlines()) == row['passed'], 'Exact pure PASS count mismatch')
    marker_counts(log, {'non_weakref_projection_engine_rejected':6, 'malformed_engine_command_held_without_exception':6,
                       'missing_projection_engine_safe_rejection':1, 'expired_projection_engine_rejected':1,
                       'shared_nested_dictionary_rejected':1, 'shared_nested_array_rejected':1,
                       'cross_field_alias_rejected':1, 'release_does_not_promote_projection_to_live':1})
    return row['passed'], None

def validate_source_map(expected, manifest):
    require(type(expected) is dict and expected, 'Empty/non-dictionary source map')
    for name, row in expected.items():
        require(type(name) is str and safe(name) and str(PurePosixPath(name)) == name, ('Unsafe source path', name))
        require(type(row) is dict and set(row) == {'bytes', 'sha256'}, ('Wrong source-map row', name))
        require(type(row['bytes']) is int and row['bytes'] >= 0, ('Wrong source size', name))
        require(type(row['sha256']) is str and re.fullmatch(r'[0-9a-f]{64}', row['sha256']) is not None, ('Wrong source hash', name))
    require(type(manifest['source_files']) is int and len(expected) == manifest['source_files'], 'Source count mismatch')
    require(type(manifest['source_bytes']) is int and sum(row['bytes'] for row in expected.values()) == manifest['source_bytes'], 'Source byte total mismatch')


def scan_tree(tree, expected, aggregate):
    """Full byte scan; mismatches are data so a failed attempt can still be audited."""
    require(tree.is_dir() and not tree.is_symlink(), 'Invalid source tree: ' + str(tree))
    actual = {}
    combined = hashlib.sha256()
    paths = list(tree.rglob('*'))
    require(all(not path.is_symlink() for path in paths), 'Source symlink forbidden')
    require(all(path.is_file() or path.is_dir() for path in paths), 'Nonregular source member forbidden')
    for path in sorted((path for path in paths if path.is_file()), key=lambda path: path.relative_to(tree).as_posix()):
        name = path.relative_to(tree).as_posix()
        require(safe(name), name)
        length = path.stat().st_size
        combined.update(name.encode() + b'\0' + str(length).encode() + b'\0')
        digest = hashlib.sha256(); observed = 0
        with path.open('rb') as stream:
            while chunk := stream.read(1024 * 1024):
                observed += len(chunk); digest.update(chunk); combined.update(chunk)
        require(observed == length, 'Source file changed during scan: ' + name)
        actual[name] = {'bytes': observed, 'sha256': digest.hexdigest()}
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    mismatched = sorted(name for name in actual.keys() & expected.keys() if actual[name] != expected[name])
    result = {'path': str(tree), 'files': len(actual), 'bytes': sum(row['bytes'] for row in actual.values()),
              'aggregate_sha256': combined.hexdigest(), 'missing': missing, 'extra': extra, 'mismatched': mismatched,
              'matches': not missing and not extra and not mismatched and combined.hexdigest() == aggregate}
    return result, actual


def verify_tree(tree, expected, aggregate):
    result, actual = scan_tree(tree, expected, aggregate)
    require(result['matches'], result)
    return result, actual


def snapshot_trees(candidate, restored, expected, aggregate, evidence, prefix):
    """Try both trees even if one is changed/missing; preserve complete observations."""
    trees = {}
    for label, tree in [('candidate', candidate), ('restored_snapshot', restored)]:
        try:
            result, actual = scan_tree(tree, expected, aggregate)
            map_path = evidence / (prefix + '_' + label + '_source_map.json')
            write_new(map_path, actual)
            result['observed_source_map_file'] = map_path.name
            result['observed_source_map_sha256'] = sha(map_path.read_bytes())
        except Exception as exc:
            result = {'path': str(tree), 'matches': False, 'error': repr(exc)}
        trees[label] = result
    return trees


def validate_paths(candidate, restored, tranche_root):
    require(candidate != restored and candidate not in restored.parents and restored not in candidate.parents,
            'Candidate and restored_snapshot must be distinct non-nested paths')
    require(not candidate.samefile(restored), 'Candidate and restored_snapshot are the same filesystem directory')
    require(candidate == tranche_root / 'candidate', 'Only this new tranche candidate may be read')
    require(tranche_root in restored.parents and restored.name == 'restored_snapshot', 'Only this new tranche restored_snapshot may run')
    require(not (restored.parent / 'run_tree').exists(), 'This attempt must not use/create a run_tree')


def validate_restore_receipt(restore, restored_tree, commit, map_sha, aggregate, source_files, source_bytes):
    """Exact new low-disk restore contract; plain validation, no filesystem writes."""
    require(restore['source_commit'] == commit and restore['source_map_sha256'] == map_sha, 'Restore receipt fixed source mismatch')
    require(restore.get('status') == 'PASS_REMOTE_UNACCEPTED_SINGLE_TREE_SOURCE_RESTORE_BYTES_ONLY', 'Exact current single-tree restore status required')
    require(restore.get('fresh_base_checkpoint_then_single_target_tree') is True, 'Fresh base checkpoint then single target tree required')
    require(restore.get('separate_runtime_copy_created') is False, 'A separate runtime copy is forbidden')
    require(type(restore.get('restored_tree')) is str and restore['restored_tree'] == str(restored_tree), 'Restore receipt exact runtime path mismatch')
    require(restore.get('game_started') is False and restore.get('gameplay_acceptance') is False, 'Restore receipt is not source-only')
    record = restore['restored']
    require(type(record['files']) is int and type(record['bytes']) is int, 'Restored counts must be strict integers')
    require(record['aggregate_sha256'] == aggregate and record['files'] == source_files and record['bytes'] == source_bytes, 'Restored aggregate/count mismatch')
    require(all(record[k] == [] for k in ['missing', 'extra', 'mismatched']), 'Restore receipt has source mismatch')


def verify_package(package, restore_path, download_path, commit, map_sha, aggregate, restored_tree, check_pins=True):
    require(re.fullmatch(r'[0-9a-f]{40}', commit) is not None, 'Fixed full commit required')
    for value in [map_sha, aggregate]:
        require(re.fullmatch(r'[0-9a-f]{64}', value) is not None, 'Explicit frozen SHA256 required')
    require(map_sha == FROZEN_SOURCE['source_map_sha256'] and aggregate == FROZEN_SOURCE['aggregate_sha256'], 'Frozen source identity mismatch')
    manifest = read_json(package / 'MANIFEST.json')
    require(all(manifest.get(key) == value for key, value in FROZEN_SOURCE.items()), 'Manifest differs from reviewed frozen candidate')
    raw = gzip.decompress((package / 'SOURCE_MAP.json.gz').read_bytes())
    require(sha(raw) == manifest['source_map_sha256'] == map_sha, 'Source-map binding mismatch')
    require(manifest['aggregate_sha256'] == aggregate, 'Aggregate binding mismatch')
    expected = json.loads(raw)
    validate_source_map(expected, manifest)
    restore = read_json(restore_path)
    validate_restore_receipt(restore, restored_tree, commit, map_sha, aggregate, len(expected), manifest['source_bytes'])
    downloaded = read_json(download_path)
    require(downloaded['source_commit'] == commit and downloaded.get('status', '').startswith('PASS_'), 'Download receipt commit mismatch')
    records = downloaded['records']
    require(type(records) is list and len(records) == downloaded['files'] and records, 'Invalid package download records')
    seen = set()
    for row in records:
        name = row['filename']
        require(type(name) is str and safe(name) and name not in seen, ('Unsafe/duplicate package name', name)); seen.add(name)
        require('/' + commit + '/' in row['url'] and row['url'].startswith('https://raw.githubusercontent.com/'), 'Package URL not fixed source commit')
        path = package / name
        require(path.is_file() and not path.is_symlink(), ('Missing package member', name))
        data = path.read_bytes()
        require(type(row['bytes']) is int and len(data) == row['bytes'] and sha(data) == row['sha256'], ('Package download hash mismatch', name))
    require({'MANIFEST.json', 'SOURCE_MAP.json.gz'} <= seen, 'Manifest and source map not freshly downloaded at fixed commit')
    if check_pins:
        require_frozen()
        for _, name, _, _ in TESTS:
            require(name in expected and expected[name]['sha256'] == PINNED_TESTS[name], ('Frozen test changed', name))
        require(FIXTURE in expected, 'Archived fixture missing')
    bindings = {'source_commit': commit, 'source_map_sha256': map_sha, 'aggregate_sha256': aggregate,
                'manifest_sha256': sha((package / 'MANIFEST.json').read_bytes()),
                'restore_receipt_sha256': sha(restore_path.read_bytes()), 'download_receipt_sha256': sha(download_path.read_bytes())}
    return manifest, expected, bindings


def verify_prepared(evidence, prepared):
    for name, meta in prepared.items():
        path = evidence / name
        require(path.is_file() and not path.is_symlink(), 'Prepared wrapper/fixture missing: ' + name)
        data = path.read_bytes()
        require(len(data) == meta['bytes'] and sha(data) == meta['sha256'], 'Prepared bytes changed: ' + name)


def run_test(label, source_name, budget, bindings, restored, evidence, expected, aggregate, env, prepared):
    # One full source map + aggregate before EACH process, not only test-source SHA.
    tree, observed = verify_tree(restored, expected, aggregate)
    map_path = evidence / (label + '_source_map.json')
    write_new(map_path, observed)
    precheck = {**bindings, 'source': source_name, 'runtime_tree': str(restored), 'runtime_mode': RUNTIME_MODE,
                'verified_at_utc': utc(), 'tree': tree, 'source_map_file': map_path.name,
                'observed_source_map_sha256': sha(map_path.read_bytes())}
    write_new(evidence / (label + '_PRECHECK.json'), precheck)
    verify_prepared(evidence, prepared)
    available = int(next(line.split()[1] for line in Path('/proc/meminfo').read_text().splitlines()
                         if line.startswith('MemAvailable:'))) * 1024
    limit = min(4 * 1024**3, available // 2)
    require(limit >= (3 * 1024**3 if label == 'lava_rebuy_real_matrix' else 512 * 1024**2), 'Insufficient memory for guarded test')
    wrapper = evidence / (label + '.gd')
    cmd = ['godot', '--headless', '--path', str(restored), '--script', str(wrapper)]
    intent = {**bindings, 'source': source_name, 'command': cmd, 'prepared_at_utc': utc()}
    write_new(evidence / (label + '_LAUNCH_INTENT.json'), intent)
    process = None; reason = 'launch_failed'; started = utc(); t = time.monotonic(); peak = 0; problem = None
    log_path = evidence / (label + '.log')
    try:
        with log_path.open('x') as log:
            process = subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT, env=env, start_new_session=True)
            reason = 'exited'
            write_new(evidence / (label + '_STARTED.json'), {**intent, 'started_at_utc': started, 'pid': process.pid})
            while process.poll() is None:
                rss = rss_for_group(process.pid); peak = max(peak, rss)
                if rss > limit or time.monotonic() - t > budget:
                    reason = 'rss_soft_limit' if rss > limit else 'timeout'; stop(process); break
                time.sleep(.1)
    except BaseException as exc:
        reason = 'runner_interrupted' if process is not None else 'launch_failed'
        problem = exc
    finally:
        if process is not None: stop(process)
        data = log_path.read_bytes() if log_path.exists() else b''
        result = {**bindings, 'source': source_name, 'command': cmd, 'runtime_mode': RUNTIME_MODE,
                  'source_sha256': expected[source_name]['sha256'], 'wrapper_sha256': prepared[wrapper.name]['sha256'],
                  'log_sha256': sha(data), 'started_at_utc': started, 'finished_at_utc': utc(),
                  'process_started': process is not None, 'exit': process.wait() if process is not None else None,
                  'reason': reason, 'exception': repr(problem) if problem is not None else None,
                  'elapsed': time.monotonic() - t, 'sampled_process_group_peak_rss': peak,
                  'rss_soft_limit': limit, 'available_start': available, 'timeout_seconds': budget,
                  'memory_enforcement': 'sampled process-group soft limit, not a cgroup hard cap',
                  'source_snapshot_matches': True, 'start_tree': tree, 'precheck_file': label + '_PRECHECK.json'}
        write_new(evidence / (label + '_result.json'), result)
    print(label, json.dumps(result), flush=True)
    if problem is not None: raise problem
    require(result['exit'] == 0 and reason == 'exited', ('Process failed', label, result))
    return result, data.decode('utf-8', errors='strict')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--candidate', required=True, type=Path)
    parser.add_argument('--restored-snapshot', required=True, type=Path)
    parser.add_argument('--package', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path, help='New remote root outside nested restored_snapshot; all evidence goes here')
    parser.add_argument('--restore-report', required=True, type=Path)
    parser.add_argument('--download-report', type=Path)
    parser.add_argument('--source-map-sha256', required=True)
    parser.add_argument('--aggregate-sha256', required=True)
    parser.add_argument('--execute', action='store_true', help='Only explicit execution starts processes; UNKNOWN metadata still refuses')
    args = parser.parse_args()
    require_frozen()
    tranche = Path(__file__).resolve().parent.parent
    candidate = args.candidate.resolve(); restored = args.restored_snapshot.resolve(); root = args.output.resolve()
    validate_paths(candidate, restored, tranche)
    require(tranche in root.parents and root in restored.parents and root != restored and restored.parent in [root, root / 'single_tree_restore'], 'Output must be current remote root outside the restored source')
    require(not (root / 'run_tree').exists(), 'No runtime copy is permitted')
    package = args.package.resolve()
    restore_path = args.restore_report.resolve()
    download_path = (args.download_report or root / 'FRESH_PACKAGE_DOWNLOAD_VERIFIED.json').resolve()
    require(package == root / 'package' and restore_path.parent == root and download_path.parent == root, 'Current new restore siblings only')
    manifest, expected, bindings = verify_package(package, restore_path, download_path, args.commit, args.source_map_sha256, args.aggregate_sha256, restored)
    if not args.execute:
        print(json.dumps({'status': 'CONFIGURATION_ONLY_NOT_EXECUTED', **bindings, 'runtime_mode': RUNTIME_MODE,
                          'tests': TESTS, 'game_started': False}, indent=2)); return
    # Shared legacy lock path is coordination only; no failed-chain data is read/edited.
    lock_path = tranche.parent / 'develop_empty_ghost_20261112' / '.independent_full_game.lock'
    with lock_path.open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        evidence = root / 'independent_tests'
        require(not evidence.exists(), 'Never overwrite an earlier attempt')
        evidence.mkdir()
        runs = {}; prepared = {}; error = None; final_trees = {}; prior_end = None
        try:
            initial = snapshot_trees(candidate, restored, expected, args.aggregate_sha256, evidence, 'INITIAL')
            require(all(row['matches'] for row in initial.values()), ('Initial source integrity failed', initial))
            for label, name, _, _ in TESTS:
                data = ('extends "res://' + name + '"\n').encode()
                path = evidence / (label + '.gd')
                with path.open('xb') as stream: stream.write(data)
                prepared[path.name] = {'bytes': len(data), 'sha256': sha(data), 'source': name,
                                       'source_sha256': expected[name]['sha256'], 'kind': 'external_wrapper'}
            fixture_data = (restored / FIXTURE).read_bytes()
            require({'bytes': len(fixture_data), 'sha256': sha(fixture_data)} == expected[FIXTURE], 'Fixture changed')
            with (evidence / 'darkcrest_sources_archived.gd').open('xb') as stream: stream.write(fixture_data)
            prepared['darkcrest_sources_archived.gd'] = {**expected[FIXTURE], 'source': FIXTURE, 'kind': 'small_remote_fixture_copy'}
            write_new(evidence / 'PREPARED_FROM_REMOTE.json', {**bindings, 'prepared_at_utc': utc(), 'entries': prepared,
                      'baseline': BASELINE, 'initial_trees': initial, 'candidate_path': str(candidate),
                      'restored_snapshot_path': str(restored), 'runtime_mode': RUNTIME_MODE, 'runtime_trees': [str(restored)],
                      'two_runtime_copies': False, 'runner_sha256': sha(Path(__file__).read_bytes()), 'new_test_metadata': NEW_TEST_METADATA})
            env = os.environ.copy()
            for key, folder in [('HOME', 'home'), ('XDG_CACHE_HOME', 'cache'), ('XDG_CONFIG_HOME', 'config'), ('XDG_DATA_HOME', 'data')]:
                destination = evidence / folder; destination.mkdir(); env[key] = str(destination)
            for label, name, budget, count in TESTS:
                result, log = run_test(label, name, budget, bindings, restored, evidence, expected, args.aggregate_sha256, env, prepared)
                require(prior_end is None or result['started_at_utc'] >= prior_end, 'Nonserial process times')
                prior_end = result['finished_at_utc']
                count, scenario = validate(label, log, count, evidence)
                row = {'source': name, 'passed_checks': count, 'log_sha256': result['log_sha256'],
                       'test_sha256': expected[name]['sha256'], 'result_sha256': sha((evidence / (label + '_result.json')).read_bytes()),
                       'source_snapshot_matches': True, 'failures': [], 'result': result}
                if scenario is not None:
                    row['verified_scenario_fields'] = scenario
                    row['scenario_sha256'] = sha((evidence / NEW_TEST_METADATA['scenario_file']).read_bytes())
                runs[label] = row
                write_new(evidence / (label + '_VALIDATED.json'), row)
        except BaseException as exc:
            error = exc
        finally:
            # Both source roots are checked even when a process/validator failed.
            final_trees = snapshot_trees(candidate, restored, expected, args.aggregate_sha256, evidence, 'FINAL')
            try:
                verify_prepared(evidence, prepared)
                _, final_expected, final_bindings = verify_package(package, restore_path, download_path, args.commit, args.source_map_sha256, args.aggregate_sha256, restored)
                require(final_expected == expected and final_bindings == bindings, 'Package/restore bindings changed during attempt')
            except Exception as exc:
                if error is None: error = exc
            if not all(row['matches'] for row in final_trees.values()) and error is None:
                error = ValueError('Post-attempt source integrity failed')
            write_new(evidence / 'ATTEMPT_SUMMARY.json', {**bindings, 'finished_at_utc': utc(),
                      'status': 'TESTS_VALIDATED_SOURCE_INTEGRITY_PASS' if error is None and len(runs) == len(TESTS) else 'FAILED_OR_INCOMPLETE_ATTEMPT',
                      'error': repr(error) if error is not None else None, 'validated_tests': list(runs),
                      'result_receipts_present': [x[0] for x in TESTS if (evidence / (x[0] + '_result.json')).exists()],
                      'tests_without_result_receipt': [x[0] for x in TESTS if not (evidence / (x[0] + '_result.json')).exists()],
                      'trees': final_trees, 'runtime_mode': RUNTIME_MODE, 'two_runtime_copies': False})
        if error is not None: raise error
        require(len(runs) == len(TESTS), 'Not all tests validated')
        final = {'status': FINAL_STATUS, **bindings, 'verified_at_utc': utc(), 'trees': final_trees,
                 'tests': runs, 'fixtures': prepared, 'baseline': BASELINE, 'runtime_mode': RUNTIME_MODE,
                 'runtime_trees': [str(restored)], 'source_integrity_trees': [str(candidate), str(restored)],
                 'two_runtime_copies': False, 'sequential_game_execution': True, 'full_game_processes': 1,
                 'old_full_matrices_repeated': False, 'new_test_metadata': NEW_TEST_METADATA,
                 'full_game_acceptance': False, 'default_pool_promoted': False, 'permanent_enchantment_opened': False,
                 'scope': NEW_TEST_METADATA['scope']}
        write_new(root / 'INDEPENDENT_GAME_VERIFICATION.json', final)
        print('DARKCREST_LAVA_REBUY_SINGLE_RUNTIME_AND_DUAL_SOURCE_REHASH_PASS', flush=True)


if __name__ == '__main__':
    main()
