# 第2批四项历史工具：远端流式字节核验通过

仅新增Old Soul、Warband Whistle、Lovely Locket、Replica Cathedral四个历史工具文件，共132,315字节；修改0、删除0。四个历史原件不证明最新版，它们本身不是当前固定准入pin，不把本批称为新准入阻断修复。

Sinstone Sticker仍暂缓，不在本轮运行增量或目标清单中。原五项试验中三态各六个依赖拒绝预期失败的报告、输入和脚本原样保存，核验检查它们确实保留，没有算作通过。其历史工具额外依赖是否适合当前全编译链未证实，不等于本轮新运行回归，不改代码或放宽测试来掩盖。

原367路径范围剩357缺口，原68历史候选剩59项含Sinstone；均非全项目所有缺口。完整Game、旧存档、完整Catalog最终指纹、全项目编译器和整体内存收益未验收。封存清单字节匹配不等于完整游戏恢复。

## 真实下载和字节核验

归档固定提交5d17cb79f7f7b6abdddb68e3b9e420e0167184b3，1,145,088字节，SHA256 51263c49a09a0a735a417e147e4f64f0529be4d5fa12529807653da7187693eb。

5个分片Git对象在fetch前均不存在于本地对象库，已从远端固定提交真实下载。辅助相同对象可被Git去重，不称全部辅助文件重新传输。证据见BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE、ARCHIVE_PUBLICATION_RECEIPT。归档发布新增11文件，无覆盖/删除或强推。

5片、整包、282成员及内部281项清单全部一致。固定第1批MANIFEST和回执重新从远端读取，哈希正确。完整前后清单、四文件增量和空删除记录一致。

重新哈希Harbinger完整树27,893文件，六份旧归档逐成员重核：native listener247、EarthMother79、GoldenArrow来源叶71、GoldenArrow工具98、Megasaur143、第1批199成员。六层依次构成输入27,904文件，清单连续。

实际流式读取全部27,908目标文件、1,548,971,251字节，逐文件重算SHA256。来源：历史树27,885、native listener5、EarthMother4、GoldenArrow来源叶3、GoldenArrow工具1、Megasaur1、第1批5、本批4。相对封存SOURCE_MAP缺失、多余和不符均为0。

目标映射SHA256：3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea。
核验末尾再次哈希历史树和六份旧归档，内容未变。没有写第二完整工程目录，没有删除旧备份、来源或未验证材料。

## 独立来源检查与边界

四个新增文件同实际历史候选和封存原文逐字节一致，历史integration_manifest/shared_manifest也与基线一致；每项目标记录的安装后SHA匹配。当前四个GDScript与封存输入哈希一致，Python只AST解析和读取字面常量，没有执行原模块。

RAW/EXPECTED及存在的PROGRAMS共9项与当前源码相符；DEPENDENCY_RAW与当前DEP_RAW相符，共16个模块-依赖条目、9个不同卡牌ID。现有55项固定pin实际读取字节核对通过，四工具自身均不在这些pin中，未更改准入常量。

从已校验Megasaur归档重新读取原367项完整总表和摘要，核对内部清单哈希。本包摘要与四条选择记录同上游一致。独立比较输入/目标清单确认缺口361降至357，Sinstone保持缺失；未重新跑102归档调查。

原161项Python检查、1098项Godot断言及69项交叉检查保留，但本次未重跑。初始五项失败试验未计入通过数量。本次未执行Godot proof_error、真实Catalog、Game、完整编译器或存档加载。

## 回执和资源

回执：HISTORICAL_TOOLS_BATCH2_STREAM_VERIFICATION.json
SHA256：45c8d5c2837861e93d92c59df791c967a226d072decbaa34f59b6f5672f35b97
实际目标字节流摘要：d411ea819fb5cf6910132c6e8ad90bea8367adf2648d9112992a708bf6cc9fdb
摘要格式：排序UTF-8路径、NUL、ASCII字节数、NUL、实际文件字节，覆盖所有目标文件。

首次受限核验通过，退出0，30.30秒，确切子进程峰值113852KiB。192MiB RSS保护、512MiB地址空间、180秒超时，无提高阈值。见BOUNDED_PROCESS及STREAM_VERIFY。核验进程峰值不代表游戏内存收益。

## 输入及历史复用

直接输入cfe5366f7e0a115532e8996549782c635481b97a：
https://github.com/Ethsigema/AI_text01/blob/cfe5366f7e0a115532e8996549782c635481b97a/battlegrounds-backup/pending/20261109-historical-tools-batch1-candidate/RECOVERY_VERIFIED.md

输入归档SHA256 d4de01b2fa7a530c00b383455e94f1a0da62d81c68b03b4205b90aca1c46aea1。
输入MANIFEST SHA256 1339271a1dc7d2789e931e1a2c2270d9b45613ed5717a7269332919949c7624d。
输入回执SHA256 c3e5df6796a973d499533adae754dc3501d26d721f62f9c78f33dd158089af1e。
输入SOURCE_MAP SHA256 53da1c13fbebb6eb8c5672ad8828109720efdfab1a8a97b6792a6da3202e6080。

本轮新下载本批包及固定元数据，历史Harbinger树、六份旧归档和更早历史链复用并重哈希；没有重新下载历史整链。其他时段的全新链审计不冒充本次运行，诊断包不是运行增量。

## 复现

Python3.9或以上标准库：

```sh
python3 verify_batch2_stream.py \
  --historical-baseline /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --native-archive /path/to/native_spell_listener_leaf_partial_candidate_20261109.tar.xz \
  --earth-archive /path/to/earth_mother_helper_leaf_partial_candidate_20261109.tar.xz \
  --golden-archive /path/to/native_golden_source_leaf_partial_candidate_20261109.tar.xz \
  --golden-tool-archive /path/to/golden_arrow_tool_patch_reconstruction_candidate_20261109.tar.xz \
  --megasaur-archive /path/to/megasaur_tool_fixed_pin_candidate_20261109.tar.xz \
  --batch1-archive /path/to/historical_tools_batch1_candidate_20261109.tar.xz \
  --output /path/to/a-new-batch2-stream-directory
```

默认从固定提交下载新包及输入元数据。可预下载同一提交MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY和5片，传--download-dir，再用--baseline-manifest、--baseline-receipt指定本目录PINNED_INPUT副本，哈希约束不变。本次采用Git预下载，因此increment_downloaded_by_this_helper:false仅指Python脚本不负责下载，实际来源见FETCH_PROVENANCE。

输出为安全解包后的证据、完整逐文件结果映射和回执，不是完整运行工程。完整工程需先恢复并校验完整上游输入，在空间充足时用封存restore_to_new.py写入不存在的新目录，再核验全部目标及输入未变。本轮未执行完整复制，delta四文件不是可独立游戏。

所有旧备份、历史失败试验及未验证材料保留，不强推。
