# 23点审计补充包恢复说明
本目录为审计台账和验证工具，不包含独立游戏源码，也不能覆盖游戏目录。
游戏固定恢复入口：
https://github.com/Ethsigema/AI_text01/blob/0b2962c294aa4c0e4354bdc119f2fecd732d3c03/battlegrounds-backup/pending/20261112-lava-mini-permanent-v2/RECOVERY.md
按其说明获取原Release、固定batch14完整24项、本候选完整17项并恢复。Godot 4.6.3；恢复Python3.12+；低空间恢复器需Linux/macOS。
本包verify_stream.py读取同目录base_package、candidate_package及original_release.zip，依据REMOTE_FILES.json和download_fresh.py先重新下载42项，再逐文件流式重建验证。只有成功输出STREAM_RECONSTRUCTION_VERIFIED.json才算本次全部字节核验；不会创建完整游戏目录，也不验收玩法。
进度台账独立保存，未改动已冻结的源码。最终实战证据链接见PROGRESS.md后续补充。所有旧备份保留。
