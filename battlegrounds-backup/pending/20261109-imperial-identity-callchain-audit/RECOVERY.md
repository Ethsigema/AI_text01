# 本次只读证据包恢复

从固定 GitHub 提交下载本目录原始 .tar.xz、MANIFEST.json、SHA256SUMS.txt 和 verify_backup.py。原包应为 265,036 字节，SHA256 f77e2a104017e743ee7c529feeef9bd4137367cacfcee65e2c34252139e9f846。

可用可信 Python 3 执行 python3 verify_backup.py <下载目录> --report verification.json。脚本只读取本包、核对全部 22 项成员与内外白名单，不联网、不下载依赖、不执行或导入归档脚本，不运行 Godot、Game 或完整编译器。

核验成功后仅在新的独立目录解包查看，不覆盖现有游戏树，也不安装任何候选。本包不构成完整游戏备份或游戏/存档验收。候选仍暂缓，345 项缺口未变，旧依赖未复核；此前取消的第 14 批依赖下载不属于本任务。
