# Devourer历史工具：远端下载及逐文件流式字节核验通过

仅新增tools/devourer_souls_patterns.py，41,205字节，修改0、删除0。历史原件未证明最新版，工具自身不在当前固定准入pin中。原367项范围剩353条引用，原68历史范围剩55项，六个此前暂缓目标仍缺失；这些不是全项目所有可能缺口的总数。

完整Game、旧存档、真实Catalog/全指纹、全项目编译器、整体内存收益均未验收。清单字节匹配不等于完整游戏恢复。

## 有效包、固定依赖与真实下载

有效包仅devourer_tool_historical_candidate_lowmem_20261109.tar.xz，2,558,872字节，SHA256 c807dd1229f5c4480631a446c8b7b0aa3f00d48e4602bc91d7d23c1480fa5a44。
固定归档提交cfb226a7f5888740371748b49aeb5ad6eda445cf。
MANIFEST SHA256 5ba05d0f1d95b5c9fb3e8e0bcf5c6a961dcaf5c5fcec5356233b28a468b9e6c7。

此前普通压缩退出137，原因未知，留下983,132字节截断包，SHA256 af7d0a1a43f34031e12224ab30146ee589f0f3bf63ee6f4f633e58dfc616e737。失败包保留且末尾重哈希未变，不作为有效包上传。PACKAGE_INTERRUPTION_NOTE和初始清单保存在有效包内。未删改源码、旧备份或未验证材料。

输入第4批固定已核验提交4df40aa115e16fce48e4a17461893d36360613d9：
https://github.com/Ethsigema/AI_text01/blob/4df40aa115e16fce48e4a17461893d36360613d9/battlegrounds-backup/pending/20261109-historical-tools-batch4-three-candidate/RECOVERY_VERIFIED.md
输入归档提交e4b9f301a494c0623daebfd17d7b60fd933c4c6f，SHA256 85e5b08ccafa5dde8ecc02bdd24ecb740a5eb20baf2a81329e8c52b61773cc20。
输入MANIFEST SHA256 c5711e27d97ab3a82a8339112d80aaa6e9d4ba045a776fbe2e44f849de801cce。
输入回执SHA256 1dffa961d83010bc496009434b113690d9a9506932acbb71bcbf1718a55ed80f。
输入SOURCE_MAP SHA256 608a981c9b82b255c37fefb004a4bfe98bcf95d9717cfa3a5ee2917961ff2d00。

11个新归档分片的Git对象在fetch前均不存在，已从固定远端提交真实下载并重组；辅助相同对象可能被Git去重，不冒称全部重新传输。见BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE、ARCHIVE_PUBLICATION_RECEIPT。归档提交只新增17文件，旧备份无修改/删除，不强推。输入MANIFEST和回执也从固定远端重新读取并按以上SHA验证。

## 独立字节核验

11片、整包、137成员和内部136项清单全部匹配。安全解包只接受规范路径的唯一普通文件，拒绝穿越、链接、重复及特殊文件。完整前后源码映射、唯一delta和空删除记录一致。

复用Harbinger完整历史树27,893文件并前后重新实际哈希；依次重核八份既有归档全部1,274成员：native listener247、EarthMother79、GoldenArrow来源叶71、GoldenArrow工具98、Megasaur143、第1批199、第2批282、第4批155。每层前后映射及实际delta连续，输入为27,911文件。第3批只读审查不作为运行增量。

流式实际读取目标27,912文件、1,549,132,284字节，逐文件计算SHA256，与SOURCE_MAP比较缺失、多余、不符均为0。来源：历史树27,885、native listener5、EarthMother4、GoldenArrow来源叶3、GoldenArrow工具1、Megasaur1、第1批5、第2批4、第4批3、新Devourer1。
目标SOURCE_MAP SHA256：9baabc104b5f2f93087dfec0e385d6cb9fceffbf3b1d4441ec91da463a727260。
实际总字节流摘要：930f77dd965da27e5d16f2e29f5b495b99c95b526cf52a1279bad7eb9f42ec0b。
摘要格式为排序UTF-8路径、NUL、ASCII文件字节数、NUL、实际字节，逐目标重复。

没有写完整工程目录。历史树和八份归档末尾再次哈希，全部未变。历史链复用，不是重新下载全链；其他时段fresh-chain审计不冒充本次执行。

## 历史证据及阶段边界

新增工具同真实基线历史候选和归档证据逐字节一致；历史integration_manifest/shared_manifest的安装SHA也匹配。解析Python AST和字面常量，不执行候选模块。RAW、EXPECTED、VALUE_OVERRIDE三项同当前来源相同，15项当前来源pin实际字节匹配，工具自身不是其中一项。

现有独立金色1/3覆盖与全局唯一对应项、原生XML DBF103508及ATK/HEALTH标签一致。没有新增覆盖值。四项DEPENDENCY_RAW同Twin Lanterns当前固定RAW文件一致，当前Devourer编译后DEPENDENCIES同自身固定JSON一致；两种表示之间变化限于编译字段，原生字段未改。

当前Catalog原文覆盖片段与真实基线精确匹配。最初CANONICAL覆盖前后完整元数据差异、跨阶段比较失败、三次探针缩进解析停止、一次JSON数值参考方向失败均保留，不计为通过。原69项Python、414项成功Godot断言、38项静态检查仅保留并检查报告，不在本次备份中重跑；不把局部片段视为完整Catalog或Game验收。

归档有意不含生成的before_runtime/after_runtime/tamper_runtime，只含probe_inputs、delta和prepare_probes.py。独立核验以实际封存输入、单文件delta及精确注释字节在内存组合，分别核对26、27、27条探针输入，不生成或执行运行树。三态原始与portable成功报告一致，仅工具指纹条目变化。

重新读取已核验Megasaur归档中的原367项目录及本包选择记录，确认354降至353和六项暂缓仍未加入。未重新运行历史全盘调查，也未重下原始ZIP；本次历史原件字节来自复用并重哈希的完整基线。

## 本次核验自身的失败与修正

首次备份核验在新包137成员和native listener247成员通过后收到SIGKILL，退出-9，峰值82,840KiB，原因未知。没有当作成功。保留verify_devourer_stream_initial.py、VERIFY.log、BOUNDED_PROCESS_INITIAL.json和本地未完成输出。

减少候选映射与历史映射同时驻留后，首次重试通过八份历史归档及完整历史树初始哈希，但脚本误以为包内应存在生成的*_runtime目录，退出1。包格式本来明确排除这些生成目录，归档没有因此损坏。保留verify_devourer_stream_first_retry.py、VERIFY_RETRY.log、BOUNDED_PROCESS_RETRY.json和本地输出。详见VERIFIER_INPUT_LAYOUT_CORRECTION.json。

修正仅按封存prepare_probes.py的精确组合规则验证三态输入，预先核对26/27/27项全部哈希相等，未降低任何哈希、成员、目标范围或限制。随后一次控制脚本错误地把旧GoldenArrow归档目录后缀也替换了，找不到历史输入而退出1，见CONTROLLER_PATH_CORRECTION、VERIFY_FINAL.log、BOUNDED_PROCESS_FINAL.json及run_bounded_verify_final.py。修正仅恢复已核验历史归档的原路径，未改归档、验证器或阈值。

最后完整重跑通过，退出0，38.42秒，确切子进程峰值117668KiB。192MiB RSS保护、512MiB地址空间、180秒超时保持不变。见VERIFY_PASS.log、BOUNDED_PROCESS_PASS.json。

本次核验进程峰值不代表游戏内存收益。原包以及所有失败材料保持不变。

## 回执与复现

回执：DEVOURER_HISTORICAL_TOOL_STREAM_VERIFICATION.json
SHA256：0403c5bd2007dc667d54394726675c4502ad46a357012f80b28cf7fb3e1ed252。

Python3.9或以上标准库：

```sh
python3 verify_devourer_stream.py \
  --historical-baseline /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --native-archive /path/to/native_spell_listener_leaf_partial_candidate_20261109.tar.xz \
  --earth-archive /path/to/earth_mother_helper_leaf_partial_candidate_20261109.tar.xz \
  --golden-archive /path/to/native_golden_source_leaf_partial_candidate_20261109.tar.xz \
  --golden-tool-archive /path/to/golden_arrow_tool_patch_reconstruction_candidate_20261109.tar.xz \
  --megasaur-archive /path/to/megasaur_tool_fixed_pin_candidate_20261109.tar.xz \
  --batch1-archive /path/to/historical_tools_batch1_candidate_20261109.tar.xz \
  --batch2-archive /path/to/historical_tools_batch2_four_candidate_20261109.tar.xz \
  --batch4-archive /path/to/historical_tools_batch4_three_candidate_20261109.tar.xz \
  --output /path/to/a-new-devourer-stream-directory
```

默认从不可变URL下载新包和固定输入元数据。可把同一归档提交MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY、11片预下载后传--download-dir；--baseline-manifest、--baseline-receipt可指向本目录PINNED副本，全部SHA约束不变。本次采用Git预下载，所以increment_downloaded_by_this_helper:false仅表示Python不负责下载，真实来源有FETCH_PROVENANCE。

输出只有安全解包证据、逐文件结果和回执，不是完整运行工程。若要完整工程，请先按依赖恢复链重建并核对完整基线，足够空间下用封存restore_to_new.py写不存在的新目录，再核对全部目标及输入未变。restore_delta_to_new.py仅恢复单文件，不能作为独立游戏。本轮未做完整复制或游戏/存档验收。

全部旧备份、未验证成果与失败材料保留，不强推。
