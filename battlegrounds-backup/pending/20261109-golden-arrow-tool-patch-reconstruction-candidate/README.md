# GoldenArrow 编译来源文件补丁重建候选

输入固定提交：839d5dd71e4d0e4bf59f97c1fb6ed50b5807daa6。
状态：已从可信旧候选和精确后续补丁重建，并通过有限低资源检查。没有找到补丁后的已安装原件，不把重建字节冒充找回的最新版原件。

## 唯一运行增量

仅新增 tools/golden_arrow_patterns.py，32647 bytes，SHA-256：
886717620eaa0da57b9a8d7f579fb78b08b2f2a54c45f7899e6e3ded10d642d3

修改0、删除0。没有改变任何Godot源码、卡牌数据、覆盖率、支持标记或旧证据。前后完整清单所有旧条目相同。

输入完整清单SHA：c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b。
候选完整清单SHA：bfd5d82ede8559200aed89547e4584ac091873a9392079af5ee20c41ea764a0a。
候选清单27898文件、1548752837逻辑bytes。完整清单未改部分继承已验证输入，本轮未重读全部旧工程。

## 原文、补丁与版本依据

1. research/golden_arrow_native_recovery/candidates/tools/golden_arrow_patterns.py，32491 bytes，SHA256 ff0073009c27627cdb4a4065c3a2f56769cd64ced5fd1033b4b5a0586e139025。它与shared_manifest及integration_manifest的安装后哈希一致；FROZEN引用的shared_manifest哈希也一致。
2. research/arrow_native_periodic_delivery/tools_golden_arrow_patterns.py.patch，715 bytes，SHA256 b3e586190991034d248a3bb80c4549b235d315a90366524df470ad244c49cd4f。
3. 两份材料均存在于固定11月1日原始Release、11月7日源码整包及当前恢复清单，且字节一致。原始Release SHA256为33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65。前序只读调查重新扫描102个历史归档，未找到补丁后已安装的该文件。
4. 本包evidence/保留原文、补丁、两份安装清单、FROZEN、输入检查点远端核验回执，以及当前Catalog/Game指纹消费处的带原文件哈希片段。PROVENANCE.json记录路径和来源关系。

严格应用单个统一差异hunk，核对目标路径、旧新行号、数量、全部上下文和删除行；没有模糊匹配，没有手写重造逻辑。原补丁只把compile_card的依赖绑定由全部原生fixture缩为实际父畸变与点金箭子卡。这是复现已有历史补丁，不是本轮发明新规则或新增范围。

## 有限验证

共69项计数检查：43项Python重建/AST/小函数检查，18项Godot轻入口/指纹检查，8项跨结果核对。

- Python峰值49948 KiB。验证严格补丁再现，拒绝错误上下文、重复应用、错误目标、错误行数及额外hunk；前后AST解析通过，compile_card外AST不变，唯一导入为copy.deepcopy。RAW、EXPECTED和实际子卡DEPENDENCY_RAW与当前GoldenArrow GDScript完全相同。
- 仅在内存中执行静态检查过的两个小函数，验证原全fixture对照、补丁后的实际父子闭包、缺失或被篡改来源拒绝、无关fixture移除以及输出deepcopy。不运行build_effect_catalog，不重新编译目录，不改数据文件。
- before_2、after_2、tamper_2三个顺序Godot 4.6.3进程，各6项。最高RSS68676 KiB，约67.1 MiB。仅加载5脚本的真实GoldenArrow来源入口，不加载完整Catalog、PrizeGolden或Game。
- before缺失路径真实返回空文本，native.log没有错误，旧指纹项是tools/golden_arrow_patterns.py:SHA256(empty)。after读取重建文件真实文本，tamper读取独立副本中添加注释后的文本。
- 执行Catalog同形的GoldenArrow.RUNTIME_PATHS文本哈希循环，共25项。三组只有该Python文件对应项不同，其余24项完全相同，片段摘要随补入/篡改分别变化。
- 原16条来源固定pin在三组全部通过。该Python文件本来就不在这些pin内，故篡改影响执行身份指纹，不等于固定证据准入拒绝。

Godot限制：192MiB RSS提前停止、启动前至少1GiB系统可用内存、运行中640MiB可用余量、2GiB地址空间、45秒超时、5ms采样、2CPU；最大RSS由os.wait4针对确切子进程取得。没有并行Godot。

初次before/after/tamper各项断言也通过，但测试报告元数据预期缺失读操作会输出错误，实际没有错误。已保留初版gate和三组原始结果，修正为中性missing_file_case后重跑，仅将后三组计入69项。候选源码从未因此变化，详见HARNESS_METADATA_NOTE.json。

## 指纹、功能与兼容性边界

该Python文件属于离线目录编译来源，不是Godot运行效果模块。当前core对它的引用仅在GoldenArrow.RUNTIME_PATHS；Catalog:1530将文件文本哈希加入指纹，:2100/:2104汇入execution_fingerprint。Game:14131保存它，:14493加载时比较。

本轮实际计算的是GoldenArrow指纹片段，不是完整Catalog最终execution_fingerprint。补入文件确实改变该片段的输入和摘要；不能声称旧存档兼容，也未运行旧存档迁移、拒绝、回放或完整游戏。没有伪造旧指纹。

原始11月1日交接包已经没有游戏tools目录，不是本轮清理造成。检查过的355个RUNTIME_PATHS声明共有368个缺失tools路径；本候选只补1个，仍有367个未解决。这个计数不是所有可能的工具引用缺口的总数。没有删引用、填空文件、静默排除缺失项，也没有声称工具链或完整项目已修复。

## 恢复与复跑

rebuild_to_new.py NEW_DIRECTORY从包内原文和补丁重新生成唯一增量，目的地必须不存在；已在focused_restore验证重建字节，但该临时副本不装入包。

restore_to_new.py BASE_RUNTIME NEW_RUNTIME可从完整匹配BASE_MAP.json的旧工程生成新完整目录；先核对全部基线和空间，不覆盖旧工程。本轮没有执行完整恢复，需要约1.55GB的新目录空间。

probe_inputs/随包携带27个原先已核验的小探针输入，总263356 bytes。解包到一个新目录后执行prepare_probes.py会生成before/after/tamper三个小runtime并逐文件核对，不需要复制完整工程。然后可运行run.py before_repeat、after_repeat、tamper_repeat等新标签；它拒绝覆盖已有输出目录。gate和run.py使用当前文件所在目录，PLAN中的原始路径仅作历史记录，不决定新运行路径。

build.py和finalize.py保留当时构建流程，引用当时工程布局并有目录不存在断言，不应在封存目录直接重跑。独立重新生成增量请使用rebuild_to_new.py，独立小探针用prepare_probes.py和run.py。原始日志不能当作新的运行证据。

## 封存状态

包包含唯一增量、原文与补丁、完整前后清单、指纹消费依据、工具、探针输入、真实日志/采样、所有检查结果。压缩包每个成员再次流式复核SHA。既有证据、恢复树、符号链接和备份全部保留。

尚未上传、发布或做远端整链回读。本候选是补丁重建且部分验证通过，不是完整游戏验收，也不解决其余工具缺口。


## 备份发布补充

以上“尚未上传”是原封存时状态，原压缩包保持不变。此后已发布增量备份。只新增一个由可信旧文件和精确历史补丁重建的候选工具文件，并非找到补丁后的已安装原件。其余367个静态RUNTIME_PATHS工具引用缺口尚存；清单逐字节匹配不表示工具链、完整Game、存档或完整游戏已恢复验收。实际远端下载与流式核验回执在完成后追加。历史链复用并重哈希，不声称本轮重新下载历史链。
