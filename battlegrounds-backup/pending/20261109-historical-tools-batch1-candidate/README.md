# 五项历史 tools 恢复候选，第 1 批

独立增量候选，仅新增以下五个历史原件，共 53,803 字节：

- tools/amalgadon_native_patterns.py，15200 字节，SHA256 aa7f535eea27cafc337c42d8f15bb3815904bd8199076affc8f4207e15bc432f
- tools/hasty_excavation_patterns.py，8111 字节，SHA256 dc8b5de5684f016142c4dba7ee53d6052db900264eac9088654c56ed2df72eab
- tools/sacrificial_altar_patterns.py，8323 字节，SHA256 072b4ff54e9797704e6c03d85139c29b502d29ed5056332766b4cc2c830d356e
- tools/suspicious_stimulant_patterns.py，8552 字节，SHA256 8f736422fa3f9eedb74f91324349889d1d16fd93d5d0d05d9741f34ae1169026
- tools/toxic_tumbleweed_patterns.py，13617 字节，SHA256 7ad13e909a77e5ee62119e9f899df8652df3849b7a57329adc93e0b0d988c0ec

## 结论与边界

五项在本次有限验证范围内适合封存为可审阅的恢复候选。它们是历史单一版本原件，不是已证实的最新版，也不是根据 GDScript 编造的代码。没有修改这些原件、当前来源常量、准入 pin、游戏数据、玩法支持范围、旧存档或任何旧备份。

输入固定检查点：d26dc87ff20c600c651bcee24b0d3dffa056a79f。
输入 SOURCE_MAP SHA256：28b1d1c523dfc566bc5eacd04ccea1e1787c1b15e0cca8f9e67ecf9229b46bf4。
候选 SOURCE_MAP SHA256：53da1c13fbebb6eb8c5672ad8828109720efdfab1a8a97b6792a6da3202e6080。
候选完整逻辑源码清单：27,904 文件，新增 5、修改 0、删除 0。delta 不是独立完整游戏。

## 精确证据

每项均保存研究目录里的原件、历史 integration_manifest 与 shared_manifest；安装后的 SHA 与原件逐字节一致。当前对应 GDScript 的 RAW、EXPECTED，以及工具拥有的同名 PROGRAMS 全部相同。详见 PROVENANCE.json、evidence/historical 和 COMPILER_TESTS.json。

本次再次完整计算固定 2026-11-01 ZIP 的 SHA256，并直接比较五个候选成员。ZIP 哈希为 33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65，来源：https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip 。这证明历史来源，不证明最新已安装状态。

既有 367 项盘点完整证据已包含在上游 Megasaur 封存包 megasaur_tool_fixed_pin_candidate_20261109.tar.xz，SHA256 27514275c7204a972de2a5193b93deb35c7d4a72b137d1bc5c9477c2f7e9cf66。本包保存原始总表摘要及五项完整证据行，不修改既有盘点。

## 依赖与功能检查

五个 Python 模块均只导入标准库 copy.deepcopy，没有其他 tools 模块导入。顶部代码仅为文档、字面常量、该标准库导入和两个已审阅纯函数 same/compile_card；先做 AST 限制检查，再在 128 MiB 地址空间上限进程中执行原始模块。没有运行全项目编译器或重写数据目录。

184 项 Python 检查覆盖：当前常量相等、8 个卡牌输出、完整声明源集依赖、无效参数、缺失或篡改来源、布尔值与数字区别、返回值深复制和输入不变。峰值 RSS 为 12,396 KiB。

这批工具并非仅仅无用的指纹文本：历史编译器有导入证据，其功能是根据精确原始来源生成 EXPECTED 输出。完整离线编译链仍未验证，不应由这五项推断全部工具已齐全。

## Godot 低资源比较

只加载五项来源脚本及三个小依赖，共 8 个未修改 GDScript，不加载 Catalog、Mechanisms 或 Game。实际来源检查接受 Python 产生的 8 项正常卡牌结果，并拒绝篡改原始/编译卡牌名称。

缺失、恢复、追加注释三态各 165 项断言，随后在仅由包内输入创建的新目录重做三态，报告完全相同。六次共 990 项断言，另有 73 项静态交叉检查。Godot 峰值 RSS 67,108 KiB，约 65.5 MiB；顺序执行，保留 192 MiB RSS 停止阈值、2 GiB 地址空间上限及系统内存余量检查。

注意：五个工具均不在当前来源的固定准入 pin 中。五项来源合计 86 个 pin 及实际 proof_error() 在三态都通过。因此，这批不构成新的准入阻断修复，也不能说注释篡改被准入校验拒绝。恢复原件及注释变化只改变对应 Catalog 指纹片段中的工具条目；五个片段分别仅此一处变化。未计算完整 Catalog 的 execution_fingerprint。

## 剩余事项

原 68 项历史材料已选出这 5 项，仍有 63 项未恢复。加上此前已恢复的 Megasaur，原 367 项缺失范围还剩 361 项。这个范围不是项目所有可能 tools 缺失的总数。

旧存档可能受指纹变化影响，兼容性未知。未做完整 Game 启动、交互玩法、完整存档加载、全 Catalog/全编译器或默认池验收。没有因此提升任何卡牌的玩法支持状态。所有旧证据与备份原样保留。

## 复现与恢复

解包后：

1. python prepare_probes.py：从已核验的 probe_inputs 创建不存在的三个小探针运行目录。拒绝覆盖已有目录。
2. python run.py before_repeat，after_repeat，tamper_repeat：顺序比较并写新日志。工具默认使用 /opt/godot/4.6.3/Godot_v4.6.3-stable_linux.x86_64。
3. python verify_candidate.py：复核原始报告、五文件增量、证据哈希及输入不变。
4. test_compilers.py 为 Python 正反例验证源码；再次运行会重写其报告，建议在新解包副本执行以保留旧证据。
5. python restore_delta_to_new.py /一个不存在的新目录：从保存的历史原件恢复五文件增量。此小恢复流程已实测。
6. restore_to_new.py 需要与 BASE_MAP 完全相符的完整上游运行树，才会创建完整新副本。本次没有运行这个全量复制流程。

原始运行、独立复现日志及资源测量均随包保存。SOURCE_MAP 是逻辑源码清单，probe_inputs、证据和报告不是新增游戏源码。


## 备份发布补充

原封存包字节不变。五个历史原件未证实为最新版；这五文件不在当前固定准入pin中，不宣称修复新的准入阻断或篡改被pin拒绝。原367范围仍缺361项，完整游戏与旧存档未验收。实际远端下载及流式字节核验材料完成后追加。历史链复用并重哈希，不冒称本轮整链重新下载。
