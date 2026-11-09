# 第十四批备份回读核验完成

原包提交：b693f364abe88509ac0986529d8c2f82a41831fd。

原包：historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz，2,589,844字节，SHA256 7b5f337521162460d87b984be77f66b99c43666407198938e52925e8b295d154。

11个分片保留原包全部字节。已从固定GitHub提交真实重新下载22个发布文件，校验大小、SHA256和Git blob SHA，不是仅看本地副本或上传返回值。

## 实际核验

- 本包395个普通成员、394个内部清单项和明确白名单全部吻合；350项只读检查通过。缓存、HOME、编辑器状态、私聊和凭据不在白名单内，路径及常见凭据特征检查未检出。
- 固定第13批依赖c2338eec7c0fc95a01614bdfdb85e7efe6a16602的21个分片真实下载、合并和校验，158个成员、157个内部清单项及白名单吻合；83项只读检查通过。其SOURCE_MAP与本包BASE_MAP逐字节相同。
- 12份捕获来源输入逐字节匹配实际基线和固定源图。递归比较器及先前数值oracle与新下载的第13批内容一致。
- 只读取历史生成器AST中的字面ID及固定raw/expected JSON，重新构造两份历史输出，与独立历史pin及保留原文字节相同。未运行历史生成器或候选模块。
- 两份历史到新修正的补丁分别正向、反向、再正向应用，零fuzz、零偏移，逐字节等于封存提案和delta。
- 从既有27,918文件基线加新下载并重建的两份文件，构成27,920文件、1,549,340,406字节的实际候选字节流，每个文件均匹配SOURCE_MAP。随后再次完整读取基线，文件和路径集合未变。

候选SOURCE_MAP SHA256：7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7。

候选整树字节流SHA256：5ba04ef124fc78cf20e2a942a60589fb92dc76e6808155648226a534a4599e05。

流算法：按路径排序，逐项串联UTF-8路径、NUL、ASCII字节数、NUL和实际文件字节；另外核对每个文件SHA256。

## 版本和未闭合项

只新增两份明确新修正，修改0、删除0：

- tools/hand_murloc_gain_patterns.py：19,690字节，SHA256 235b6876dccb9ebf7e7266c195742ad8597d968b8cb2a424352039bc36ad67c4。
- tools/piranha_vacancy_patterns.py：21,608字节，SHA256 03b2112c131ba35923d95bb9f482226928ab154e268f25d1f54cc88c77acecda。

不是历史原件或已证实最新版；历史输入来自生成载荷重建并匹配独立pin，不冒充找回安装后的完整原件。适用范围为CPython 3.12.14、有限无环JSON形状值。

原参考范围仍缺345条路径，并非全部项目依赖计数。以下状态已与实际基线重新核对，没有因哈希通过而豁免：

- research/piranha_immediate_attack_recovery/SOURCE_CONTRACT.md缺失，且仍在Piranha声明的RUNTIME_PATHS内。
- research/hand_murloc_gain_recovery/SOURCE_CONTRACT.md也缺失。两份文档均未编造，没有新增允许缺失豁免。
- Hand Murloc当前host字节与历史摘要不同，实际当前字节保留；host未执行，不把历史准入记录当成当前host验收。
- aggregate CardDefs.Bacon_latest.xml及完整编译驱动tools/build_effect_catalog.py仍缺失。

完整依赖、Game、Catalog、host、完整编译驱动、触发时序、默认池、UI和旧存档仍未验收。Bolvar金色暂缓及现有partial、normal/golden和其他运行限制不变。

## 本次核验边界

复用既有历史基线并重新哈希，没有重新下载或重跑全历史链，没有重新核验原始ZIP。未新建完整候选目录，只生成审查输出并逐文件读取实际候选字节流。

封存中的Python矩阵、Godot运行、来源搜索和资源记录均按字节核对；备份阶段没有重跑动态Python测试、Godot、游戏、host、完整编译器或存档。不要把已有测试报告误称本次重跑。

Python断言保持开启，禁止-O、-OO或非零PYTHONOPTIMIZE。详细结果和真实下载记录见REMOTE_STREAM_VERIFIED.json；复现回读脚本见verify_remote_backup.py；恢复步骤见RECOVERY.md。本增量不构成独立完整游戏。

全部旧源码、旧备份及失败证据保留，只在备份分支追加文件，不强推，不修改main。
