# Megasaur固定pin历史原件候选：流式字节核验通过

仅新增tools/megasaur_adapt_patterns.py，32,296字节，SHA256 adf31c928468bb9be4dcca89bda2dd0096626dbbbc926dae639ce24bea23b1a2。修改0、删除0，旧源码所有条目不变。文件与真实历史候选原文逐字节一致，也精确匹配当前未修改core/amalgadon_sources.gd的显式pin。本项不是GoldenArrow式补丁重建，也不是依据GDScript新编逻辑。

恢复前367项调查原样封存；只恢复本项，余366项仍缺失。这个范围不是全项目所有缺口。tools/amalgadon_native_patterns.py仍缺失，其余68个历史候选未恢复，不宣称其为最新版或已验收。完整Game、完整Catalog最终指纹、旧存档兼容、回放、离线全编译和整体内存收益未知或未验证。

## 下载与独立核验结果

归档固定提交a00e227da42ecf4563c324e7994ecf9c5a63dde8，SHA256 27514275c7204a972de2a5193b93deb35c7d4a72b137d1bc5c9477c2f7e9cf66，1,490,252字节。

6个新分片Git对象在fetch前都不存在于本地对象库，本次从固定远端提交真实下载。辅助相同对象可能被Git去重，不称其全部重新传输。BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE和ARCHIVE_PUBLICATION_RECEIPT记录证据。上传仅新增12个文件，旧文件未修改或删除。

6片、整包、143成员及内部142项清单全部一致。固定输入MANIFEST及流式回执通过连接器重新远端读取并按固定SHA核对。完整前后清单、唯一delta和空REMOVALS对应一致。

历史Harbinger完整树27,893文件重新实际哈希，四层旧归档也逐成员重新核验：native listener 247成员、EarthMother 79成员、GoldenArrow来源叶71成员、GoldenArrow工具重建98成员。四层顺序组成直接输入27,898文件，所有前后清单连续。

实际流式读取全部27,899目标文件、1,548,785,133字节，并逐文件重新计算SHA256。来源：历史树27,885文件、native listener 5、EarthMother 4、GoldenArrow来源叶3、GoldenArrow工具1、本次Megasaur工具1。相对于SOURCE_MAP，缺失、多余、哈希不符均为0。目标映射SHA256：28b1d1c523dfc566bc5eacd04ccea1e1787c1b15e0cca8f9e67ecf9229b46bf4。

结束后再次哈希历史完整树和四份旧归档，均未变。未创建第二完整工程目录，未运行Godot或Game，未删除备份、源文件或未验证材料。

## 历史原件和固定pin复核

历史原件与新增文件逐字节相同。封存的原文、两份历史安装清单和创建补丁都与实际历史基线同路径文件逐字节相同。原创建补丁的目标、唯一hunk、行数和纯新增内容独立复核，完整重现原文件。这里只用创建补丁交叉验证找到的历史原件，不冒称根据后续补丁推导新版。

当前Amalgadon源文件哈希与封存证据和探针输入完全相同，显式43项pin静态逐字节检查：输入存在的42项均匹配，恢复该文件后43项全部匹配；委托Megasaur的32项pin也全部匹配。未修改pin常量，未放宽任何准入。

本次备份核验不重新执行Godot proof_error()。实际缺失/恢复/篡改三态返回值和重复小输入运行属于原封存6进程546断言及55项静态交叉检查；回执明确区分这些已保存证据和本次独立字节检查。没有全游戏行为结论。

## 367项调查保存

22个调查文件与INVENTORY_SNAPSHOT_MAP逐文件一致，没有缺失或额外文件。FINAL_INVENTORY保留367个唯一目标及恢复前全部缺失状态，本次独立与输入/目标清单比较确认只补1项，余366项未恢复。

调查原分类是1项当前pin原件、68项限定版本历史候选、21项待审查、277项在已查范围未找到可验证材料。旧报告不被改写为新恢复状态。本次没有重跑102归档扫描，也不把原调查说成本次新研究；21或277项不等于永久丢失。

## 回执与资源

回执：MEGASAUR_FIXED_PIN_STREAM_VERIFICATION.json
SHA256：58b2679422af16d3d0705f6f6eb7f2791dc42308a4f0c3b0f3a67c56f9d6abf4
实际目标字节流摘要：fdef1db1ea09cea6ec1405cf0df80c6bd945c3fccdbe8608d352b8eee6da52e5
格式为排序UTF-8路径、NUL、ASCII字节数、NUL、实际文件字节，覆盖所有目标。

首次受限核验通过，退出0，36.06秒，确切子进程峰值114156KiB。192MiB RSS保护、512MiB地址空间、180秒超时，未提高限制。BOUNDED_PROCESS与STREAM_VERIFY记录本次执行。小核验内存不代表全游戏内存收益。

## 固定依赖与历史复用

直接输入9b60cad21ed6dc06d2b4c8f67a36f8c88ab92290：
https://github.com/Ethsigema/AI_text01/blob/9b60cad21ed6dc06d2b4c8f67a36f8c88ab92290/battlegrounds-backup/pending/20261109-golden-arrow-tool-patch-reconstruction-candidate/RECOVERY_VERIFIED.md

输入归档SHA256 3122135a4912a58c361b522e67b946dffbbe29b3618051972a4898e8cac7edd9。
输入MANIFEST SHA256 a5016309666174b5a84523f5760f50b530110d8ce6f6dcdb1012c0f614af1a94。
输入回执SHA256 088ba4a90cda426adf92be1af7516689511e08f6ce3c1d40f5225589022ba862。
输入SOURCE_MAP SHA256 bfd5d82ede8559200aed89547e4584ac091873a9392079af5ee20c41ea764a0a。

本轮真实重新下载本次新包和固定输入元数据。Harbinger完整树、四份旧增量及更早历史链复用并重新哈希，没有重新下载历史整链。以前的全新链审计不能冒充本次执行，诊断档案不是运行补丁。

## 复现流式核验

Python3.9或以上标准库，准备历史完整树和四个旧增量：

```sh
python3 verify_megasaur_stream.py \
  --historical-baseline /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --native-archive /path/to/native_spell_listener_leaf_partial_candidate_20261109.tar.xz \
  --earth-archive /path/to/earth_mother_helper_leaf_partial_candidate_20261109.tar.xz \
  --golden-archive /path/to/native_golden_source_leaf_partial_candidate_20261109.tar.xz \
  --golden-tool-archive /path/to/golden_arrow_tool_patch_reconstruction_candidate_20261109.tar.xz \
  --output /path/to/a-new-megasaur-stream-directory
```

默认从固定远端提交下载新包和固定输入元数据。亦可事先下载同一固定提交的MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY和6片，传--download-dir；用--baseline-manifest、--baseline-receipt传本目录PINNED_INPUT文件，固定哈希约束不变。本轮采用Git预下载，故increment_downloaded_by_this_helper:false仅指Python不负责下载，真实下载证据见FETCH_PROVENANCE。

脚本安全解包，逐层验证，实际逐文件读取目标字节，输出全部逐文件映射和新回执。输出是证据目录，不是完整运行工程。若要完整工程，需要足够空间，先恢复并校验完整输入，再用封存restore_to_new.py写入不存在的新目录并验证前后；本轮没有执行完整复制。

所有旧备份与材料保留。精确恢复清单字节，不表示全部引用已经补齐或游戏整体可用。
