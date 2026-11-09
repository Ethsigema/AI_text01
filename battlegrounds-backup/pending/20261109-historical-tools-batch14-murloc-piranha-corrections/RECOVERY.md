# 第十四批 Hand Murloc / Piranha 新修正恢复说明

这是两份有条件的新修正工具增量，不是历史原件或已证实最新版，也不是独立完整游戏。只新增 tools/hand_murloc_gain_patterns.py 和 tools/piranha_vacancy_patterns.py，修改和删除均为零。

1. 下载固定提交的 MANIFEST.json 和 11 个 .part000 至 .part010 分片，逐个检查大小、SHA256 后依序连接为 historical_tools_batch14_murloc_piranha_corrections_20261109.tar.xz。总大小 2,589,844 字节，SHA256 7b5f337521162460d87b984be77f66b99c43666407198938e52925e8b295d154。
2. 在新目录安全解包；外部清单覆盖395个成员，FILE_MANIFEST.json覆盖394个文件，FILE_WHITELIST.json与这些内部清单项严格相同。
3. 运行仅限已测试的CPython 3.12.14和有限无环JSON形状值；必须启用断言，禁止-O、-OO或非零PYTHONOPTIMIZE。python3 -B verify_candidate.py仅核对封存证据。恢复工具字节可从review/original应用review/patches中的两份严格补丁，并核对delta和SOURCE_MAP，不需要执行历史生成器或候选模块。
4. 固定依赖第13批提交c2338eec7c0fc95a01614bdfdb85e7efe6a16602，目录battlegrounds-backup/pending/20261109-historical-tools-batch13-bounded-bolvar-correction。其SOURCE_MAP与本包BASE_MAP SHA256均为de45de078a3b334eff7b901085deb8140561f21af3013b8af31b266628cacc6f。
5. 如需完整候选目录，先准备严格匹配BASE_MAP的27,918文件基线，再运行python3 -B restore_to_new.py /基线目录 /不存在的新目录。只复制原树并加入两份delta，不覆盖旧树或备份。

候选27,920文件、1,549,340,406字节；SOURCE_MAP SHA256为7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7；排序路径、NUL、字节数、NUL、实际文件字节的整树流SHA256为5ba04ef124fc78cf20e2a942a60589fb92dc76e6808155648226a534a4599e05。

原参考范围仍缺345条路径。两份SOURCE_CONTRACT.md仍未找回，Piranha那份还在RUNTIME_PATHS内；没有新增允许缺失豁免。Hand Murloc当前host与历史摘要不同，保留当前字节且未执行验收。完整依赖、编译驱动、Game、Catalog、host、UI、触发顺序及旧存档均未验收。Bolvar金色暂缓与其他既有运行限制继续保留。

封存测试报告不等同本次备份阶段重跑。失败记录、历史原文、全部旧备份保留，不强推。
