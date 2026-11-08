# 金色永恒召唤者：远端回读及独立恢复核验

本材料追加到原封存增量旁，不改写原包、历史备份或游戏源码。核验范围是精确源码恢复，不是完整玩法验收。

## 已完成结果

- 已确认恢复分支以非强制快进方式指向归档提交 `9cab53df735383aa7469dab71451dfcc283c3231`，该提交只新增21个文件，无修改或删除。
- 使用 `git fetch origin 9cab53df735383aa7469dab71451dfcc283c3231` 重新取得远端新增对象，再从同一固定提交读取全部21个上传文件。下载前15个归档分片的Git对象全部不存在于本地对象库，证明本次归档不是沿用上传前的本地文件；Git可能去重复用相同的历史辅助文件对象，例如空删除清单。记录见 `BEFORE_FETCH_OBJECTS.json`、`FETCH_PROVENANCE.json` 与 `ARCHIVE_PUBLICATION_RECEIPT.json`。
- 15个分片、3,686,500字节整包和全部71个归档文件的大小、SHA256均通过，外部清单与包内70项清单严格对应。整包SHA256：`b5da7d7e86a59b6ae2dce39ff071feaedef80d6c10947f72cca6bd55ea418522`。
- 基线27,883个文件全部重新哈希，精确符合BASE_MAP。源码新增6个文件、修改7个文件、删除0个文件，全部13个差量覆盖真实完整差异，没有遗漏或多余差量。
- 在全新目录独立复制、叠加，得到27,889个文件、1,548,697,882字节。所有文件大小与SHA256符合SOURCE_MAP，缺失、多余、不符均为零。无硬链接。
- 恢复后再次完整哈希基线，内容未变。全部旧备份保留，没有删除操作，没有启动Godot。

完整回执：`HOPEBRINGER_SUMMONER_GOLDEN_REMOTE_CHAIN_VERIFICATION.json`，SHA256：`95a9eea6be3b1e309e535aabd3936705d7f4d69a27569ab1f357a5a4dea3880d`。

## 历史链复用边界

本轮重新下载的是金色永恒召唤者增量。金色永恒大亨基线来自上一轮已经独立恢复的源码树，本轮逐文件重哈希，但没有重新下载全部历史依赖；早期全链下载证明复用，不能描述为本轮历史全链重新下载。

固定基线恢复说明：
https://github.com/Ethsigema/AI_text01/blob/ddae092130aa47ef311d2d616bd489e769477452/battlegrounds-backup/pending/20261109-hopebringer-tycoon-golden/RECOVERY_VERIFIED.md

基线归档SHA256：`b7e400d6f2a9ffc6812029503a79765934c22f9c38368fd1dc2d7483d71771f3`。
基线SOURCE_MAP SHA256：`84b6a30eb6f82121013e45cd75faab7492803b57efba48fe404a25a5c3c022a2`。
基线回执SHA256：`974151e300525abebb03bf91d957e30f7798ac10634ca10f97cf7c50f53437e2`。本目录PINNED_BASELINE_RECEIPT.json已从该固定远端提交重新取得并核对。
目标SOURCE_MAP SHA256：`32cd814943a82a4ee79fb05de8a3f4d24d7f74d7b609dd6247aebcd5a4cc7449`。

## 重现恢复

使用Python 3.9及以上标准库。按上述固定说明恢复金色永恒大亨基线，并保留其源码树、SOURCE_MAP。准备至少2GB额外空间，下载本目录的独立恢复脚本，运行：

```sh
python3 verify_and_restore_hopebringer_summoner_golden.py \
  --baseline-dir /path/to/restored_hopebringer_tycoon_golden_runtime \
  --baseline-source-map /path/to/hopebringer_tycoon_golden_20261109/SOURCE_MAP.json \
  --output /path/to/a-new-golden-summoner-recovery-directory
```

脚本默认从固定GitHub提交下载本次增量，验证全部分片、整包、成员、内部清单、基线回执及变更/删除清单，然后独立复制恢复，逐文件前后检查基线。输出目录必须不存在。保留失败输出及旧备份，重试时使用新的目录。

若使用Git或连接器下载，可先从相同固定提交取MANIFEST.json、CHANGES.json、REMOVALS.json、SHA256SUMS.txt、README.md、RECOVERY.md及15个分片，额外传入 `--download-dir /path/to/downloaded`，并可用 `--baseline-receipt /path/to/PINNED_BASELINE_RECEIPT.json`。所有输入仍由固定SHA256约束。此次采用预下载模式，回执 `increment_bytes_freshly_downloaded_by_this_helper:false` 只表示下载不由该Python进程执行，真实本轮下载证明在FETCH_PROVENANCE.json，不意味着沿用本地待上传包。

请用追加的独立恢复脚本，而非包内开发用途的materialize.py；后者绑定开发目录并使用硬链接。本脚本不使用硬链接，不容许多余基线文件，也不运行游戏。原包中的uploaded:false是封存时状态，原包未改写。

## 未验收范围

本次是源码恢复核验，没有新增玩法测试。封存包有界测试及失败记录保持原样。自然金色获取/三连、满场失败、额外亡语/复生观察者、多局完整房间、UI与美术尚未验收。首轮加载被SIGKILL和两次构建失败没有记为通过。没有声称找回11月6日已经丢失的工作，整体游戏完成度仍未知。
