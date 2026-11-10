# 恢复本次独立只读审查包

从固定 GitHub 提交下载本目录 .tar.xz、MANIFEST.json、SHA256SUMS.txt 和 verify_backup.py。原包必须为 228,404 字节，SHA256 2ccad346879d2b1fe0cd4f020b338d5a7d403bcff92f9312a1df4a4fbf046414。

可在可信 Python 3 环境执行 python3 verify_backup.py <下载目录> --report verification.json，核对原包与全部 141 项成员、内外白名单及审查边界。校验器仅在内存读取归档，不联网、不下载依赖、不执行或导入归档代码，不重跑 Python/Godot 或类型诊断探针。

核验后只在新的独立目录解包查看，不覆盖现有源码树，不安装原工具或直接应用整包历史补丁。包内 replay_to_new.py 是原审查提供的可选复现入口，不由备份校验器自动执行。

差异尚未证明实际游戏可达，安装仍暂缓；345 缺口未变，Game/旧存档未验收。本包不是完整游戏备份。旧依赖未复核，已取消的第 14 批依赖下载不属于本任务。
