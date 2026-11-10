# 恢复本次独立 receipt 修正审查包

从固定 GitHub 提交下载本目录 .tar.xz、MANIFEST.json、SHA256SUMS.txt、verify_backup.py。原包须为 344,252 字节，SHA256 b171c951c38d65a80f02d70d69ba6711f335490ce254e13cf5cf3e665ec2a4c7。

可信 Python 3 环境可执行 python3 verify_backup.py <下载目录> --report verification.json，核验107项成员、内外哈希白名单和未安装边界。脚本只在内存读取归档，不联网、不下载依赖、不执行或导入归档代码，也不重跑Godot矩阵/控制测试。

核验后仅在新的独立目录解包查看，不覆盖现有游戏树或安装候选。包内 replay_to_new.py 是原审查的可选复现入口，不会被备份校验器自动执行。

新receipt与既有unit候选均未安装，真实Game可达性未证明，345缺口及Game/旧存档未验收状态不变。此包不是完整游戏备份。旧依赖未复核，已取消的第14批依赖下载不属于本任务。
