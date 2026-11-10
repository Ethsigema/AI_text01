# 恢复暗潮发放恢复候选证据包

从固定GitHub提交下载MANIFEST.json、SHA256SUMS.txt、verify_package.py和.part000至.part007八片。按编号拼接应为1,851,676字节，SHA256 874a91a8ea263ded562f033e04ebc9335bfef14cda963942b07c9790f230d064。

可信Python 3环境可执行 python3 verify_package.py <下载目录> --write-archive --report verification.json。脚本读取分片，在内存核验427项成员、内外哈希及candidate295项白名单，然后写不存在的新归档；不覆盖已有归档、不联网、不下载依赖、不执行包内代码或重跑测试。

只解包到新独立目录审查，不覆盖游戏树、不应用补丁或安装。候选不是完整游戏副本，恢复此证据不能证明其全部依赖或整链可恢复。归档运行器不自动执行，恢复证据不是新测试授权。

104项局部断言不代表真实Game/Waiting或交付恢复验收。金色/高等级域继续限制，候选未安装，345缺口及Game/存档未验收边界保留。历史依赖未复核，取消的第14批依赖下载不属于本任务。
