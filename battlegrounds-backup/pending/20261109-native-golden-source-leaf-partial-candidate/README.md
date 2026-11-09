# GoldenArrow 原生普通/金色来源校验叶模块候选

输入检查点：27dd08d164f1df0dd9ffe9391b9fcaa751529779（EarthMother 候选）。
输入完整清单 SHA-256：d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960。
候选完整清单 SHA-256：c0454c30ce7eb2a71fb8ea3e513f0db0d2fd684f63129a1b7da2e4a47666603b。

状态：纯辅助函数与实际 GoldenArrow 轻入口的有限验证通过，未验收完整 PrizeGolden、Catalog、Game 或旧存档。此实验不提升任何先前候选的验收级别。

## 改动范围

新增1、修改2、删除0，逻辑净增加768 bytes：

- 新增 core/native_golden_source_validation.gd：从原 prize_golden_effects.gd 原文迁移 _native_error、_strings、integer、_string，以及 MAX_STAT、MAX_EXACT_FLOAT。叶文件没有 preload。
- 修改 core/prize_golden_effects.gd：4个函数保持原签名并委托叶模块，2个常量改为引用原值。其余函数原文不变。
- 修改 core/golden_arrow_sources.gd：NativeGolden preload 改指新叶；既有 RUNTIME_PATHS 末尾追加新叶。所有函数、来源常量、16条固定证据pin不变。

无卡牌数据、中文名称、池、英雄、畸变规则、实际变金执行逻辑改动。before/保留两个旧文件，delta/保留三个运行增量，SOURCE.patch、CHANGES.json、空REMOVALS.json和前后完整清单一并封存。

整数校验保留原分支差异：int 可至 int64 最大值；float 必须有限、整数值且绝对值不超过9007199254740991。bool、StringName 与对应 String/int 不混同。既有校验允许的输入，例如非空 quality_flags/source_conflicts 数组、空 effect type 字符串，本次未擅自收紧。

## 中断续接审计

接手时3个delta及部分稀疏runtime已存在，没有提取证明、PLAN或运行结果。未盲目重跑原 build.py；resume_prepare.py 逐文件校验已存在内容，并完成证明与测试输入。

发现既有 RUNTIME_PATHS 包含 tools/golden_arrow_patterns.py，但它不在输入完整清单中，基线相应路径亦不存在。旧 build.py 直接复制此路径会失败。该文件确实存在于 research 下的候选路径，但本实验没有把那个文件冒充已安装的正式文件，也未改变运行源码的原路径列表。

该缺失路径是输入已有问题，另行保留到 RESUME_AUDIT.json。Catalog:1530 对每个路径读取文本并取哈希，缺失项可能导致错误输出或空文本指纹；本轮没有运行完整 Catalog，因此不宣称其运行后果已经实测。fingerprint 探针只确认其仍缺失，并验证追加新叶的身份覆盖，不把完整指纹循环标为通过。环境中断与此前 SIGKILL 原因均未知。

## 本轮验证

只复制27个必要输入，总263356 bytes；GoldenArrow实际preload闭包为5脚本。没有新建 data/assets 符号链接，没有复制完整1.55GB工程。

6个独立 Godot 4.6.3进程顺序执行，共1030项：

- helpers：963项，62104 KiB。原文提取oracle、新叶、实际宿主委托的薄代理三方比较。包含整数类型/上下界/非有限数、String/StringName/重复集合、正常/金色来源、必填字段、坏来源与类型矩阵。
- arrow：58项，69064 KiB。加载实际 GoldenArrow；对照仅把旧重依赖换成原文oracle的原GoldenArrow。验证原始/编译来源、3个依赖、原生普通/金色对、当前和来源catalog的分别篡改等。TinyCatalog仅为测试替身，不代表完整Catalog。
- fingerprint：6项，68864 KiB。确认旧列表原前缀不变、新叶末尾加入、真实叶字节的Catalog相同哈希表达式可消费、改文本会改摘要、既有缺失项如实保留、原pin字典未变。未执行整个Catalog或含缺失项的完整循环。
- tamper_native、tamper_raw、tamper_contract：各1项，最高68800 KiB。在三份独立小副本中分别改原生XML、raw_rows、source_contract，实际 proof_error 均返回既有 golden_arrow_native_proof_changed 错误。正式稀疏输入和原证据未改。

每进程192MiB RSS提前停止、启动前至少1GiB系统可用内存、运行中至少640MiB可用余量、2GiB地址空间上限、45秒超时、5ms采样、2个CPU。最大RSS由 os.wait4 对确切Godot子进程取得。日志均无ERROR，退出码均为0。本轮没有失败的Godot运行。

## 静态依赖与不能声称的结论

- GoldenArrow Sources：837 → 5脚本。
- PrizeGolden：837 → 838脚本。
- 完整Catalog：1541 → 1542脚本。
- Game：2069 → 2070脚本。

这证明轻来源入口切断了对重执行模块的直接preload链，不证明完整项目的峰值或总驻留内存降低。67.4MiB是本轮小探针峰值，不是完整游戏内存，更不能拿它与此前SIGKILL试验直接计算百分比。

原文提取oracle不是完整原PrizeGolden；薄代理不是完整修改后PrizeGolden编译。没有加载完整PrizeGolden、Catalog或Game，没有施法/购买/EOT/回放/存档/UI实测，没有原重入口内存A/B，也没有重试此前SIGKILL。

## 指纹和兼容性

新叶通过 GoldenArrow.RUNTIME_PATHS 进入既有 Catalog:1530 指纹循环。修改宿主和来源文件也仍在旧列表中。此处覆盖执行代码身份，不是新增叶的固定证据pin；并不声称初次加载会拒绝任意改过的叶文件。原16条来源证据固定SHA均按原值核对，测试后仍不变。

运行代码身份已变，旧存档指纹兼容性没有保留或验证，不伪造旧指纹。对当前输入gd文件搜索两个被改旧文件的明文SHA，没有发现固定代码pin级联；此静态扫描不能穷举编码形式、外部工具和历史描述。

## 恢复、封存与可复跑性

27个稀疏输入及其正式来源在测试后按字节数和SHA复核。3个增量恢复到新 focused_restore 并逐文件验证。前后清单其余条目严格相同；未重新散列全部旧工程，未冒充新的整链实测。

SOURCE_MAP.json含27897个文件、1548720190逻辑bytes。restore_to_new.py仅接受完整匹配BASE_MAP.json的输入工程，并恢复至不存在的新目录；先核对源清单和空间，不覆盖任何基线。本轮未运行完整工程恢复。

压缩包包含增量、旧文件、完整清单、运行gate、真实日志/采样、各输入清单、静态证明与恢复工具。排除runtime及其篡改副本、用户目录、Godot缓存和focused_restore，以避免复制基线。包内每个成员再次解压流式核对SHA。

原 build.py 为中断前版本，保留作溯源，不应直接复跑；请使用 resume_prepare.py 并提供其对应基线和先前两个delta。测试工具中原GoldenArrow oracle的辅助依赖是创建时绝对路径，换目录需要在新的隔离实验目录重新生成/定位oracle，不可把旧日志当新验证。运行源码delta不含实验绝对路径。

所有既有备份、Catalog Memory/Harbinger依赖恢复树及其符号链接均未删除。此局部候选尚未上传或发布，也未完成远端下载整链恢复。应先做正式备份/链验证，再决定下一项小规模诊断；不建议在当前资源条件下直接启动完整Game。


## 上传时补充

以上“未上传”是原封存时状态，原包字节保持不变；现已按增量备份保存。恢复核验严格相对于封存SOURCE_MAP，不表示所有引用路径齐全。旧指纹列表引用的tools/golden_arrow_patterns.py仍缺失，未用research中的相似文件替代，未修复或假称完整指纹通过。完整Game、存档兼容性及整体内存收益均未验证。
