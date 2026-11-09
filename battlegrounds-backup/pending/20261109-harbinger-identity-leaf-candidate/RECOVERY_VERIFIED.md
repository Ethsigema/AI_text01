# Harbinger身份共享叶实验：远端下载与独立源码恢复通过

状态仍为EXPERIMENTAL_SCOPED_EQUIVALENCE_AND_ENTRY_MEMORY_PASS_FULL_GAME_UNTESTED。完整catalog/Game没有验收，本次不运行探针或游戏，不提升此前基线。a71d3e4ea64dc52264a3f789a48ddae2e4a043cd仅延续此前限定范围验收，不应描述成全机制回归已通过。

## 已完成核验

- 原包提交 `9c6255899ed6fffc853c274c8f302d1af10c9764`，只新增11个备份文件，旧文件无修改或删除，未强推。
- 使用git fetch固定提交实际下载，再逐个读取同一提交的上传文件。全部5个归档分片对象在下载前均不存在本地Git对象库，不是复用本地待上传包。Git可能对相同辅助文件去重。证明见FETCH_PROVENANCE.json、BEFORE_FETCH_OBJECTS.json及ARCHIVE_PUBLICATION_RECEIPT.json。
- 5个分片、1,092,872字节整包、126个归档文件的大小及SHA256全部匹配。内部125项清单严格核对，清单本身由外部MANIFEST覆盖。
- 整包SHA256：`b666e972100a402ae3b9fa92ab2126e5324f4327842ac88fecebcc204c6f4ee4`。
- 从固定远端重新读取直接依赖的MANIFEST与恢复回执，并验证固定SHA256。复用的依赖归档重新核对整包哈希。基线27,892个文件逐个重哈希。
- 实际差异为新增core/eot_repeat_identity.gd，修改core/end_turn_repeats.gd及core/harbinger_eot_admission.gd，删除0，净增418字节。只有delta/三文件应用到运行树，测试篡改目录不应用。
- 在全新目录独立复制恢复27,893个文件，共1,548,714,522字节。没有硬链接，每个文件严格符合SOURCE_MAP，缺失、多余、不符均为0。
- 恢复后再次逐文件重哈希基线，内容未变。没有运行Godot、改写原归档、删除任何旧备份。

完整回执：`HARBINGER_IDENTITY_LEAF_CANDIDATE_REMOTE_VERIFICATION.json`，SHA256：`a6d29ead3af28eb40c81bcc7b7a23a56ea5fb0f85c38125262e5b717c2bd14dc`。

## 固定依赖与复用边界

直接输入为catalog memory候选，固定提交4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1：
https://github.com/Ethsigema/AI_text01/blob/4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1/battlegrounds-backup/pending/20261109-catalog-memory-candidate/RECOVERY_VERIFIED.md

输入归档SHA256：`e5272cc3556bf626d353993b142a75d40ea26c4522eb94bcb2f5a55994f7f7d6`。
输入SOURCE_MAP SHA256：`e52121d24d2b21f75af73521362928a2da449f7f42915fb692cfcb3d425ab0a0`。
输入MANIFEST SHA256：`2218f998a299ee221fb31ee06c123737d8cc53c07d6a2c3eb6e122c744c87ad6`。
输入恢复回执SHA256：`45d53273107a8411727d9d2e1462810ac6e685c4e1f62727eb55fdfd81a4d384`。
目标SOURCE_MAP SHA256：`e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe`。

本轮真实重新下载本次叶模块包，复用此前独立恢复的catalog memory基线、历史归档及历史链；本轮对基线重新哈希，不冒称历史全链重新下载。输入自身依赖女妖及更早增量，不能跳过。诊断提交2bd2ce9296a0ad8c397e4efc25301601ed9e5275没有运行源码改变，不插入补丁链。

较早的独立全链重下审计只覆盖到女妖，不包含catalog memory或本候选：
https://github.com/Ethsigema/AI_text01/blob/0d47d1b6bf8c2943647fbc59ba8448cd6dde0ab9/battlegrounds-backup/pending/20261109-banshee-golden-fresh-chain/RECOVERY.md

## 重现独立恢复

使用Python3.9及以上标准库，至少2GB可用空间。先按固定输入说明恢复catalog memory及SOURCE_MAP，再下载本目录独立脚本执行：

```sh
python3 verify_and_restore_harbinger_leaf_candidate.py \
  --baseline-dir /path/to/restored_catalog_memory_candidate_runtime \
  --baseline-source-map /path/to/catalog_memory_candidate_20261109/SOURCE_MAP.json \
  --output /path/to/a-new-harbinger-leaf-recovery-directory
```

脚本默认从固定提交下载本次归档及输入元数据，验证分片、整包、全部成员、内外清单、变更及删除记录、依赖连续性和实验状态。独立复制之后核对完整输出，并再次确认基线未变。不会运行包内探针、使用硬链接或覆盖已有目录。保留旧备份，输出目录必须不存在。

若已经从同一固定提交预下载MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY及全部5片，可加 `--download-dir /path/to/downloaded`。输入元数据可用本目录PINNED_BASELINE_RECEIPT.json和PINNED_BASELINE_MANIFEST.json，经--baseline-receipt和--baseline-manifest传入。可选--baseline-archive另外核验输入归档的SHA256。所有固定哈希检查保持执行。

本轮使用Git预下载模式，所以回执increment_bytes_freshly_downloaded_by_this_helper:false只说明Python恢复脚本不负责下载；本轮新增分片确实远端重新下载，证据记录在FETCH_PROVENANCE.json。

## 未验收范围

封存试验88项/585条限定A/B结果保留，没有在本次重跑。Admission入口测得82.72%峰值下降仅适用于该入口，EndTurn峰值基本不变；完整catalog图仍增加一个脚本，不能认定此前SIGKILL已修复。畸形错误等价、单个证据篡改拒绝、指纹子列表测试及函数正文一致均不代表完整来源检查、自然获取、EOT实际回调、完整catalog/Game、存档、回放、UI或全机制回归通过。本次只证明远端字节可独立完整恢复。
