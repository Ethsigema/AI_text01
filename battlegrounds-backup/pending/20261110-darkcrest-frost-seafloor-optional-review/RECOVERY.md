# 恢复霜鳞/海床可选字段fixture审查包

从固定GitHub提交下载MANIFEST.json、SHA256SUMS.txt、verify_package.py和.part000至.part021共22片。按编号拼接应为5,393,436字节，SHA256 00097718164f6665867f6ee79d5f033cf99e112f921cfc6b2040ba6760d53a70。

可信Python 3环境可执行 python3 verify_package.py <下载目录> --write-archive --report verification.json。脚本读取分片，在内存核验908项成员、内外清单、893项公开白名单及新旧结果边界，再写不存在的新归档。不覆盖已有归档、不联网、不下载依赖、不执行包内代码或重跑测试。

仅解包到新独立目录审查，不覆盖游戏树、不应用补丁或安装。原FAILED保留，新2810项PASS只对应新独立小helper fixture，生产原校验未改。完整Game、真实入手、Fandral→Catalog getter链、等级4与存档未验收。

本包不是完整游戏树，旧依赖未复核，取消的第14批依赖下载不属于本任务，不能保证整链可恢复。
