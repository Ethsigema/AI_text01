# Initial final document diffs

Original actual Game receipt/statistics unchanged. This late correction changes explanation only.

## GAMEPLAY_VERIFIED_SLICE.md

```diff
--- initial/GAMEPLAY_VERIFIED_SLICE.md
+++ corrected/GAMEPLAY_VERIFIED_SLICE.md
@@ -4,10 +4,12 @@
 
 唯一普通 Mini 原生发出三叉戟，先对原普通 Lava 施放本回合第一张塑造，2/5 → 4/5、kept 1。该原 token 已消费并离开全部区域，手中没有 child；随后以公开 sell 命令出售原 Mini，按原生机制返金、返池并记录出售。
 
-已消耗 token 的原对象和原凭据历史保持不变，不重新发牌或恢复使用权限。一次真实非空战斗及下轮招募后，Lava 仍4/5、kept重置0，暗潮成长至2级，离场Mini不再发牌。实际日志顺序严格为先cast、确认已消费、再sell、最后combat。
+已消耗 token 的原对象和原凭据历史保持不变，不重新发牌或恢复使用权限。一次真实非空战斗及下轮招募后，Lava 仍4/5、kept重置0，暗潮的获取牌等级推进至2（不是随从星级变化），离场Mini不再发牌。实际日志顺序严格为先cast、确认已消费、再sell、最后combat。
 
 实际检查：新 Game 103 项；新 pure 85 项；10份既有纯合同 3163 项；总计 3351 项。只执行一棵新 restored_snapshot，候选与恢复树分别完整核验；旧完整Game不重跑，不称两个runtime。
 
 资金使用已披露的源激活前Coin夹具，不称无夹具自然对局。preview仅为形状诊断；纯合同的消费历史内容判定和fake权限拒绝不冒充真实权限或live故障注入。
 
+未覆盖售后未用token到期。
+
 不开放第二Mini、重买、金色、额外目标或任意token复制，也不新增Lava永久算法。不代表默认启用、全卡池或全游戏验收。保留既有source a96a033 / accepted final d914d669及更早历史。
```
## GAMEPLAY_OUTCOME.md

```diff
--- initial/GAMEPLAY_OUTCOME.md
+++ corrected/GAMEPLAY_OUTCOME.md
@@ -4,12 +4,14 @@
 
 唯一普通 Mini 原生发出三叉戟，先对原普通 Lava 施放本回合第一张塑造，2/5 → 4/5、kept 1。该原 token 已消费并离开全部区域，手中没有 child；随后以公开 sell 命令出售原 Mini，按原生机制返金、返池并记录出售。
 
-已消耗 token 的原对象和原凭据历史保持不变，不重新发牌或恢复使用权限。一次真实非空战斗及下轮招募后，Lava 仍4/5、kept重置0，暗潮成长至2级，离场Mini不再发牌。实际日志顺序严格为先cast、确认已消费、再sell、最后combat。
+已消耗 token 的原对象和原凭据历史保持不变，不重新发牌或恢复使用权限。一次真实非空战斗及下轮招募后，Lava 仍4/5、kept重置0，暗潮的获取牌等级推进至2（不是随从星级变化），离场Mini不再发牌。实际日志顺序严格为先cast、确认已消费、再sell、最后combat。
 
 实际检查：新 Game 103 项；新 pure 85 项；10份既有纯合同 3163 项；总计 3351 项。只执行一棵新 restored_snapshot，候选与恢复树分别完整核验；旧完整Game不重跑，不称两个runtime。
 
 资金使用已披露的源激活前Coin夹具，不称无夹具自然对局。preview仅为形状诊断；纯合同的消费历史内容判定和fake权限拒绝不冒充真实权限或live故障注入。
 
+未覆盖售后未用token到期。
+
 不开放第二Mini、重买、金色、额外目标或任意token复制，也不新增Lava永久算法。不代表默认启用、全卡池或全游戏验收。保留既有source a96a033 / accepted final d914d669及更早历史。
 
 
```
