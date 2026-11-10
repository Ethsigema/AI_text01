# 恢复本次独立艾丽斯特拉新修正审查包

从固定GitHub提交下载本目录.tar.xz、MANIFEST.json、SHA256SUMS.txt、verify_backup.py。原包应为182,164字节，SHA256 0d743ad1e5c15305adccf46032276ab59dc09fb034d6ca3bc2525a6555c2da5f。

可信Python 3环境可执行 python3 verify_backup.py <下载目录> --report verification.json，核验130项成员、内外哈希白名单、候选身份和未安装边界。校验器只在内存读取归档，不联网、不下载依赖、不执行或导入归档代码，不重跑Godot/Python测试。

核验后仅解包至新的独立目录审查，不覆盖现有游戏树、不安装候选、不直接应用历史整包补丁或新修正补丁。包内replay_to_new.py是可选复现入口，不由备份校验器自动执行。

候选不是历史原件或已证实最新版；8项历史hook前置异常仍未修复，345缺口不变，完整驱动/Game/旧存档未验收。本包不是完整游戏备份。旧依赖未复核，已取消的第14批依赖下载不属于本任务。
