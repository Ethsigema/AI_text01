"""Fixed-commit single-runtime-tree buffed Lava native-sale compatibility runner. No Game without --execute.

The only runtime is the NEW restored_snapshot; no run_tree is created. All
wrappers, logs, results, HOME/XDG folders are in sibling independent_tests.
Candidate and restored_snapshot are distinct source roots, both fully rehashed
at completion (also after failure). These are NOT two runtime copies.
Frozen exact schemas and source identity require matching fixed-commit fresh restore receipts before execution. Existing native permanence is not a new algorithm.
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

BASELINE = {'source_commit': '610cad09b7d19fe2615201f054a68c6e1a31d79d', 'accepted_final_commit': '838043a91d995a93bf916846e960465ee05966e7', 'accepted_audit_commit': '7a5d886bbdd1216c93289f9f3e6f3c0eb51c90ce', 'old_full_matrices_repeated': False, 'empty_slot_v1_v2_v3_excluded': True}
RUNTIME_MODE = 'single_new_restored_snapshot_no_run_tree_copy'
FINAL_STATUS = 'PASS_FIXED_REMOTE_LAVA_BUFFED_SALE_SINGLE_RUNTIME_AND_CONTRACTS_POST_TEST_DUAL_SOURCE_REHASH'
PLANNED_SCOPE = {'new_full_cases': 1, 'native_round_cycles': 1, 'native_targeted_casts': 1, 'native_buffed_lava_sales': 1, 'mini_remains_on_board': True, 'next_round_original_mini_grant': True, 'no_lava_target_cast_held': True, 'new_full_game_processes': 1, 'old_full_matrices_repeated': False, 'buffed_lava_rebuy_golden_multi_buff_new_target_opened': False, 'default_pool_promoted': False, 'new_native_permanence_algorithm_added': False}
NEW_TEST_METADATA = {'status': 'FROZEN_REVIEWED', 'full_checks_mode': 'exact_PASS_count_and_JSON_checks_plus_one', 'pure_checks': 44, 'scenario_file': 'DARKCREST_LAVA_BUFFED_SALE_MATRIX_RESULT.json', 'scope': 'one ordinary Lava first Mini permanent buff then native sale with live Mini regrant', 'test_revision': 'V2_code_V4_README_real_fe7224_pure_cc17_static_count_corrected44', 'readme_sha256': '90fbd6c8eb3b0803f3d1256c1fc09100add206f1e965bd6faef01a3d56407f58', 'full_cases': 1, 'native_round_cycles': 1, 'native_targeted_casts': 1, 'native_buffed_lava_sales': 1}
NEW_VALIDATORS_READY = True
FROZEN_SOURCE = {'source_files':27991,'source_bytes':1550926264,'source_map_sha256':'619f853c7aecfc6b7f559e8c9d98888abe49a32e16541ed00a7a0280ad0c8601','aggregate_sha256':'af984538541f2b3caabfd50a827421511a2a91b0a8f663669a6c8c4d9dd923e6'}
FROZEN_SOURCE_COMMIT = 'b74934926d8e5eaeb4a9b27328cd07da3da54007'
LEGACY_REBUY_PURE_CHECKS = 89
LEGACY_PERMANENT_PURE_CHECKS = 344
LEGACY_MINI_SALE_PURE_CHECKS = 102
LEGACY_MINI_AFTER_CAST_PURE_CHECKS = 85
LEGACY_ELEVEN_PURE_TOTAL = 3248

T6 = ['BG31_035', 'BG32_837', 'BG36_622', 'BG36_640']
T5 = ['BG23_008', 'BG31_920', 'BG31_925', 'BG32_111', 'BG32_820', 'BG32_835']
PINNED_TESTS = {'tests/darkcrest_lava_sale_20261112/content_contract.gd': '18570c38bb5b3d52238aa6cadb84d515ef5d8caa886c86365e79fa9a88d140f6', 'tests/darkcrest_lava_20261112/content_contract.gd': '301a5c9e56618baf42ae6ccbd80eea92f3eadc27a3fcfa02030fb51052004beb', 'tests/darkcrest_tier6_20261112/content_contract.gd': '01e5874b444db4950cd9a3a08aec18a0bd4443c28c2a17500f59ee39f38eb787', 'tests/darkcrest_tier5_20261112/content_contract.gd': 'd039a22573d7340d0779e17adbbc70b0e2f3f958334fd7c742bdd4b6e3bd6248', 'tests/darkcrest_20261112/source_eot_contract.gd': '2d37ee1063792093a0fd1ad683c2e8786f196caad43abe0c82ea831caaaf7790', 'tests/darkcrest_20261112/hand_shape_contract.gd': '1577c66e9524b4db1875309104cf55cf67d254d1e024a41b9b094fff8331fa2e', 'tests/darkcrest_20261112/seafloor_annotation_contract.gd': 'c0e0046fa010ccfb83d87bedf87a4616b23fef5e1700e88438f27f9aca6dc4cb', 'tests/darkcrest_lava_rebuy_20261112/content_contract.gd': 'e197cf58afdac7b751ab9056d3822152331416c3d1cf504f77b9177e7ede9f73', 'tests/darkcrest_lava_permanent_20261112/content_contract.gd': '2fd3807f7d983fff73fc876576fb77c1db427ccb4883383bda15ffc346de34d4', 'tests/darkcrest_mini_sale_20261112/content_contract.gd': 'e390781a2cc7af2131f06357d814472801486f2328433f3b239d3db2a443f9ef', 'tests/darkcrest_mini_after_cast_20261112/content_contract.gd': '8aec0b31be23ceed2f6b344618c70a3aedf8999fcd73358bbb0d73f8315a80dc', 'tests/darkcrest_lava_buffed_sale_20261112/real_matrix.gd': 'fe7224d40d4a40a43952a505d2f8bb5a89fa5b64ae528c07d2c7a7fee8e42544', 'tests/darkcrest_lava_buffed_sale_20261112/content_contract.gd': 'cc17f6c1210165e314dce1ce1a7bf427c0c037c864b1ce2c81cce4f45d40d0fe'}
TESTS = [('lava_buffed_sale_real_matrix', 'tests/darkcrest_lava_buffed_sale_20261112/real_matrix.gd', 3600, None), ('lava_buffed_sale_content_contract', 'tests/darkcrest_lava_buffed_sale_20261112/content_contract.gd', 180, 44), ('mini_after_cast_content_contract', 'tests/darkcrest_mini_after_cast_20261112/content_contract.gd', 180, 85), ('mini_sale_content_contract', 'tests/darkcrest_mini_sale_20261112/content_contract.gd', 180, 102), ('lava_permanent_content_contract', 'tests/darkcrest_lava_permanent_20261112/content_contract.gd', 180, 344), ('lava_rebuy_content_contract', 'tests/darkcrest_lava_rebuy_20261112/content_contract.gd', 180, 89), ('lava_sale_content_contract', 'tests/darkcrest_lava_sale_20261112/content_contract.gd', 180, 140), ('lava_content_contract', 'tests/darkcrest_lava_20261112/content_contract.gd', 180, 211), ('tier6_content_contract', 'tests/darkcrest_tier6_20261112/content_contract.gd', 180, 966), ('tier5_content_contract', 'tests/darkcrest_tier5_20261112/content_contract.gd', 180, 810), ('source_eot_contract', 'tests/darkcrest_20261112/source_eot_contract.gd', 180, 68), ('hand_shape_contract', 'tests/darkcrest_20261112/hand_shape_contract.gd', 180, 166), ('seafloor_annotation_contract', 'tests/darkcrest_20261112/seafloor_annotation_contract.gd', 180, 267)]
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
    require(NEW_TEST_METADATA.get('status') == 'FROZEN_REVIEWED', 'UNKNOWN new buffed Lava sale metadata: not executable')
    require(NEW_VALIDATORS_READY is True, 'UNKNOWN new validators: not executable')
    require(isinstance(NEW_TEST_METADATA.get('full_checks_mode'), str) and NEW_TEST_METADATA['full_checks_mode'] not in ['', 'UNKNOWN_NOT_FROZEN'], 'UNKNOWN full check-count contract')
    require(type(NEW_TEST_METADATA.get('pure_checks')) is int and NEW_TEST_METADATA['pure_checks'] > 0, 'UNKNOWN pure checks')
    require(type(NEW_TEST_METADATA.get('full_cases')) is int and NEW_TEST_METADATA['full_cases'] == 1 and type(NEW_TEST_METADATA.get('native_round_cycles')) is int and NEW_TEST_METADATA['native_round_cycles'] == 1 and type(NEW_TEST_METADATA.get('native_targeted_casts')) is int and NEW_TEST_METADATA['native_targeted_casts'] == 1, 'One case, one targeted cast and one native combat round required')
    require(type(NEW_TEST_METADATA.get('native_buffed_lava_sales')) is int and NEW_TEST_METADATA['native_buffed_lava_sales']==1, 'One original permanently buffed Lava public sale required')
    require(safe(NEW_TEST_METADATA.get('scenario_file')) and '/' not in NEW_TEST_METADATA['scenario_file'], 'UNKNOWN scenario filename')
    require(isinstance(NEW_TEST_METADATA.get('scope'), str) and NEW_TEST_METADATA['scope'] not in ['', 'UNKNOWN'], 'UNKNOWN scope')
    require(isinstance(NEW_TEST_METADATA.get('test_revision'), str) and NEW_TEST_METADATA['test_revision'] not in ['', 'UNKNOWN_NOT_FROZEN'], 'UNKNOWN reviewed test revision')
    for field in ['source_files','source_bytes']:
        require(type(FROZEN_SOURCE.get(field)) is int and FROZEN_SOURCE[field] > 0, 'UNKNOWN frozen ' + field)
    for field in ['source_map_sha256','aggregate_sha256']:
        require(re.fullmatch(r'[0-9a-f]{64}', FROZEN_SOURCE.get(field,'')) is not None, 'UNKNOWN frozen ' + field)
    require(len(TESTS) == 13 and len(set(x[0] for x in TESTS)) == 13, 'Exactly one new full Game + new pure + eleven legacy pure required')
    require(re.fullmatch(r'[0-9a-f]{40}', FROZEN_SOURCE_COMMIT) is not None, 'UNKNOWN fixed source commit')
    require([x[3] for x in TESTS[2:]] == [85,102,344,89,140,211,966,810,68,166,267], 'Exact eleven old pure regressions required')
    for _, name, _, _ in TESTS:
        require(name.startswith('tests/') and re.fullmatch(r'[0-9a-f]{64}', PINNED_TESTS.get(name, '')) is not None, 'UNKNOWN pinned test path/hash: ' + name)


def validate(label, log, expected_checks, evidence):
    require(label in [x[0] for x in TESTS], 'Unknown test label: ' + label)
    failures = [line for line in log.splitlines() if re.search(r'^\s*FAIL(?:\s|$)', line)
                or any(marker in line for marker in ['SCRIPT ERROR', 'Parse Error', 'ParseError', 'COMMAND_FAILURE', 'WARNING', 'ERROR:'])]
    require(not failures, {'failure_markers': failures})
    if label == 'lava_buffed_sale_real_matrix': return validate_lava_buffed_sale_full(log,evidence)
    if label == 'lava_buffed_sale_content_contract': return validate_lava_buffed_sale_pure(log,expected_checks)
    if label == 'mini_after_cast_content_contract': return validate_legacy_mini_after_cast_pure(log,expected_checks)
    if label == 'mini_sale_content_contract': return validate_legacy_mini_sale_pure(log,expected_checks)
    if label == 'lava_permanent_content_contract': return validate_legacy_permanent_pure(log,expected_checks)
    if label == 'lava_rebuy_content_contract': return validate_rebuy_pure(log, expected_checks)
    return validate_old(label, log, expected_checks, evidence)


def exact_keys(row, keys, label):
    require(type(row) is dict and set(row) == set(keys), ('Unexpected schema', label, sorted(row) if isinstance(row, dict) else type(row).__name__))


def integer_fields(row, keys):
    for key in keys: require(type(row[key]) is int, ('Strict integer required', key))


def marker_counts(log, markers):
    lines = log.splitlines()
    for marker, count in markers.items():
        require(lines.count('PASS ' + marker) == count, ('Required PASS marker multiplicity', marker, count))


def validate_rebuy_pure(log, expected_checks):
    marker = 'DARKCREST_LAVA_REBUY_CONTENT_CONTRACT '
    rows = [json.loads(line.removeprefix(marker)) for line in log.splitlines() if line.startswith(marker)]
    require(len(rows) == 1, 'One pure summary required')
    row = rows[0]
    exact_keys(row, ['passed','failed','failures','real_game_run','scope','actual_purchase_proven'], 'pure summary')
    integer_fields(row, ['passed','failed'])
    require(row['passed'] == expected_checks == LEGACY_REBUY_PURE_CHECKS and row['failed'] == 0 and row['failures'] == [], 'Pure check summary mismatch')
    require(row['real_game_run'] is False and row['actual_purchase_proven'] is False, 'Pure contract must not claim live purchase')
    require(row['scope'] == 'detached typed purchase snapshots and projection authority refusal only', 'Pure scope mismatch')
    require(sum(line.startswith('PASS ') for line in log.splitlines()) == row['passed'], 'Exact pure PASS count mismatch')
    marker_counts(log, {'non_weakref_projection_engine_rejected':6, 'malformed_engine_command_held_without_exception':6,
                       'missing_projection_engine_safe_rejection':1, 'expired_projection_engine_rejected':1,
                       'shared_nested_dictionary_rejected':1, 'shared_nested_array_rejected':1,
                       'cross_field_alias_rejected':1, 'release_does_not_promote_projection_to_live':1})
    return row['passed'], None

PERMANENT_PURE_SCOPE = 'detached Mini context shape and unbound authority refusal only'
PERMANENT_PURE_MARKERS = {
    'native_added_key_is_stringname_max_health':1,
    'native_added_key_is_stringname_expires_at_end_turn':1,
    'wrong_string_key_type_refused_max_health':1,
    'wrong_string_key_type_refused_expires_at_end_turn':1,
    'complete_new_source_and_runtime_proof':1, 'ordinary_native_mini_pair':1,
    'original_mini_child_complete_payload':1, 'detached_untouched_1_4_mini_shape_only':1,
    'complete_detached_native_child_shape_not_provenance':1,
    'child_shape_checks_do_not_write_fixtures':1,
    'detached_nine_field_context_content_only':1,
    'shallow_equal_refs_shape_does_not_authorize':1,
    'extra_context_field_rejected':1, 'wrong_nonce_reference':1,
    'same_guard_reference_content_not_live_flush_provenance':1,
    'missing_guard_null_flush_never_matches':1, 'missing_guard_real_ref_refused':1,
    'explicit_null_guard_null_flush_refused':1, 'wrong_flush_ref_refused':1, 'wrong_guard_refused':1,
    'non_refcounted_requested_flush_refused':5, 'non_refcounted_active_flush_refused':5,
    'fake_calls_create_no_success_authority':1,
    'unbound_completion_fails_closed':1, 'unbound_reset_completion_fails_closed':1,
    'unbound_expiry_completion_fails_closed':1,
    **{label:2 for label in ['fake_actual_true_does_not_authorize','fake_mini_play_preflight_refused',
       'fake_context_cannot_begin_native_operation','unbound_insert_refused','unissued_mini_board_refused',
       'unissued_token_refused','fake_waiting_ticket_refused','fake_child_factory_refused',
       'unbound_child_receive_refused','fake_empty_flush_close_cannot_self_sign_ready','unissued_cast_refused',
       'unbound_reset_begin_refused','unbound_expiry_begin_refused']},
    **{'missing_context_field_'+key:1 for key in ['owner','unit','target','nonce','index','position','round','sequence','kind']},
    **{'copied_context_reference_'+key:1 for key in ['owner','unit','target']},
}


def validate_legacy_permanent_pure(log,expected_checks):
    marker='DARKCREST_LAVA_PERMANENT_CONTENT_CONTRACT '
    rows=[json.loads(line.removeprefix(marker)) for line in log.splitlines() if line.startswith(marker)]
    require(len(rows)==1, 'Exactly one new pure summary required')
    row=rows[0]
    exact_keys(row,['passed','failed','failures','real_game_run','scope','actual_provenance_proven'],'Mini pure summary')
    integer_fields(row,['passed','failed'])
    require(row['passed']==expected_checks==LEGACY_PERMANENT_PURE_CHECKS and row['failed']==0 and row['failures']==[], 'Legacy Mini permanent pure count/failure mismatch')
    require(row['scope']==PERMANENT_PURE_SCOPE and row['real_game_run'] is False and row['actual_provenance_proven'] is False, 'Detached pure must not claim actual provenance/Game')
    require(sum(line.startswith('PASS ') for line in log.splitlines())==row['passed'], 'Legacy Mini permanent pure PASS count mismatch')
    marker_counts(log,PERMANENT_PURE_MARKERS)
    return row['passed'],None

# Godot 4 Variant enum: BOOL=1, INT=2, STRING=4, STRING_NAME=21,
# DICTIONARY=27, ARRAY=28. This is a source-shape diagnostic, never authority.
NATIVE_PREVIEW_TOP_TYPES = {
    **{key:(4,4) for key in ['uid','card_id','name','kind','text','image']},
    **{key:(4,2) for key in ['tier','attack','health','cost','pool_count','spellcraft_kept','spell_triggers',
                           'blood_gems_received_turn','recruit_shop_aura_attack','recruit_shop_aura_health']},
    **{key:(4,1) for key in ['golden','temporary','is_spellcraft','individually_frozen']},
    **{key:(4,28) for key in ['keywords','tribes','effects','temporary_buffs','permanent_keywords','attachments',
                            'pool_components','magnetic_tribes']},
    'recruit_shop_bonus_applied':(4,27), 'max_health':(21,2),
    'base_unit':(21,27), 'expires_at_end_turn':(21,1),
}
NATIVE_PREVIEW_BASE_TYPES = {
    **{key:(4,4) for key in ['card_id','name']},
    **{key:(4,2) for key in ['tier','attack','health','max_health']},
    **{key:(4,28) for key in ['keywords','tribes','effects']}, 'golden':(4,1),
}


def validate_native_preview(diagnostic,log):
    exact_keys(diagnostic,['native_factory_preview','actual_token_issuance','uid_allocated','zone_inserted',
                          'shape_error','key_types','base_key_types'],'same-Game native preview diagnostic')
    require(diagnostic['native_factory_preview'] is True, 'Native factory preview required')
    for key in ['actual_token_issuance','uid_allocated','zone_inserted']:
        require(diagnostic[key] is False, 'Detached preview is not token issuance, UID allocation, or zone insertion')
    require(type(diagnostic['shape_error']) is str and diagnostic['shape_error']=='', 'Native preview must match complete child shape')
    for field,expected in [('key_types',NATIVE_PREVIEW_TOP_TYPES),('base_key_types',NATIVE_PREVIEW_BASE_TYPES)]:
        records=diagnostic[field]
        require(type(records) is list and len(records)==len(expected), 'Complete native key/type list required: '+field)
        seen={}
        for record in records:
            exact_keys(record,['key','key_type','value_type'],'native key/type entry')
            integer_fields(record,['key_type','value_type'])
            require(type(record['key']) is str and record['key'] not in seen, 'Unique native diagnostic key names required')
            seen[record['key']]=(record['key_type'],record['value_type'])
        require(seen==expected, 'Exact native String/StringName key and value types required: '+field)
    prefix='MINI_NATIVE_PREVIEW_KEY_TYPES '
    diagnostics=[json.loads(line.removeprefix(prefix)) for line in log.splitlines() if line.startswith(prefix)]
    require(len(diagnostics)==1 and diagnostics[0]==diagnostic, 'Exactly one native diagnostic log must equal the scenario JSON')


def native_uid(value):
    require(type(value) is str and re.fullmatch(r'u[1-9][0-9]*', value) is not None, 'Original native UID required')
    return int(value[1:])


MINI_SALE_SCOPE = 'single ordinary Mini sale retains previously issued original token for same-turn first Lava cast'
MINI_SALE_PURE_SCOPE = 'detached Mini sale context and refusal only'
MINI_SALE_PURE_MARKERS = {
    **{name:1 for name in ['detached_live_source_presence_content_only','lost_source_without_retirement_rejected',
      'copied_live_source_not_original_ref','wrong_source_owner_reference_rejected','wrong_issued_source_uid_rejected',
      'detached_completed_retirement_content_only','changed_retired_source_snapshot_rejected']},
    **{'missing_retirement_fact_'+key:1 for key in ['retired_complete','retired_uid','retired_round','retired_sequence','snapshot']},
    'retired_source_reinsert_or_invalid_zone_rejected':5,
    'fake_source_custody_cannot_authorize_cast':3,'fake_source_custody_refusal_no_mutation':3,
    **{name:1 for name in ['complete_mini_sale_source_runtime_proof','detached_sale_context_shape_not_authority',
      'equal_reference_copy_shape_not_authority','extra_sale_context_rejected','same_plan_ref_deep_mutation_rejected',
      'same_plan_ref_float_equal_value_rejected','restored_detached_plan_shape_only','token_facts_exclude_only_identity_fields',
      'token_facts_preserve_all_history','token_facts_are_detached_deep_copy','fake_sale_calls_create_no_receipts_or_poison',
      'fake_retired_record_never_grants_board_authority','fake_retired_record_never_grants_sale_authority','fake_retired_checks_do_not_consume_record']},
    **{'missing_sale_context_'+key:1 for key in ['owner','sold','sold_uid','index','sales_before','round','sequence','generated_tier7_plan']},
    **{'copied_sale_context_ref_'+key:1 for key in ['owner','sold','generated_tier7_plan']},
    **{name:2 for name in ['fake_actual_cannot_authorize_mini_sale','fake_context_cannot_bind_mini_sale','unbound_mini_sale_cannot_complete']},
}


MINI_SALE_PURE_PREFIX_COUNTS = {**{'strict_sale_context_integer_'+key:6 for key in ['index','sales_before','round','sequence']},
    'strict_sale_context_uid_':5,'invalid_retirement_flag_':4,'partial_or_nonbool_completion_rejected_':4,
    'wrong_retirement_round_':5,'wrong_retirement_sequence_':6}


def validate_legacy_mini_sale_pure(log,expected_checks):
    actual=LEGACY_MINI_SALE_PURE_CHECKS
    prefix='DARKCREST_MINI_SALE_CONTENT_CONTRACT '
    rows=[json.loads(line.removeprefix(prefix)) for line in log.splitlines() if line.startswith(prefix)]
    require(len(rows)==1,'Exactly one Mini-sale pure summary')
    row=rows[0];exact_keys(row,['passed','failed','failures','real_game_run','actual_provenance_proven','scope'],'Mini-sale pure summary')
    integer_fields(row,['passed','failed'])
    require(row['passed']==expected_checks==actual and row['failed']==0 and row['failures']==[],'New pure actual counts/failures mismatch')
    require(row['scope']==MINI_SALE_PURE_SCOPE and row['real_game_run'] is False and row['actual_provenance_proven'] is False,'Pure must not claim actual sale/provenance')
    require(sum(line.startswith('PASS ') for line in log.splitlines())==actual,'Pure PASS count mismatch')
    marker_counts(log,MINI_SALE_PURE_MARKERS)
    for prefix,n in MINI_SALE_PURE_PREFIX_COUNTS.items():
        require(sum(line.startswith('PASS '+prefix) for line in log.splitlines())==n,'Exact pure rejection prefix multiplicity: '+prefix)
    return actual,None


MINI_AFTER_CAST_SCOPE = 'single ordinary Mini native first cast before same-turn sale with preserved consumed history'
MINI_AFTER_CAST_PURE_SCOPE = 'detached consumed Mini token history and unbound refusal only'
BUFFED_SALE_SCOPE='one ordinary Lava first Mini permanent buff then native sale with live Mini regrant'
BUFFED_SALE_FULL_MARKERS={'real_temporary_spell_and_reset_lava_before_cast': 1, 'other_original_board_target_held_no_consumption': 1, 'public_native_first_trident_cast': 1, 'first_trident_permanent_exact_plus2_kept1_no_temporary_layer': 1, 'cast_consumes_original_token_only_no_factory_rng_stock': 1, 'mini_cast_does_not_consume_darkcrest_growth_or_source_state': 1, 'actual_completed_cast_updates_only_observer_receipt': 1, 'used_original_token_replay_rejected_without_mutation': 1, 'original_live_mini_required_before_buffed_sale': 1, 'original_buffed_lava_sale_preflight': 1, 'copied_wrongowner_buffed_lava_sale_refused': 1, 'unbound_buffed_lava_sale_preserves_state': 1, 'public_native_buffed_lava_sell': 1, 'buffed_sale_only_original_board_departure': 1, 'buffed_sale_exact_native_accounting': 1, 'buffed_sale_no_uid_rng_and_original_absent': 1, 'buffed_lava_authority_retired': 1, 'live_mini_not_retired_by_lava_sale': 1, 'mini_token_record_reference_survives_lava_sale': 1, 'buffed_stats_do_not_leak_to_native_factory_preview': 1, 'actual_buffed_retirement_history_owner_bound': 1, 'actual_retirement_history_blocks_buy_and_play_gate': 1, 'history_gate_checks_do_not_change_live_state': 1, 'retired_buffed_lava_replay_refused_no_mutation': 1, 'original_mini_publicplay_real_waiting_grant': 1, 'one_nonempty_post_lava_sale_combat': 1, 'actual_combat_mini_present_lava_absent': 1, 'buffed_history_buy_gate_persists_next_round': 1, 'live_mini_native_regrant_without_lava': 1, 'no_lava_new_token_cast_held_without_consumption': 1, 'matrix_result_file': 1, 'complete_game_script': 1, 'complete_catalog': 1, 'same_game_native_child_preview_created': 1, 'native_preview_does_not_change_live_state_or_receipts': 1, 'native_preview_complete_child_shape_matches': 1, 'native_four_player_full_23_card_room': 1, 'mini_lava_original_hand_before_play': 1, 'copied_mini_token_rejected': 1, 'wrong_owner_mini_token_rejected': 1, 'copied_lava_target_rejected': 1, 'fabricated_mini_cast_context_rejected': 1, 'mini_preconsume_negative_calls_leave_full_state_unchanged': 1, 'actual_original_lava_preflight': 1, 'copied_lava_preflight_rejected': 1, 'wrong_owner_preflight_rejected': 1, 'fabricated_live_play_context_rejected': 1, 'no_live_completion_without_native_context': 1, 'preplay_rejections_preserve_all_live_state': 1, 'original_lava_object_unchanged_after_play': 1, 'actual_completed_original_lava_board_custody': 1, 'copied_board_lava_rejected': 1, 'wrong_owner_board_lava_rejected': 1, 'completed_transaction_replay_rejected': 1, 'postplay_rejections_clear_and_preserve_live_state': 1, 'lava_play_is_only_original_hand_to_board_no_birth_rng_or_stock': 1, 'native_parent_offer_and_gold': 1, 'native_parent_purchase': 1, 'pre_source_original_purchase_BG23_000': 1, 'pre_source_original_purchase_BG23_009': 1, 'public_original_lava_play_position_0': 1, 'native_eot_context_released': 1, 'one_real_mini_trident_in_original_hand': 3, 'original_waiting_token_bound_to_exact_mini_owner_round': 3, 'pre_source_public_tavern_upgrade_3': 1, 'pre_source_public_tavern_upgrade_4': 1, 'pre_source_public_tavern_upgrade_5': 1, 'native_opponent_tier1_offer_and_gold_1': 1, 'native_opponent_tier1_offer_and_gold_2': 1, 'native_opponent_tier1_offer_and_gold_3': 1, 'opponent_public_buy_1': 1, 'opponent_public_buy_2': 1, 'opponent_public_buy_3': 1, 'opponent_public_nonempty_board_1': 1, 'opponent_public_nonempty_board_2': 1, 'opponent_public_nonempty_board_3': 1, 'native_opponent_ready_1': 1, 'native_opponent_ready_2': 1, 'native_opponent_ready_3': 1}

def buffed_sale_ordered_markers(round_number):
 return ['public_native_first_trident_cast','original_live_mini_required_before_buffed_sale','original_buffed_lava_sale_preflight','public_native_buffed_lava_sell','buffed_lava_authority_retired','actual_retirement_history_blocks_buy_and_play_gate','native_eot_combat_next_recruit_'+str(round_number),'buffed_history_buy_gate_persists_next_round','live_mini_native_regrant_without_lava','no_lava_new_token_cast_held_without_consumption']

def _validate_lava_buffed_sale_full_schema(r,log,evidence):
 require=r.require;exact=r.exact_keys;ints=r.integer_fields
 require(r.NEW_VALIDATORS_READY is True,'UNKNOWN exact buffed Lava sale validator')
 lines=log.splitlines();prefix='DARKCREST_LAVA_BUFFED_SALE_REAL_MATRIX_PASS'
 require(lines.count('DARKCREST_LAVA_BUFFED_SALE_MATRIX_LOAD_BEGIN')==1,'Exactly one new initializer')
 markers=[line for line in lines if line.startswith(prefix)];require(len(markers)==1,'Exactly one full result')
 match=re.fullmatch(prefix+r' cases=1 casts=1 combats=1 checks=([1-9][0-9]*)',markers[0]);require(match is not None,'Exact one-case/cast/combat result')
 count=int(match.group(1));require(sum(line.startswith('PASS ') for line in lines)==count,'Dynamic PASS count mismatch')
 r.marker_counts(log,BUFFED_SALE_FULL_MARKERS)
 path=evidence/r.NEW_TEST_METADATA['scenario_file'];require(path.is_file() and not path.is_symlink(),'Actual external scenario required')
 row=r.read_json(path)
 exact(row,['scope','seed','checks','sale','casts','darkcrest_uid','darkcrest_final_tier','mini_uid','old_token_uid','new_token_uid','combat_start','native_preview_diagnostic','acquisitions','coin_pre_source_fixture','entirely_natural_game','actual_lava_rebuy_tested','old_full_matrix_repeated'],'buffed Lava sale scenario')
 ints(row,['seed','checks','darkcrest_final_tier'])
 require(row['scope']==BUFFED_SALE_SCOPE==r.NEW_TEST_METADATA['scope'] and row['seed']==20261120,'Exact scoped seed')
 require(row['checks']==count-1 and row['darkcrest_final_tier']==2,'Pre-file count and acquisition-card level')
 require(row['coin_pre_source_fixture'] is True,'Disclosed Coin fixture required')
 for key in ['entirely_natural_game','actual_lava_rebuy_tested','old_full_matrix_repeated']:require(row[key] is False,'Unproven claim '+key)
 r.validate_native_preview(row['native_preview_diagnostic'],log)
 sale=row['sale'];exact(sale,['lava_uid','mini_uid','index','retirement','departed_stats','gold_before','gold_after','sold_before','sold_after','stock_before','stock_after','uid_before','uid_after','rng_before','rng_after','native_preview_attack','native_preview_health','preview_not_actual_rebuy','owner_bound_history_gate_observed','actual_shop_buy_attempted'],'native buffed Lava sale')
 ints(sale,['index','gold_before','gold_after','sold_before','sold_after','stock_before','stock_after','uid_before','uid_after','rng_before','rng_after','native_preview_attack','native_preview_health'])
 bodies=[row['mini_uid'],sale['lava_uid'],row['darkcrest_uid']]
 for uid in bodies:r.native_uid(uid)
 require(len(set(bodies))==3 and sale['mini_uid']==row['mini_uid'] and sale['index']==0,'Exact original sale/source/position')
 old_token=r.native_uid(row['old_token_uid']);new_token=r.native_uid(row['new_token_uid'])
 require(old_token>max(r.native_uid(x) for x in bodies) and new_token>old_token,'Distinct original native token identities')
 require(sale['uid_before']==sale['uid_after']>old_token and new_token>=sale['uid_after'],'Sale allocates no UID; later regrant is new')
 for key in ['gold','sold','stock']:require(sale[key+'_before']>=0 and sale[key+'_after']==sale[key+'_before']+1,'Exact native '+key+' delta')
 require(sale['rng_before']==sale['rng_after'],'Sale must not change RNG')
 require((sale['native_preview_attack'],sale['native_preview_health'])==(2,5),'Returned stock/native preview must not inherit buff')
 require(sale['preview_not_actual_rebuy'] is True and sale['owner_bound_history_gate_observed'] is True and sale['actual_shop_buy_attempted'] is False,'Only actual-ledger denial observation, not real shop rebuy')
 retirement=sale['retirement'];exact(retirement,['owner','round','sequence','mini_buffed'],'native retirement');ints(retirement,['owner','round','sequence'])
 require(retirement['owner']==0 and retirement['round']>0 and retirement['sequence']>0 and retirement['mini_buffed'] is True,'Original owner-bound buffed retirement')
 departed=sale['departed_stats'];exact(departed,['attack','health','kept'],'departed stats');ints(departed,['attack','health','kept']);require(departed=={'attack':4,'health':5,'kept':1},'Single first Mini +2 kept1 before sale')
 require(type(row['casts']) is list and len(row['casts'])==1,'Exactly one original cast')
 cast=row['casts'][0];exact(cast,['round','source_uid','token_uid','target_uid','attack_before','attack_after','health','kept'],'first cast');ints(cast,['round','attack_before','attack_after','health','kept'])
 require(cast['round']==retirement['round']>0 and cast['source_uid']==row['mini_uid'] and cast['token_uid']==row['old_token_uid'] and cast['target_uid']==sale['lava_uid'],'Same-round first cast exact source/token/target')
 require((cast['attack_before'],cast['attack_after'],cast['health'],cast['kept'])==(2,4,5,1),'Single native permanent +2, not second buff')
 r.marker_counts(log,{'public_darkcrest_play_'+row['darkcrest_uid']:1,'native_eot_combat_next_recruit_'+str(cast['round']):1,'native_growth_exact_once_'+str(cast['round']):1})
 ordered=buffed_sale_ordered_markers(cast['round']);offsets=[lines.index('PASS '+key) for key in ordered];require(offsets==sorted(offsets) and len(set(offsets))==len(offsets),'Actual cast then live Mini precondition then sale then combat then regrant/hold')
 require(type(row['acquisitions']) is list and len(row['acquisitions'])==2,'Two original pre-source acquisitions')
 for acquisition,card,uid,limit in zip(row['acquisitions'],['BG23_000','BG23_009'],bodies[:2],[80,100]):
  exact(acquisition,['id','uid','rolls','source_owned'],'acquisition');ints(acquisition,['rolls']);require(acquisition['id']==card and acquisition['uid']==uid and 0<=acquisition['rolls']<=limit and acquisition['source_owned'] is False,'Original acquisition with bounded rolls')
 combat=row['combat_start'];require(type(combat) is dict,'Actual combat_start event')
 # Native combat event/unit fields are extensible. All scenario-owned dictionaries are exact;
 # here validate mandatory native fields without inventing an exhaustive engine-event schema.
 required={'event','sequence','seed','rules','sort_formation_contract','left','right','left_hand_count','right_hand_count','left_hand_summon_locks','right_hand_summon_locks','round_up_plain_contract'}
 require(required<=set(combat),'Complete native combat_start required');ints(combat,['sequence','seed','left_hand_count','right_hand_count'])
 require(combat['event']=='combat_start' and combat['rules']=='sandbox-1' and combat['sort_formation_contract']=='actual_combat_start_before_start_effects_v1' and combat['sequence']>=0,'Native combat_start identity')
 sides=[];all_uids=[]
 for side in ['left','right']:
  board=combat[side];require(type(board) is list and board,'Nonempty actual combat sides')
  require(type(combat[side+'_hand_summon_locks']) is list and combat[side+'_hand_count']>=0,'Native hand counts and locks')
  for unit in board:
   require(type(unit) is dict,'Native public combat unit');r.native_uid(unit.get('uid'));ints(unit,['attack','health','max_health']);require(unit.get('kind')=='minion' and type(unit.get('golden')) is bool and type(unit.get('card_id')) is str and unit['attack']>=0 and unit['health']>0 and unit['max_health']>=unit['health'],'Native living minion combat shape');all_uids.append(unit['uid'])
  if any(unit['uid']==row['mini_uid'] for unit in board):sides.append(board)
 require(len(set(all_uids))==len(all_uids) and sale['lava_uid'] not in all_uids and len(sides)==1,'Departed Lava absent and exactly one original Mini combat side')
 own=sides[0];require({x['uid'] for x in own}=={row['mini_uid'],row['darkcrest_uid']} and len(own)==2,'Only original Mini and Darkcrest remain on player board')
 for uid,card in [(row['mini_uid'],'BG23_000'),(row['darkcrest_uid'],'BG31_920')]:
  unit=next(x for x in own if x['uid']==uid);require(unit['card_id']==card and unit['golden'] is False,'Original ordinary surviving source bodies')
 return count,row


def validate_lava_buffed_sale_full(log,evidence):
    import sys
    return _validate_lava_buffed_sale_full_schema(sys.modules[__name__],log,evidence)

BUFFED_SALE_PURE_SCOPE = 'buffed departure denial history and unbound refusal only'
BUFFED_SALE_PURE_MARKERS = {**{name:1 for name in ['complete_buffed_sale_source_runtime_proof','empty_history_not_buffed_departure','untouched_native_sale_history_not_blocked','mixed_history_finds_only_matching_denial','history_predicate_does_not_mutate_records','fabricated_history_shape_is_denial_not_authority','isolated_history_reset_shape_only','fake_calls_create_no_success_or_retirement']},'fake_actual_buffed_sale_authority_refused':2,'fake_buffed_sale_preflight_refused':2,'fake_native_buffed_sale_context_refused':2}
BUFFED_SALE_PURE_PREFIX_COUNTS = {'detached_buffed_history_denial_owner_':8,'other_owner_history_not_applied_':8,'invalid_history_owner_type_':4,'invalid_history_buff_flag_':5,'unissued_buff_receipt_never_authorizes_sale_':5}

def validate_lava_buffed_sale_pure(log,expected_checks):
    actual=NEW_TEST_METADATA.get('pure_checks');require(type(actual) is int and actual>0,'UNKNOWN actual new pure count')
    prefix='DARKCREST_LAVA_BUFFED_SALE_CONTENT_CONTRACT '
    rows=[json.loads(line.removeprefix(prefix)) for line in log.splitlines() if line.startswith(prefix)]
    require(len(rows)==1,'Exactly one buffed sale pure summary')
    row=rows[0];exact_keys(row,['passed','failed','failures','real_game_run','actual_provenance_proven','scope'],'buffed sale pure')
    integer_fields(row,['passed','failed'])
    require(row['passed']==expected_checks==actual and row['failed']==0 and row['failures']==[],'New pure actual count/failure mismatch')
    require(row['scope']==BUFFED_SALE_PURE_SCOPE and row['real_game_run'] is False and row['actual_provenance_proven'] is False,'Denial history content is not actual retirement, shop purchase, or issued authority')
    require(sum(line.startswith('PASS ') for line in log.splitlines())==actual,'New pure exact PASS count mismatch')
    marker_counts(log,BUFFED_SALE_PURE_MARKERS)
    for prefix,n in BUFFED_SALE_PURE_PREFIX_COUNTS.items():
        require(sum(line.startswith('PASS '+prefix) for line in log.splitlines())==n,'Required strict buffed-sale rejection prefix: '+prefix)
    return actual,None


MINI_AFTER_CAST_PURE_MARKERS = {
 **{name:1 for name in ['complete_after_cast_source_runtime_proof','detached_consumed_history_content_not_authority',
  'explicit_unexpired_consumed_content','copied_history_owner_refused','content_checks_leave_original_fixtures_unchanged',
  'equal_detached_token_content_does_not_prove_issued_identity','fake_consumed_history_cannot_install_receipts']},
 **{'missing_consumed_history_'+key:1 for key in ['owner','unit','source_uid','round','ready','used','cast_sequence','cast_target_uid','snapshot']},
 'consumed_token_reappeared_or_invalid_zone':8,'fake_actual_consumed_sale_refused':2,'unissued_consumed_sale_preflight_refused':2}
MINI_AFTER_CAST_PURE_PREFIX_COUNTS = {'wrong_consumed_source_':5,'wrong_consumed_round_':6,
 'incomplete_consumed_flag_ready':5,'incomplete_consumed_flag_used':5,'expired_or_wrongtype_history_':5,
 'invalid_prior_cast_sequence_':7,'invalid_cast_target_uid_':5,'invalid_consumed_snapshot_':5,
 'invalid_consumed_unit_':4,'invalid_consumed_token_identity_uid':5,'invalid_consumed_token_identity_card_id':5}


def validate_legacy_mini_after_cast_pure(log,expected_checks):
    actual=LEGACY_MINI_AFTER_CAST_PURE_CHECKS
    prefix='DARKCREST_MINI_AFTER_CAST_CONTENT_CONTRACT '
    rows=[json.loads(line.removeprefix(prefix)) for line in log.splitlines() if line.startswith(prefix)]
    require(len(rows)==1,'Exactly one consumed-history pure summary')
    row=rows[0];exact_keys(row,['passed','failed','failures','real_game_run','actual_provenance_proven','scope'],'consumed-history pure')
    integer_fields(row,['passed','failed'])
    require(row['passed']==expected_checks==actual and row['failed']==0 and row['failures']==[],'New pure actual count/failure mismatch')
    require(row['scope']==MINI_AFTER_CAST_PURE_SCOPE and row['real_game_run'] is False and row['actual_provenance_proven'] is False,'Detached consumed history is not actual native sale or issued authority')
    require(sum(line.startswith('PASS ') for line in log.splitlines())==actual,'New pure exact PASS count mismatch')
    marker_counts(log,MINI_AFTER_CAST_PURE_MARKERS)
    for prefix,n in MINI_AFTER_CAST_PURE_PREFIX_COUNTS.items():
        require(sum(line.startswith('PASS '+prefix) for line in log.splitlines())==n,'Required strict consumed-history rejection prefix: '+prefix)
    return actual,None


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
    require(commit == FROZEN_SOURCE_COMMIT, 'Source commit is not the reviewed published freeze')
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
    require(limit >= (3 * 1024**3 if label == 'lava_buffed_sale_real_matrix' else 512 * 1024**2), 'Insufficient memory for guarded test')
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
                 'old_full_matrices_repeated': False, 'planned_scope': PLANNED_SCOPE, 'new_test_metadata': NEW_TEST_METADATA,
                 'full_game_acceptance': False, 'default_pool_promoted': False, 'new_native_permanence_algorithm_added': False,
                 'scope': NEW_TEST_METADATA['scope']}
        write_new(root / 'INDEPENDENT_GAME_VERIFICATION.json', final)
        print('DARKCREST_MINI_AFTER_CAST_SINGLE_RUNTIME_AND_DUAL_SOURCE_REHASH_PASS', flush=True)


if __name__ == '__main__':
    main()
