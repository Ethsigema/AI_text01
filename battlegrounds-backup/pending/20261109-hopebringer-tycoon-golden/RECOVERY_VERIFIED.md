# 金色永恒大亨：已完成的远端回读与独立恢复核验

本说明及回执是对原始封存包的追加材料，不修改原归档、既有说明、历史备份或游戏源码。核验范围是精确源码恢复，不是完整玩法验收。

## 核验结果

- 从固定提交 `893662b9ee76a37e60695c52cbc0fb8cb09379bb` 重新下载全部七个分片，以及 MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README 和 RECOVERY。
- GitHub 连接器实际取得的每个文件 URL、Git blob SHA 和时间见 `FETCH_PROVENANCE.json`；下载字节已核对 Git blob SHA。恢复脚本使用这些刚下载的字节，因此回执 `increment_bytes_freshly_downloaded_by_this_helper` 为 false，仅表示下载由连接器完成，而非此 Python 进程完成。新增量不是沿用上传前的本地副本。
- 七个分片、1,659,404 字节整包和全部 54 个归档文件均通过大小与 SHA256 检查。
- 基线 27,880 文件逐文件重新哈希，精确符合 BASE_MAP；新增 3 文件、修改 5 文件、删除 0 文件。
- 在全新目录独立复制并叠加增量，得到 27,883 文件、1,548,667,393 字节。所有文件大小与 SHA256 均符合 SOURCE_MAP，缺失、多余、不符均为零。无硬链接。
- 恢复后再次完整哈希基线，内容未改变。旧包全部保留，没有删除操作，也没有启动 Godot。

完整回执：`HOPEBRINGER_TYCOON_GOLDEN_REMOTE_CHAIN_VERIFICATION.json`，SHA256 `974151e300525abebb03bf91d957e30f7798ac10634ca10f97cf7c50f53437e2`。

## 明确的历史链复用边界

本轮重新下载的是金色永恒大亨增量。永恒大亨基线是上轮已恢复的精确源码树，本轮重新逐文件哈希，但没有重新下载它的全部历史依赖；早期全链下载证明明确复用，不声称本轮全链重新下载。

固定基线恢复说明：
https://github.com/Ethsigema/AI_text01/blob/819c10f12cade5f2ed67b20cc6e42ad0e3fd0a0b/battlegrounds-backup/pending/20261108-hopebringer-tycoon/RECOVERY.md

基线 SOURCE_MAP SHA256：`1ae20915de380fa09051261af4e1aae1abe07f7d9f682dbbca00c3da04619135`。
基线回执 SHA256：`5ce663d0633c43ed6d87207c8b2ce352f23ffb163729231be4ba363acc6f290e`。本目录 PINNED_BASELINE_RECEIPT.json 是从其固定远端提交重新取得的同一份回执。
目标 SOURCE_MAP SHA256：`84b6a30eb6f82121013e45cd75faab7492803b57efba48fe404a25a5c3c022a2`。

## 重现独立恢复

使用 Python 3 标准库，先按上述固定说明恢复永恒大亨基线，保留其源码树和 SOURCE_MAP。至少准备约 2 GB 额外空间。下载本目录 `verify_and_restore_hopebringer_tycoon_golden.py`，运行：

```sh
python3 verify_and_restore_hopebringer_tycoon_golden.py \
  --baseline-dir /path/to/restored_hopebringer_tycoon_runtime \
  --baseline-source-map /path/to/hopebringer_tycoon_20261108/SOURCE_MAP.json \
  --output /path/to/a-new-golden-recovery-directory
```

脚本默认从固定 GitHub 提交重新下载新增量，验证所有分片、整包、归档成员、变更/删除清单、基线回执和源文件清单，再独立复制重建并前后检查基线。输出目录必须不存在；失败目录和旧备份保留，以另一新目录重试。

若执行环境必须通过连接器取文件，可先从同一固定提交下载 MANIFEST.json、CHANGES.json、REMOVALS.json、SHA256SUMS.txt、README.md、RECOVERY.md 和七个分片，额外传入 `--download-dir /path/to/downloaded`；可用 `--baseline-receipt /path/to/PINNED_BASELINE_RECEIPT.json` 避免脚本再次下载基线回执。所有输入仍受固定 SHA256 和完整文件清单约束。

恢复核验请使用本追加脚本，而非包内开发用途的 `materialize.py`。后者绑定开发目录且使用硬链接；本脚本不使用硬链接，不允许多余基线文件，也不在验证树启动游戏。原包保持封存状态，没有重写其中任何文件。

要求输出回执状态为 `PASS_EXACT_SOURCE_ONLY`，missing/mismatched/unexpected 三个列表为空、baseline_unchanged_after_restore 和 independent_copy_no_hardlinks 为 true。

## 未验收内容

本次恢复核验没有运行玩法。原封存包中的有界夹具结果及失败记录保持原样，旧基线完整对照被 SIGKILL 未算通过。自然金色获取/三连、重复复仇、满场、多大亨、完整房间与 UI 等仍未验收。没有声称找回 11 月 6 日已丢失的工作。
