# EarthMother辅助叶部分候选：远端下载及完整流式字节核验通过

状态仍为PARTIAL_PURE_HELPER_AND_LIGHT_ENTRY_PASS_FULL_HOST_UNVERIFIED。完整宿主、Catalog/Game、存档兼容性及回放未验证，不提升之前任何部分候选验收。代码身份和execution_fingerprint改变，旧存档指纹不再相同；未实际测试旧存档迁移或拒绝，不假称兼容，也不伪造旧指纹。

## 实际完成

- 新包固定提交 `851466e4964562e8cf172bd40d37a389386fcfdf`，只新增11个备份文件，旧文件无修改或删除，未强推。
- git fetch固定提交后逐个读取同一提交的上传文件。全部5个归档分片对象在下载前不在本地Git对象库，因此本次确实从远端重新下载，不使用本地待上传包；相同辅助对象可能由Git去重。证明见BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE和ARCHIVE_PUBLICATION_RECEIPT。
- 5片、1,169,808字节整包、79个成员及内部78项清单全部匹配；内部清单本身由外部MANIFEST覆盖。
- 整包SHA256：`333aad27ba8ed0d0699c97cd4a33be5494310247a8350993532cd725f26e753c`。
- 直接依赖的MANIFEST和流式回执从固定远端重新读取。复用native listener输入归档重新哈希，247个成员重新逐项核对。
- Harbinger完整基线27,893文件重新逐项哈希，结合已核验输入归档的5个delta，实际字节哈希组成27,895文件的直接输入，严格符合BASE_MAP。输入并不存在完整目录，本轮也没有假称它存在。
- 本次新增1、修改3、删除0，四个新delta严格对应来源差异，净增367字节。before/三原文件逐项符合输入映射，失败探针和tamper目录不作为运行补丁。
- 按新delta优先、旧delta其次、历史完整树最后的规则，逐文件实际读取27,896文件、1,548,719,422字节并重新计算SHA256。来源分别为新delta4文件、旧delta5文件、历史树27,887文件，所有目标字节都经过读取，不是只检查映射或四个变动文件。
- 缺失、多余、哈希不符均为0。之后再次完整哈希Harbinger历史树，并重核输入归档，二者未变。
- 没有写第二个完整运行目录、运行Godot、改写原归档或删除任何旧备份。开始磁盘约2.5GiB，空间数值见DISK_PLAN与回执。

完整回执：`EARTH_MOTHER_HELPER_PARTIAL_STREAM_VERIFICATION.json`，SHA256：`9e00b1c2957add5c5cc77fe9fa5ac881030780833b6d6ca9c683b3c1be84a9be`。
实际重建映射SHA256：`d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960`，语义逐项等于目标SOURCE_MAP；脚本会生成该映射。
实际目标字节流摘要：`66d9a44df5d45025cf997a355ca9e18d0ee9c38e1716ef57cf2e51776621b0ed`。格式为按路径排序的UTF-8路径、NUL、ASCII文件字节数、NUL、实际文件字节，逐文件连续计算SHA256。

## 固定依赖及复用

直接输入固定提交1288c092b970edaa6a75c2be89809354eed19405：
https://github.com/Ethsigema/AI_text01/blob/1288c092b970edaa6a75c2be89809354eed19405/battlegrounds-backup/pending/20261109-native-spell-listener-leaf-partial-candidate/RECOVERY_VERIFIED.md

输入归档SHA256：`46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7`。
输入SOURCE_MAP SHA256：`9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111`。
输入MANIFEST SHA256：`c10934e5554eec684c1ceb287cea81073a1dae45b7195905bb8211d86d6fd06a`。
输入流式回执SHA256：`ba73c82db88ceaedbb57f395da246433deb89d55ddd3ff6296a871c9d03b3cda`。
Harbinger历史完整树SOURCE_MAP SHA256：`e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe`。
新目标SOURCE_MAP SHA256：`d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960`。

本轮真实重新下载新EarthMother包。历史Harbinger树、native listener归档及更早所有历史链复用，不重新下载。历史完整核验与并行另一次整链审计均不是本回执的本轮新下载。本轮保留全部中间候选，不能跳过运行依赖。只读组合诊断不改变源码，不属于补丁链。

## 重现流式核验

Python3.9及以上标准库。准备之前独立恢复的Harbinger完整树及native listener归档，下载本目录脚本：

```sh
python3 verify_earth_leaf_stream.py \
  --historical-baseline /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --prior-archive /path/to/native_spell_listener_leaf_partial_candidate_20261109.tar.xz \
  --output /path/to/a-new-earth-helper-stream-verification-directory
```

默认从固定提交下载新包和固定依赖元数据。脚本验证归档全部成员、完整历史树、复合输入、增量/删除记录、目标全部实际字节及输入不变性，不运行Godot、不创建完整运行目录，也不使用硬链接。输出是证据和完整重建映射，不是运行工程。旧备份及所有既有输出保留，目标目录必须不存在。

可以先下载相同固定提交的MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY及5片，再传入--download-dir。固定元数据可用本目录PINNED_INPUT_RECEIPT与PINNED_INPUT_MANIFEST，通过--baseline-receipt及--baseline-manifest提供。固定哈希仍核验。本次采用Git预下载，回执increment_bytes_freshly_downloaded_by_this_helper:false只指Python恢复脚本不负责下载，本轮新下载证据见FETCH_PROVENANCE。

## 未来完整目录与风险

需要完整运行目录时，先按直接输入说明恢复并严格验证native listener输入，再在充分空间下用本包restore_to_new.py向全新目录复制和验证。该步骤本轮未做，不能把verified_stream目录当作完整运行树。既有基线不能被覆盖、硬链接或删除。

封存1439项是六个有限探针结果，不是本次新跑，也不是完整宿主回归。earth/最初失败探针虽有部分PASS报告但已明确无效并排除。薄代理不是整个宿主，原文oracle不是原完整入口。循环容器、病态递归、栈耗尽未证明等价；没有完整游戏、旧存档迁移/拒绝、回放或全局内存A/B。新叶纳入消费指纹不等于固定准入pin，9条原来源证据保留。静态图仍增加一个脚本，不证明全局驻留下降或此前SIGKILL解决。
