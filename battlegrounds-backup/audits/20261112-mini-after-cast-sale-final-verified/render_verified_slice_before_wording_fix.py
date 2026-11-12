"""Pure Chinese cast-before-sale evidence renderer, no Game, uploads or invented totals."""
import json
import run_remote_mini_after_cast as runner

def render_slice(summary,audit,final,scenario,commit):
 from packaging_common import outcome_metadata
 outcome=outcome_metadata(summary,audit,final)
 assert all(row.get('source_commit')==commit for row in [summary,audit]+([final] if final else []))
 if outcome=='failure':
  assert scenario is None
  classes={key:value['classification'] for key,value in audit['tests'].items()}
  executed=[key for key,value in audit['tests'].items() if value.get('process_started') is True]
  omitted=[key for key,value in audit['tests'].items() if value['classification']=='omitted']
  not_started=[key for key,value in audit['tests'].items() if value['classification'] in ['omitted','preflight_only_not_started','launch_failed_not_executed']]
  uncertain=[key for key,value in audit['tests'].items() if value['classification']=='launch_or_execution_without_completion_receipt']
  validated={key:value['revalidated_checks'] for key,value in audit['tests'].items() if value['classification']=='executed_validated'}
  assert all(type(n) is int and n>0 for n in validated.values())
  prefix='首次新 Game 失败，后续 11 份纯合同全部未运行，不能计为通过。\n\n' if classes[runner.TESTS[0][0]]=='process_failed' and len(omitted)==11 else ''
  detail='\n'.join('- '+key+'：'+value for key,value in classes.items())
  return f'''# Mini 先施法后出售切片未获验收

源码：{commit}。本次失败或未完成，未运行、结果不明或证据不足项目不计为通过。

{prefix}确认启动 {len(executed)} 项；明确未启动 {len(not_started)} 项，其中完全未运行 {len(omitted)} 项；结果待确认 {len(uncertain)} 项。审计验证的检查数仅为 {validated}。

新 pure 预冻结85项与既有10份纯合同3163项不能自动算作本轮通过。原错误：{summary.get('error')}。

逐测试分类：
{detail}

原日志、源码与完整源哈希观察均保留，不通过包装改变结论。旧完整Game不重跑；本页不表示默认启用、全卡池或全游戏验收。
'''
 assert runner.NEW_VALIDATORS_READY is True and isinstance(scenario,dict)
 full=final['tests']['mini_after_cast_real_matrix'];assert full['verified_scenario_fields']==scenario
 actual_full=full['passed_checks'];assert type(actual_full) is int and actual_full>0
 pure={key:value['passed_checks'] for key,value in final['tests'].items() if key!='mini_after_cast_real_matrix'}
 expected={label:count for label,_,_,count in runner.TESTS[1:]};assert pure==expected and all(type(n) is int and n>0 for n in pure.values())
 new_pure=pure['mini_after_cast_content_contract'];assert new_pure==runner.NEW_TEST_METADATA['pure_checks']
 old_pure=sum(n for key,n in pure.items() if key!='mini_after_cast_content_contract');assert old_pure==3163
 assert scenario['scope']==runner.MINI_AFTER_CAST_SCOPE and len(scenario['casts'])==len(scenario['combats'])==1
 sale=scenario['sale'];cast=scenario['casts'][0];combat=scenario['combats'][0]
 assert scenario['cast_before_sale'] is True and scenario['ready_token_at_sale'] is False
 assert sale['mini_uid']==scenario['mini_uid'] and sale['token_uid']==cast['token_uid']
 assert all(sale[key] is True for key in ['retired','token_same_reference','token_record_same_reference','token_used_before_sale','token_absent_from_zones'])
 assert cast['source_uid']==scenario['mini_uid'] and cast['target_uid']==scenario['lava_uid'] and cast['round']==sale['round']==1
 assert (cast['attack_before'],cast['attack_after'],cast['health'],cast['kept'])==(2,4,5,1)
 assert (combat['recruit_attack'],combat['recruit_health'],combat['recruit_kept'])==(4,5,0)
 assert scenario['darkcrest_final_tier']==2 and scenario['no_next_round_mini_token'] is True
 assert scenario['coin_pre_source_fixture'] is True and all(scenario[key] is False for key in ['entirely_natural_game','sold_source_unused_expiry_tested','old_full_matrix_repeated'])
 runner.validate_native_preview(scenario['native_preview_diagnostic'],'MINI_NATIVE_PREVIEW_KEY_TYPES '+json.dumps(scenario['native_preview_diagnostic'])+'\n')
 return f'''# 已验证的有限玩法：Mini 先施法再原生出售

源码：{commit}。

唯一普通 Mini 原生发出三叉戟，先对原普通 Lava 施放本回合第一张塑造，2/5 → 4/5、kept 1。该原 token 已消费并离开全部区域，手中没有 child；随后以公开 sell 命令出售原 Mini，按原生机制返金、返池并记录出售。

已消耗 token 的原对象和原凭据历史保持不变，不重新发牌或恢复使用权限。一次真实非空战斗及下轮招募后，Lava 仍4/5、kept重置0，暗潮成长至2级，离场Mini不再发牌。实际日志顺序严格为先cast、确认已消费、再sell、最后combat。

实际检查：新 Game {actual_full} 项；新 pure {new_pure} 项；10份既有纯合同 {old_pure} 项；总计 {actual_full+new_pure+old_pure} 项。只执行一棵新 restored_snapshot，候选与恢复树分别完整核验；旧完整Game不重跑，不称两个runtime。

资金使用已披露的源激活前Coin夹具，不称无夹具自然对局。preview仅为形状诊断；纯合同的消费历史内容判定和fake权限拒绝不冒充真实权限或live故障注入。

不开放第二Mini、重买、金色、额外目标或任意token复制，也不新增Lava永久算法。不代表默认启用、全卡池或全游戏验收。保留既有source a96a033 / accepted final d914d669及更早历史。
'''
