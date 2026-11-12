# 独立恢复5级暗潮重建源码

不得覆盖现有工作树或旧备份。恢复输出必须是不存在的新目录。MANIFEST的未验收状态记录源码冻结时点；后续若附有玩法回执，以其明确范围为准，不能据恢复成功推断全游戏通过。

1. 下载原始Release：
https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65

2. 下载第14批固定基线的全部文件，依其RECOVERY.md恢复：
https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
基线SOURCE_MAP.json.gz解压内容SHA256：7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7

3. 下载本目录全部文件，执行sha256sum -c SHA256SUMS.txt，再运行：

    python3 restore_increment.py --base-tree /路径/已恢复基线 --base-map /路径/基线包/SOURCE_MAP.json.gz --destination /路径/不存在的新树 --report /路径/恢复报告.json

本包是相对第14批的累积增量，不要叠加到4级树，也无需叠加其它候选或13点快照。恢复器重新校验完整基线和全部输出文件。预期PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED。

目标27,965文件、1,550,610,791字节。
来源清单SHA256：7701a57e0cf2e97b82149be5ad6cc3d82e38a443b56477998daa80b4350f5014
路径/长度/内容聚合SHA256：ca24bc997ed0661ea9b5c45194fb19c76777d66b1a0bbfaf19724b580d0b6612

固定源码提交为3da3922e990fd2ed2637d1cc95c8a6e11322e32f。之后的回执提交不改delta、来源清单或已测试源码。重建证据包按REBUILD_EVIDENCE_MANIFEST.json逐成员核验。

实际矩阵入口tests/darkcrest_tier5_20261112/real_matrix.gd，继承的旧helper及fixture必须完整保留。旧矩阵中的4级拒绝断言是历史边界，不能直接作为5级验收入口。完整Game严格串行，建议至少4GiB可用内存和3600秒软时限；这些不是硬资源保证。

本批是从已上传4级备份重建，不是找回环境更换前失踪的未上传文件。旧发现案例与成绩不验证本重建树。文件恢复、局部玩法验证与全范围验收是不同阶段。
