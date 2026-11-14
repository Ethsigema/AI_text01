# 本次已发布文件集恢复
Python 3.12+，游戏运行要求Godot 4.6.3。本目录为审计及恢复凭证，不是独立游戏包。
完整固定链接、大小、Git对象哈希见DOWNLOAD_REQUESTS.json；逐下载SHA256见FRESH_DOWNLOAD_VERIFIED.json。
1. 原Release：https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
   324041102字节；SHA256 33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65。
2. batch14全部24文件（含13分卷）：
https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
3. 累积源码全部30文件：
https://github.com/Ethsigema/AI_text01/tree/6a047aadfb2562c464bc06fd17777275c2a3b246/battlegrounds-backup/pending/20261112-lava-carried-sale
4. 台账工具：
https://github.com/Ethsigema/AI_text01/tree/f2296d9db1209f4b8c0068fb2edb51f5f7df2f0b/battlegrounds-backup/tooling/20261113-minion-ledger
ZIP SHA256 bc94f25a2deeb2736fa541f88ffa3ea5cd4afe9dd3d7beeba50756b704a3a2c2。
原源码相对batch14有157新增或修改、0移除；台账overlay为6新增、0修改、0移除。不能把累积增量叠到旧候选上。

从不存在的新工作目录执行本目录download_verify.py（按DOWNLOAD_REQUESTS.json保存为base、candidate、ledger、review及original_release.zip）；每项通过大小与固定哈希后才落名。该脚本拒绝覆盖既有目标，失败时不要删除唯一材料或盲目重试。
随后：
```sh
python3 base/restore.py --base-zip original_release.zip --destination restored_base --report BASE_RESTORE_CURRENT.json
python3 candidate/restore_increment.py --base-tree restored_base --base-map base/SOURCE_MAP.json.gz --destination restored_current --report CANDIDATE_RESTORE_CURRENT.json
python3 apply_verify_overlay.py
```
恢复器要求新输出，逐字节核验基准、累积源码、工具依赖和六个overlay，无覆盖未知文件。工程入口restored_current/project.godot。
最终28000文件、1553142049字节，聚合SHA256 bf59b4cf2198a4dd364449b3244e50216d85edfb0600ffb443619b6628ab9973。
本目录FULL_SOURCE_MAP.json.gz.part0000至part0005按数字顺序拼接；全部分卷均须保留。拼接gzip的SHA256 a28a85fbd61e75546ac906223166709bf9e0d564847f5fa65971195888ea8c32，解压后为完整路径、大小和SHA清单。其字节与上一轮冻结清单完全相同，Git复用既有已核验对象，不表示新游戏源码。
审计PROGRESS、docs台账和review证据独立保存，不解入冻结游戏工程。未知中断线程未上传成果不在恢复保证内，恢复成功不等于功能验收。所有旧备份保留。


