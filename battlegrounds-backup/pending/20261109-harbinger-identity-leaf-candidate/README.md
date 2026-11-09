# Harbinger EOT身份识别叶模块：独立实验候选

状态：真实模块的限定范围A/B等价性与Admission入口节约已验证；完整catalog/Game仍未验收，不替换已验收游戏基线。

## 改动范围

直接输入为内存实验检查点4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1；最近诊断档案提交2bd2ce9296a0ad8c397e4efc25301601ed9e5275不改变其运行源码。最后完整游戏验收基线仍为a71d3e4ea64dc52264a3f789a48ddae2e4a043cd。

新增1文件、修改2文件、删除0文件，运行源码净增418 bytes：
- 新增 core/eot_repeat_identity.gd（612 bytes）：承载原来的TYPE和四项IDENTITIES唯一原定义，并引用原有OwnerRepeats/OwnedRepeats轻模块。
- core/end_turn_repeats.gd：TYPE/IDENTITIES转为共享叶的别名；原其他公开成员、依赖与全部23个函数正文逐字不变。
- core/harbinger_eot_admission.gd：Repeats预载转向新叶；全部7个函数正文逐字不变；RUNTIME_PATHS加入新叶。

没有删机制、删来源检查、扩大效果准入、变更卡牌/中文名或开发英雄机制。历史来源记录未改。新叶被原catalog路径循环纳入执行指纹；这不是给新叶添加固定PROOF_HASHES pin，原固定证据检查仍只覆盖原证据文件。

## 真正执行的测试

所有Godot顺序运行，RSS提前停止512MiB、系统余量640MiB、地址空间2GiB、90秒、2 CPUs、25ms采样。没有完整catalog或Game加载。

最终新进程A/B使用os.wait4收集确切Godot PID的峰值，并在启动前核验脚本来源哈希：

1. 真实Admission模块：75项检查、288条结果，两侧完整报告逐字一致。
   - 普通/金色、四项重复身份、owned标记、owner family排除、未知repeat类型、源字段缺失/改写、typed flags、附着/base篡改、canonical目录差异、domain和permits。
   - 身份表键顺序、类型和值、顶层/嵌套只读属性保持一致。
   - 峰值RSS378820→65452KiB，降低313368KiB（306.02MiB，82.72%）；用时5.409→0.839秒。
   - 仅代表这个独立入口，不能说完整Game也节约306MiB。
2. 真实EndTurn模块：13项检查、297条结果，完整报告逐字一致。
   - 原公开常量/依赖、全部方法名、effect/source-card校验、倍率代数及上限、interval、依赖图拒绝、has_modifier边界。
   - 峰值RSS375948→376276KiB，基本不变。实际调度器及其附件依赖仍保留。
3. 三种畸形输入：null effects、Dictionary effects、整数type，双方产生完全相同的原有错误文字且完成所有用例。这是错误行为等价，不是新增的友好拒绝。
4. 对独立复制的原生XML追加测试注释，原版/候选的proof_error及domain_error产生同一个预期拒绝。没有修改原资源或任何备份。
5. 执行Harbinger路径子列表的原文本哈希组装，确认新叶仅包含一次，修改其内存中文本会改变子列表摘要。未执行完整catalog指纹计算。
6. 静态检查：两原模块全部函数正文逐字不变，身份定义原文字节一致；未发现当前两个被改文件摘要的现存固定pin。历史快照未更新。

合计两主A/B组88项通过检查、585条完全相同结果，另有畸形与证据篡改专项。

## 失败与测量说明

最初baseline_admission_1将整数type放进普通矩阵，触发原有运行错误，日志和当时脚本已保留，不计通过。之后将正常矩阵和畸形错误测试分开，在新进程重新运行。

初版launcher使用累计RUSAGE_CHILDREN；复合shell末条命令可能继承先前子进程的峰值（candidate_fingerprint_1出现该现象）。不使用这些辅助记录的maxrss作性能结论。最终四次主对照已改用确切子PID的wait4，并重新运行全部主检查；原始记录保留，不静默改写。

## 节约的边界

Admission静态preload闭包从178脚本降到7；EndTurn从177增到178；完整catalog图从1538增到1539。共享叶解决入口耦合，不删除最终仍需要的执行宿主。因此它不保证完整图最终驻留下降，也没有证明先前SIGKILL问题已解决。

完整catalog、Game、完整来源证据链、自然获取、实际EOT回调顺序/附件执行、存档、回放及UI未验证。此次保持所有原函数正文并验证选定真实边界，不应冒充全机制回归。

## 恢复和完整性

BASE_MAP.json与SOURCE_MAP.json给出完整前后清单（27892→27893文件）；CHANGES.json有全部前后哈希，REMOVALS.json为空；delta/包含唯一有效运行增量，SOURCE.patch供审阅。

全部27892个输入文件重新按哈希核验未变；179个测试脚本与测试前快照一致；三个新增/修改文件已在新位置实际恢复并核验。没有另建完整1.6GiB工程。测试sandbox独立复制静态脚本，data/research/assets只读沿用原资源目录，不是完整工程副本。tampered_*目录仅供失败证据，绝不能作为运行增量应用。

restore_to_new.py只接受全新目标目录，先核验完整输入，再复制并应用delta，最后核验全体输出；不会修改或删除基线。所有已有备份保留。


## 上传补充与验收范围澄清

原包保持封存不变。原文中的“最后完整游戏验收基线”不得解释为全部机制、完整回归均通过：a71d3e4ea64dc52264a3f789a48ddae2e4a043cd仅保留此前已验证的限定范围，本包不扩大或提升其验收范围。最新运行依赖为catalog memory候选；诊断档案不含运行增量，不必叠加。此次后续完整目录重建仅为源码字节核验，不运行Game。所有旧备份保留。
