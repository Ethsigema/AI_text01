# 独立恢复暗潮/骑手/碎地者累积候选

不要覆盖任何已有工作树或旧备份。输出目录必须不存在。

1. 原始Release：
https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65

2. 固定第14批基线：
https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
下载全部文件，按其RECOVERY.md恢复基线；保留SOURCE_MAP.json.gz，其解压SHA256为7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7。

3. 下载本目录全部文件，先sha256sum -c SHA256SUMS.txt，再执行：

    python3 restore_increment.py --base-tree /路径/已恢复基线 --base-map /路径/基线包/SOURCE_MAP.json.gz --destination /路径/不存在的新候选 --report /路径/新恢复报告.json

恢复器检查完整基线后应用累计delta，再逐文件重读结果。预期PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED。无需下载/叠加以前两批候选增量。

最终 27,958 文件、1,550,392,621 字节。
增量SHA256：90939392bc9d525f0b95af1fdc1858cfcdaea46f24d5e3880f23fdd7a542c993
完整来源清单SHA256：aa9cf9558ca4afc9f7932aa96b7ef5567059c4739eb05d20702c5cdff7f80067

evidence.tar.xz按EVIDENCE_MANIFEST.json逐成员验证。运行tests/darkcrest_20261112/README.md中的测试，source_eot_contract与其darkcrest_sources_archived.gd必须一起保留。完整Game测试串行运行，隔离HOME和缓存；此前骑手/碎地者测试仍随工程保留。

文件恢复完整不等于原工作树找回，也不等于完整游戏或全部内容验收。
