# 第十三批 Bolvar 低内存新修正候选恢复说明

这是一份显式新修正增量，不是历史原件，也未证明最新版或完整游戏。只新增 tools/native_bolvar_shield_patterns.py；普通输出仍为部分实现，金色版本继续暂缓。原范围引用缺口剩余 347 项，不是全项目依赖计数。

1. 下载固定提交下的 MANIFEST.json 和 21 个 .part000 至 .part020 分片，逐个核对大小和 SHA256 后按顺序连接。原包名 historical_tools_batch13_bounded_bolvar_correction_20261109.tar.xz，5,112,724 字节，SHA256 69688097600dcdf79f754d065848ddff6f194366c611c78241fb4cff26d2769b。
2. 在新目录安全解包，外部清单验证全部 158 个成员，FILE_MANIFEST.json 验证其中 157 个文件。FILE_WHITELIST.json 必须与除 FILE_MANIFEST.json 外的文件集合完全相同。
3. 仅在已测试的 CPython 3.12.14 上复现，Python 必须启用断言，禁止 -O、-OO 和非零 PYTHONOPTIMIZE。python3 -B verify_candidate.py 仅核对封存证据。python3 -B apply_review_patch_to_new.py /不存在的新审查目录 从保留历史字节精确应用显式新补丁，生成最终 V3 文件，不运行候选模块或游戏。
4. 固定源码依赖第十二批提交 1e2ede27d0312440996e2c7c9e88ebdd033ee195，目录 battlegrounds-backup/pending/20261109-historical-tools-batch12-new-enforcer-correction。更多历史依赖沿其 DEPENDENCIES.json 递归。第十二批 SOURCE_MAP 与本批 BASE_MAP SHA256 均为 d4b0801f7c69dcb8899149680f8a51979db644fa118b7bafd93b922d248ef3c1。
5. 若需要完整候选目录，准备严格匹配 BASE_MAP 的 27,917 文件基线，再运行 python3 -B restore_to_new.py /基线目录 /不存在的新目录。只复制基线并增加最终 V3，不能安装被否决的初版或 V2，不能覆盖旧树或旧备份。

候选有 27,918 文件、1,549,299,108 字节；SOURCE_MAP SHA256 de45de078a3b334eff7b901085deb8140561f21af3013b8af31b266628cacc6f；按排序路径、NUL、字节数、NUL、实际字节拼接的整树流 SHA256 fefcdb171d91f8101f743848cf4266925004991e66c32d513493cc4abad6e57c。

测试仅覆盖 CPython 3.12.14 上稳定、可 seek 的普通文件。不是并发修改的原子快照，任意巨大的单值也不保证适配 128 MiB；错误文本、位置及回溯不保证相同。历史原件对完整当前数据没有成功执行结果，不能声称全量旧版与新版等价。受限停止、初版深度问题和 V2 编码优先级问题证据均保留。

历史限定测试报告不代表本次备份重跑。完整 Game、Catalog、完整编译驱动、真实 UI、触发时序及旧存档仍未验收；金色、部分实现和非默认池限制保留。旧备份全部保留，不强推。
