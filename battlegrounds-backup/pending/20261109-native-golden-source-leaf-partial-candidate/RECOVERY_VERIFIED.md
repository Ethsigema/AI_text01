# GoldenArrow来源叶：封存清单字节恢复通过，已知引用缺口保留

候选仍为PARTIAL_PURE_HELPER_AND_LIGHT_ENTRY_PASS_FULL_HOST_UNVERIFIED。完整PrizeGolden、Catalog/Game、旧存档与回放、全局内存收益未验证，不提升任何此前候选。新叶改变代码身份，不假称旧存档指纹兼容，也不伪造旧指纹。

## 必须保留的已知缺口

原指纹列表引用tools/golden_arrow_patterns.py，但输入和目标SOURCE_MAP都没有此文件，历史基线实际路径也不存在。原/候选GoldenArrow文件的引用均保留，本次没有把research中的同名文件当作正式文件，也没有修复该缺口。下文“缺失0”严格相对封存SOURCE_MAP，不意味着全部运行引用齐全。未运行包含缺失项的完整Catalog指纹循环，真实后果未测。

## 远端及流式核验

- 新包固定提交 `11e9e8188a23f62542aad8a43a2560aff9e3b402`，仅新增11个备份文件，旧文件未修改或删除，未强推。
- git fetch固定提交后读取所有上传文件；5个分片对象在下载前不在本地Git对象库，证明本次确实远端重新下载。相同辅助对象可能由Git去重。证据见BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE及ARCHIVE_PUBLICATION_RECEIPT。
- 5片、1,065,532字节归档、71个成员及内部70项清单逐一匹配。清单自身由外部MANIFEST覆盖。
- 原包SHA256：`181a6415d954795e0b40286165c39a55d0469745185e7e6d24840eb769025cef`。
- 固定EarthMother输入MANIFEST和回执重新远端读取并核对。复用EarthMother归档79成员、native listener归档247成员重新核验，Harbinger完整历史树27,893文件重新哈希。
- 三层历史字节组合严格对应直接输入的27,896文件。新增1、修改2、删除0，净增768字节；新delta三文件及before/两原文件都严格符合前后映射。
- 流式实际读取目标27,897文件、1,548,720,190字节并重新计算各文件SHA256，严格等于SOURCE_MAP。来源为新GoldenArrow delta3、EarthMother delta4、native listener delta5和历史树27,885文件。
- 相对封存清单，缺失、多余、哈希不符均为0。已知未列入清单的工具引用缺口另外明确记录，未掩盖。
- 完成后再哈希完整历史树和两份旧归档，内容未变。没有完整运行目录复制，没有执行Godot，没有删除任何旧备份或未验证成果。

完整回执：`GOLDEN_SOURCE_LEAF_PARTIAL_STREAM_VERIFICATION.json`，SHA256：`2f24988e51c5acfc08df4f2417aefad974dd8717b9bbf2673ad4baadf48b66b0`。
实际重建映射SHA256：`c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b`，脚本会生成包含全部目标逐文件结果的JSON。
实际目标字节流摘要：`9a2d810ca0fbf68879a3d481c75fb03e7df20eb049b72a0575b57ab771d1e07e`；格式为按路径排序的UTF-8路径、NUL、ASCII字节数、NUL、实际文件字节。

## 核验自身的首次失败与低内存重试

首次Python核验在新包71成员检查通过后收到SIGKILL，退出137，没有成功回执。原因未知，不将其断言为OOM，也没有把旧成功回执充当本次结果。原核验脚本、失败日志及失败说明均保留。

随后降低内存保留：逐成员按1MiB块哈希，只保留历史清单和必要delta，及时释放临时清单，历史目录逐文件扫描而不复制整份元数据字典。只进行一次低内存重试，192MiB RSS保护、512MiB地址空间、180秒超时，没有提高资源上限。重试结果、确切子进程峰值及退出码见BOUNDED_RETRY_PROCESS.json，STREAM_VERIFY.log是实际重试日志。失败输出目录保留，重试使用全新目录。

## 固定依赖与历史复用

直接输入EarthMother候选27dd08d164f1df0dd9ffe9391b9fcaa751529779：
https://github.com/Ethsigema/AI_text01/blob/27dd08d164f1df0dd9ffe9391b9fcaa751529779/battlegrounds-backup/pending/20261109-earth-mother-helper-leaf-partial-candidate/RECOVERY_VERIFIED.md

输入归档SHA256：`333aad27ba8ed0d0699c97cd4a33be5494310247a8350993532cd725f26e753c`。
输入清单SHA256：`d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960`。
输入MANIFEST SHA256：`e6f5562344c7c5ddee0b0cdd6c31684a4b32f570c68e834d9d00145402eb69f7`。
输入流式回执SHA256：`9e00b1c2957add5c5cc77fe9fa5ac881030780833b6d6ca9c683b3c1be84a9be`。
更早native listener归档SHA256：`46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7`。
新目标SOURCE_MAP SHA256：`c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b`。

本轮只重下GoldenArrow新包及固定元数据。历史Harbinger完整树、两份旧候选归档和更早历史链复用并重哈希，没有历史整链重下。另一次到EarthMother的全新链审计是独立运行，不冒充本次执行，也未包含本GoldenArrow包。诊断档案不属于运行补丁链。

## 重现流式验证

Python3.9及以上标准库，准备历史Harbinger完整树、EarthMother和native listener归档，下载本目录脚本后运行：

```sh
python3 verify_golden_leaf_stream.py \
  --historical-baseline /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --prior-archive /path/to/earth_mother_helper_leaf_partial_candidate_20261109.tar.xz \
  --older-archive /path/to/native_spell_listener_leaf_partial_candidate_20261109.tar.xz \
  --output /path/to/a-new-golden-source-stream-directory
```

默认下载固定新包与固定输入元数据，安全解压，完整检查历史层、增量、目标实际字节、输入不变性及已知缺失引用。输出仅为证据和目标映射，不是可运行工程。目标目录必须全新，所有旧备份和已有输出保留。

也可预下载同一固定提交MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY及5片后传入--download-dir；用--baseline-manifest和--baseline-receipt提供本目录PINNED_INPUT副本。固定哈希检查不变。本次使用Git预下载，所以increment_bytes_freshly_downloaded_by_this_helper:false只代表Python脚本不负责下载，实际下载证据见FETCH_PROVENANCE。

若需完整运行目录，先恢复并严格核验EarthMother输入，再在足够空间下用包内restore_to_new.py向不存在的新目录恢复并核对全部目标及基线未变。该完整复制本轮未执行。缺失工具引用不会因为精确恢复SOURCE_MAP而自动补齐，不能假称修复。

## 验证上限

封存6个进程1030项是有限小探针，未在备份任务重跑。oracle不是完整原PrizeGolden，薄代理不是完整修改后宿主，TinyCatalog不是完整Catalog。未跑实际变金、施法、购买、EOT、旧存档、回放或UI；67.4MiB仅为小探针峰值，不是全局内存收益。16条原证据pin保留，新叶进入指纹不等于固定准入pin。没有重试SIGKILL或提高阈值。
