# 恢复真实Game受限加载能力记录

从固定GitHub提交下载本目录.tar.xz、MANIFEST.json、SHA256SUMS.txt、verify_backup.py。原包应为223,496字节，SHA256 15fc0d1d986c36296bb5d2dc3bbf7d3a9d9bf8d2cd681fc90515f7b0da436c2d。

可信Python 3环境可执行 python3 verify_backup.py <下载目录> --report verification.json，核验22项成员、内外哈希清单和未加载/未实例化/未调用_buff边界。校验器仅在内存读取归档，不联网、不下载依赖、不执行或导入归档代码，不启动Godot。

核验后只解包到新的独立目录审查，不覆盖游戏树或安装候选。包内监督程序只记录已发生的试验，不自动执行；恢复证据不是重试加载或提高预算的授权。

此包不含完整依赖，历史依赖未复核，不能声称完整游戏可恢复。唯一768MiB试验触阈停止，不是Game或旧存档验收。取消的第14批依赖下载不属于本任务。
