# 恢复深渊打手原生接收能力审查包

从固定 GitHub 提交下载 MANIFEST.json、SHA256SUMS.txt、verify_package.py 和 .part000 至 .part003 四片。按编号拼接应为833,060字节，SHA256 e23b8cbd5eee07c4c468ec476fbbdd73c0ba91e7a04405a3620bbe5c8bfd4e6c。

可信 Python 3 环境可执行 python3 verify_package.py <下载目录> --write-archive --report verification.json。脚本读取分片，在内存核验290项成员、内外清单、trial 274项白名单及未验收边界，再写不存在的新归档。不覆盖已有归档、不联网、不下载依赖、不执行包内代码或重跑测试。

仅解包到新独立目录审查，不覆盖游戏树、不应用补丁或安装。原试验是192MiB触阈停止，没有 LOAD_OK/属性提交；683项计划测试未执行，不得当作通过记录。

本包不是完整游戏树，Game/等级4/存档仍未验收。旧依赖未复核，取消的第14批依赖下载不属于本任务，不能保证整链可恢复。
