# 第4批三项历史工具：远端流式字节核验通过

仅新增Boom Controller、Soul Fermenter、Twin Lanterns三文件，共119,828字节，修改0、删除0。历史原件未证明最新版，三个工具本身不是当前固定准入pin；不把本批称为新准入阻断修复。

原367范围剩354路径，原68历史类别剩56项。此前Sinstone、Ancient Wishbone、Factory Line、Balinda Spell、Boogie Monster、Partner in Crime六项仍缺失，未恢复或改写其审查证据。上述范围不是全项目所有缺口。完整Game、旧存档、真实Catalog/全指纹、全项目编译器及整体内存收益未验收，清单字节精确匹配不代表完整游戏恢复。

## 两个检查点不混淆

原包制作检查点92710e8471cd9353b2393ddf6f55c1a9454a760f包含第3批只读审查，不含新运行增量。独立重新远端读取其回执，SHA256 671519fca12a0275d3b598672561f4d94dd03ffa5602621fdbc78ab262f330b0，确认源码变更0，仍引用第2批运行输入和相同SOURCE_MAP。

实际运行依赖固定8a675dc886b8686e6bdd9a47463366cafb9c020f：
https://github.com/Ethsigema/AI_text01/blob/8a675dc886b8686e6bdd9a47463366cafb9c020f/battlegrounds-backup/pending/20261109-historical-tools-batch2-four-candidate/RECOVERY_VERIFIED.md

第3批只读包不作为运行补丁应用，也没有更改原包RESULT。

## 真正下载与独立核验

本包归档固定提交e4b9f301a494c0623daebfd17d7b60fd933c4c6f，1,095,004字节，SHA256 85e5b08ccafa5dde8ecc02bdd24ecb740a5eb20baf2a81329e8c52b61773cc20。

五个分片Git对象在fetch前均不存在于本地对象库，已从固定远端提交真实下载。辅助相同对象可能被Git去重，不称全部重新传输。BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE和ARCHIVE_PUBLICATION_RECEIPT保存证据。归档发布仅新增11文件，旧文件没有修改/删除或强推。

5片、整包、155成员及内部154项清单匹配。完整前后映射、三文件delta和空删除记录一致。第2批固定MANIFEST和回执重新远端读取并按固定SHA核对。

重新实际哈希Harbinger完整历史树27,893文件，逐成员重核七份旧归档：native listener247、EarthMother79、GoldenArrow来源叶71、GoldenArrow工具98、Megasaur143、第1批199、第2批282成员。依次组合成输入27,908文件，各层前后映射连续。

流式实际读取目标27,911文件、1,549,091,079字节，每文件重新计算SHA256。来源：历史树27,885、native listener5、EarthMother4、GoldenArrow来源叶3、GoldenArrow工具1、Megasaur1、第1批5、第2批4、本批3。相对封存SOURCE_MAP，缺失、多余和不符均为0。

目标SOURCE_MAP SHA256：608a981c9b82b255c37fefb004a4bfe98bcf95d9717cfa3a5ee2917961ff2d00。
末尾再次哈希历史树及七份归档，内容未变。没有完整运行工程目录复制，没有删除任何旧备份或未验证材料。

## 历史来源和依赖表示检查

三工具同实际历史候选和封存原文逐字节一致，历史integration_manifest/shared_manifest同基线相同，目标安装SHA匹配；三个FROZEN对shared_manifest的固定哈希也独立匹配。当前三来源脚本未变。

仅对原Python做AST解析和字面常量读取，不执行模块。RAW/EXPECTED及存在的PROGRAMS共6项与当前来源一致。50项现有固定pin实际字节哈希全部匹配，三个工具自身不是这些pin。

三工具DEPENDENCY_RAW逐项同固定dependency_raw.json一致，当前GDScript的DEPENDENCIES逐项同固定dependencies.json一致；两份JSON本身都是当前PROOF_SHA256固定项。独立检查16个模块-依赖条目、6个不同ID，RAW到编译表示变化仅限supported、effects、coverage_rule、coverage_text_sha256、default_pool、pool_supported，原生身份/来源/数值等其他字段未变。没有把编译后依赖误当RAW直接比较。

上游Megasaur完整367项总表和摘要重新按已核验归档读取；本批摘要及三条选择记录一致。与输入/目标比较确认357降至354，六个暂缓目标仍未加入。未重跑102归档调查。

原封存165项Python、1080项Godot断言、69项交叉检查及构建器初始路径定位失败记录保留，但本次备份任务没有重跑这些测试，没有执行Godot、真实Catalog、Game、全编译器或存档。局部证据不提升玩法支持状态。

## 回执与资源

回执：HISTORICAL_TOOLS_BATCH4_STREAM_VERIFICATION.json
SHA256：1dffa961d83010bc496009434b113690d9a9506932acbb71bcbf1718a55ed80f
实际目标字节流摘要：540314029d35100030257837829f0f3cdff60e37bb3a5e0503902675952a9349
摘要格式：排序UTF-8路径、NUL、ASCII字节数、NUL、实际文件字节，覆盖所有目标。

首次受限核验通过，退出0，33.36秒，确切子进程峰值115928KiB。192MiB RSS保护、512MiB地址空间、180秒超时，未提高阈值。见BOUNDED_PROCESS与STREAM_VERIFY。核验峰值不是游戏内存收益。

## 复用范围和固定依赖哈希

输入第2批归档SHA256 51263c49a09a0a735a417e147e4f64f0529be4d5fa12529807653da7187693eb。
输入MANIFEST SHA256 26e1d37470f663358cc246c5a860d0d563b1eae60a3729f466f2080546ed678b。
输入流式回执SHA256 45c8d5c2837861e93d92c59df791c967a226d072decbaa34f59b6f5672f35b97。
输入SOURCE_MAP SHA256 3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea。

本轮新下载本批归档和固定元数据。历史树、七份旧归档及更早历史链复用并重哈希，没有重新下载历史全链。其他时段全新链审计不冒充本次执行，诊断/只读审查档案不是运行增量。

## 复现

Python3.9或以上标准库：

```sh
python3 verify_batch4_stream.py \
  --historical-baseline /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --native-archive /path/to/native_spell_listener_leaf_partial_candidate_20261109.tar.xz \
  --earth-archive /path/to/earth_mother_helper_leaf_partial_candidate_20261109.tar.xz \
  --golden-archive /path/to/native_golden_source_leaf_partial_candidate_20261109.tar.xz \
  --golden-tool-archive /path/to/golden_arrow_tool_patch_reconstruction_candidate_20261109.tar.xz \
  --megasaur-archive /path/to/megasaur_tool_fixed_pin_candidate_20261109.tar.xz \
  --batch1-archive /path/to/historical_tools_batch1_candidate_20261109.tar.xz \
  --batch2-archive /path/to/historical_tools_batch2_four_candidate_20261109.tar.xz \
  --output /path/to/a-new-batch4-stream-directory
```

默认下载固定新包、运行输入元数据及只读检查点回执。可预下载同一固定提交MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY和5片，传--download-dir；另以--baseline-manifest、--baseline-receipt、--readonly-checkpoint-receipt提供本目录三个PINNED副本。哈希约束不变。本次为Git预下载，increment_downloaded_by_this_helper:false只指Python不负责下载，真实来源见FETCH_PROVENANCE。

输出是安全解包证据、完整逐文件结果和回执，不是完整运行工程。若需完整工程，应先按输入恢复链重建并校验完整基线，空间足够时用封存restore_to_new.py写入不存在的新目录并核验全部目标及输入未变。本轮未执行完整复制，三个delta文件不是独立游戏。

旧备份及所有未验证材料保留，不强推。
