# Godot 酒馆战棋恢复备份

本次快照：2026-11-03 05:17:13 UTC（北京时间13:17:13）。上传时间晚于截点，实际远端恢复验证状态见 LATEST.json。后续本地变化不自动属于本备份。

## 下载与恢复

本次完整增量压缩包为35,099,798字节，分成9块保存在 checkpoints/20261103T051713Z/。请下载该目录全部9个 .part 文件、.parts.json 清单，以及 tools/assemble_backup.py，保持文件名不变。也可克隆整个分支。先合并并逐块校验：

```sh
python3 battlegrounds-backup/tools/assemble_backup.py \\
 battlegrounds-backup/checkpoints/20261103T051713Z/battlegrounds_overlay_20261103T051713Z.parts.json \\
 battlegrounds_overlay_20261103T051713Z.zip
```

然后解压合并的ZIP，按其中 battlegrounds-backup/RESTORE.md 恢复。恢复工具需要[原始完整交接包](https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip)，目标目录必须尚不存在，不覆盖已有工程。不能仅凭增量直接运行游戏。

- 原包 SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65
- 合并ZIP SHA256：3fbc73ac1862e45749f2eb6ca74dbbcfd72d51465af9a8827f514214b07f0665
- 完整文件清单 SHA256：35c25fe6295ef87629ce6b6ce85c46e8baa9372719c3a94685f2f96de9787758

恢复后28457文件；相对原包7308个新增/变化文件（331325805字节），包含源码、必需资源、原始测试证据、验收矩阵和进度台账。缓存.git/.godot/__pycache__排除，素材和.import元数据保留。恢复后按说明用Godot4.6.3重新导入资源；已验证导入3950项成功。

## 截点验证范围

限定基本效果30/433（6.93%）：6随从、20酒馆法术、4英雄。局部边界验证不等于任意组合或总体完成率，全部全局verified仍false。总体完成率与六机制完整覆盖率未知。历史153/433不移植为恢复工程验收。

最后Naga批次exit124超时，保留36实际命令信封和35完成的存读/等值检查，不计完整身份。所有限制以快照内PROGRESS/ledger/验收矩阵和原始日志为准。

先前两个独立快照及验证记录保留。后续快进提交，不强推、不修改main。备份仅限游戏工程，不含凭据或私人聊天。
