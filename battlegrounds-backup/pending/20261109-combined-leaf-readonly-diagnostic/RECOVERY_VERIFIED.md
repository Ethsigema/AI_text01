# 两项来源叶组合只读诊断：远端证据与固定依赖核验通过

本包只保存诊断资料，运行源码新增0、修改0、删除0，不是新运行增量，不改变之前部分验证状态。完整Game未验收。本次没有执行任何Godot探针。

## 已完成

- 档案固定提交 `3bc00aebf6ae235d819c2f9ad9fb0a71fcd2b1eb`，仅新增7个备份文件，无修改或删除旧文件，未强推。
- 真实git fetch固定提交后回读全部上传文件。唯一归档分片对象在下载前不在本地Git对象库，证明确实重新下载本次档案；相同辅助对象可能由Git去重。证明见BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE及ARCHIVE_PUBLICATION_RECEIPT。
- 78,984字节整包、38个归档文件、内部37项清单逐项匹配；清单本身由外部MANIFEST覆盖。
- 原包SHA256：`41d8059e6a5db3e1c7de4f9acc7396537dc7f9b6a5902dea75cd7988ed5978c3`。
- 从固定远端重新读取直接依赖MANIFEST和流式回执，核对固定SHA256、候选状态和源码映射关联。复用的输入归档重新哈希，其247个成员也重新逐项核对。
- 41个诊断输入实际字节重哈希，共366,179字节，全部符合固定候选SOURCE_MAP及TEST_INPUT_MAP。其中37个来自以前独立恢复的Harbinger完整树，4个来自输入候选归档delta；缺失、不符均为0。
- 复查37个基线输入及输入归档未变。没有声称本轮重新哈希整套约1.55GB运行树。
- 核对四份封存报告的SHA256、进程退出记录、脚本与夹具摘要、47项已记录检查，以及两种顺序下结果与独立运行的对应一致性。这是原证据一致性核查，不是新跑47项测试。
- 没有新建完整运行目录、重下历史全链、改写源码或删除任何旧备份。

完整回执：`COMBINED_DIAGNOSTIC_REMOTE_VERIFICATION.json`，SHA256：`9048629625a1fc6e91b14e50da21a1ffb5085b433810709ad3ba5898ecb5d945`。
41项实际输入记录：SELECTED_INPUT_VERIFICATION.json，SHA256：`a0e0497d11d3c14c78922ead06470a032a39364071103e904860a247d754b94b`。

## 固定依赖

运行输入仍为部分验证候选1288c092b970edaa6a75c2be89809354eed19405：
https://github.com/Ethsigema/AI_text01/blob/1288c092b970edaa6a75c2be89809354eed19405/battlegrounds-backup/pending/20261109-native-spell-listener-leaf-partial-candidate/RECOVERY_VERIFIED.md

输入归档SHA256：`46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7`。
输入SOURCE_MAP SHA256：`9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111`。
输入MANIFEST SHA256：`c10934e5554eec684c1ceb287cea81073a1dae45b7195905bb8211d86d6fd06a`。
输入流式回执SHA256：`ba73c82db88ceaedbb57f395da246433deb89d55ddd3ff6296a871c9d03b3cda`。

本轮只重新下载新诊断档案及固定元数据；输入归档、Harbinger树和全部历史链均复用。先前native listener的完整逐文件流式字节检查不是本轮执行；该输入也没有完整运行目录。本诊断不能替代或省略运行依赖，更不能作为补丁应用。

## 重现核验

Python3.9及以上标准库。准备既有Harbinger完整树与之前下载的native listener输入归档，下载本目录脚本后执行：

```sh
python3 verify_combined_diagnostic.py \
  --historical-baseline /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --input-archive /path/to/native_spell_listener_leaf_partial_candidate_20261109.tar.xz \
  --output /path/to/a-new-combined-diagnostic-evidence-directory
```

脚本默认下载固定诊断提交及依赖元数据，安全解压诊断证据，验证完整新包及输入归档，独立读取41项输入字节，并检查原报告一致性。不会执行原探针、写运行树或改动基线。输出目录必须不存在，旧备份及输出全部保留。

已从同一固定提交预下载MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY及part000时，可加--download-dir；固定输入元数据可由--input-manifest和--input-receipt提供本目录副本，所有固定哈希检查仍执行。本轮采用Git预下载模式，因此回执diagnostic_download_by_this_helper:false；本轮真实下载证明见FETCH_PROVENANCE.json。

## 确切边界

只支持封存的轻入口、来源适配器及限定apply诊断。静态依赖图不代表Godot实际编译/分配顺序或RSS。约66–67MiB组合峰值不是完整项目内存，不能计算全局降幅。重型执行宿主、真实EOT/施法事件、完整Catalog/Game、存档、回放及UI均未验收。此前SIGKILL原因未知。本轮不实施任何未来优化，也不提高阈值或重跑累计预载。
