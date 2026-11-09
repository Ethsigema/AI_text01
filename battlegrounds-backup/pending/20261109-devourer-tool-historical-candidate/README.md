# Devourer of Souls 历史工具恢复候选

仅新增 tools/devourer_souls_patterns.py，41,205 字节。SHA256：94e7daabb4d61603418ca3d14bc8ea0a8be71bf057d32d1f541154abdc0d185f。修改 0、删除 0。

输入固定检查点：4df40aa115e16fce48e4a17461893d36360613d9。
BASE_MAP SHA256：608a981c9b82b255c37fefb004a4bfe98bcf95d9717cfa3a5ee2917961ff2d00。
SOURCE_MAP SHA256：9baabc104b5f2f93087dfec0e385d6cb9fceffbf3b1d4441ec91da463a727260。
完整逻辑源码清单 27,912 文件；本包 delta 不是完整游戏。

## 历史来源和版本

原件 research/devourer_souls_native_recovery/candidates/tools/devourer_souls_patterns.py 与历史 integration_manifest/shared_manifest 安装 SHA 完全一致。本次重新计算固定 2026-11-01 ZIP SHA，并比较其中原件成员，逐字节相同。ZIP SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65，来源 https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip 。

这是历史原件恢复候选，不是已证实最新版，也不是编造或修改后的工具。没有更改游戏源码、旧证据、全局数值覆盖、玩法支持范围或任何备份。

## 必须区分的数值核验阶段

金色 BG_RLK_538_G 的独立原生值是 1 攻击、3 生命，不能按普通卡翻倍。历史工具 VALUE_OVERRIDE、当前来源 VALUE_OVERRIDE、当前固定的 existing_value_override.json、全局 data/catalog_value_overrides.json 中唯一对应项一致；现有独立金色 XML 的 CardID、DBF 103508、ATK 47=1、HEALTH 45=3 也核验一致。没有新增或改写任何数值覆盖。

首次把覆盖后的完整结果与覆盖前 CANONICAL 全表相等比较时失败：CANONICAL 已有 1/3，但 field_status 仍为 unverified，且没有 value_override_verification。原始差异和失败测试均保留，未删改。

进一步核对当前代码后确认了两个阶段：CANONICAL 在 unit_error 中用作原生身份/基础数值表；当前 Catalog 已有明确的覆盖步骤，随后补齐 known/confirmed_independent_entity 状态和核验元数据。历史工具要求的是这个覆盖后的输入。

本候选没有忽略差异或改变比较容差。探针逐字执行当前 Catalog 的十行既有覆盖片段，分别作用于 RAW 和 CANONICAL，再要求编译输入及覆盖后完整卡牌精确一致。实际 source_error、unit_error、依赖检查与 closure_error 均通过；篡改姓名、独立基础攻击值或核验出处会被拒绝。原始 raw_source_error 继续保持覆盖前边界，不声称它接受覆盖后的行。

详情：PHASE_AND_DEPENDENCY_REVIEW.json、CANONICAL_DIFFERENCE.json、INITIAL_COMPARISON_FAILURE.json、existing_catalog_override_fragment.gd。

## 四项依赖

历史工具的四个 DEPENDENCY_RAW 行与当前 Twin Lanterns 来源固定 pin 的 dependency_raw.json 完全一致。当前 Devourer 的 DEPENDENCIES 与其自身固定 pin 的 dependencies.json 完全一致。二者只在编译字段上不同，原生身份/文本等字段一致。

实际 dependency_error 接受当前编译模板、拒绝篡改；实际 closure_error 对两张来源卡和四项依赖的每一个缺失反例都拒绝。使用的是最小卡牌容器，不是实际 Catalog 实例。Python 模块只有 copy.deepcopy 标准库导入，无项目工具导入。

## 验证结果及保留的初期问题

- 69 项 Python 阶段/依赖检查通过，峰值 RSS 14,284 KiB，128 MiB 地址空间限制。
- Godot 仅实际加载 Devourer 来源与 Pool Identity 两个脚本。缺失、恢复、注释三态各 69 项检查通过，从包内输入独立重做三态，报告完全相同，共 414 项通过断言。
- 38 项静态交叉检查通过。成功 Godot 进程峰值 RSS 66,664 KiB，约 65.1 MiB；均顺序执行，具有 RSS、地址空间、时间和系统余量限制。
- 初期三次探针因新写的探针与原文片段缩进混用而受控停止，另一次因将 JSON 浮点夹具放在现有严格比较函数的参考位置而失败。保留全部脚本及日志；只修正探针缩进和比较方向，仍用实际覆盖结果作为参考，不改来源代码。相关说明见 HARNESS_INDENTATION_NOTE.json、HARNESS_NUMERIC_REFERENCE_NOTE.json。
- 成功原始比较位于 before_3、after_3、tamper_3。初期失败不计入通过断言；portable_reports 为独立复现结果。

15 项既有来源 pin 在成功三态均通过。新增工具本身不在固定准入 pin 中，所以这不是新的准入阻断修复，注释变化不会被 proof_error 拒绝。Devourer 指纹片段只有工具条目变化，未计算完整 Catalog execution_fingerprint。

## 未测范围

没有加载完整 Catalog 或 Game，没有执行完整离线编译器、真实招募/战斗或旧存档加载，也没有重新生成任何数据。当前 Catalog 原文片段的局部执行不能代表完整 Catalog 验收。不能承诺旧存档接受新的指纹。

原 367 项范围还剩 353 项；原 68 项历史类别累计恢复 13 项、剩 55 项。此前暂缓六项及所有原始盘点、封存包和备份都未变。这个统计不是所有可能缺失工具的总数。

## 复现与恢复

解包后 python prepare_probes.py 创建不存在的三套小输入目录；随后顺序运行 python run.py before_repeat、after_repeat、tamper_repeat。默认 Godot 路径为 /opt/godot/4.6.3/Godot_v4.6.3-stable_linux.x86_64。

python verify_candidate.py 复核完整原件、清单、覆盖原文片段、输入哈希、成功及失败记录。test_compiler.py 为阶段正确的 Python 检查；建议在新解包副本复跑，避免覆盖原报告。initial_test_compiler.py 刻意保留最初跨阶段全表比较，运行会重现原失败，不是当前通过门禁。

python restore_delta_to_new.py /不存在的新目录 从保存的原件恢复单文件增量，本次已验证。restore_to_new.py 需要与 BASE_MAP 相符的完整上游运行树，本次未执行全量复制。


## 封存压缩补充

首次普通压缩退出137，原因未知，留下截断档案，保留但不作为有效包上传。此处仅上传新文件名lowmem有效包；精确SHA、成员清单及中断说明均保留。新包真实下载后追加流式字节核验，历史链复用，不写完整运行树。
