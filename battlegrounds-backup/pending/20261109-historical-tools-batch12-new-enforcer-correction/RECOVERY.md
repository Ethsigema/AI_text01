# 第十二批 Enforcer 新修正候选恢复说明

这是一份显式新修正增量，不是历史原件，也未证明最新版或完整游戏。只新增 tools/native_enforcer_shield_patterns.py；Bolvar 提案仅审查，不得安装。原范围引用缺口剩余 348 项。

1. 从本固定提交下载 MANIFEST.json 和六个 .part000 至 .part005 分片，逐个核对大小和 SHA256 后按顺序连接。原包名 historical_tools_batch12_new_enforcer_correction_20261109.tar.xz，1,473,752 字节，SHA256 a7ce5385a8eef690c4ca0babfbf2fce1d5afc60882a87dac0803671f0599e3b4。
2. 在新目录安全解包，外部清单验证全部 274 个成员，FILE_MANIFEST.json 验证其中 273 个文件。FILE_WHITELIST.json 必须与除 FILE_MANIFEST.json 外的文件集合完全相同。
3. Python 必须启用断言，禁止 -O、-OO 和非零 PYTHONOPTIMIZE。python verify_candidate.py 仅核对封存证据，不执行游戏或 Godot。python apply_review_patch_to_new.py /不存在的新审查目录 从保留历史字节精确应用新补丁，得到两份提案，但只有 Enforcer 允许进入候选。
4. 固定源码依赖第十批提交 1266c9d1c78bf3f388d2f695467d60af9807ac75，审查依赖第十一批 c920ae817ceb3c822ebb8456bcf7ba55643f27e4。完整路径和包 SHA 见 DEPENDENCIES.json。第十批与第十一批源码映射均为 dc3968e2c02fc646100ad1a1745fe885414ad679250363c732f4ae4fae2920cb。
5. 若需要完整候选目录，先沿固定历史依赖准备严格匹配 BASE_MAP.json 的 27,916 文件基线，再执行 python restore_to_new.py /基线目录 /不存在的新目录。不得覆盖旧基线或旧备份。它只复制原树并增加 Enforcer，不安装 Bolvar。

候选有 27,917 文件、1,549,281,831 字节；SOURCE_MAP SHA256 d4b0801f7c69dcb8899149680f8a51979db644fa118b7bafd93b922d248ef3c1；按排序路径、NUL、字节数、NUL、实际文件字节拼接的整树流 SHA256 c7698b11fbc7045b82ce0f7f096d3417b31d5984b6a6ec5236de74cc8034aff9。

封存中的限定测试报告不代表本次备份阶段重跑。真实护盾触发、完整 Game、Catalog、完整编译驱动、UI 和旧存档仍未验收。历史输出由生成载荷重建并匹配独立 pin，并非找到安装后完整原件。不得把新修正误称历史原样恢复。保留全部旧备份，不强推。
