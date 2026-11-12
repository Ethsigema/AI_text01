# 恢复这个独立候选

仅需原始 Release + 第 14 批合并增量 + 本目录增量。不需要叠加旧碎地者候选；本包已包含它的必要游戏文件。保留所有旧备份，输出路径必须是不存在的新目录。

1. 下载原始 Release：
   https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
   SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65
2. 下载固定基线目录所有文件，按其 RECOVERY.md 独立恢复基线：
   https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
   保留 SOURCE_MAP.json.gz。其解压后 SHA256 必须为 7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7。
3. 下载本目录的全部文件并执行 `sha256sum -c SHA256SUMS.txt`。之后执行：

    python3 restore_increment.py --base-tree /路径/已核验基线 --base-map /路径/基线包/SOURCE_MAP.json.gz --destination /路径/不存在的新候选目录 --report /路径/不存在的恢复报告.json

该工具先逐文件读回基线，再使用本增量中的变化文件和未变基线构建新目录，最后从磁盘再次核验完整路径集、大小及 SHA256。不会运行游戏或执行证据包代码。成功状态必须为 PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED。

可复现测试位于新工程的 tests/shatterer_20261112/。资源限制、44 项集成检查、28 项合同检查及范围见 README.md。证据包 evidence.tar.xz 中保留修复前失败及修复后成功日志；EVIDENCE_MANIFEST.json 是其逐成员校验表。恢复成功仅证明列出的全部游戏文件可恢复，不证明未上传原始工作树、默认池、完整对局或旧存档已被验收。

本候选增量 SHA256：14333a741fcaffaf2218f46b467575d5fb807f422f69f38cecb46c26f4492006

完整候选源码清单 SHA256：2d0a4d9eb70e49b810c0fe16e88e1ca5dec64a61dbb7706a4b96b01755535368
