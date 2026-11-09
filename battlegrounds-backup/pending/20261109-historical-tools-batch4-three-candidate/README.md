# 第 4 批历史 tools 恢复候选：三文件

仅恢复 Boom Controller、Soul Fermenter、Twin Lanterns 三项历史原件，共 119,828 字节。新增 3、修改 0、删除 0。此前暂缓的六项未恢复，也未改写其证据。

- tools/boom_controller_patterns.py，40955 字节，SHA256 00a0fb66643a7036cf95bd12147a8fed6b6d06a4e2694460224075632d5eb51c
- tools/soul_fermenter_patterns.py，41072 字节，SHA256 ab9de696e039c12b4a813c284780c5bab88f93f39f8607d28901c2ec07118fd2
- tools/twin_lanterns_patterns.py，37801 字节，SHA256 a1f16a334fb01888e7b4124c524910c9f80ed333c5d0d7452daf52cbf0f3e745

## 版本和原件

输入固定检查点：92710e8471cd9353b2393ddf6f55c1a9454a760f，包含第 3 批只读审查；其游戏源码仍是第 2 批候选。
BASE_MAP SHA256：3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea。
SOURCE_MAP SHA256：608a981c9b82b255c37fefb004a4bfe98bcf95d9717cfa3a5ee2917961ff2d00。
完整逻辑清单 27,911 文件；delta 不是完整游戏。

三项来自已有研究目录里的候选原件，逐字节匹配历史 integration_manifest/shared_manifest 安装 SHA，FROZEN 中的清单 SHA 也核验一致。保留原件、清单和冻结记录。本次重算固定 2026-11-01 ZIP SHA，并直接比较原件成员；ZIP SHA256 为 33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65，来源 https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip 。

这些是可信历史原件，不是已证实的最新版。没有根据当前 GDScript 编造工具，也没有修改原件、当前脚本、pin、游戏数据、玩法范围或旧备份。

## 依赖证据为什么成立

三项当前 GDScript 的 DEPENDENCIES 保存的是完整编译后依赖卡牌，不是 RAW。不能把两种表示直接比较后误判为原文不一致。

每项当前 PROOF_SHA256 同时固定 research/.../dependency_raw.json 与 dependencies.json：

- 历史 Python 的 DEPENDENCY_RAW 与当前固定的 dependency_raw.json 完全相同。
- 当前 GDScript 的 DEPENDENCIES 与当前固定的 dependencies.json 完全相同。
- 原始与编译后记录的差别仅限 supported、effects、coverage_rule、coverage_text_sha256、default_pool、pool_supported；身份、来源、文本、数值等原生字段未变。
- 实际 dependency_source_error 接受这些当前编译模板并拒绝篡改，实际 closure_error 拒绝逐项移除任何必需依赖。

共有 16 个“模块-依赖”条目、6 个不同依赖卡牌 ID。详见 DEPENDENCY_REVIEW.json。三项工具只导入标准库 deepcopy，没有其他项目工具导入。完整项目编译链仍未验证。

## 有限验证结果

Python 顶部经过 AST 限制检查，原始模块在 128 MiB 地址空间上限进程内执行局部 compile_card/same 正反例。165 项检查通过，覆盖 RAW/EXPECTED、依赖原文和编译数据固定 SHA、四个正常来源输出、缺失/篡改来源及依赖、布尔/数字区别、输入不变和返回值深复制。峰值 RSS 16,056 KiB。

Godot 只加载三项来源和两个小依赖，共五个未修改脚本。缺失、恢复、追加注释三态各 180 项断言通过，从包内输入新建目录独立重复三态，报告完全相同。六次共 1,080 项断言；另有 69 项静态交叉检查。Godot 峰值 RSS 69,104 KiB，约 67.5 MiB。均顺序执行，设有 RSS、地址空间、时限和系统内存余量限制。

来源依赖闭包使用最小卡牌容器调用真实来源函数，不是实例化真实 Catalog；四个来源编译卡牌和所有依赖模板均通过局部校验，缺失及篡改反例均按预期拒绝。没有执行战斗、招募或存档操作。

三项来源合计 50 个固定 pin 在所有状态均通过，依赖数据属于这些 pin；三个新增 Python 工具本身不在当前准入 pin 中。因此这批不是新的准入阻断修复，注释变化也不会被当前来源 proof_error 拒绝。对应三段 Catalog 指纹比较分别只有目标工具条目改变，未计算完整 Catalog execution_fingerprint。

## 未验证及剩余范围

原 367 项范围还剩 354 项；原 68 项历史类别累计恢复 12 项，还剩 56 项，包括此前暂缓的六项。这个范围不是全项目所有可能 tools 缺失的总数。

完整 Game、实际 Catalog、完整离线编译器、玩法效果及旧存档兼容性均未验收。新增工具会改变相应指纹片段，不能承诺旧存档继续接受。没有重新生成数据或提高任何默认池/玩法支持状态。

原有封存包、备份、原始盘点和已暂缓项全部保留。初始构建器在定位额外证据目录时选错父级，被断言拦住，尚未生成增量；保留该初始目录和脚本，在本新目录正确构建，详见 BUILD_METADATA_NOTE.json。

## 复现

解包后运行 python prepare_probes.py，再顺序运行 python run.py before_repeat、after_repeat、tamper_repeat。新运行写入新的日志目录，不覆盖已保存报告。默认 Godot 路径 /opt/godot/4.6.3/Godot_v4.6.3-stable_linux.x86_64。

python verify_candidate.py 复核原件/清单/冻结记录、增量、输入哈希和报告。test_compilers.py 可在新解包副本重跑，避免覆盖原报告。

python restore_delta_to_new.py /不存在的新目录 从保存的原件生成三文件增量；此小恢复流程已测试。restore_to_new.py 需要与 BASE_MAP 完全相符的完整上游运行树，本次未执行全量复制。


## 备份依赖补充

原封存包保持不变。制作检查点92710e…包含第3批只读证据，其运行源码依赖仍固定第2批8a675d…；只读审查不作为运行补丁。三项是历史版本，未证实最新版，剩354路径，完整游戏和旧存档未验收。新包真实下载和流式核验完成后追加回执；历史基线复用并重哈希，不冒称整链重下。
