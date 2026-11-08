# 金色永恒大亨增量恢复说明

本包是源码增量备份，不是完整独立游戏包。它保留既有内容，只新增 3 个文件并修改 5 个文件，删除列表为空。不要删除旧备份。

## 固定基线

先按以下不可变版本恢复永恒大亨基线：
https://github.com/Ethsigema/AI_text01/blob/819c10f12cade5f2ed67b20cc6e42ad0e3fd0a0b/battlegrounds-backup/pending/20261108-hopebringer-tycoon/RECOVERY.md

基线归档固定位置：
https://github.com/Ethsigema/AI_text01/tree/40ee9b3883b19226d252f9fc7b1c7f8e38fa5643/battlegrounds-backup/pending/20261108-hopebringer-tycoon

基线归档 SHA256：032055ad0dfad78ad88ee3270efd2a78b18c8d99f6c6bd43e4e147c878933e41。
基线完整 SOURCE_MAP SHA256：1ae20915de380fa09051261af4e1aae1abe07f7d9f682dbbca00c3da04619135。
基线核验回执 SHA256：5ce663d0633c43ed6d87207c8b2ce352f23ffb163729231be4ba363acc6f290e。

基线说明逐层固定到原始完整包和 Git 源码，不依赖会移动的分支。历史全链下载核验配方：
https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md

## 恢复本次增量

从本目录同一提交下载 MANIFEST.json、CHANGES.json、REMOVALS.json、SHA256SUMS.txt 和全部七个 part000 至 part006 分片。按 MANIFEST.json 的 parts 数组顺序拼接为 hopebringer_tycoon_golden_20261109.tar.xz。

归档大小 1,659,404 字节，SHA256：b7e400d6f2a9ffc6812029503a79765934c22f9c38368fd1dc2d7483d71771f3。

每片大小和 SHA256、归档全部 54 个成员的大小和 SHA256 均在 MANIFEST.json。安全解压到新目录，拒绝绝对路径、上层跳转、符号链接及重复成员，并逐个核对。完整目标树清单为包内 SOURCE_MAP.json，基线完整清单为 BASE_MAP.json。

逐文件验证基线与 BASE_MAP.json 完全相符。将基线复制到一个全新的目录，再用 delta/ 覆盖八个差量文件。本次没有文件删除。最终目录必须严格符合 SOURCE_MAP.json，不得缺失、多出或哈希不符。不要使用硬链接，也不要在核验基线中启动 Godot。保留基线和所有旧包不变。

目标树：27,883 个文件，1,548,667,393 字节。完整 SOURCE_MAP SHA256：84b6a30eb6f82121013e45cd75faab7492803b57efba48fe404a25a5c3c022a2。

本次回读核验会实际下载新增量，复用并重新逐文件哈希先前已验证的永恒大亨基线，不声称重新下载整个历史链。源码恢复核验不是完整玩法验收。金色自然获取/三连、重复复仇、满场、多大亨、完整房间及 UI 尚未验收；旧基线完整对照运行被 SIGKILL 的记录保留，未算通过。归档内 uploaded:false 反映封存时状态，不修改原包。
