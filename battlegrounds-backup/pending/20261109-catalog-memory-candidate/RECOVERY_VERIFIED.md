# 目录内存实验候选：远端下载及独立源码恢复通过

实验状态仍为EXPERIMENTAL_DATA_ONLY_PASS_FULL_GAME_UNTESTED。完整Game没有运行或通过；最后已验收基线仍是金色召唤者a71d3e4ea64dc52264a3f789a48ddae2e4a043cd。本次直接依赖女妖候选，未省略或提升该未完成中间版本。源码恢复通过不能当作完整玩法验收。

## 已完成结果

- 原包固定提交 `60883b1d19faf947134db07e7ba3f9fdeacc2de6`，提交仅新增12个文件，无修改或删除旧文件。
- 使用git fetch固定提交实际下载本次新增对象，然后读取同一提交全部上传文件。六个归档分片对象在下载前均不存在本地Git对象库，不是复用本地待上传包；Git可能去重相同的历史辅助文件。下载记录见FETCH_PROVENANCE.json、BEFORE_FETCH_OBJECTS.json及ARCHIVE_PUBLICATION_RECEIPT.json。
- 六个分片、1,309,192字节归档及113个归档文件的大小和SHA256全部匹配；包内112项文件清单也严格对应，内部清单本身由外部MANIFEST覆盖。
- 原包SHA256：`e5272cc3556bf626d353993b142a75d40ea26c4522eb94bcb2f5a55994f7f7d6`。
- 基线27,892个文件逐个重哈希。真实差异只有core/catalog.gd一个文件，净增432字节，新增0、删除0；完整替换文件位于patch/core/catalog.gd。
- 全新目录独立复制并覆盖，恢复27,892文件、1,548,714,104字节。每个文件严格符合SOURCE_MAP，缺失、多余、不符均为0。未使用硬链接。
- 恢复后再次完整哈希基线，内容未变。没有运行Godot、改动原包、删除旧备份或提升已验收基线。

完整回执：`CATALOG_MEMORY_CANDIDATE_REMOTE_VERIFICATION.json`，SHA256：`45d53273107a8411727d9d2e1462810ac6e685c4e1f62727eb55fdfd81a4d384`。

## 历史链边界

本轮重新下载本内存实验增量，直接基线复用之前已独立恢复的女妖候选并重新逐文件核验。历史全链没有在本轮重新下载。

直接基线恢复说明：
https://github.com/Ethsigema/AI_text01/blob/35c7fc04e0cb85c4ec9435bf4d2861b65c057971/battlegrounds-backup/pending/20261109-hopebringer-banshee-golden-candidate/RECOVERY_VERIFIED.md

基线归档SHA256：`a20b6c427a1219903df1d4a927693d3e553a337236f509408eff651318297433`。
基线SOURCE_MAP SHA256：`45dcd76fe50c5e2e03cea65032189b15cca35894cac08b2e704c17139b7fd6a8`。
基线核验回执SHA256：`f7befb5b72d4bb9773f92413144635e1ac3388b7bc0ba1998227bc03027d6e78`，已从固定远端提交重新取回并验证，副本见PINNED_BASELINE_RECEIPT.json。
目标SOURCE_MAP SHA256：`e52121d24d2b21f75af73521362928a2da449f7f42915fb692cfcb3d425ab0a0`。

此外，另一次定时核验曾重新下载历史全链直至女妖候选，固定说明如下。它未包含本内存实验增量，不能把它说成本轮全链重新下载：
https://github.com/Ethsigema/AI_text01/blob/0d47d1b6bf8c2943647fbc59ba8448cd6dde0ab9/battlegrounds-backup/pending/20261109-banshee-golden-fresh-chain/RECOVERY.md

## 重现独立恢复

Python3.9及以上标准库，至少2GB额外空间。先恢复女妖候选及其SOURCE_MAP，下载本目录脚本后执行：

```sh
python3 verify_and_restore_catalog_memory_candidate.py \
  --baseline-dir /path/to/restored_hopebringer_banshee_golden_candidate_runtime \
  --baseline-source-map /path/to/hopebringer_banshee_golden_20261109/SOURCE_MAP.json \
  --output /path/to/a-new-catalog-memory-recovery-directory
```

脚本从固定提交下载本次实验，验证分片、归档、所有成员、内外清单、基线回执、源文件映射、变更/删除清单及实验状态。之后独立复制恢复，并前后完整检查基线。输出目录必须不存在，已有输出及旧备份全部保留。

也可先从相同提交下载MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY及全部6片，加 `--download-dir /path/to/downloaded`；基线回执可经 `--baseline-receipt /path/to/PINNED_BASELINE_RECEIPT.json` 提供。固定SHA256验证仍全部执行。

本轮采用Git预下载模式，回执increment_bytes_freshly_downloaded_by_this_helper:false只表示下载不由该Python进程执行，真实新下载证明见FETCH_PROVENANCE.json。脚本不使用硬链接、不容许基线额外文件、不启动游戏。

## 保持未验收的范围

本次未重跑封存的数据探针或战斗探针。原数据A/B的逐卡输出等价、8项边界检查及约21.8%数据探针RSS下降均保留原证据，不能外推完整Game收益。畸形输入仍出现相同旧错误，不是新实现的友好拒绝。全部来源验证器、额外overlay/registry、完整catalog编译、Game、存档、回放及希望信使同场未验收；旧女妖独立战斗通过不是新catalog完整验收。先前SIGKILL系统原因未获确认。没有声称恢复已丢失的11月6日工作。
