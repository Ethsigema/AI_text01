# 恢复本次独立探针包

从固定 GitHub 提交下载本目录原始 .tar.xz、MANIFEST.json、SHA256SUMS.txt、verify_backup.py。原包须为 171,788 字节，SHA256 b7ea490684bb5b9ef1db93f4ad0c8c5d0c46c8da431ac4e8007fe5c28ecc75ca。

在可信 Python 3 环境执行 python3 verify_backup.py <下载目录> --report verification.json，可核验所有 75 项成员和内外哈希白名单。脚本只在内存读取归档，不联网、不下载依赖、不执行或导入归档代码，不重跑 Python/Godot 探针或 Game。

核验后仅在新的独立目录解包查看，不覆盖现有游戏树，不直接安装历史工具。包内 replay_to_new.py 是原审查的可选复现入口，不会由备份校验器执行；不要执行历史生成器或完整驱动。

原件与当前 GD 存在输入校验差异，安装仍暂缓、345 缺口不变、Game/存档未验收。本包不是完整游戏备份。旧依赖未复核，已取消的第 14 批依赖下载不属于本任务。
