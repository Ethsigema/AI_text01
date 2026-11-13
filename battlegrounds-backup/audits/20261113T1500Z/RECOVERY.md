# 本次已发布文件集恢复
Python3.12+；游戏Godot4.6.3。本次Linux实际双树落盘恢复成功；仅文件完整性，不是全游戏验收。
1. 原Release https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
2. 固定batch14全部24项含13分卷 https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
3. 累积源码包全部30项 https://github.com/Ethsigema/AI_text01/tree/6a047aadfb2562c464bc06fd17777275c2a3b246/battlegrounds-backup/pending/20261112-lava-carried-sale
4. 台账工具包 https://github.com/Ethsigema/AI_text01/tree/f2296d9db1209f4b8c0068fb2edb51f5f7df2f0b/battlegrounds-backup/tooling/20261113-minion-ledger

下载目录依次命名base、candidate、ledger；原包名original_release.zip。先按candidate/RECOVERY.md恢复base，再叠累积源码（不可叠旧候选）。再应用ledger ZIP中overlay/6个新增文件，禁止覆盖未知同名文件。本目录apply_verify_overlay.py为本次实际应用与全量重新读取核验程序，要求前一步输出CANDIDATE_RESTORE_CURRENT.json；源码在restored_current。它核验各依赖SHA和无覆盖后添加6文件。全部固定文件链接及大小/哈希见DOWNLOAD_REQUESTS.json、FRESH_DOWNLOAD_VERIFIED.json；工具原依赖清单也重新核对。FULL_SOURCE_MAP.json.gz是叠工具后的28000文件完整清单。

血缚审查ZIP在 https://github.com/Ethsigema/AI_text01/tree/6a047aadfb2562c464bc06fd17777275c2a3b246/battlegrounds-backup/audits/20261113-bloodbound-price-review ，单独保存，不解进工程。审计PROGRESS/docs台账也单独保存，不称冻结源码内原有文件。

新增/修改/移除：原源码增量相对batch14为157新增或修改、0移除；台账overlay为6新增、0修改、0移除。本期没有新游戏源码变化或新独立全量游戏包。未知未上传工作不在恢复保证内；所有历史备份保留。

全量清单分卷：按part0000开始编号顺序拼接FULL_SOURCE_MAP.json.gz.part*成FULL_SOURCE_MAP.json.gz，然后gzip解压；所有分卷均须下载。完整压缩文件SHA256 a28a85fbd61e75546ac906223166709bf9e0d564847f5fa65971195888ea8c32。
