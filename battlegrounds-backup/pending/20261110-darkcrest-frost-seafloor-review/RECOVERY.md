# 恢复最新霜鳞/海床阶段审查包

从固定GitHub提交下载MANIFEST.json、SHA256SUMS.txt、verify_package.py和.part000至.part034共35片。按编号拼接应为8,697,600字节，SHA256 5b0854c68b9c3b705cafcb81eeb6239a096110db892664ce8e936490742064e7。只恢复091927Z最新澄清版，不混入被替代091805Z。

可信Python 3环境可执行 python3 verify_package.py <下载目录> --write-archive --report verification.json。脚本读取分片，在内存核验1229项成员、内外清单、初版338项与后继863项公开白名单及未验收边界，再写不存在的新归档。不覆盖已有归档、不联网、不下载依赖、不执行包内代码或重跑测试。

仅解包到新独立目录审查，不覆盖游戏树、不应用补丁或安装。初版未运行，唯一后继试验FAILED，fixture对可选字段pool_blocker要求错误，没有2802项PASS总结。完整getter调用链、真实入手、Game/等级4/存档未验收。

本包不是完整游戏树，旧依赖未复核，取消的第14批依赖下载不属于本任务，不能保证整链可恢复。
