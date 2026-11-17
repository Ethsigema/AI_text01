# 普通骨颅购买与神圣魔杖规则核查

基线：portrait_backup_20261117/postupload/fresh_restore/project。远端全链回执确认 source_commit=55e0b21eb1a430e057ef1bf8cf98383b52f5d58c，485个远端项/28372个恢复文件；本轮独立复制，旧成果不改。

## 神圣魔杖：已有规则，不是新增玩法
稳定ID BG36_MagicItem_307，DBF 133379，本地名称神圣魔杖，小型饰品。
实际读取官方37.0.2：费用2，对随从施放2个法术获得1铸币，开发者说明禁止野猪人局。
https://news.blizzard.com/en-us/article/24307311/37-0-2-patch-notes
实际读取官方已知问题页，Tracked Issues仍列它可能出现在野猪人局。这是客户端未遵循设计规则的已知问题，不是设计规则反转，更不能推定本项目也有该缺陷。
https://us.forums.blizzard.com/en/hearthstone/t/370-highlights-known-issues/153567
本轮定向官方搜索未找到明确修复公告，不宣称全部后续补丁都已穷尽。页面日期显示与本地资料时间存在差异，不能据此推断精确修复时序。
本地 patch_3702_wand_divination_sources.room_error 已拒绝选定野猪人局，all模式也扫描实际启用随从；room_config.errors 调用该规则。原有规则保留，无相关逻辑改动。新增小范围函数级测试仅复核门禁，不代表随机提供器或整卡功能完成。

## 新增实际切片
上一增量接通骨颅规范手牌fixture打出/出售，但肖像持有者购买普通骨颅仍被 incoming_payload_partial 拒绝。本轮仅为精确普通骨颅身份增加商店购买桥，沿用既有余额、手牌容量、三连、库存及实际购买事件处理，不实现新的购买算法。
不允许金色商店新路径，不按亡语前缀泛放行。篡改效果/附属/种族/关键词/金色标记仍应付款前拒绝。
测试用规范工厂建立商店fixture后真实buy、play、sell，接续Fire/Snow各自同族成长；不是随机商店生成验收。
保持部分实现，完整卡新增0。多饰品、其他英雄、混合投球手、完整战斗/存取档等仍未完成。

## 最终验证
修改前：实际购买被 greater_baller_incoming_payload_partial 拒绝，退出1；保留日志。
修改后：60项通过（其中3项是神圣魔杖既有门禁复核），退出0；寒热骤变购买回归17项通过，退出0。最终日志无警告。
游戏逻辑只改 greater_baller_portrait.gd 的精确普通骨颅购买分支，未改神圣魔杖规则。未上传Git。
