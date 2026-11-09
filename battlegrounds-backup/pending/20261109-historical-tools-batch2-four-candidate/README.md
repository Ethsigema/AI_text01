# 第 2 批历史 tools 恢复候选：四文件

本次经过依赖检查后，从最初五项缩为以下四项。仅新增历史原件，共 132,315 字节；修改和删除均为 0。

- tools/lovely_locket_patterns.py，49055 字节，SHA256 096ef062da3ce6380468d19cebe155258a9f78fb7d4127cc4b6ca7c9c8977f24
- tools/old_soul_patterns.py，15521 字节，SHA256 b0d3a90388112f9669ca8191004f86c6908fdf67ec8896b655560877f41b70a1
- tools/replica_cathedral_patterns.py，48625 字节，SHA256 2b9f4b6d5c471c6f5bb7ec1b1e675040cee0fe644e4fe4eb64ef6dc53826e703
- tools/warband_whistle_patterns.py，19114 字节，SHA256 6ce217d3de494483dd42c1375d71412575ac50a3803c7472ebda21ef31739df8

## 版本依据

输入固定检查点：cfe5366f7e0a115532e8996549782c635481b97a。
BASE_MAP SHA256：53da1c13fbebb6eb8c5672ad8828109720efdfab1a8a97b6792a6da3202e6080。
SOURCE_MAP SHA256：3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea。
完整逻辑清单为 27,908 文件。delta 只有这四个新增文件，不是完整游戏。

四项均是找到的历史单一版本原件，与历史 integration_manifest/shared_manifest 的安装 SHA 一致。本次再次完整哈希固定 2026-11-01 ZIP，并直接比较四个历史成员。ZIP SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65。来源：https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip 。

原件与当前来源 RAW/EXPECTED、工具拥有的同名 PROGRAMS 相符。它们是可审阅的历史恢复候选，不是已证实最新版。没有编造、修补或修改原件，没有调整准入 pin、当前来源脚本、游戏数据或池支持状态。原始来源、安装清单、版本回读收据及逐项 SHA 保存在 evidence 与 PROVENANCE.json。

## 为什么暂不恢复 Sinstone Sticker

最初五项测试包含 Sinstone Sticker。它的历史 Python 工具要求六个额外依赖原文，而当前 GDScript closure_error() 只检查自身来源，没有要求这些依赖。移除这六个依赖时，当前 closure_error() 仍通过；原先“都应拒绝”的六项测试在缺失、恢复、注释三态均未通过。

这不是本次恢复造成的新运行回归，也不证明现有运行代码错误。但它意味着不能把这六个样本直接说成当前运行必需依赖，历史工具的额外要求是否适合当前完整编译链仍未证实。因此本批不新增 Sinstone，不修改原代码或放宽测试来宣称通过。

evidence/deferred_sinstone_trial 保存原五项测试输入、原件、脚本、三态失败报告与资源记录，可独立复现；这些仅为研究证据，不是本候选的游戏增量。DEFERRED_SINSTONE_REVIEW.json 说明发现及初期证据脚本的元数据问题。所有旧文件均保留。

## 四项通过的验证

Python：顶部 AST 限制为字面常量、copy.deepcopy 标准库导入和已审阅的纯函数。原始模块在 128 MiB 地址空间上限进程中执行，仅运行局部 compile_card/same 测试，不执行完整编译器。161 项检查通过，包括正常输出、无效参数、缺失/篡改完整来源集、返回值复制、输入不变及布尔/数字区别。峰值 RSS 15,356 KiB。

依赖：Old Soul 没有额外工具依赖。其余三项的 DEPENDENCY_RAW 与当前 DEP_RAW 完全一致，共 16 个“模块-依赖”条目、9 个不同卡牌 ID。没有其他项目 Python 模块导入。实际 GDScript 依赖来源检查接受当前依赖模板并拒绝篡改；使用最小卡牌容器的真实 closure_error() 接受完整来源，拒绝缺失来源或依赖。这不是实例化完整 Catalog，也不是完整玩法测试。

Godot：只加载四个来源脚本和两个小依赖，共 6 个未修改脚本。当前来源校验接受 5 个 Python 编译卡牌结果，并拒绝篡改。缺失、恢复、注释三态各 183 项断言；从包内输入新建目录独立重做三态，报告完全相同。六次通过的探针共 1,098 项断言，另有 69 项静态交叉检查。初始五项失败探针不计入这些通过数量。Godot 峰值 RSS 69,112 KiB，约 67.5 MiB，均顺序执行且有内存余量及 RSS 停止阈值。

四项来源合计 55 项固定 pin 和实际 proof_error() 在三态均通过。四个新增工具本身不是当前准入 pin，因此这批不解决新的准入阻断，也不宣称注释变化会被准入拒绝。当前 Catalog 对应四段指纹算法的比较显示，每段只有目标工具条目变化；完整 Catalog execution_fingerprint 未计算。

## 余项与未测范围

原 68 项历史类别累计恢复 9 项，剩 59 项，其中包含本次暂缓的 Sinstone；原 367 项缺失范围还剩 357 项。这不是全项目所有可能 tools 缺失的总数，原始盘点未改写。

未运行完整 Game、实际 Catalog、完整离线编译器或存档加载；未重新生成任何数据。历史工具与当前源码局部相符，不等于整个编译链可用。工具内容加入会改变指纹，旧存档兼容性未知。没有因此提升玩法或默认池支持状态。所有旧证据及备份保留。

## 复现

- 解包后运行 python prepare_probes.py，从包内输入创建不存在的三套小运行目录。
- 顺序运行 python run.py before_repeat、after_repeat、tamper_repeat，输出新日志，不覆盖原报告。默认 Godot 路径：/opt/godot/4.6.3/Godot_v4.6.3-stable_linux.x86_64。
- python verify_candidate.py 检查四文件增量、历史证据、原始运行结果、已暂缓第五项以及输入哈希。
- test_compilers.py 是 Python 正反例验证源码。复跑会重写其报告，建议在新解包副本执行。
- python restore_delta_to_new.py /不存在的新目录：从保存的原件恢复四文件增量。此小恢复流程已测试。
- restore_to_new.py 需输入与 BASE_MAP 完全相符的完整上游运行树。本次未执行全量复制，避免重复大项目和高资源测试。
- 若研究暂缓项，可在新的 evidence/deferred_sinstone_trial 副本运行 prepare_probes.py 和 run.py。其原始门禁包含未经证实的“缺失依赖均应拒绝”假设，预期可重现六项失败，不可将其当作通过验收。


## 备份发布补充

原封存包保持不变。只恢复四个历史候选，最新版未证实。Sinstone暂缓，其原五项三态失败证据完整保留且不计入通过验收。原367范围剩357路径。完整游戏、旧存档和整体内存收益未验证。新远端下载和流式核验完成后追加回执，历史基线复用，不冒称历史整链重下。
