# 五项历史工具候选第1批：远端字节流核验通过

新增5文件、53,803字节，修改0、删除0。历史原件及安装清单字节吻合，但未证实为最新版。五个工具本身不在当前来源的固定准入pin中，不把本批称为修复新的准入阻断，也不声称注释篡改会被pin拒绝。

原367路径范围剩361缺口，原68历史候选尚有63未恢复。此范围不是全项目所有工具缺口。完整Game、旧存档兼容、完整Catalog指纹、全离线编译器及整体内存收益未验证。清单精确匹配不代表完整游戏恢复或所有引用已经齐全。

## 本次真实下载

原包固定提交1e60aed5d8555d76a0e81704e84ad15dacb737d2，1,144,624字节，SHA256 d4de01b2fa7a530c00b383455e94f1a0da62d81c68b03b4205b90aca1c46aea1。

五个分片Git对象在fetch前均不在本地对象库，已从远端固定提交真实下载。相同辅助对象可能由Git去重，不声称全部辅助文件重新传输。证据为BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE和ARCHIVE_PUBLICATION_RECEIPT。归档发布仅新增11文件，未改旧文件或删除。

5片、整包、199成员及内部198项清单一致。固定上游Megasaur MANIFEST和回执重新从远端读取并校验。完整前后清单、五文件delta和空REMOVALS一致。

## 独立流式恢复

重新哈希Harbinger完整历史树27,893文件，逐成员复核五份旧归档：native listener 247成员、EarthMother 79成员、GoldenArrow来源叶71成员、GoldenArrow工具98成员、Megasaur143成员。五层按顺序组成输入27,899文件，前后清单连续。

实际读取全部27,904目标文件，共1,548,838,936字节，每文件重新计算SHA256。来源是历史树27,885文件、native listener 5、EarthMother 4、GoldenArrow来源叶3、GoldenArrow工具1、Megasaur1、本批5。相对SOURCE_MAP缺失、多余、哈希不符全部为0。

目标SOURCE_MAP SHA256：53da1c13fbebb6eb8c5672ad8828109720efdfab1a8a97b6792a6da3202e6080。
结束后再次哈希历史树和五份旧归档，均未变。没有写第二完整运行树，没有运行Game，没有删除旧备份或未验证材料。

## 历史来源与限定检查

五个新增文件分别与实际历史基线候选原文、封存原文逐字节相同。每项历史integration_manifest和shared_manifest都与基线相同，并独立读取其目标记录确认安装后SHA匹配。不是以mtime或文件大小选最新版。

对应五个当前GDScript与封存输入哈希一致。对原Python文件只做AST解析和字面常量读取，RAW/EXPECTED及存在的PROGRAMS合计11项与当前GDScript一致，没有执行候选Python模块。五来源现有86项pin实际读取字节后匹配，工具自身均不属于这些pin，没有修改准入常量。

从已核验上游Megasaur归档读取完整367项调查总表和摘要，核对哈希。原表恢复前状态保持不变；与本轮输入/目标比较，缺口由366降至361。新包保存的摘要与五条调查记录同上游逐字节或完整结构一致。未重跑102归档调查，不将旧调查算作本次新研究。

原包184项有限Python检查、990项Godot断言和73项静态交叉检查保留，但本次备份核验没有重新执行它们。三态来源proof_error均通过本来就是原候选事实，不能改称篡改会被pin拒绝。未跑全Catalog/全Game或旧存档。

## 回执和资源

回执：HISTORICAL_TOOLS_BATCH1_STREAM_VERIFICATION.json
SHA256：c3e5df6796a973d499533adae754dc3501d26d721f62f9c78f33dd158089af1e
实际字节流摘要：03ffe29f1a3a9b1180d48551f129b7896c49946c2c5f37d182d65a968404c385
摘要格式：排序UTF-8路径、NUL、ASCII字节数、NUL、实际文件字节，重复覆盖每个目标。

首次受限核验通过，退出0，35.47秒，确切子进程峰值111772KiB。限制为192MiB RSS保护、512MiB地址空间、180秒超时，未提高阈值。BOUNDED_PROCESS和STREAM_VERIFY记录该次真实执行；这不是游戏内存收益。

## 固定依赖及复用披露

输入提交d26dc87ff20c600c651bcee24b0d3dffa056a79f：
https://github.com/Ethsigema/AI_text01/blob/d26dc87ff20c600c651bcee24b0d3dffa056a79f/battlegrounds-backup/pending/20261109-megasaur-tool-fixed-pin-candidate/RECOVERY_VERIFIED.md

输入归档SHA256 27514275c7204a972de2a5193b93deb35c7d4a72b137d1bc5c9477c2f7e9cf66。
输入MANIFEST SHA256 b79689ba046d94fc59f08b8c870cde67e0ed46fe1d3dbf32b0f103db7f78b370。
输入回执SHA256 58b2679422af16d3d0705f6f6eb7f2791dc42308a4f0c3b0f3a67c56f9d6abf4。
输入SOURCE_MAP SHA256 28b1d1c523dfc566bc5eacd04ccea1e1787c1b15e0cca8f9e67ecf9229b46bf4。

本轮重下本批新包及固定元数据。历史树、五份旧归档与更早链复用并重哈希，没有重新下载历史整链。其他时段全新链审计不冒充本次执行，诊断包不是运行增量。

## 复现

Python3.9或以上标准库：

```sh
python3 verify_batch1_stream.py \
  --historical-baseline /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --native-archive /path/to/native_spell_listener_leaf_partial_candidate_20261109.tar.xz \
  --earth-archive /path/to/earth_mother_helper_leaf_partial_candidate_20261109.tar.xz \
  --golden-archive /path/to/native_golden_source_leaf_partial_candidate_20261109.tar.xz \
  --golden-tool-archive /path/to/golden_arrow_tool_patch_reconstruction_candidate_20261109.tar.xz \
  --megasaur-archive /path/to/megasaur_tool_fixed_pin_candidate_20261109.tar.xz \
  --output /path/to/a-new-batch1-stream-directory
```

默认下载固定新包和固定输入元数据。也可先下载同一固定提交MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY和5片，传--download-dir，使用--baseline-manifest和--baseline-receipt指定本目录PINNED_INPUT文件。哈希约束不变。本轮采用Git预下载，increment_downloaded_by_this_helper:false仅指脚本不负责网络下载，实际证据见FETCH_PROVENANCE。

脚本安全解包、逐层校验、实际流式读取全部目标并生成完整逐文件结果映射和新回执。证据输出不是完整运行工程。如需完整树，在空间充足时先复原完整输入，核对后用封存restore_to_new.py写入不存在的新目录并校验全部目标和输入未变。本轮没有执行此完整复制，五个delta文件不能独立运行游戏。

保留所有旧备份和证据，不强推。
