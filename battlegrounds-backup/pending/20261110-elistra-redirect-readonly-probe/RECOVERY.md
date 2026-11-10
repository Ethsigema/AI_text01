# 恢复本次独立艾丽斯特拉证据包

从固定 GitHub 提交下载本目录 .tar.xz、MANIFEST.json、SHA256SUMS.txt、verify_backup.py。原包须为149,468字节，SHA256 bf2e9bf9747469d66c7caad93ef3af87512d02d3622914633189af6436833ef8。

可信 Python 3 环境可执行 python3 verify_backup.py <下载目录> --report verification.json，核验82项成员、内外哈希白名单和未安装边界。脚本只在内存读取归档，不联网、不下载依赖、不执行或导入归档代码，不重跑Godot/Python探针。

核验后仅在新的独立目录解包查看，不覆盖现有游戏树、不安装候选、不直接应用历史整包补丁。包内 replay_to_new.py 是原审查可选复现入口，不由备份校验器自动执行。

历史工具与GD准入差异仍待进一步研究，真实Game可达性未知，345缺口不变，完整驱动和旧存档未验收。本包不是完整游戏备份。旧依赖未复核，已取消的第14批依赖下载不属于本任务。
