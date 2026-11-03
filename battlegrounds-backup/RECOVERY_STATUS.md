# Godot 酒馆战棋恢复备份

快照时间：2026-11-03 02:41:31 UTC（北京时间10:41:31）。

## 恢复所需文件

- 本目录 checkpoints/battlegrounds_overlay_20261103T024131Z.zip：当前恢复工程相对原包的全部增量、完整清单、恢复脚本及验证记录。
- 原始完整交接包：[下载原包](https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip)。
- 原包 SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65。
- 增量 ZIP SHA256：507dac5bc207e5d3970b4cb5ae8fc2dde062b7901b5df36a00d1ccecf3f09b56。

先解压增量 ZIP，再按其中 battlegrounds-backup/RESTORE.md 运行 Python 恢复工具。目标目录必须尚不存在，工具不覆盖已有工程。

此版本包含21193个恢复后文件，18个变化/新增文件（1422783字节）。清单 SHA256：0b7bb668050d0f16f0c966deeab1c1de1969bd494651cf508a6102ba80df7efe。独立新目录恢复后，全部21193个文件大小和SHA256一致。

## 验证边界

原交接包21179条文件清单已核对。当前包含启动解析的初步修复及失败日志；完整Game解析仍有错误，未通过玩法验收。历史153/433不算此恢复工程的新验收。文件恢复验证不是可玩版本或全功能验收。

旧主分支、原始Release和历史备份保留。本分支后续用快进提交保存新检查点，不强推。每12小时上传更新并核对远端内容；未上传成功须明确记录。备份仅含游戏工程，不含账号凭据或私人聊天。
