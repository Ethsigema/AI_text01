# 恢复暗潮未完成阶段证据

从固定GitHub提交下载MANIFEST.json、SHA256SUMS.txt、verify_package.py和.part000至.part005六片。按编号拼接应为1,471,044字节，SHA256 2842db24f2cc3acfa22e3e941e017b4a7e11929e8e374dc071027e18c63d5a99。

可信Python 3环境可执行 python3 verify_package.py <下载目录> --write-archive --report verification.json。脚本读取分片，在内存核验311成员、内外清单、candidate132项白名单与FAILED/NOT RUN边界，再写不存在的新归档；不覆盖已有归档、不联网、不下载依赖、不执行包内代码或重跑fixture。

仅解包到新独立目录审查，不覆盖游戏树、不应用补丁或安装。唯一fixture失败，最终守卫修订未重测；任何备份校验PASS仅表示字节完整，不能升级为候选验收。归档运行器不自动执行，恢复证据不是新测试授权。

外部金色获取、失败票据恢复、高等级完整随机域及真实Game交付未闭合。候选未安装，345缺口及Game/存档未验收状态保留。旧依赖未复核，本包不能保证完整游戏可恢复；取消的第14批依赖下载不属于本任务。
