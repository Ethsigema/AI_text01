# 普通Mini到Lava有限永久桥 未验收累积候选恢复

状态：UNACCEPTED_LAVA_MINI_PERMANENT_BEFORE_GAME。这不是完整游戏或全量最新内容验收。仅从已验证rebuy候选继续，范围为单普通Mini→原生Trident→普通Lava每轮首cast永久+2及kept重置、暗潮在场的有限authority桥；原效果本已存在，不扩第2Mini/同轮第2cast/其他target/附魔后sale-rebuy，不重写普通Lava能力，不扩Tier2出生或等级上限，暂停的空位候选未带入；不声称找回未上传内容。保留全部旧备份、独立恢复树及日志；仅经完整等价核验并授权的已完成开发工作副本已清理，详见清理证据。

## 输入准备
需要 Python 3.12+。低盘工具使用fcntl，仅支持Linux/macOS；传统双树路线需额外空间。以下命令从一个新工作目录执行。运行恢复所必需的依赖仅原Release、固定batch14全部24项和本候选包；本阶段下载的旧rebuy最终30项用于前像/历史证据核验，并非运行恢复的依赖。

1. 下载原始Release为 `original_release.zip`：
https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
大小324,041,102字节；SHA256 `33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65`。

2. 下载固定batch14目录全部24文件到 `base_package/`，保持文件名：
https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
必须有restore.py、MANIFEST.json、SOURCE_MAP.json.gz、BASE_MEMBERS.json.gz及13片payload.tar.xz.part0000至part0012。

3. 从同一固定提交下载本候选目录全部文件到 `mini_package/`。目录为 `battlegrounds-backup/pending/20261112-lava-mini-permanent`，首次源码提交号以发布回执为准。不要混用不同提交的MANIFEST、delta或校验清单。证据包不是源码，不要解进工程。

## 推荐低空间完整恢复（新单树路线）
本批新工具restore_low_disk.py与传统restore_increment.py并存，不改旧恢复器。
低盘路线从不存在的新工作目录开始，在其中先实际恢复完整batch14并逐文件核验checkpoint，再在同一新树应用已完整验证的累积增量并两次全量核验。不会修改任何旧base/restored_snapshot/candidate。
```sh
touch common.lock
python3 mini_package/restore_low_disk.py --execute --base-package base_package --release original_release.zip --candidate-package mini_package --new-workspace fresh_single_restore --lock-file common.lock
```
首次独立恢复可按上例创建新工作目录内的common.lock；同一工作流所有恢复和Game进程必须复用此共同锁，不可用不同锁绕过互斥。fresh_single_restore必须不存在，其父目录必须已存在；失败保留FAILED_RESTORE.json和当前状态，不自动删除/重试。成功报告SINGLE_TREE_RESTORE_VERIFIED.json，工程在fresh_single_restore/restored_snapshot/project.godot。外置HOME/缓存/日志直接测试此树并测试前后全SHA，不另复制runtime树；只能称一棵独立远端恢复/测试树，不能称双恢复树。保留本批实际55项下载的证据；实际恢复最低依赖仍是原Release+batch14全部24项+本候选，不需旧rebuy最终30项。

### 本批远端工具布局与runner参数
固定提交下载协调器将新恢复工作目录置于remote_snapshot_<commit>/single_tree_restore，因此源码在remote_snapshot_<commit>/single_tree_restore/restored_snapshot，不在package旁边。下载包仍在remote_snapshot_<commit>/package，独立恢复总回执在remote_snapshot_<commit>/INDEPENDENT_RESTORE_VERIFIED.json。
后续runner必须显式传入 `--package remote_snapshot_<commit>/package --restore-report remote_snapshot_<commit>/INDEPENDENT_RESTORE_VERIFIED.json --output remote_snapshot_<commit>`，并用其对应源码参数指定 `remote_snapshot_<commit>/single_tree_restore/restored_snapshot`；不能依赖默认siblings推断。此为路径约束，不是声称runner已执行或默认参数已适配。

## 传统双树完整恢复（额外空间）
```sh
printf '%s\n' '33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65  original_release.zip' | sha256sum -c -
(cd base_package && sha256sum -c SHA256SUMS.txt)
(cd mini_package && sha256sum -c SHA256SUMS.txt)
python3 base_package/restore.py --base-zip original_release.zip --destination restored_batch14 --report BASE_RESTORE.json
python3 mini_package/restore_increment.py --base-tree restored_batch14 --base-map base_package/SOURCE_MAP.json.gz --destination restored_mini --report MINI_RESTORE.json
```
两个输出目录和两个报告必须不存在。**本包是相对batch14的累积增量，直接叠batch14，不能叠旧Lava、Tier6或空位候选。** 不需要逐层叠历史包，也不能只解增量当完整工程。

两个恢复器实际重新读取每个文件，验证完整路径集、长度和SHA256；输入SHA256SUMS只校验包文件，不能替代源码恢复核验。基线应报告PASS_ACTUAL_DISK_RESTORE_EVERY_FILE_REHASHED（27,920文件、1,549,340,406字节）。候选应报告PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED，27,982文件、1,550,853,439字节；missing/extra/mismatched均为空。

完整每文件SHA/大小见解压后的SOURCE_MAP.json.gz。解压地图内容SHA256：`302328d7278ce8902ceba79d4532fa564c9f17022e76c0bf6b7165ea442becca`。
聚合SHA256：`d60d121e67ea42517535430f22fa667036c84eac2d24d9921e8c17707fc9ab6c`；MINI_RESTORE.json的aggregate_sha256必须一致。

工程入口 `restored_mini/project.godot`，对应Godot 4.6.3。本批实际采用一棵独立fresh restore/runtime树，外置HOME/缓存/日志并测试前后逐文件全SHA，不另复制运行树；传统双树命令仅提供额外空间下的可选恢复方式。恢复成功仅证明字节可重建；真实玩法验收必须另有固定来源的实际测试回执。若包内附带证据归档，按相邻成员清单逐项验证，不把历史成绩算作本候选通过。
