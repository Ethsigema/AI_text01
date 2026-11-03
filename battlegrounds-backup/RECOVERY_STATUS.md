# Godot 酒馆战棋恢复备份

最新快照：2026-11-03 03:02:56 UTC（北京时间11:02:56）。历史快照保留在 checkpoints/。

## 恢复所需文件

- checkpoints/battlegrounds_overlay_20261103T030256Z.zip：完整增量、逐文件清单、恢复脚本与验证记录。
- [原始完整交接包](https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip)。
- 原包 SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65。
- 最新增量 ZIP SHA256：d57a7c9e6e4683a2849b38024bbb54ce6bb99fac3b9534c9a2ba452c0a343338。

先解压增量 ZIP，再按其中 battlegrounds-backup/RESTORE.md 执行 Python 恢复工具。目标目录必须尚不存在，不覆盖已有工程。必须同时保留原包和所选增量，增量不能独立运行。

最新版本包含21248个恢复后文件，相比原包有96个变化/新增文件（8682537字节）。清单 SHA256：1a4c6e41f6a1764a07d7ce1b5a3783bbc06dd470967f055b278ca425e627e103。最新远端读取恢复验证状态以 LATEST.json 为准。

## 当前验证范围

Game完整依赖解析无SCRIPT ERROR，实际Catalog构建load_errors为空。自定义双人对局24/24冒烟检查通过，包含买入、打出、冻结、结束回合、出售及5次新Game对象原生存读档，状态/库存/RNG一致。退出仍有ObjectDB及176资源使用警告，明确保留。

原始导入守卫266项及递归序列化59项隔离检查通过；这不是完整卡牌验收。恢复后完整基础身份验收仍为0/433（尚未重新逐身份验证），不表示没有代码。历史153/433不移植为当前验收；总体完成率仍未知。

旧主分支、原始Release和历史备份均保留。不强推覆盖，后续每12小时备份并核对远端；仅含游戏工程，不含凭据或私人聊天。
