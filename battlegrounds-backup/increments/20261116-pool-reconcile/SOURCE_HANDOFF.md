# 饰品范围逐项核对（研究增量）

基线 a8c77287，回执2585d46c。未修改游戏或旧备份。

## 实质发现
- 263行候选漏了大型记忆之球：BG36_MagicItem_372 / DBF133712。官方36.2季初表明确列为新大型饰品，36.2.2又将回合末复制数量从2改3；已有用户原始工作簿同一稳定ID及大小可交叉绑定。因此新增到独立衍生候选表，而非仅因社区API有它就认定在池。
- 旧候选与社区“current”快照相差21条，其中4条已有明确37.0.2移除记录，另外17条不能仅因社区缺席删除。训练证明（小型，BG30_MagicItem_962 /111417）就是反例：社区快照缺席，但37.0.2官方仍明确调整其费用3→4。
- 衍生表共264行，含已移除项目，不是当前卡池分母；完成数和分母均保持null。污染者大小及大型救赎者3个身份的官方表自相矛盾仍未解决，独立列出，不默默加减。
- 四个酒馆法术变更按稳定ID交叉绑定，明确是平衡变更，不是4张新增卡或移除卡。

## 文件
TARGETED_LEDGER.json/.csv：21条差异＋记忆之球的22条身份及证据决策；DERIVED_CANDIDATES.json：保持全部旧候选、增加遗漏身份；SPELL_IDENTITIES.json：四个法术身份；SUMMARY.json：可计算但不误导的研究统计；INPUT_SHA256.json：输入快照指纹。

## 主要来源与范围
官方S14季初表：https://us.forums.blizzard.com/en/hearthstone/t/battlegrounds-season-14-trinket-updates/163710 （2026-07-27，按New/Staying与大小分区）
官方36.2.2：https://hearthstone.blizzard.com/en-us/news/24293284 （Greater Trinket Text Changes / Sphere of Memory）
官方37.0.2：https://hearthstone.blizzard.com/en-us/news/24307311 （Trinket Pool Changes、Lesser Cost Increases、Tavern Spells）
社区线索：https://hsbg.cards/patch-notes/37.0.2 。页头同时存在67项与5+1+97项等不同统计表达，不直接使用其聚合数或季节日期；详情与官方一致时只作交叉线索，未作为权威。

不是全量后续热修复合并，不是所有264行完成当前在池认证，也不是玩法验收。没有新增游戏功能或整卡完成数。
