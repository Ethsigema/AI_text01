# 第14批：Hand Murloc / Piranha 的明确新修正候选

本批只在独立开发树增加两份经限定验证的新工具，不是原样历史恢复，也不称最新版。输入为第13批固定备份 `c2338eec7c0fc95a01614bdfdb85e7efe6a16602`。原基线、全部备份和原始证据均保留。

- Hand Murloc 新文件：19,690字节，SHA256 `235b6876dccb9ebf7e7266c195742ad8597d968b8cb2a424352039bc36ad67c4`。
- Piranha 新文件：21,608字节，SHA256 `03b2112c131ba35923d95bb9f482226928ab154e268f25d1f54cc88c77acecda`。
- 原367路径参考范围的未补位置由347降至345，仅表示新增两个工具路径，不是全项目依赖/玩法缺口统计。

## 历史证据与修正范围

通过固定生成脚本中的字面表达式、原JSON及AST读取的ID重建历史文件，没有执行历史生成器。历史重建分别精确匹配独立输出pin `fc9393a3dfc7adbc862858176b0cb755449f9bc6058a8abeda2459134fc39028` 和 `de8a0592e5a606d619e17e2823e3cad0a6b30be2fd657974a8e247d1e9aa3026`，历史重建文件与新修正分别保留。

历史代码会忽略传入card本体；普通Python相等还会混同布尔与数字。本批只新增当前GD对应的递归比较器并修改compile_card：要求普通JSON字典、合法字符串ID、完整传入原始卡牌，以及所有既有原始依赖行均一致。常量、导入、RAW、EXPECTED、ID列表与完整返回内容保持不变。不存在新动态文件读取、证明豁免或其他编译器导入。

Hand Murloc只闭合两张原有来源卡。Piranha闭合两张来源卡及普通子体BG32_201t；子体仍不得作为该工具的编译输出，不推导金色子体。每份输出为独立deepcopy。

## 已完成的限定验证

- 五条完整实际raw行、五份实际编译overlay、七处canonical来源、五份独立native XML及数值、图片和文本覆盖摘要相符；没有适用的数值override。
- 2,177项Python检查及便携重跑通过，包含22个历史错误见证、字段/标量变化、依赖、类型、数值、deepcopy和输入/常量不变性。每份工具重放33个此前实际GD类型数值案例；不冒称为新运行的该数值实验。
- 另一独立矩阵共961种输入：Hand Murloc402，Piranha559。Python每次1,960项检查，实际Godot每次2,015项检查。缺工具、新工具、仅注释篡改三态各重复一次，再在新目录完整重放，共12次串行Godot。
- 对原历史工具可见的330处假接受，新修正与实际GD组合来源入口均拒绝。各态准入结果一致，只有预期工具指纹变化；指纹变化不是证明验收。
- Godot只加载两份来源脚本、phase_undead_army_sources及pool_identity。host文件只作为指纹字节，未加载执行。
- 两份历史到新修正的补丁按零偏移、零模糊重现。独立树逐文件校验，不使用硬链接。

这些是完整传入raw卡牌、原始依赖和固定EXPECTED前提下的来源/辅助工具比较，不是所有接口、运行时证据、host或游戏行为等价证明。

## 明确保留的缺口和版本限制

- `research/piranha_immediate_attack_recovery/SOURCE_CONTRACT.md`仍缺失，且在Piranha的RUNTIME_PATHS中。
- Hand Murloc的SOURCE_CONTRACT.md也缺失，有历史摘要但不在其当前RUNTIME_PATHS中。两份文档均不属于既有五项允许缺失说明文档；没有编造文件或新增豁免。
- 限定搜索核对原ZIP、固定Git树、相关源/模板/补丁与既有清单，未找到可精确恢复的正文。搜索范围与排除项完整记录，不能称穷尽所有历史。
- 当前Hand Murloc host与其历史host摘要不同，保持当前字节，不用旧admission记录冒充当前执行验收。
- 原aggregate CardDefs.Bacon_latest.xml仍缺失；本批依靠保留的五份独立XML及历史pin，未称重新获取上游最新版。
- 完整编译驱动tools/build_effect_catalog.py仍缺失。完整Game、Catalog、host、玩法/触发顺序、UI、默认池和存档未验收。
- 原Bolvargolden暂缓保持不变；这两组原已存在的normal/golden来源标记、partial说明、默认池false和其他运行限制均未改变。没有解除任何金色执行限制。
- 候选适用于经测CPython3.12.14、有限无环JSON形状值；不保证特殊Python对象/循环结构与GD等价。不要用-O或PYTHONOPTIMIZE。

## 资源与复现

Python限定检查使用128MiB地址空间上限。Godot串行运行：2GiB地址空间、192MiB RSS停止阈值、45秒超时、2 CPU，启动前至少1GiB可用内存，低于640MiB则停止。实际用量见TESTS_VERIFIED.json。

添加文件后的整树核验曾在同一128MiB进程中触发MemoryError。文件状态随后核实，未重复安装或提高上限；在独立128MiB进程中以64KiB分块重新完成全树核验。原脚本与失败记录保留，不算通过记录。

- `python3 -B verify_candidate.py`：静态校验封存包。
- `python3 -B replay_review_to_new.py /新不存在目录`：独立重放2,177项Python检查和两份严格补丁。
- `PYTHONDONTWRITEBYTECODE=1 python3 -B gates/replay.py /新不存在目录`：重放独立Python矩阵和六次受控Godot。需要当前已安装的/usr/local/bin/godot，不会启动完整游戏。
- `python3 -B restore_to_new.py /完全匹配第13批的runtime /新不存在目录`：按完整基线清单和两份delta重建候选，不覆盖输入或目标。实际复制/安装/重哈希另有收据，此通用恢复入口未额外执行。

采用精确白名单封存源码、固定证据、最小来源测试夹具及日志。排除完整游戏树、HOME、字体/编辑器/可重建缓存、.godot、__pycache__、私聊、凭据和无关文件。缺失文档与未验收范围不会因清单或哈希通过而消失。
