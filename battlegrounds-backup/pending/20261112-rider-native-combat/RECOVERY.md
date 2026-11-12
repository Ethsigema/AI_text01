# 恢复骑手与碎地者累积候选

需要原始 Release + 第 14 批合并基线 + 本目录增量。无需旧骑手或碎地者候选包。不要覆盖任何旧备份，恢复输出必须为不存在的新目录。

1. 原始 Release：
https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65

2. 固定基线目录：
https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
下载全部文件并按其 RECOVERY.md 恢复。保留 SOURCE_MAP.json.gz，解压后 SHA256 应为 7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7。

3. 下载本目录全部文件，执行 sha256sum -c SHA256SUMS.txt，再运行：

    python3 restore_increment.py --base-tree /路径/已恢复基线 --base-map /路径/基线包/SOURCE_MAP.json.gz --destination /路径/不存在的新候选 --report /路径/新恢复报告.json

恢复器读取并逐文件校验全部基线，再应用累积增量，最后再次读取完整结果，核验路径、大小及 SHA256。预期状态 PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED。

完整结果：27,942 文件，1,549,765,294 字节。
增量 SHA256：f6942847d8faf19fe2bfcedac7ac722a0727e012ef99931d7069485a81770f35
完整来源清单 SHA256：7841925369aed679fe017ef6b91f98132424f74cd574a0bb3447724fdd94d8c2

新测试位于 tests/rider_20261112/，保留的碎地者测试位于 tests/shatterer_20261112/。详细命令和限制见各自 README.md。证据包 evidence.tar.xz 由 EVIDENCE_MANIFEST.json 逐成员验证，包含旧错误和实际成功日志。

恢复成功只证明这些上传文件可完整恢复，不证明原不可见工作树、未知未上传修改、默认全池、完整对局或旧存档已验证。
