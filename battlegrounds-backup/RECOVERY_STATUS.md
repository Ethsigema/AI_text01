# Godot 酒馆战棋恢复备份

当前快照：2026-11-03 06:42:23 UTC（北京时间14:42:23）。后续本地变化不自动属于本备份；实际远端验证结果见 LATEST.json。

## 合并与恢复

完整增量使用标准TAR.XZ整体压缩，保留全部源码和证据，压缩后15,868,140字节，分成4块。请克隆本分支或下载 checkpoints/20261103T064223Z/ 中全部4个 .part 文件与 .parts.json 清单，并下载 tools/assemble_backup.py 和 tools/extract_backup.py。

```sh
python3 battlegrounds-backup/tools/assemble_backup.py battlegrounds-backup/checkpoints/20261103T064223Z/battlegrounds_overlay_20261103T064223Z.parts.json battlegrounds_overlay_20261103T064223Z.tar.xz
python3 battlegrounds-backup/tools/extract_backup.py battlegrounds_overlay_20261103T064223Z.tar.xz extracted-backup --sha256 130d07a9a79318dd307eae422312389f7d6aa73d131af32d5fef02a41829f2cc
```

然后按 extracted-backup/battlegrounds-backup/RESTORE.md 恢复。工具仅用Python标准库。必须另有[固定原始完整交接包](https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip)，目标目录必须尚不存在，不覆盖已有工程。增量不能独立运行。

- 原包SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65
- TAR.XZ SHA256：130d07a9a79318dd307eae422312389f7d6aa73d131af32d5fef02a41829f2cc
- 完整清单SHA256：2c6d12a5a7196dc2c3b60d2b92d8837004cc0fc859d4deb1132d95f15c9b9662

恢复后29517文件；相对原包8370个新增/变化文件（626021921字节）。包含源代码、必需数据/素材/原始证据、验收矩阵和进度台账。排除.git/.godot/__pycache__缓存，保留素材及.import元数据；恢复后按说明使用Godot4.6.3重新导入。

## 截点验证范围

当前限定普通效果33/433（7.62%）：9随从、20酒馆法术、4英雄。11个复验套件经独立复核，16518项检查、250次原生重载检查点、249个不同原生输入及261条战斗记录。运行来源清单为c3b958ef50c2032b5bedf59cfcd0af42228157a17d316dbed8e235ad933ea623。

仅声明各测试注明的普通程序与边界，不等于所有金色、任意组合或全功能验收。全局verified仍false，总体完成率与六机制完整覆盖率未知；历史153/433不移植为当前验收。

旧主分支、原始Release、前三个快照及各自验证记录均保留。所有推送为保留历史的快进提交，不强推。备份仅限游戏工程，不含凭据或私人聊天。
