# 恢复独立hook根类型守卫审查包

从固定GitHub提交下载本目录.tar.xz、MANIFEST.json、SHA256SUMS.txt、verify_backup.py。原包应为133,628字节，SHA256 45dc3cfcf03d27802fe90fd76279d47e42167d43a646517a20651bf45a1a8be5。

可信Python 3环境可执行 python3 verify_backup.py <下载目录> --report verification.json，核验47项成员、内外哈希白名单、提议片段身份与未安装边界。校验器只在内存读取归档，不联网、不下载依赖、不执行或导入归档代码、不重跑探针。

核验后仅解包到新的独立目录审查，不覆盖游戏树、不安装提议、不应用局部hunk。包内replay_to_new.py是可选复现入口，不由备份校验器自动执行。

局部提前拒绝仍是编译失败，不能当成功产物；没有完整修改版driver。345缺口、完整驱动/Game/旧存档未验收状态不变。本包不是完整游戏备份。旧依赖未复核，取消的第14批依赖下载不属于本任务。
