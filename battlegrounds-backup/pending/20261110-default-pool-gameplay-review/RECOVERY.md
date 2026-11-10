# 恢复当前默认池玩法筛选证据包

从固定GitHub提交下载本目录.tar.xz、MANIFEST.json、SHA256SUMS.txt、verify_backup.py。原包应为42,440字节，SHA256 5cddce944074f4b9a4eacc6686bd91019117c6b8df78daba9e20feb42c2fdd39。

可信Python 3环境可执行 python3 verify_backup.py <下载目录> --report verification.json，核验27项成员、内外哈希白名单与未实现边界。校验器只在内存读取归档，不联网、不下载依赖、不执行或导入归档代码、不启动Godot或重跑测试。

核验后只解包到新的独立目录审查，不覆盖游戏树、不安装候选。包内运行器仅记录已发生的成员选择试验，恢复证据不构成自动重跑授权。

27项通过仅限CurrentScope主池选择，不是四项玩法实现验收。源码变更0，345工具缺口和完整Game/旧存档未验收状态不变。本包不是完整游戏备份。旧依赖未复核，取消的第14批依赖下载不属于本任务。
