# 独立恢复本轮累积候选

请勿覆盖工作树或旧备份。输出目录必须不存在。

1. 下载原始Release：
https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65

2. 下载第14批固定基线全部文件，按其RECOVERY.md恢复：
https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
解压后SOURCE_MAP内容SHA256：7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7。

3. 下载本目录全部文件，执行sha256sum -c SHA256SUMS.txt，然后：

    python3 restore_increment.py --base-tree /路径/已恢复基线 --base-map /路径/基线包/SOURCE_MAP.json.gz --destination /路径/不存在的新候选 --report /路径/报告.json

累积增量相对第14批，不需要叠加前3个候选或13点未验收快照。恢复器验证完整基线，应用增量，再重新读取全部结果。预期PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED。

目标27,961文件、1,550,488,214字节。
增量SHA256：c2f362372a703c4a88bfe9daf271da0c3191e38b5286d7b4084da4ad1317ffea
完整来源清单SHA256：e6fa0c1dc2bcbdc52f82ea9e1fb0a5f91078bead2512558cbc237e2b38628001

证据包按EVIDENCE_MANIFEST.json逐成员核验。运行tests/darkcrest_tier4_20261112/README.md指定的新矩阵，旧real_matrix保留历史4级拒绝断言，不能作当前版本验收入口；新矩阵继承其帮助方法与等待回归。完整Game进程严格串行、隔离HOME和缓存。源码恢复不等于找回原工作树，也不等于完整游戏验收。
