"""Pure Chinese Mini-sale evidence renderer; never runs Game or invents counts."""
import json
import run_remote_mini_sale as runner

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
  prefix='本轮首次新 Game 失败，后续 10 份纯合同全部未运行，不能计为通过。\n\n' if classes[runner.TESTS[0][0]]=='process_failed' and len(omitted)==10 else ''
  detail='\n'.join('- '+key+'：'+value for key,value in classes.items())
  return f'''# Mini 原生出售切片未获验收

源码：{commit}。实际尝试失败或未完成，未运行、结果不明或证据不足项目不计为通过。

{prefix}确认启动 {len(executed)} 项；明确未启动 {len(not_started)} 项，其中完全未运行 {len(omitted)} 项；启动或完成状态待确认 {len(uncertain)} 项。已由审计验证的检查数仅为 {validated}。

新 pure 的预冻结检查与基线已有 3061 项纯合同、旧131项 Game，都不能自动算作本轮通过。实际错误：{summary.get('error')}。

逐测试分类：
{detail}

保留原日志、失败源码和完整源哈希观察，不因包装而升级为玩法验收。修复另建候选；不改写此前 accepted source0b2962c/final7f88，也不重跑旧完整矩阵。
'''
 assert runner.NEW_VALIDATORS_READY is True and isinstance(scenario,dict)
 full=final['tests']['mini_sale_real_matrix'];assert full['verified_scenario_fields']==scenario
 actual_full=full['passed_checks'];assert type(actual_full) is int and actual_full>0
 pure={key:value['passed_checks'] for key,value in final['tests'].items() if key!='mini_sale_real_matrix'}
 expected={label:count for label,_,_,count in runner.TESTS[1:]}
 assert pure==expected and all(type(n) is int and n>0 for n in pure.values())
 new_pure=pure['mini_sale_content_contract'];assert new_pure==runner.NEW_TEST_METADATA['pure_checks']
 old_pure=sum(n for key,n in pure.items() if key!='mini_sale_content_contract');assert old_pure==3061
 assert scenario['scope']==runner.MINI_SALE_SCOPE and len(scenario['casts'])==len(scenario['combats'])==1
 sale=scenario['sale'];cast=scenario['casts'][0];combat=scenario['combats'][0]
 assert sale['mini_uid']==scenario['mini_uid'] and sale['token_uid']==cast['token_uid']
 assert sale['retired'] is True and sale['token_same_reference'] is True and sale['token_record_same_reference'] is True
 assert cast['source_uid']==scenario['mini_uid'] and cast['target_uid']==scenario['lava_uid'] and cast['round']==sale['round']==1
 assert (cast['attack_before'],cast['attack_after'],cast['health'],cast['kept'])==(2,4,5,1)
 assert (combat['recruit_attack'],combat['recruit_health'],combat['recruit_kept'])==(4,5,0)
 assert scenario['darkcrest_final_tier']==2 and scenario['no_next_round_mini_token'] is True
 assert scenario['coin_pre_source_fixture'] is True and all(scenario[key] is False for key in ['entirely_natural_game','sold_source_unused_expiry_tested','old_full_matrix_repeated'])
 runner.validate_native_preview(scenario['native_preview_diagnostic'],'MINI_NATIVE_PREVIEW_KEY_TYPES '+json.dumps(scenario['native_preview_diagnostic'])+'\n')
 return f'''# 已验证的有限玩法：Mini 原生出售后既有三叉戟保留

源码：{commit}。

唯一普通 Mini 经原生机制发出原始三叉戟后，以公开 sell 命令出售。真实手牌中的原 token 及其原记录仍保留，同回合对原普通 Lava 施放本轮第一张塑造，2/5 → 4/5、kept 1。一次真实非空战斗后进入下轮招募，永久攻击保留、kept 重置为0，暗潮成长至2级；已离场 Mini 不再发牌。

实际检查：新 Game {actual_full} 项；新 pure {new_pure} 项；9 份既有纯合同 {old_pure} 项；总计 {actual_full+new_pure+old_pure} 项。旧131项完整 Game 未重跑。所有运行仅使用一棵新的完整 restored_snapshot；候选与恢复树分别做完整源核验，不称两个 runtime。

使用已披露的暗潮激活前 Coin 夹具，不称为无夹具自然对局。原生 preview 是形状诊断，不是发牌；fake source-custody 负例只验证早期权限拒绝；另有深层内容谓词检查，但均不是 live 故障注入或伪造真实权限。

本批不覆盖售后未用 token 到期，不开放第二 Mini、重买或金色，不代表全卡池/默认启用/全游戏验收。Lava 原永久算法本来已存在，此处仅为有限出售后的来源生命周期兼容。此前 source0b2962c / accepted final7f88 以及更早失败历史保留。
'''
