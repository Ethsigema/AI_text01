"""Fixed-commit single-runtime-tree Mini cast-then-sale compatibility runner. No Game without --execute.

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

BASELINE = {'source_commit':'a96a03307c43c5641793663b99e864877543d1b5',
 'accepted_final_commit':'d914d66999536eb4250841488d09ae7ba3f82ccf',
 'old_full_matrices_repeated':False,'empty_slot_v1_v2_v3_excluded':True}
RUNTIME_MODE = 'single_new_restored_snapshot_no_run_tree_copy'
FINAL_STATUS = 'PASS_FIXED_REMOTE_MINI_AFTER_CAST_SINGLE_RUNTIME_AND_CONTRACTS_POST_TEST_DUAL_SOURCE_REHASH'
PLANNED_SCOPE = {'new_full_cases':1,'native_round_cycles':1,'native_targeted_casts':1,
 'native_mini_sales':1,'cast_before_sale':True,'sale_with_no_child_in_hand':True,
 'new_full_game_processes':1,'old_full_matrices_repeated':False,
 'second_mini_or_rebuy_or_golden_opened':False,'new_native_permanence_algorithm_added':False}
NEW_TEST_METADATA = {'status':'FROZEN_REVIEWED','full_checks_mode':'exact_PASS_count_and_JSON_checks_plus_one','pure_checks':85,
 'scenario_file':'DARKCREST_MINI_AFTER_CAST_MATRIX_RESULT.json','scope':'single ordinary Mini native first cast before same-turn sale with preserved consumed history','test_revision':'real_47e2fb62_pure_8aec0b31_cast_then_sale_v1','full_cases':1,
 'native_round_cycles':1,'native_targeted_casts':1,'native_mini_sales':1}
NEW_VALIDATORS_READY = True
FROZEN_SOURCE = {'source_files':27988,'source_bytes':1550904881,
 'source_map_sha256':'378619e4219a4f394b972d79c79e9e173c86abd562e3e4cba00f453bcc07bb9e',
 'aggregate_sha256':'5d50a63d42883f99295d40aee1daaa1ee494330644d21afe42c14d0ffc4d88ed'}
FROZEN_SOURCE_COMMIT = '610cad09b7d19fe2615201f054a68c6e1a31d79d'
LEGACY_REBUY_PURE_CHECKS = 89
LEGACY_PERMANENT_PURE_CHECKS = 344
LEGACY_MINI_SALE_PURE_CHECKS = 102
LEGACY_TEN_PURE_TOTAL = 3163

T6 = ['BG31_035', 'BG32_837', 'BG36_622', 'BG36_640']
T5 = ['BG23_008', 'BG31_920', 'BG31_925', 'BG32_111', 'BG32_820', 'BG32_835']
PINNED_TESTS = {'tests/darkcrest_lava_sale_20261112/content_contract.gd': '18570c38bb5b3d52238aa6cadb84d515ef5d8caa886c86365e79fa9a88d140f6', 'tests/darkcrest_lava_20261112/content_contract.gd': '301a5c9e56618baf42ae6ccbd80eea92f3eadc27a3fcfa02030fb51052004beb', 'tests/darkcrest_tier6_20261112/content_contract.gd': '01e5874b444db4950cd9a3a08aec18a0bd4443c28c2a17500f59ee39f38eb787', 'tests/darkcrest_tier5_20261112/content_contract.gd': 'd039a22573d7340d0779e17adbbc70b0e2f3f958334fd7c742bdd4b6e3bd6248', 'tests/darkcrest_20261112/source_eot_contract.gd': '2d37ee1063792093a0fd1ad683c2e8786f196caad43abe0c82ea831caaaf7790', 'tests/darkcrest_20261112/hand_shape_contract.gd': '1577c66e9524b4db1875309104cf55cf67d254d1e024a41b9b094fff8331fa2e', 'tests/darkcrest_20261112/seafloor_annotation_contract.gd': 'c0e0046fa010ccfb83d87bedf87a4616b23fef5e1700e88438f27f9aca6dc4cb', 'tests/darkcrest_lava_rebuy_20261112/content_contract.gd': 'e197cf58afdac7b751ab9056d3822152331416c3d1cf504f77b9177e7ede9f73', 'tests/darkcrest_lava_permanent_20261112/content_contract.gd': '2fd3807f7d983fff73fc876576fb77c1db427ccb4883383bda15ffc346de34d4', 'tests/darkcrest_mini_sale_20261112/content_contract.gd': 'e390781a2cc7af2131f06357d814472801486f2328433f3b239d3db2a443f9ef', 'tests/darkcrest_mini_after_cast_20261112/real_matrix.gd': '47e2fb62a94f1904009eeda5f24c71855573b0f6f6c8734dba84d733a121cdbf', 'tests/darkcrest_mini_after_cast_20261112/content_contract.gd': '8aec0b31be23ceed2f6b344618c70a3aedf8999fcd73358bbb0d73f8315a80dc'}
TESTS = [('mini_after_cast_real_matrix', 'tests/darkcrest_mini_after_cast_20261112/real_matrix.gd', 3600, None), ('mini_after_cast_content_contract', 'tests/darkcrest_mini_after_cast_20261112/content_contract.gd', 180, 85), ('mini_sale_content_contract', 'tests/darkcrest_mini_sale_20261112/content_contract.gd', 180, 102), ('lava_permanent_content_contract', 'tests/darkcrest_lava_permanent_20261112/content_contract.gd', 180, 344), ('lava_rebuy_content_contract', 'tests/darkcrest_lava_rebuy_20261112/content_contract.gd', 180, 89), ('lava_sale_content_contract', 'tests/darkcrest_lava_sale_20261112/content_contract.gd', 180, 140), ('lava_content_contract', 'tests/darkcrest_lava_20261112/content_contract.gd', 180, 211), ('tier6_content_contract', 'tests/darkcrest_tier6_20261112/content_contract.gd', 180, 966), ('tier5_content_contract', 'tests/darkcrest_tier5_20261112/content_contract.gd', 180, 810), ('source_eot_contract', 'tests/darkcrest_20261112/source_eot_contract.gd', 180, 68), ('hand_shape_contract', 'tests/darkcrest_20261112/hand_shape_contract.gd', 180, 166), ('seafloor_annotation_contract', 'tests/darkcrest_20261112/seafloor_annotation_contract.gd', 180, 267)]
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
    require(NEW_TEST_METADATA.get('status') == 'FROZEN_REVIEWED', 'UNKNOWN new cast-then-sale metadata: not executable')
    require(NEW_VALIDATORS_READY is True, 'UNKNOWN new validators: not executable')
    require(isinstance(NEW_TEST_METADATA.get('full_checks_mode'), str) and NEW_TEST_METADATA['full_checks_mode'] not in ['', 'UNKNOWN_NOT_FROZEN'], 'UNKNOWN full check-count contract')
    require(type(NEW_TEST_METADATA.get('pure_checks')) is int and NEW_TEST_METADATA['pure_checks'] > 0, 'UNKNOWN pure checks')
    require(type(NEW_TEST_METADATA.get('full_cases')) is int and NEW_TEST_METADATA['full_cases'] == 1 and type(NEW_TEST_METADATA.get('native_round_cycles')) is int and NEW_TEST_METADATA['native_round_cycles'] == 1 and type(NEW_TEST_METADATA.get('native_targeted_casts')) is int and NEW_TEST_METADATA['native_targeted_casts'] == 1, 'One case, one targeted cast and one native combat round required')
    require(type(NEW_TEST_METADATA.get('native_mini_sales')) is int and NEW_TEST_METADATA['native_mini_sales']==1, 'One original Mini public sale required')
    require(safe(NEW_TEST_METADATA.get('scenario_file')) and '/' not in NEW_TEST_METADATA['scenario_file'], 'UNKNOWN scenario filename')
    require(isinstance(NEW_TEST_METADATA.get('scope'), str) and NEW_TEST_METADATA['scope'] not in ['', 'UNKNOWN'], 'UNKNOWN scope')
    require(isinstance(NEW_TEST_METADATA.get('test_revision'), str) and NEW_TEST_METADATA['test_revision'] not in ['', 'UNKNOWN_NOT_FROZEN'], 'UNKNOWN reviewed test revision')
    for field in ['source_files','source_bytes']:
        require(type(FROZEN_SOURCE.get(field)) is int and FROZEN_SOURCE[field] > 0, 'UNKNOWN frozen ' + field)
    for field in ['source_map_sha256','aggregate_sha256']:
        require(re.fullmatch(r'[0-9a-f]{64}', FROZEN_SOURCE.get(field,'')) is not None, 'UNKNOWN frozen ' + field)
    require(len(TESTS) == 12 and len(set(x[0] for x in TESTS)) == 12, 'Exactly one new full Game + new pure + ten legacy pure required')
    for _, name, _, _ in TESTS:
        require(name.startswith('tests/') and re.fullmatch(r'[0-9a-f]{64}', PINNED_TESTS.get(name, '')) is not None, 'UNKNOWN pinned test path/hash: ' + name)


def validate(label, log, expected_checks, evidence):
    require(label in [x[0] for x in TESTS], 'Unknown test label: ' + label)
    failures = [line for line in log.splitlines() if re.search(r'^\s*FAIL(?:\s|$)', line)
                or any(marker in line for marker in ['SCRIPT ERROR', 'Parse Error', 'ParseError', 'COMMAND_FAILURE', 'WARNING', 'ERROR:'])]
    require(not failures, {'failure_markers': failures})
    if label == 'mini_after_cast_real_matrix': return validate_mini_after_cast_full(log,evidence)
    if label == 'mini_after_cast_content_contract': return validate_mini_after_cast_pure(log,expected_checks)
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
MINI_AFTER_CAST_FULL_MARKERS = {'complete_game_script': 1, 'complete_catalog': 1, 'native_four_player_full_23_card_room': 1, 'same_game_native_child_preview_created': 1, 'native_preview_does_not_change_live_state_or_receipts': 1, 'native_preview_complete_child_shape_matches': 1, 'pre_source_original_purchase_BG23_000': 1, 'pre_source_original_purchase_BG23_009': 1, 'pre_source_public_tavern_upgrade_3': 1, 'pre_source_public_tavern_upgrade_4': 1, 'pre_source_public_tavern_upgrade_5': 1, 'native_parent_offer_and_gold': 1, 'native_parent_purchase': 1, 'mini_lava_original_hand_before_play': 1, 'public_original_lava_play_position_0': 1, 'lava_play_is_only_original_hand_to_board_no_birth_rng_or_stock': 1, 'original_mini_publicplay_real_waiting_grant': 1, 'original_mini_sale_preflight': 1, 'copied_mini_sale_rejected': 1, 'wrong_mini_sale_owner_rejected': 1, 'unbound_mini_sale_context_rejected': 1, 'mini_sale_negative_calls_preserve_live_state': 1, 'public_original_mini_sell': 1, 'mini_sale_exact_board_removal': 1, 'mini_sale_original_token_hand_unchanged': 1, 'mini_sale_native_gold_stock_sold_deltas': 1, 'mini_sale_no_uid_rng_spellpool_change': 1, 'mini_original_record_retired_once': 1, 'retired_original_mini_cannot_sell_again': 1, 'mini_sale_completion_replay_rejected': 1, 'retired_mini_refusals_do_not_mutate': 1, 'copied_mini_token_rejected': 1, 'wrong_owner_mini_token_rejected': 1, 'copied_lava_target_rejected': 1, 'fabricated_mini_cast_context_rejected': 1, 'mini_preconsume_negative_calls_leave_full_state_unchanged': 1, 'real_temporary_spell_and_reset_lava_before_cast': 1, 'other_original_board_target_held_no_consumption': 1, 'public_native_first_trident_cast': 1, 'first_trident_permanent_exact_plus2_kept1_no_temporary_layer': 1, 'cast_consumes_original_token_only_no_factory_rng_stock': 1, 'mini_cast_does_not_consume_darkcrest_growth_or_source_state': 1, 'actual_completed_cast_updates_only_observer_receipt': 1, 'used_original_token_replay_rejected_without_mutation': 1, 'buffed_lava_sale_remains_held_no_consumption': 1, 'one_actual_mixed_board_combat': 1, 'actual_nonempty_combat_for_permanent_buff': 1, 'actual_combat_copy_includes_permanent_buff': 1, 'next_recruit_preserves_buff_and_native_kept_reset': 1, 'departed_mini_no_next_round_token': 1, 'no_mini_regrant_only_original_used_history': 1, 'matrix_result_file': 1, 'native_eot_context_released': 1, 'native_eot_combat_next_recruit_1': 1, 'native_growth_exact_once_1': 1, 'one_real_mini_trident_in_original_hand': 2, 'original_waiting_token_bound_to_exact_mini_owner_round': 2, 'native_opponent_ready_1': 1, 'native_opponent_ready_2': 1, 'native_opponent_ready_3': 1, 'native_opponent_tier1_offer_and_gold_1': 1, 'native_opponent_tier1_offer_and_gold_2': 1, 'native_opponent_tier1_offer_and_gold_3': 1, 'opponent_public_buy_1': 1, 'opponent_public_buy_2': 1, 'opponent_public_buy_3': 1, 'opponent_public_nonempty_board_1': 1, 'opponent_public_nonempty_board_2': 1, 'opponent_public_nonempty_board_3': 1, 'original_cast_consumed_only_ready_token_before_sale': 1, 'actual_completed_cast_history_allows_sale': 1, 'consumed_token_history_preserved_across_sale': 1}

def validate_mini_after_cast_full(log,evidence):
    require(NEW_VALIDATORS_READY is True,'UNKNOWN Mini-sale exact validator')
    lines=log.splitlines();prefix='DARKCREST_MINI_AFTER_CAST_REAL_MATRIX_PASS'
    require(lines.count('DARKCREST_MINI_AFTER_CAST_MATRIX_LOAD_BEGIN')==1,'Exactly one new Mini-sale initializer')
    markers=[line for line in lines if line.startswith(prefix)]
    require(len(markers)==1,'Exactly one Mini-sale full result marker')
    match=re.fullmatch(prefix+r' cases=1 casts=1 combats=1 checks=([1-9][0-9]*)',markers[0])
    require(match is not None,'Exact single-case/single-cast/single-combat result required')
    count=int(match.group(1));require(sum(line.startswith('PASS ') for line in lines)==count,'Dynamic PASS count mismatch')
    marker_counts(log,MINI_AFTER_CAST_FULL_MARKERS)
    path=evidence/NEW_TEST_METADATA['scenario_file'];require(path.is_file() and not path.is_symlink(),'Actual external Mini-sale scenario required')
    row=read_json(path)
    exact_keys(row,['scope','seed','checks','acquisitions','native_preview_diagnostic','sale','casts','combats','darkcrest_uid',
       'darkcrest_final_tier','lava_uid','mini_uid','no_next_round_mini_token','coin_pre_source_fixture','entirely_natural_game',
       'sold_source_unused_expiry_tested','old_full_matrix_repeated','cast_before_sale','ready_token_at_sale'],'Mini cast-before-sale scenario')
    integer_fields(row,['seed','checks','darkcrest_final_tier'])
    require(row['scope']==MINI_AFTER_CAST_SCOPE==NEW_TEST_METADATA['scope'] and row['seed']==20261120,'Exact sale scope/seed required')
    require(row['checks']==count-1 and row['darkcrest_final_tier']==2,'Pre-file check count/source level mismatch')
    require(row['no_next_round_mini_token'] is True and row['coin_pre_source_fixture'] is True,'No regrant and disclosed Coin fixture required')
    for key in ['entirely_natural_game','sold_source_unused_expiry_tested','old_full_matrix_repeated']:
        require(row[key] is False,'Unproven scope claim: '+key)
    require(row['cast_before_sale'] is True and row['ready_token_at_sale'] is False,'Only consumed original token history can authorize this new sale path')
    ordered=['public_native_first_trident_cast','original_cast_consumed_only_ready_token_before_sale','actual_completed_cast_history_allows_sale','public_original_mini_sell','consumed_token_history_preserved_across_sale','native_eot_combat_next_recruit_1']
    offsets=[lines.index('PASS '+name) for name in ordered]
    require(offsets==sorted(offsets) and len(set(offsets))==len(offsets),'Actual cast must precede no-child native sale and then combat')
    validate_native_preview(row['native_preview_diagnostic'],log)
    bodies=[row[key] for key in ['mini_uid','lava_uid','darkcrest_uid']]
    for value in bodies:native_uid(value)
    require(len(set(bodies))==3,'Distinct original bodies required')
    marker_counts(log,{'public_darkcrest_play_'+row['darkcrest_uid']:1})
    require(type(row['acquisitions']) is list and len(row['acquisitions'])==2,'Exactly two pre-source acquisitions')
    for acquisition,card,uid,limit in zip(row['acquisitions'],['BG23_000','BG23_009'],bodies[:2],[80,100]):
        exact_keys(acquisition,['id','uid','rolls','source_owned'],'pre-source original acquisition')
        integer_fields(acquisition,['rolls'])
        require(acquisition['id']==card and acquisition['uid']==uid and 0<=acquisition['rolls']<=limit and acquisition['source_owned'] is False,'Bounded original pre-source acquisition mismatch')
    sale=row['sale']
    exact_keys(sale,['mini_uid','token_uid','index','round','gold_before','gold_after','stock_before','stock_after','sold_before','sold_after',
      'uid_before','uid_after','rng_before','rng_after','retired','retired_sequence','token_same_reference','token_record_same_reference','token_used_before_sale','token_absent_from_zones'],'original Mini sale after cast')
    integer_fields(sale,['index','round','gold_before','gold_after','stock_before','stock_after','sold_before','sold_after','uid_before','uid_after','rng_before','rng_after','retired_sequence'])
    require(sale['mini_uid']==row['mini_uid'] and sale['index']==1 and sale['round']==1,'Original Mini public sale position/round mismatch')
    require(sale['gold_before']>=0 and sale['gold_after']==sale['gold_before']+1 and sale['stock_before']>=0 and sale['stock_after']==sale['stock_before']+1 and sale['sold_before']>=0 and sale['sold_after']==sale['sold_before']+1,'Native sale exact gold/stock/sold deltas required')
    token_number=native_uid(sale['token_uid'])
    require(sale['uid_before']==sale['uid_after']>token_number>max(native_uid(x) for x in bodies),'Sale must not allocate another UID')
    require(sale['rng_before']==sale['rng_after'] and sale['retired_sequence']>0,'Sale RNG/retirement sequence mismatch')
    require(all(sale[key] is True for key in ['retired','token_same_reference','token_record_same_reference','token_used_before_sale','token_absent_from_zones']),'Original retirement and preserved token references required')
    require(type(row['casts']) is list and len(row['casts'])==1,'Exactly one pre-sale cast')
    cast=row['casts'][0]
    exact_keys(cast,['round','source_uid','token_uid','target_uid','attack_before','attack_after','health','kept'],'pre-sale cast')
    integer_fields(cast,['round','attack_before','attack_after','health','kept'])
    require(cast['round']==sale['round']==1 and cast['source_uid']==row['mini_uid'] and cast['token_uid']==sale['token_uid'] and cast['target_uid']==row['lava_uid'],'Sale must preserve the exact earlier consumed original token history')
    require((cast['attack_before'],cast['attack_after'],cast['health'],cast['kept'])==(2,4,5,1),'Exact first permanent +2/kept1')
    require(type(row['combats']) is list and len(row['combats'])==1,'Exactly one actual combat/recruit')
    combat=row['combats'][0]
    exact_keys(combat,['round','target_uid','combat_start','recruit_attack','recruit_health','recruit_kept'],'post-sale combat/recruit')
    integer_fields(combat,['round','recruit_attack','recruit_health','recruit_kept'])
    require(combat['round']==1 and combat['target_uid']==row['lava_uid'] and (combat['recruit_attack'],combat['recruit_health'],combat['recruit_kept'])==(4,5,0),'Permanent4/5 preserved and kept reset')
    unit=combat['combat_start'];require(type(unit) is dict,'Original combat snapshot dictionary')
    integer_fields(unit,['attack','health','max_health'])
    require(unit['uid']==row['lava_uid'] and unit['card_id']=='BG23_009' and unit['kind']=='minion' and unit['golden'] is False and (unit['attack'],unit['health'],unit['max_health'])==(4,5,5),'Actual non-golden Lava combat copy with permanent buff')
    return count,row


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


def validate_mini_after_cast_pure(log,expected_checks):
    require(NEW_VALIDATORS_READY is True,'UNKNOWN exact cast-before-sale validator')
    actual=NEW_TEST_METADATA.get('pure_checks');require(type(actual) is int and actual>0,'UNKNOWN actual new pure count')
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
    require(limit >= (3 * 1024**3 if label == 'mini_after_cast_real_matrix' else 512 * 1024**2), 'Insufficient memory for guarded test')
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
