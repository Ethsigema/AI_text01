"""Synthetic Chinese renderer tests only. No Game, logs or package operations."""
import copy,json
from render_verified_slice import render_slice,runner
from test_mini_after_cast_schema_synthetic import full_fixture
labels=[row[0] for row in runner.TESTS];commit='a'*40
original_tests=runner.TESTS;original_count=runner.NEW_TEST_METADATA['pure_checks']
runner.TESTS=[(label,name,budget,85 if label=='mini_after_cast_content_contract' else count) for label,name,budget,count in runner.TESTS]
runner.NEW_TEST_METADATA['pure_checks']=85
scenario,_,_=full_fixture()
s={'source_commit':commit,'runtime_mode':runner.RUNTIME_MODE,'two_runtime_copies':False,'status':'TESTS_VALIDATED_SOURCE_INTEGRITY_PASS','error':None,'validated_tests':labels}
a={'source_commit':commit,'runtime_mode':runner.RUNTIME_MODE,'two_runtime_copies':False,'runner_suite_accepted':True,'status':'PASS_POST_ATTEMPT_SOURCE_AND_EVIDENCE_AUDIT','tests':{key:{'classification':'executed_validated','process_started':True,'revalidated_checks':count if count else 123} for key,_,_,count in runner.TESTS}}
f={'source_commit':commit,'status':runner.FINAL_STATUS,'tests':{t[0]:{'passed_checks':t[3]} for t in runner.TESTS},'full_game_processes':1,'full_game_acceptance':False,'default_pool_promoted':False,'old_full_matrices_repeated':False}
f['tests'][labels[0]]={'passed_checks':123,'verified_scenario_fields':scenario}
rendered=render_slice(s,a,f,scenario,commit)
assert str(123+85+3163) in rendered;checks=['synthetic_dynamic_new_pure_plus3061_plus_Game']
assert '暗潮的获取牌等级推进至2（不是随从星级变化）' in rendered and '暗潮成长至2级' not in rendered
checks.append('acquisition_card_level_not_minion_tier_wording')
assert '未覆盖售后未用token到期。' in rendered
checks.append('sold_source_unused_token_expiry_explicitly_not_covered')
for name,mutation in [('wrong_pure',lambda x:x[2]['tests'][labels[1]].update(passed_checks=60)),('wrong_commit',lambda x:x[0].update(source_commit='b'*40)),('old_full_repeat',lambda x:x[2].update(old_full_matrices_repeated=True)),('unproven_unused_expiry',lambda x:x[3].update(sold_source_unused_expiry_tested=True)),('second_cast',lambda x:x[3]['casts'].append(copy.deepcopy(x[3]['casts'][0]))),('wrong_same_token',lambda x:x[3]['sale'].update(token_same_reference=False)),('ready_token_at_sale',lambda x:x[3].update(ready_token_at_sale=True)),('unconsumed_token',lambda x:x[3]['sale'].update(token_used_before_sale=False))]:
 x=copy.deepcopy([s,a,f,scenario]);mutation(x)
 try:render_slice(*x,commit)
 except (AssertionError,ValueError):checks.append(name)
 else:raise AssertionError('accepted '+name)
fs={**s,'status':'FAILED_OR_INCOMPLETE_ATTEMPT','error':'synthetic failure','validated_tests':[]}
fa={**a,'runner_suite_accepted':False,'status':'FAIL_POST_ATTEMPT_AUDIT','tests':{key:{'classification':'omitted','process_started':False} for key in labels}}
fa['tests'][labels[0]]={'classification':'process_failed','process_started':True}
text=render_slice(fs,fa,None,None,commit);assert '11 份纯合同全部未运行' in text;checks.append('first_full_failure_eleven_remaining')
partial=copy.deepcopy(fa);partial['tests'][labels[0]]={'classification':'executed_validated','process_started':True,'revalidated_checks':123};partial['tests'][labels[1]]={'classification':'process_failed','process_started':True}
text=render_slice(fs,partial,None,None,commit);assert '11 份纯合同全部未运行' not in text and '明确未启动 10 项' in text;checks.append('later_pure_failure_ten_remaining')
uncertain=copy.deepcopy(fa);uncertain['tests'][labels[0]]={'classification':'launch_or_execution_without_completion_receipt','process_started':None}
text=render_slice(fs,uncertain,None,None,commit);assert '待确认 1 项' in text and '确认启动 0 项' in text;checks.append('uncertain_not_claimed_started')
runner.TESTS=original_tests;runner.NEW_TEST_METADATA['pure_checks']=original_count
print(json.dumps({'status':'PASS_SYNTHETIC_RENDERER_ONLY','passed':len(checks),'checks':checks,'game_started':False,'package_created':False,'actual_new_count_not_inferred':True}))
