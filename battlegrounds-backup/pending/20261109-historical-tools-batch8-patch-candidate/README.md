# 第八批：两项历史补丁重建候选

状态：TWO_PATCH_RECONSTRUCTED_CANDIDATES_NOT_PROVEN_LATEST。只在全新独立候选树增加Aggramar与Mystery Cube两个工具，84,192字节。未修改任何已有游戏文件，未删除文件，未改变玩法支持状态、来源常量或准入pin。原基线及此前备份保留。

## 来源与版本边界

两项均从原始ZIP中的历史Python原件及后续patch精确重建。原件、patch、integration/shared manifest对应的SHA已核对。此次完整重哈希原ZIP，SHA256为33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65，相关成员逐字匹配。自编逐行应用器严格核对原行号、上下文和行数，不允许偏移；另用GNU patch --fuzz=0独立重做，字节完全一致。

- tools/aggramar_patterns.py：25,578字节，SHA256 a2275e84f82de72643d7c10c84bc18a8714b6be2ae9acd0671d14b1b6625c855。
- tools/mystery_cube_patterns.py：58,614字节，SHA256 8d124fa3697067784ef4fe4383dd36393d22c543bcbe211a1e33b7782cfe2310。

这是有历史证据的补丁重建版本，不是从当前GDScript编造Python。没有找到独立历史完整postimage，也没有补丁后SHA manifest；原安装manifest只证明初始版本。不能称其为最新安装原件，不能把原清单中的B类直接改成“历史最新版已取回”。

## 与当前来源的对应关系

Aggramar的补丁更新EXPECTED并把编译依赖缩为自身RAW，保留严格card和cards来源行比较。重建RAW/EXPECTED与当前GD全等；演示英雄不再是编译或当前来源闭包的准入条件。

Mystery Cube的补丁把依赖缩为SOURCE_IDS。唯一编译入口BG30_MagicItem_703的RAW及EXPECTED与当前GD相等。**完整RAW字典不相等**：GD另外含BG30_MagicItem_970和BG30_MagicItem_984两个选中替换目标，它们不是Python编译入口。当前GD在target_error阶段严格检查这些目标。本轮实际验证目标正常、改名、额外字段和未知目标的接受/拒绝边界，但没有执行完整槽位替换、支付或交互流程。

## 限定测试

Python只执行两份已审阅的纯模块（copy.deepcopy、字面常量、same、compile_card），128 MiB地址空间上限。262项检查包括正常输出、每个顶层字段缺失、额外字段、card与cards分别篡改、布尔/数字区分、深复制隔离、忽略非拥有的历史演示依赖、拒绝把GD替换目标当编译入口。

Godot只加载两个当前来源及其8个实际preload脚本，不加载Game或完整Catalog。缺失、恢复、追加注释三态各195项断言，另在三份独立输入目录复现，报告逐字相同。随后通过包内portable replay在全新目录再次完整复现。两轮Python峰值最大16,116 KiB；12次Godot峰值最大75,192 KiB。全部正常退出，无Godot错误。

每次Godot串行运行，192 MiB RSS停止阈值、2 GiB地址空间上限、45秒超时；启动前至少1 GiB可用内存，系统余量低于640 MiB则停止。MiniCatalog是测试夹具，不是真实Catalog。

37项当前固定proof输入及实际proof_error在三态均通过。两个工具不在这些固定准入pin里，故本批不是新的准入阻断修复；注释变异没有被proof拒绝。两个Catalog指纹片段各只改变工具自身条目。未计算完整execution_fingerprint，旧存档兼容性未知。

## 暂缓及其余调查

Perfected Alchemy原件+补丁也可精确重建，但Python只要求自身和BG26_813t；当前GD另调用GoldenSources闭包，检查六项入口，额外五项仍是差异。此项只做静态追踪，未执行候选Python或加载其较大的父Godot闭包，未加入delta。

另外20项旧A类静态审阅：12项忽略传入card本体；8项检查card但使用普通Python字典相等。20项均存在布尔/数字类型边界差异，未原样恢复。其中8份历史patch仅是从/dev/null创建同一个旧版本，精确重建后SHA仍相同，不提供更严格替代版本。

原13项明确暂缓保持不变，Alchemy新增静态暂缓；20项静态结果不冒充20次动态验收。初版静态辅助脚本错误假设raw_source_error都是单行，读取阶段停止；初版与说明保留，修正版读取完整函数体，未改原源码，初次失败不计通过。

## 实际树与恢复范围

输入SOURCE_MAP SHA256：9baabc104b5f2f93087dfec0e385d6cb9fceffbf3b1d4441ec91da463a727260，27,912文件。
候选SOURCE_MAP SHA256：5e7e06673ff9a6b9eaf0668af1327b5ea3b86cf7f1ea866a105edbf2afd32e10，27,914文件、1,549,216,476字节。
候选实际整树字节流SHA256：2808118a744b4b62973ddd639dc39d4313a6d653e2ced479909a7a125e067f55。

新树从独立输入树复制，所有既有文件inode不同，没有硬链接；输入树与候选树都逐文件实际重哈希。原范围353个缺失路径在候选树中减为351，原基线仍保持原样。这不是项目全部潜在缺口统计。原68项历史A类仍有55项未恢复；本次两项来自B类补丁链。

188项静态证据核验通过。完整Game、完整离线编译器、真实UI、完整玩法、随从/法术/饰品覆盖率、旧存档以及原中断工作树均未因此验收。第六批四份原核验文件未找回。

## 复现及备份

先验证FILE_MANIFEST.json每项字节数及SHA256；运行python verify_candidate.py可检查本包证据与两文件delta。运行python reconstruct_to_new.py /一个不存在的新目录，可独立从原件+补丁恢复这两个delta文件。运行python replay_to_new.py /另一个不存在的新目录，可复现限定Python与三态Godot检查；需要Python 3及/usr/local/bin/godot，本轮Godot为4.6.3。

完整树复原入口为python restore_to_new.py /精确匹配BASE_MAP的输入树 /不存在的新树。它拒绝不匹配输入和已有目标，复制后逐文件验证；本轮实际全树复制核验已通过，但该附带入口未额外重跑一次。

本包是增量候选及完整限定审查证据，不是独立完整游戏备份。完整恢复还需要与BASE_MAP精确匹配的上游树。包内不含字体缓存、HOME、.godot、__pycache__、可重建缓存、私聊、凭据或无关文件；使用明确文件白名单封存。所有历史备份及失败材料仍保留。
