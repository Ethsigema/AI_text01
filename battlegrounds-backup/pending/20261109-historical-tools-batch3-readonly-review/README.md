# 第 3 批历史 tools：审查证据，不是恢复候选

本轮审查五项，没有新增、修改或删除任何游戏源码。当前源码清单仍为 3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea，输入固定检查点 8a675dc886b8686e6bdd9a47463366cafb9c020f。

五项历史原件、安装 SHA、固定交接包成员及当前 RAW/EXPECTED 均有匹配证据。但更深检查发现四项边界差异，另一项仍缺运行验证。仅有原文和常量一致，不能据此确认最新版或当前完整链可用，因此本轮不制造恢复候选。没有 delta、候选 SOURCE_MAP 或源码补丁。

## 实际发现

1. Ancient Wishbone：历史 Python 工具必须看到 BG32_HERO_001 等七个固定原文样本。当前 GDScript 明确说明英雄和目标在实际命令阶段绑定，固定房间随从不是闭包依赖。只提供本来源编译卡牌时，实际 closure_error() 通过，但历史工具返回 None。
2. Factory Line：历史工具要求 BG32_HERO_001 原文；当前实际 closure_error() 对没有该英雄样本的最小来源容器仍通过，而历史工具返回 None。
3. Balinda Spell：保持 cards 字典为准确原始来源，只改独立 card 参数的 name，历史 compile_card 仍返回 EXPECTED；当前实际 raw_source_error 拒绝，报 balinda_spell_raw_source_changed。
4. Boogie Monster：把独立 card 的 is_golden 从 bool 改为数值 0，Python 字典比较把 False 与 0 当作相等，历史工具仍返回 EXPECTED；当前实际 raw_source_error 拒绝，报 boogie_monster_raw_source_changed。
5. Partner in Crime：原文、当前来源和六个依赖常量一致，局部 Python 正反例通过。当前准确源码层的静态 preload 闭包为 312 个脚本；明显超出本轮已经验证的小来源加载范围，没有盲跑、删减依赖或用假通过替代实际加载。本轮暂缓，不能说它已坏或已通过运行验证。

以上是历史工具与当前来源政策/验证边界的可复现差异，不是本轮新增的回归，也不自动证明所有正常编译流程必然失败。完整调用链的用途和后续版本仍需进一步核实。尤其前两项，运行时与离线编译器可能有意采用不同输入要求；在确认前不直接恢复。

## 验证及限制

- 五项历史模块顶部只含字面常量、copy.deepcopy 和已检查纯函数，先 AST 检查再在 128 MiB 地址空间上限进程中执行局部测试。40 项 Python 证据检查通过，未运行完整编译器或生成游戏数据。
- 四个小来源实际加载到 Godot，完整输入探针 30 项检查通过；从包内输入独立新建运行目录重复一次，报告完全相同。两个通过探针的意义是“观察到差异”，不是“四个历史文件通过恢复验收”。
- 初始隔离探针遗漏 Ancient Wishbone Active 的 13 个 NATIVE_PROOFS 文件，出现一个验证失败。实际源文件存在并与当前清单/固定哈希一致，只补齐新探针输入后重跑。原失败日志、原输入清单均保留；这不是项目文件缺失。详见 PROBE_INPUT_CORRECTION.json。
- 包内 before 表示初始不完整探针输入，after 表示完整探针输入，两者都没有安装这五个工具，不是恢复前后状态。
- 三个 Godot 进程含初始失败试验的峰值 RSS 为 106,632 KiB，约 104.1 MiB，均顺序执行，有 192 MiB RSS 停止阈值、2 GiB 地址空间上限及系统余量检查。
- 未加载真实 Catalog 或 Game，未测试完整编译器、完整玩法或旧存档。使用的最小卡牌容器仅用于实际来源 closure_error 的局部调用。未改源码，所以本轮不产生新的源码指纹变化；旧存档兼容性仍未验收。

## 来源、余项与后续

五项完整历史原件、历史安装清单、当前相关 GDScript 原文保存在 evidence/historical。REVIEW_CONFIG.json 逐项列出精确 SHA、依赖图与当前函数原文。本次重新计算固定 2026-11-01 ZIP 哈希并比较成员：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65；来源 https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip 。历史版本不能宣称最新版。

原 367 项缺失范围仍剩 357 项，原 68 项历史类别仍剩 59 项。其中本轮暂缓五项，加上上轮 Sinstone 共六项已有明确待审问题或待验证范围，其余 53 项没有因此被判为不安全。旧盘点、所有已验证候选及备份未改写。

建议后续先找这些工具是否存在可验证的后续补丁/版本，或明确原编译器调用约定。Partner 可单独评估低内存验证方案。不要为减少数字直接把剩余历史文件整体放回，也不要凭当前 GDScript 臆造缺失工具。

## 复现

解包后运行 python prepare_probes.py，创建不存在的 before_runtime/after_runtime。然后 python run.py after_repeat，执行完整输入的局部差异验证并写新日志。默认 Godot 路径为 /opt/godot/4.6.3/Godot_v4.6.3-stable_linux.x86_64。

python verify_review.py 核验历史证据、输入哈希、已保存差异报告及没有候选增量。probe_python.py 可在新的解包副本复跑，避免覆盖原 Python 报告。若主动复现 before_repeat，预期会再次因缺少隔离输入中的 Active proof 文件而失败，不应将它当作游戏源码问题。


## 备份发布补充

仅备份只读审查证据，不是新的运行候选或游戏验收。源码新增/修改/删除均为0，五项均未恢复，357路径缺口不变。原初次探针输入遗漏和失败记录保留，补齐的是隔离探针，不是游戏源码。新归档下载及依赖核验完成后追加回执；不重跑游戏、不重新下载或重建历史全链。
