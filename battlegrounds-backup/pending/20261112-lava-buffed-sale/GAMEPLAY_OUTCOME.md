# 已验证的有限玩法：首次永久增益后的普通 Lava 原生出售

源码：b74934926d8e5eaeb4a9b27328cd07da3da54007。范围限于 active 暗潮路径，不是 inactive/off-Darkcrest 全游戏行为变更。

原普通 Mini 通过原生 Waiting 发出原三叉戟，同回合首次施放给唯一原普通 Lava，2/5 → 4/5、kept 1。活着的原 Mini、原已消费 token 历史与真实施法目标/序号仍可核验时，通过公开 sell 出售该 Lava，原生返金、返池并撤销其原在场权限。原生工厂 preview 仍为2/5，未把4/5增益污染库存；preview 不是实际重买。

随后一次真实非空战斗及下轮招募中，Mini仍在、已售Lava不在。原Mini继续经原生 Waiting 发出不同UID的新三叉戟；无Lava目标时对Mini的实际施法请求被拒，原牌不消费。暗潮的获取牌等级推进至2（不是随从星级变化）。本次样本为第1回合的首次增益出售，同轮首次不是代码硬限制为round 1。

真实 owner-bound 退休记录触发 buy/play 门禁，并在下一回合仍被观察到；这是门禁观察，不是实际商店重买挑战，也未实测Mini后来离场的完整反向长链。不覆盖buffed Lava重买、金色、多个永久buff、新目标、售后未用token到期、默认启用或全游戏验收。不新增Lava永久塑造或原生出售算法。

实际检查：新 Game 102 项；新 pure 44 项；11份既有纯合同 3248 项；总计 3394 项。只用一棵新 restored_snapshot 执行，candidate与恢复树分别完整SHA核验；旧完整Game不重跑，不称两个runtime。资金为已披露的暗潮激活前Coin夹具，不称完全自然对局。纯合同与静态审查不冒充live故障注入或原生发证。

证据更正：最初43只是静态误计，当时未执行Godot，不是实际测试失败；修正后实际pure为44。V2显式Mini.board_error是caller-local冗余约束，callee既有检查已存在，不能称发现并验证了V1活源漏洞。

保留限制：初始未发布研究小包db9a67c511460b5d84e280e198290f309635c4f9b1a4ac978ec2ef1f3e0cc798被覆盖，其原封装字节丢失，不能声称所有unique产物都保留。两份源码原SHA仍可核验且可按保存差分精确重建，具体见RECONSTRUCTION_NOTE；后续修订原版本另路径保留。


保留基线 source 610cad09b7d19fe2615201f054a68c6e1a31d79d / accepted final 838043a91d995a93bf916846e960465ee05966e7。本批范围仅原Mini原token首cast原普通Lava永久4/5，再public出售该buffed Lava；Mini留场，一次非空combat/nextrecruit发出原生新token但无Lava目标时cast held。未开放buffed Lava重买、金色、多个buff或新目标。暗潮获取牌等级推进不是随从星级变化。旧完整Game不重复，原永久算法不重写。最终远端发布回读仍待完成。
