# 恢复本次只读编译器证据包

从固定 GitHub 提交下载 MANIFEST.json、SHA256SUMS.txt、verify_package.py，以及 .part000 至 .part003 四个分片。分片大小与 SHA256 见 MANIFEST.json；按编号拼接后必须为 770,616 字节，SHA256 c92e371e0dbb447093d9348f558dc7bfd2b75056eba36a38e99d3a738901be87。

可在可信 Python 3 环境执行 python3 verify_package.py <下载目录> --write-archive --report verification.json。脚本只读取本包分片，在内存检查 73 项成员、内外白名单和审查边界，再写入不存在的新归档；不会覆盖现有归档。它不联网、不下载依赖、不执行或导入包内脚本，不运行 Godot、Game 或编译器。

核验成功后仅在新的独立目录解包查看。本包不是可安装驱动或独立完整游戏备份。当前权威驱动仍未确认，345 缺口未变，Game/存档未验收。旧依赖未复核，之前被取消的第 14 批依赖下载不属于本任务。
