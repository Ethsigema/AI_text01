# 只恢复本次审查包

从固定 GitHub 提交下载本目录的原始 .tar.xz、MANIFEST.json、SHA256SUMS.txt 和 verify_backup.py。核对归档为 104,588 字节、SHA256 19750c8aa7ad3117befab977d8dd338fbb934d5ed5c958cf373a52e71e54bde0。

可在可信 Python 3 环境执行 python3 verify_backup.py <下载目录> --report verification.json。此脚本只读取并检查本归档的 57 个文件、内外 SHA256 白名单、候选身份和明确暂缓边界；不联网，不下载任何依赖，不执行或导入包内工具，不运行 Godot 或 Game。

验证成功后，仅在新的独立目录解包查看。不要覆盖当前游戏树，也不要直接安装修正稿。候选仍有 3 项映射身份差异，345 项缺口不变，Game 与存档未验收。包内 replay_to_new.py 是原审查提供的可选测试复现入口，不属于本次备份验收，也不会由备份校验器自动执行。

此前被取消的第 14 批依赖下载不属于本任务；本次旧依赖未复核。
