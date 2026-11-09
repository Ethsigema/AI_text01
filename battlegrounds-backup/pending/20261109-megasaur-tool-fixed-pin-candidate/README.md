# Megasaur 单文件固定 pin 恢复候选

这是独立增量候选，仅恢复 tools/megasaur_adapt_patterns.py。没有修改现有 GDScript、准入 pin、数据、旧存档或其他备份。它是找到的历史原件逐字节恢复，不是根据现有 GDScript 编造，也不是补丁重建。

## 版本与来源

- 输入检查点：9b60cad21ed6dc06d2b4c8f67a36f8c88ab92290。
- 原件：research/megasaur_adapt_native_recovery/candidates/tools/megasaur_adapt_patterns.py。
- 文件长度：32,296 字节。SHA256：adf31c928468bb9be4dcca89bda2dd0096626dbbbc926dae639ce24bea23b1a2。
- 原件与当前 core/amalgadon_sources.gd 的显式 PROOF_SHA256 完全一致；历史 source_candidates_manifest 和创建补丁也给出完全相同的字节。
- 本次再次完整哈希 2026-11-01 固定 ZIP，并直接比较其历史候选成员，确认原件相同。固定 ZIP SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65。
- evidence/historical 保存原件、两个历史清单及原始完整创建补丁；PROVENANCE.json 保存来源路径、成员路径和哈希。

## 真实验证范围

以未修改的三个小脚本 Amalgadon Sources、Megasaur Adapt Sources、Pool Identity 进行 Godot 4.6.3 headless 探针。没有加载 Catalog、Mechanisms 或完整 Game，没有执行 Python 编译器。

1. 缺失状态：43 项 Amalgadon pin 中 42 项匹配。实际 proof_error() 返回 amalgadon_native_proof_changed:tools/megasaur_adapt_patterns.py。
2. 恢复状态：43 项全部匹配，委托的 32 项 Megasaur pin、完整 OPTIONS 和 TOKEN 一致性检查通过；实际 Amalgadon.proof_error() 返回空。
3. 篡改状态：只给工具追加一行探针注释，实际 proof_error() 再次精确拒绝该文件。未放宽任何 pin。

每种状态 91 项断言；三种状态在仅使用包内小输入的新目录重复一次，报告逐字相同。六次共 546 项 Godot 断言，另有 55 项静态及交叉检查。峰值 RSS 为 65,076 KiB，约 63.6 MiB。探针均顺序执行，设有 192 MiB RSS 停止阈值、2 GiB 地址空间上限和系统余量监测。

采用当前 Catalog 中对应两段的相同算法比较 Amalgadon 49 项和 Megasaur 36 项 RUNTIME_PATHS 指纹：只有该工具条目变化，两段都发生变化。这不是整个 Catalog 最终 execution_fingerprint。tools/amalgadon_native_patterns.py 仍缺失，探针未恢复它。新增该文件可能改变存档指纹，旧存档兼容性未知。

## 完整 367 项盘点证据

完整只读盘点及脚本原样纳入 evidence/tools_reference_inventory_20261109，共 22 个文件，逐文件哈希见 evidence/INVENTORY_SNAPSHOT_MAP.json。它描述恢复前的检查点，故其中“367 项均缺失”仍是原始历史状态，不是本候选恢复后的状态。不要改写旧报告为新状态。

恢复前分类：1 项当前显式 pin 原件、68 项单一历史版本且安装清单/当前 RAW 与 EXPECTED 匹配、21 项版本或补丁需审查、277 项在已检查材料内未找到可验证恢复材料。后两类不等于永久丢失。其他 68 项不能宣称最新版或已经通过运行验收，本次未恢复它们。

恢复本单文件后，原 367 项范围还剩 366 项。此前确认 358 项有 Catalog 指纹消费者、9 项只有声明未确认消费者，另有 357 项历史 Python 导入用途；这些是恢复前盘点统计，不能把这些工具全部说成无用离线元数据。367 也不是整个项目所有 tools 缺失的总数。

## 可复现方式

解包后在本目录运行：

- python prepare_probes.py：只创建不存在的 before_runtime、after_runtime、tamper_runtime，逐项核验包内输入。
- python run.py before_repeat，然后 after_repeat、tamper_repeat：输出到新的日志目录，不覆盖已封存日志。run.py 默认 Godot 路径为 /opt/godot/4.6.3/Godot_v4.6.3-stable_linux.x86_64；更改工具路径后应保留原运行证据。
- python verify_candidate.py：静态检查并核对原始三态报告、输入、历史创建补丁和盘点快照。仅 AST 解析工具，不执行工具模块。
- python restore_leaf_to_new.py /一个不存在的新目录：仅从已校验原件生成独立单文件增量。本次已完成这个小恢复测试。
- restore_to_new.py 需提供与 BASE_MAP.json 完全相符的完整上游运行树，才能创建新的完整副本。此全量恢复脚本本次未执行，避免重复大项目复制。

SOURCE_MAP.json 是完整逻辑源码清单，BASE_MAP.json 是原始清单。CHANGES.json 仅一项新增，REMOVALS.json 为空。delta 仅包含目标文件。probe_inputs 与 evidence 不属于新增游戏源码。

## 明确未完成

没有完整游戏启动/交互验收、旧存档加载、全 Catalog 指纹计算、离线全编译器运行、默认池/玩法支持提升，也没有解决其余 366 项缺失。修复这一明确准入阻断，不代表游戏整体可用。所有旧来源、备份与已有证据保留。


## 备份发布补充

本次保存原封存压缩包，不改写原调查与测试记录。367项调查是恢复前状态；候选只恢复其中1项，尚余366项。该历史原件SHA与当前代码显式pin一致，不是GoldenArrow式补丁重建。其他68项未恢复，不宣称最新版。完整游戏、旧存档及整体内存收益未验证。远端下载与流式核验材料完成后追加；历史链复用并重哈希，不冒称本轮整链重下。
