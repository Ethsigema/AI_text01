# Tier6 未验收累积候选恢复

状态：UNACCEPTED_DARKCREST_TIER6_BEFORE_GAME。这不是完整游戏或全量最新内容验收。仅从已验证Tier5继续，暂停的空位候选未带入；不声称找回未上传内容。保留旧工作树与全部备份。

## 输入准备
需要 Python 3.12+、约4GB恢复磁盘；以下命令从一个新工作目录执行。

1. 下载原始Release为 `original_release.zip`：
https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
大小324,041,102字节；SHA256 `33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65`。

2. 下载固定batch14目录全部24文件到 `base_package/`，保持文件名：
https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
必须有restore.py、MANIFEST.json、SOURCE_MAP.json.gz、BASE_MEMBERS.json.gz及13片payload.tar.xz.part0000至part0012。

3. 从同一固定提交下载本候选目录全部文件到 `tier6_package/`。目录为 `battlegrounds-backup/pending/20261112-darkcrest-tier6-native-hand`，首次源码提交号以发布回执为准。不要混用不同提交的MANIFEST、delta或校验清单。证据包不是源码，不要解进工程。

## 核验并实际恢复
```sh
printf '%s\n' '33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65  original_release.zip' | sha256sum -c -
(cd base_package && sha256sum -c SHA256SUMS.txt)
(cd tier6_package && sha256sum -c SHA256SUMS.txt)
python3 base_package/restore.py --base-zip original_release.zip --destination restored_batch14 --report BASE_RESTORE.json
python3 tier6_package/restore_increment.py --base-tree restored_batch14 --base-map base_package/SOURCE_MAP.json.gz --destination restored_tier6 --report TIER6_RESTORE.json
```
两个输出目录和两个报告必须不存在。**本包是相对batch14的累积增量，直接叠batch14，不能叠Tier5或空位候选。** 不需要逐层叠历史包，也不能只解增量当完整工程。

两个恢复器实际重新读取每个文件，验证完整路径集、长度和SHA256；输入SHA256SUMS只校验包文件，不能替代源码恢复核验。基线应报告PASS_ACTUAL_DISK_RESTORE_EVERY_FILE_REHASHED（27,920文件、1,549,340,406字节）。候选应报告PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED，27,968文件、1,550,696,801字节；missing/extra/mismatched均为空。

完整每文件SHA/大小见解压后的SOURCE_MAP.json.gz。解压地图内容SHA256：`f6305aee3349b70d01292b351ac0923a2a3152b56a1f41fb1f18c763410d3e9c`。
聚合SHA256：`d72e2b1a7a0b6c257c3001f63959a9f717b2a1645feb02c33002c728786cf2fc`；TIER6_RESTORE.json的aggregate_sha256必须一致。

工程入口 `restored_tier6/project.godot`，对应Godot 4.6.3。先保留这棵核验树，另复制运行以免缓存/测试输出污染源码证据。恢复成功仅证明字节可重建；真实玩法验收必须另有固定来源的实际测试回执。若包内附带证据归档，按相邻成员清单逐项验证，不把历史成绩算作本候选通过。
