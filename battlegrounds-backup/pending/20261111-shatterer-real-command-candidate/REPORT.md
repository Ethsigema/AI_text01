# 碎地者真实指令链：受限独立候选（2026-11-11）

## 交付状态

完整候选工程保留在 `../game_candidate_shatterer/`。`../game_working/` 已恢复为逐文件核验的27920文件基线，源清单SHA256为7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7。未把有限门禁候选推广到通用默认工程。全部源码写入已冻结。

干净增量 `../shatterer_candidate_payload/` 有87份新增/变化文件，具体前后哈希见 FINAL_SOURCE_DELTA.json。三大引擎前像与历史候选精确匹配；保留真实Game、Catalog、Combat和全部依赖。原 `_buff`、`_unit`、`_factory_unit` 未替换或抽取，77份既有source只精确重钉必要引擎哈希。最终2594条指向现有文件的字面摘要匹配，0不匹配。

## 本次新增源码修正

真正执行完整Catalog后发现，原碎地者候选未接受Catalog为金色随从加入的标准 `pool_blocker`，使金色完整来源校验拒绝，继而普通随从依赖闭包失败，get_card返回空。

新修改 `core/shatterer_sources.gd:source_error` 只额外接受完整金色记录中值严格等于原 `PoolIdentity.MINION_REASON` 的该字段。保持其他所有字段完整相等；不删除metadata、不放宽原PoolIdentity、不改原XML、overlay来源或失败门。普通来源不接受这个新字段。独立16项来源合同正反例通过；真实Catalog普通/金色均supported=true、get_card非空。

## 真实测试结果

- 原基线：Game资源加载、实例化、完整Catalog成功，load_errors=[]，退出0，109.60秒，采样RSS峰3,004,555,264字节。
- 首个整合测试：完整Game/Catalog成功，默认房间因既有七级及衍生入池合同拒绝，退出5。失败保留，不宣称默认房间可玩。
- 限定房间初测：暴露上述金色来源合同错误，退出5。失败保留。
- 修正后第一矩阵：Catalog与真实Game.start成功，但测试直接调用私有_play被既有actual_success_command守卫拒绝，退出8。没有删除守卫；改用公开apply_command，旧失败保留。
- 最终公开指令矩阵：退出0，108.53秒，采样RSS峰3,019,808,768字节。真实Game.start、原_unit、原_add_hand、公开apply_command、原_play及原_buff均执行。普通碎地者6/4在打出迷你侍从后成为7/5（max_health=5）。随后依次打出金色碎地者及乘波骑士，普通成为9/7，金色成为14/10。越域纳迦命令返回shatterer_other_naga_prefix_partial，手牌序列及两源属性保持不变。这是连续不同卡出牌，不是重复发送同一命令的幂等性测试。
- 独立source合同：16项通过，退出0；包含合法原记录、精确金色注释、普通额外字段、错误值/类型、未知字段与攻击值篡改拒绝。

## 测试范围与保留边界

真实矩阵使用原艾德温、限定三个普通纳迦家族、无额外任务/饰品/畸变机制的独立测试房间。没有修改生产默认池以迁就测试。卡牌通过真实工厂和入手函数加入，但不是商店随机抽取、购买或完整金色获取路线。全程法术计数为0，未覆盖3/6法术阈值增长、重复同一命令、全部家族组合、战斗、复制/复生/三连、旧存档或完整对局。

候选overlay仍含default_pool=true，但host仅支持明确有限域，不能直接作为通用默认版本。故保留独立完整候选工程，并将活动工程恢复基线。没有新增英雄或其他机制，未引入暗潮/骑手累计候选，娜迦保留、畸变怪不扩入本轮范围。

## 资源与复现

Godot 4.6.3。原基线上限120秒；后续真实矩阵预设240秒、4GiB进程组RSS软门槛，20ms采样，TERM后2秒未退出则KILL。环境无暴露cgroup硬限，采样值不是硬峰值保证。本轮无触限、无强制结束。

监视脚本已支持第三参数指定项目。为保留既有失败/成功日志，请复制测试到新名字再运行，例如：

`cp shatterer_command_matrix.gd shatterer_command_matrix_rerun.gd`

`python3 monitor.py shatterer_command_matrix_rerun 240 ../game_candidate_shatterer`

历史运行日志里的game_working是当时的候选目录名；测试后该整棵树更名为game_candidate_shatterer，文件未改。所有旧失败与最终成功日志均保留。正式证据白名单见 EVIDENCE_ALLOWLIST.json，排除HOME、缓存和Godot生成缓存。
