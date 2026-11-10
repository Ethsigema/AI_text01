# 恢复本次独立类型/调用链审查包

从固定 GitHub 提交下载本目录 .tar.xz、MANIFEST.json、SHA256SUMS.txt、verify_backup.py。原包应为 229,156 字节，SHA256 2be4232e82443cd5c285420eecae39d318d18847dc4405ea9a7fc5f92f260237。

可在可信 Python 3 环境执行 python3 verify_backup.py <下载目录> --report verification.json，核验全部 99 项成员、内外白名单及审查边界。脚本仅在内存读取归档，不联网、不下载依赖、不执行或导入包内代码，不重跑 Godot 或调用链片段。

核验后仅在新的独立目录解包查看，不覆盖游戏树，不直接安装候选。包内 replay_to_new.py 为原审查的可选复现入口，不由备份校验器执行。

6 次坏 receipt 诊断仍未修复，真实游戏故障可达性未证明；345 缺口未变、Game/旧存档未验收。此包不是完整游戏备份。旧依赖未复核，已取消的第 14 批依赖下载不属于本任务。
