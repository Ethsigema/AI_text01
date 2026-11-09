# Native spell listener 来源校验叶：部分验证候选

状态：纯来源校验迁移及候选小入口已验证；原完整入口探针被SIGKILL中止，完整宿主编译/运行及Game未验证。不得替换已验收游戏基线，也不提供完整入口内存节约比例。

## 输入和真实改动

输入为26679da39e12f73907a9d15c325ca4028daf8474核验的Harbinger叶模块候选；最后完整游戏验收仍为a71d3e4ea64dc52264a3f789a48ddae2e4a043cd。

新增2文件、修改3文件、删除0文件，净增4533 bytes：
- 新增 core/spell_listener_source_proof.gd：原宿主6个完整纯校验函数及必需常量原文迁移，含全部recipient、tavern四来源、当前Azerite适配和完整配对检查。
- core/spell_cast_listeners.gd：保留同签名的6个代理以及原常量别名；其余10个函数正文逐字不变，实际执行依赖保留。
- core/native_spell_listener_stock.gd：仅将Listeners预载指向新叶，全部函数正文不变。
- 新增 research/spell_listener_source_leaf/provider_revision.json：明确后续实现修订、前后源码和函数摘要、未验收范围。
- core/patch_3702_azerite_sources.gd：固定stock摘要更新为新精确实现；新增叶和revision固定pin；原其他所有pin及全部函数正文不变。RUNTIME_PATHS只增加新叶和revision。

原research/patch_3702_azerite/source_evidence.json逐字不动，并继续受原摘要保护。其baseline与v3“unchanged provider”描述保留为历史，不伪造旧provider从未变化。REVISION、overlay、原生实体、官方/当前成员资格、旧历史证明均未改。

revision中的host摘要是被签定的审计记录，并非新增的host文件运行期固定pin；原host执行指纹覆盖保留。没有通过删除或跳过proof来获得准入。

## 有界验证

单Godot、2 CPUs、90秒、5ms采样、384MiB RSS提前停止（预留512MiB以内余量）、640MiB系统余量、2GiB地址空间。所有实际进程最大RSS低于512MiB。峰值使用os.wait4读取确切子PID，不使用累计子进程最大值。

1. 原文oracle与真实候选叶：26检查、346条完整结果逐字一致。
   - oracle由原宿主的6函数和必要定义机械提取，不stub来源验证，也不加载原执行依赖。
   - 覆盖普通EXACT_EFFECTS、8个完整native配对来源、字段缺失/额外字段、关键词/效果/签名、配对缺失、原文修订、当前stock展示逆变换、数值及类型比较。
   - 两侧约63MiB RSS，退出0。
   - 这支持所迁移纯校验逻辑等价，不等于完整原宿主运行等价。
2. 真实候选stock入口：成功加载并对来源夹具执行admission_error和apply，活化艾泽里特/女沙皇两个普通来源的准入与标记通过，金色来源池标记保持false。峰值67392KiB（约65.8MiB），4.268秒。
   - 使用来源衍生的轻量catalog适配器，不是Game自然获取或完整Catalog。
3. 29项代理检查：实际抽出的常量别名和6个代理方法编译、调用结果一致。只是薄代理，不是完整宿主编译。
4. 4种畸形输入在oracle/候选产生同样的原有运行错误。它们不是新增的友好拒绝，不声称原有错误路径已经修复。
5. 独立复制资源分别篡改新stock、新叶、新revision、原native XML，原proof函数实际逐文件哈希，四种情况均按预期拒绝并返回空packet。
6. 所有23项当前固定pin与真实文件一致；旧21项仅stock一项替换，其他原pin逐项保持。旧source_evidence完整保留。

最初baseline_validation_1把原本会抛运行错误的supported整数/String放进正常矩阵，记录保留且不计通过。成功矩阵在新进程重新执行，畸形错误另行对照。

## 原完整入口未完成，不能算内存A/B通过

原stock真实加载探针在2.538秒、387188KiB RSS（约378.1MiB）收到SIGKILL，尚未到384MiB停止阈值。控制器记录process_exit，不是主动阈值或超时停止；没有完成报告。原因缺少内核/cgroup证据，不能断言OOM或固定限额。

没有重试原完整入口、提高阈值或盲目加载完整Game。该失败是未完成的资源探针，不等于原基线功能失败。候选小入口的65.8MiB不能与这个未完成峰值计算正式降幅。

静态stock入口闭包838→9脚本；完整host闭包837→838，完整catalog闭包1539→1540。它解决入口耦合而不删执行宿主，不保证最终完整图驻留下降。

## 未验证范围

完整原host与新版host整体编译、真实事件调用接线、施法触发及效果执行、完整catalog/来源证据链、Game、存档、回放、UI及全局内存收益均未验收。尤其薄代理不是完整host，oracle不是原host。

## 空间、完整性与恢复

未复制大工程。初始测试sandbox只复制9个静态脚本和必要证据，约0.30MB；data/assets只读沿用输入，失败测试另用小型私有副本。

BASE_MAP.json与SOURCE_MAP.json列出完整前后清单（27893→27895），CHANGES.json提供前后哈希，REMOVALS.json为空；唯一有效运行增量在delta/。SOURCE.patch、原文oracle、夹具来源说明、所有成功/失败日志与采样均保留。

全部27893个输入文件重新核验未变；32个测试输入文件与测试前快照一致；5个增量文件在新位置完成实际恢复及哈希核验。原基线和所有备份未删除。

restore_to_new.py只向不存在的新目录恢复，先核验完整输入，再复制delta并逐文件核验；不修改/删除基线。完整恢复约需1,548,719,055字节加目录与运行缓存余量，本轮未执行此完整复制。tamper_*_runtime仅为失败证据，不得作为运行增量应用。


## 上传范围澄清

原归档保持封存不变。文中“最后完整游戏验收”不得解释成全部机制或完整回归均通过，a71d3e4ea64dc52264a3f789a48ddae2e4a043cd仅保留此前限定范围验收。本候选只部分验证，旧入口SIGKILL，完整Game未验收。此次备份后采用流式逐文件重建字节核验，读取全部目标字节，不另写完整运行目录。历史基线复用并重哈希，全部旧备份保留。
