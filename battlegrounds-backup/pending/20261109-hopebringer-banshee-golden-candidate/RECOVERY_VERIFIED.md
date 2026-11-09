# 金色障蔽女妖候选：源码远端回读及独立恢复通过

候选状态仍为candidate_pending_full_game_validation，不能替代上一已验收金色永恒召唤者基线。此次通过的仅是源码备份与恢复完整性，不是完整玩法验收。完整Game加载4次SIGKILL、没有玩法报告；独立战斗与来源契约20项检查通过、实际独立战斗2次。失败和局部成功记录均完整保留。

## 已完成核验

- 恢复分支非强制快进至归档提交 `c6e62f2af2277b43b139b8049936008772df979d`。该提交仅新增11个备份文件，无修改或删除旧文件。
- 通过 `git fetch origin c6e62f2af2277b43b139b8049936008772df979d` 取得远端新增对象，再读取该固定提交的全部11个文件。5个归档分片Git对象在下载前均不存在于本地对象库，不是沿用本地待上传包；相同的历史辅助文件对象可能由Git去重复用。记录见BEFORE_FETCH_OBJECTS.json、FETCH_PROVENANCE.json及ARCHIVE_PUBLICATION_RECEIPT.json。
- 5个分片、1,182,008字节整包及全部109个归档成员的大小与SHA256均一致。包内108项文件清单也已严格核对，清单本身由外部MANIFEST覆盖。
- 归档SHA256：`a20b6c427a1219903df1d4a927693d3e553a337236f509408eff651318297433`。
- 对27,889个基线文件重新哈希；真实源码差异为新增3、修改5、删除0，8个delta文件完整覆盖差异。
- 全新目录无硬链接独立复制与覆盖，恢复27,892个文件、1,548,713,672字节，严格符合SOURCE_MAP。缺失、多余、不符均为零。
- 恢复后再次完整哈希基线，内容未变。没有运行Godot，没有删除任何旧备份，也没有将候选提升为完整验收版本。

核验回执：`HOPEBRINGER_BANSHEE_GOLDEN_CANDIDATE_REMOTE_VERIFICATION.json`，SHA256：`f7befb5b72d4bb9773f92413144635e1ac3388b7bc0ba1998227bc03027d6e78`。

## 明确的历史链边界

本轮真实重新下载女妖候选增量，历史依赖复用上一轮已独立恢复的金色召唤者基线并重新逐文件核对。没有重新下载历史全链；此前全链下载证明是复用的，不能说成本轮重下。

基线固定恢复说明：
https://github.com/Ethsigema/AI_text01/blob/a71d3e4ea64dc52264a3f789a48ddae2e4a043cd/battlegrounds-backup/pending/20261109-hopebringer-summoner-golden/RECOVERY_VERIFIED.md

基线归档SHA256：`b5da7d7e86a59b6ae2dce39ff071feaedef80d6c10947f72cca6bd55ea418522`。
基线SOURCE_MAP SHA256：`32cd814943a82a4ee79fb05de8a3f4d24d7f74d7b609dd6247aebcd5a4cc7449`。
基线核验回执SHA256：`95a9eea6be3b1e309e535aabd3936705d7f4d69a27569ab1f357a5a4dea3880d`，已从固定远端提交重新取回并核对，副本见PINNED_BASELINE_RECEIPT.json。
候选SOURCE_MAP SHA256：`45dcd76fe50c5e2e03cea65032189b15cca35894cac08b2e704c17139b7fd6a8`。

## 重现独立恢复

使用Python 3.9及以上标准库，准备至少2GB额外空间。先按上述说明恢复金色召唤者基线及其SOURCE_MAP，再下载本目录脚本：

```sh
python3 verify_and_restore_hopebringer_banshee_golden_candidate.py \
  --baseline-dir /path/to/restored_hopebringer_summoner_golden_runtime \
  --baseline-source-map /path/to/hopebringer_summoner_golden_20261109/SOURCE_MAP.json \
  --output /path/to/a-new-banshee-candidate-recovery-directory
```

默认从固定提交下载本次候选，检查分片、归档、全部成员、内外清单、基线回执、源文件映射、变更/删除清单及候选状态，然后独立恢复并前后哈希基线。输出目录必须不存在，已有输出及旧备份均保留。归档内部根目录是hopebringer_banshee_golden_20261109，名称没有candidate；候选身份以归档名及状态文件为准。

若已通过Git或连接器从相同提交下载MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY和5个分片，可加 `--download-dir /path/to/downloaded`；也可加 `--baseline-receipt /path/to/PINNED_BASELINE_RECEIPT.json`。固定SHA256检查仍全部执行。

本轮采用预下载模式，回执increment_bytes_freshly_downloaded_by_this_helper:false只表示下载不是这个Python进程执行，实际新下载证明在FETCH_PROVENANCE.json。原包uploaded:false仅代表封存时状态。

独立恢复使用这里追加的脚本，不能用绑定开发路径及硬链接的materialize.py替代。要求PASS_EXACT_SOURCE_ONLY，三个差异列表为空、基线未变、无硬链接，同时candidate_status保持候选、promote_over_verified_baseline及full_game_validation_passed必须仍为false。

## 未通过范围

完整Game初始化、希望信使同场的公开招募/出牌/结束回合/结算、拥有者永久成长、原生存读档和完整命令重放未验证。自然金色获取/三连、多次复生、已有圣盾重触发、满场、额外观察者、完整房间和UI也未验收。SIGKILL的确切系统原因未经确认。本次未声称找回11月6日已丢失的工作，整体完成度仍未知。
