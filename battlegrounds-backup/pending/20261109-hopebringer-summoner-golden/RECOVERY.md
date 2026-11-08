# 金色永恒召唤者增量恢复说明

本包为源码增量备份，不是完整独立游戏包。保留旧备份。源码新增6个文件、修改7个文件、删除0个文件；完整目标树为27,889个文件、1,548,697,882字节。

## 固定基线

先按金色永恒大亨固定版本恢复说明完成历史链恢复：
https://github.com/Ethsigema/AI_text01/blob/ddae092130aa47ef311d2d616bd489e769477452/battlegrounds-backup/pending/20261109-hopebringer-tycoon-golden/RECOVERY_VERIFIED.md

基线归档：
https://github.com/Ethsigema/AI_text01/tree/893662b9ee76a37e60695c52cbc0fb8cb09379bb/battlegrounds-backup/pending/20261109-hopebringer-tycoon-golden

基线归档SHA256：b7e400d6f2a9ffc6812029503a79765934c22f9c38368fd1dc2d7483d71771f3。
基线SOURCE_MAP SHA256：84b6a30eb6f82121013e45cd75faab7492803b57efba48fe404a25a5c3c022a2。
基线核验回执SHA256：974151e300525abebb03bf91d957e30f7798ac10634ca10f97cf7c50f53437e2。

历史全链下载配方：
https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md

## 恢复本次增量

从本目录同一提交下载MANIFEST.json、CHANGES.json、REMOVALS.json、SHA256SUMS.txt、README.md、RECOVERY.md，以及全部15个分片part000至part014。按MANIFEST.json parts数组顺序拼接为hopebringer_summoner_golden_20261109.tar.xz。

归档大小：3,686,500字节。
归档SHA256：b5da7d7e86a59b6ae2dce39ff071feaedef80d6c10947f72cca6bd55ea418522。

先验证每片大小和SHA256，再核对整包。安全解压至全新目录，拒绝绝对路径、上层跳转、链接、特殊文件和重复成员。逐一核对MANIFEST.json全部71个文件的大小及SHA256；PACKAGE_MANIFEST.json也须核对，其本身由外部MANIFEST.json覆盖。

基线运行树逐文件必须严格匹配包内BASE_MAP.json。复制基线到新目录，不使用硬链接，不在基线启动Godot。叠加delta/的13个文件。删除清单为空。最终目录必须严格匹配SOURCE_MAP.json：不得缺失、多出或大小/哈希不符。恢复后重新完整哈希基线，确认未修改。

目标SOURCE_MAP SHA256：32cd814943a82a4ee79fb05de8a3f4d24d7f74d7b609dd6247aebcd5a4cc7449。

包内materialize.py是开发用途脚本，绑定开发路径并使用硬链接。独立安全恢复请使用本目录追加的verify_and_restore_hopebringer_summoner_golden.py和RECOVERY_VERIFIED.md。输出目录须为新目录；已有输出和全部旧包保留。

本轮会重新下载本次金色永恒召唤者增量，复用并重新逐文件哈希已经核验的金色永恒大亨基线，不声称重新下载历史全链。源码恢复不等于完整玩法验收。本包有界测试修正金色召唤者为每次亡语召唤一个金色骑士，并验证复生及希望信使同场；自然金色获取/三连、满场失败、额外亡语/复生观察者、完整房间及UI仍未验收。首次SIGKILL及构建失败记录保留且不算通过。
