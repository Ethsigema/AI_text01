"""Pure Chinese buffed Lava-sale evidence renderer, no Game, uploads or invented totals."""
import json
import run_remote_lava_buffed_sale as runner

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
  prefix='首次新 Game 失败，后续 12 份纯合同全部未运行，不能计为通过。\n\n' if classes[runner.TESTS[0][0]]=='process_failed' and len(omitted)==12 else ''
  detail='\n'.join('- '+key+'：'+value for key,value in classes.items())
  return f'''# Buffed Lava 原生出售切片未获验收

源码：{commit}。本次失败或未完成，未运行、结果不明或证据不足项目不计为通过。

{prefix}确认启动 {len(executed)} 项；明确未启动 {len(not_started)} 项，其中完全未运行 {len(omitted)} 项；结果待确认 {len(uncertain)} 项。审计验证的检查数仅为 {validated}。

新 pure 预冻结44项与既有11份纯合同3248项不能自动算作本轮通过。原错误：{summary.get('error')}。

逐测试分类：
{detail}

原日志、源码与完整源哈希观察均保留，不通过包装改变结论。旧完整Game不重跑；本页不表示默认启用、全卡池或全游戏验收。
'''
 assert runner.NEW_VALIDATORS_READY is True and isinstance(scenario,dict)
 full=final['tests']['lava_buffed_sale_real_matrix'];assert full['verified_scenario_fields']==scenario
 actual_full=full['passed_checks'];assert type(actual_full) is int and actual_full>0
 pure={key:value['passed_checks'] for key,value in final['tests'].items() if key!='lava_buffed_sale_real_matrix'}
 expected={label:count for label,_,_,count in runner.TESTS[1:]};assert pure==expected and all(type(n) is int and n>0 for n in pure.values())
 new_pure=pure['lava_buffed_sale_content_contract'];assert new_pure==runner.NEW_TEST_METADATA['pure_checks']
 old_pure=sum(n for key,n in pure.items() if key!='lava_buffed_sale_content_contract');assert old_pure==3248
 assert scenario['scope']==runner.BUFFED_SALE_SCOPE and len(scenario['casts'])==1
 sale=scenario['sale'];cast=scenario['casts'][0]
 assert sale['mini_uid']==scenario['mini_uid'] and cast['source_uid']==scenario['mini_uid'] and cast['target_uid']==sale['lava_uid']
 assert cast['token_uid']==scenario['old_token_uid'] and scenario['old_token_uid']!=scenario['new_token_uid']
 assert cast['round']==sale['retirement']['round']>0 and sale['retirement']['owner']==0 and sale['retirement']['mini_buffed'] is True
 assert (cast['attack_before'],cast['attack_after'],cast['health'],cast['kept'])==(2,4,5,1)
 assert sale['departed_stats']=={'attack':4,'health':5,'kept':1}
 assert (sale['native_preview_attack'],sale['native_preview_health'])==(2,5)
 assert sale['owner_bound_history_gate_observed'] is True and sale['preview_not_actual_rebuy'] is True and sale['actual_shop_buy_attempted'] is False
 assert scenario['darkcrest_final_tier']==2 and scenario['coin_pre_source_fixture'] is True
 assert all(scenario[k] is False for k in ['entirely_natural_game','actual_lava_rebuy_tested','old_full_matrix_repeated'])
 return f'''# 已验证的有限玩法：首次永久增益后的普通 Lava 原生出售

源码：{commit}。范围限于 active 暗潮路径，不是 inactive/off-Darkcrest 全游戏行为变更。

原普通 Mini 通过原生 Waiting 发出原三叉戟，同回合首次施放给唯一原普通 Lava，2/5 → 4/5、kept 1。活着的原 Mini、原已消费 token 历史与真实施法目标/序号仍可核验时，通过公开 sell 出售该 Lava，原生返金、返池并撤销其原在场权限。原生工厂 preview 仍为2/5，未把4/5增益污染库存；preview 不是实际重买。

随后一次真实非空战斗及下轮招募中，Mini仍在、已售Lava不在。原Mini继续经原生 Waiting 发出不同UID的新三叉戟；无Lava目标时对Mini的实际施法请求被拒，原牌不消费。暗潮的获取牌等级推进至2（不是随从星级变化）。本次样本为第{cast['round']}回合的首次增益出售，同轮首次不是代码硬限制为round 1。

真实 owner-bound 退休记录触发 buy/play 门禁，并在下一回合仍被观察到；这是门禁观察，不是实际商店重买挑战，也未实测Mini后来离场的完整反向长链。不覆盖buffed Lava重买、金色、多个永久buff、新目标、售后未用token到期、默认启用或全游戏验收。不新增Lava永久塑造或原生出售算法。

实际检查：新 Game {actual_full} 项；新 pure {new_pure} 项；11份既有纯合同 {old_pure} 项；总计 {actual_full+new_pure+old_pure} 项。只用一棵新 restored_snapshot 执行，candidate与恢复树分别完整SHA核验；旧完整Game不重跑，不称两个runtime。资金为已披露的暗潮激活前Coin夹具，不称完全自然对局。纯合同与静态审查不冒充live故障注入或原生发证。

证据更正：最初43只是静态误计，当时未执行Godot，不是实际测试失败；修正后实际pure为{new_pure}。V2显式Mini.board_error是caller-local冗余约束，callee既有检查已存在，不能称发现并验证了V1活源漏洞。

保留限制：初始未发布研究小包db9a67c511460b5d84e280e198290f309635c4f9b1a4ac978ec2ef1f3e0cc798被覆盖，其原封装字节丢失，不能声称所有unique产物都保留。两份源码原SHA仍可核验且可按保存差分精确重建，具体见RECONSTRUCTION_NOTE；后续修订原版本另路径保留。
''' 

# Wording policy retained from accepted corrected baseline; never describe minion-star growth.
ACQUISITION_LEVEL_WORDING = '暗潮的获取牌等级推进（不是随从星级变化）'
