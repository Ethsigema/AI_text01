# EarthMother 纯比较及 UID 叶模块候选

输入运行检查点：1288c092b970edaa6a75c2be89809354eed19405。
输入完整清单 SHA-256：9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111。
候选完整清单 SHA-256：d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960。

状态：仅纯辅助函数及轻入口的有限验证通过。不是完整宿主、Catalog 或 Game 验收，不提升此前任何部分候选的验收状态。

## 真实源码增量

新增 1、修改 3、删除 0，逻辑文件净增加 367 bytes：

- 新增 core/exact_value_identity.gd：从原 EndTurn 原文迁移 _uid、_same，没有 preload。
- 修改 core/end_turn_repeats.gd：增加叶 preload，上述两函数保持原签名并委托；其余 21 个函数原文不变。
- 修改 core/earth_mother_sources.gd：只将 Exact preload 指向新叶，全部来源和活体校验函数不变。
- 修改 core/catalog.gd：仅在第1357行既有短指纹路径列表末尾加入新叶。其他代码字节不变。

没有修改卡牌、中文名、数据池、法术规则、英雄或畸变怪范围。大地母亲之眼及托尼证据沿用原来源，9条固定来源证据 SHA 全部核对无变化。原始函数、原文件、增量、差异、完整文件清单、删除空清单均封存。

## 等价约束

_same 保留递归 Dictionary/Array、原 Dictionary.has 键语义、数值有限性、类型区分与原比较式。原注释写 integer-valued，但代码接受相等有限小数；本次没有“修正”成整数限制。NaN 和正负 Infinity 均仍拒绝。bool 与 int/float 不混同。

_uid 保留 String 类型、u 前缀、总长≤20、is_valid_int、str(int(suffix)) == suffix 和正值检查，不用近似正则替代。

保留原函数的有限输入语义，不增加循环检测或深度限制。旧宿主多一层委托，病态递归、循环容器和栈耗尽行为没有被证明等价，亦未运行这类危险探针。

## 本轮新测试

所有 Godot 都顺序启动，192 MiB RSS提前停止、640 MiB系统可用余量、启动前1 GiB可用内存、2 GiB地址空间上限、45秒超时、5ms观测、2 CPUs。峰值由 os.wait4 对确切子进程取得，没有并行 Godot。

6个有效新进程，共1439项检查：

- helpers：1395项，最高61272 KiB。原文提取 oracle、新叶、实际两段宿主委托的薄代理做三方比较；包括明确预期边界、24×24类型矩阵、32层嵌套、UID边界和768个生成UID。
- earth_2：38项，最高89700 KiB，约87.6 MiB。实际候选 EarthMother 与仅替换其旧 Exact 依赖为原文 oracle 的对照：原始证据、三身份 raw/compiled/base、活体 Eyes、UID/非有限数/畸形字段等边界一致。实际 CurrentSpellStock 轻入口成功加载并共享同一 EarthMother Script；只检验其限定 claimed 分支，没有执行购买或施法。
- fingerprint：3项，最高61032 KiB。执行从修改处提取的原/候选短指纹循环，证实前三项不变、末尾读取新叶真实文本哈希、变更文本会改变摘要。没有加载完整 Catalog。
- tamper_native、tamper_raw、tamper_contract：各1项，最高68076 KiB。仅在新建私有副本追加篡改字节，实际既有 validation_evidence 都返回原 evidence_changed 错误。原文件、正式稀疏输入和备份不变。

第一次 earth 测试脚本误将 bool UID fixture 与 String 直接比较，Godot 报 Invalid operands，控制器终止。虽然脚本错误后写出一个部分 PASS 报告，该报告无效，明确排除。失败的 gate、日志、PROCESS、报告完整保留于 earth/；改的是测试脚本的类型守卫，不是候选源码，随后 earth_2 完整通过。

## 不能据此声称的结果

原文 oracle 不是完整原 EndTurn 宿主。薄委托代理不是整个修改宿主的编译。没有运行原重入口作内存 A/B，没有重试以前的 SIGKILL，没有完整 Catalog/Game、实际EOT/施法事件、存档、回放或UI测试。89700 KiB只是小探针峰值，不是完整项目内存，不能计算完整项目节约比例。

静态 preload 图：
- EarthMother：182→8脚本。
- CurrentSpellStock：183→21脚本。
- EndTurn：178→179脚本。
- 完整 Catalog：1540→1541脚本。

因此切断轻来源入口的重宿主依赖已成立，但完整图没有移除原重模块。后续其他入口仍可引入 EndTurn；总驻留或编译峰值下降未证明。

## 指纹与兼容性风险

新增叶进入 Catalog:1357 的现有短循环，再由 :2100/:2104 汇入 execution_fingerprint。现有 Game:14131 保存该指纹，:14493 回读比较。新增叶的消费身份得到覆盖，旧宿主/EarthMother继续在原长列表中。

这不是新叶的固定准入pin：修改叶会改变保存指纹，并不等于首次加载会自动拒绝该叶。原9条来源证据门未减弱。

代码身份改变意味着旧存档指纹不再相同；不能伪造旧指纹维持表面兼容。上述保存/读取路径是静态核验，本轮没有实际跑存档迁移、拒绝或回放。

对当前 .gd 文件搜索3个旧源码的明文 SHA，没有找到固定代码pin级联。这个扫描不等于穷举外部工具、历史叙述或所有编码形式。

## 恢复和完整性

独立候选只复制21个脚本及必要证据，共538646 bytes；data/assets只读沿用已核验基线。没有新复制约1.55GB完整工程。

35个稀疏输入和其原引用在测试后均按SHA复核。3个被改旧文件与已核验输入清单相符。4个增量文件已恢复到独立 focused_restore 并逐文件核验。没有重新散列全套旧工程，完整清单的未改部分继承输入检查点，不冒充新的整链实测。

SOURCE_MAP.json列出27896文件，共1548719422逻辑bytes；CHANGES.json包括每个增量前后大小和哈希，REMOVALS.json为空。before/保留3个原文件。restore_to_new.py只允许从完全匹配 BASE_MAP.json 的输入工程恢复到不存在的新目录，先核查空间，再复制验证，不覆盖任何基线；本轮未运行该完整恢复命令。

包内测试工具记录当时真实路径，原始 EarthMother oracle 有指向同目录 helper 的绝对路径。若在别处复跑，应在新的实验目录重新执行 build.py生成对应路径，或重新定位测试工具，不能直接把旧路径日志当新验证。运行源码 delta 没有实验绝对路径。

已保留失败证据及所有既有备份，无删除。此候选应先经备份和流式完整恢复验证，再安排下一项小规模诊断；当前条件下不建议直接完整加载。


## 上传与恢复核验边界

原包封存不变。保留全部旧备份，非强推追加。本轮低磁盘流式读取每个目标文件实际字节核验，历史Harbinger树及native listener增量复用，不另建完整运行树。完整游戏、存档兼容性及回放未验证；代码身份与execution_fingerprint改变，不能假称旧存档兼容，也不伪造旧指纹。
