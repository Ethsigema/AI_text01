# 两项来源叶优化的组合诊断（只读）

输入为1288c092b970edaa6a75c2be89809354eed19405核验的组合候选，源码清单SHA256为9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111。本轮仅新增诊断资料，运行工程新增0、修改0、删除0；不改变原工程、已有备份或任何验收状态。

## 实际小探针

新建稀疏测试目录，只复制14个现有脚本及必要证据，共366,179 bytes。每个文件均匹配已核验清单；data/assets只读沿用已有输入。没有复制完整工程。

四个新Godot进程依次运行，192MiB RSS提前停止、640MiB系统余量、45秒、5ms采样、2 CPUs；无并行Godot。峰值由wait4取得确切子进程计量：

- Harbinger独立入口：65748KiB，0.679秒。
- Stock独立入口：67560KiB，3.036秒。
- Harbinger后Stock：68288KiB，5.570秒。
- Stock后Harbinger：67772KiB，5.665秒。

四次均退出0，合计47项检查通过。两种顺序下，各模块结果与独立运行相同；执行另一入口后重新读取，结果仍相同。原proof检查通过。同一路径重复load返回同一Script，两个入口共享实际Exact辅助Script，Stock与来源叶共享Scope Script。

这些事实仅覆盖本次轻入口、source-derived catalog适配器、来源检查和限定apply行为。它们不证明所有ResourceLoader/编译器中间对象的生命周期，也不证明真实全局游戏状态没有任何交互。

没有运行完整Catalog、Game、重型执行宿主、实际EOT/施法事件、存档、回放或UI。约66–67MiB的组合峰值不是完整项目内存，也不能与此前未完成的大进程峰值计算整体验收或降幅。

## 两项优化共同作用的静态结果

- Harbinger入口闭包：178→7脚本。
- Native stock入口闭包：优化前837脚本，Harbinger-only时838，组合后9。
- 两个轻入口合计只需14个脚本。
- 完整catalog：1538→1539→1540脚本。没有任何原脚本从完整图中消失，只增加两个共享叶。

因此，优化有效切断了轻入口对重型宿主的不必要耦合，但不删除最终仍要加载的宿主。最终驻留不保证下降，解析期间重叠峰是否降低仍未证明。

按源码声明顺序模拟首次触及依赖，新的大闭包会从其他入口重新出现：
- catalog第102行CurrentSpellStock：新增168脚本、5,696,781源码bytes，重新触及EndTurn。
- 第106行FleeingFugitiveStock：新增108脚本、2,156,664源码bytes。
- 第154行GoldenArrowSources：新增415脚本、10,089,279源码bytes，重新触及Mechanisms。
- 第793行EndTurnRepeats已经由其他入口触及；第795行SpellCastListeners仍直接引入宿主自身。
- 第850行Combat仍新增230脚本、3,577,933源码bytes。

上述是静态引用图和假定源码顺序，不是Godot真实编译/分配顺序，更不是RSS。完整逐项结果在GRAPH_COMPARISON.json。

## 下一步低内存路径与风险

优先只读设计EarthMother的两个纯辅助函数解耦：
current_spell_stock_acquisition.gd → earth_mother_sources.gd → end_turn_repeats.gd。
EarthMother仅使用EndTurn._same和_uid，两函数无外部模块依赖。可考虑原文迁移、原接口委托，但本轮没有实施。

不能直接替换成现有phase_undead_army_sources.same：
- EndTurn._same拒绝非有限数，现有轻same未检查finite，Infinity语义不同，包括嵌套结构。
- EndTurn注释写integer-valued，但实际代码接受相等的有限小数；不能顺手增加floor限制。
- _uid要求String、u前缀、长度≤20、整数格式、整数转回文本完全相同且值>0；不能用近似正则替换。

下一轮若做独立候选，应先覆盖嵌套结构、bool/int/float、有限小数、Infinity/NaN，以及UID零/负数/前导零/加号/空白/类型/长度/整数边界；再检查实际来源及活体眼睛边界、固定pin和实际消费的指纹路径。当前明文摘要检查未发现EarthMother/EndTurn pin级联，不等于穷举所有运行规则。

GoldenArrow还有一条候选来源校验耦合：
golden_arrow_sources.gd → prize_golden_effects.gd → minion_activate.gd → mechanism_effects.gd。
GoldenArrow调用_native_error，但其完整闭包与安全迁移范围尚未证明；本轮不扩展实现。

不要在当前资源条件下再次累计预载到Combat或完整catalog。此前进程可能在RSS软阈值以下被SIGKILL，原因仍未确认；软阈值不能保证存活，更不能因此提高上限。后续应保持独立小进程、有明确低成本预期的探针，完整验收必须另在资源稳定且可观测的环境完成，不能把分块通过拼成整体验收。

## 完整性和范围

41个复制输入及其原始引用在测试后按哈希复核，未变；避免重复读取整套约1.55GB工程。本轮没有新的运行源码增量，也未改变之前候选的部分验证状态。

RESULT.json、四次运行的脚本/日志/采样、TEST_INPUT_MAP.json和静态图均在本包。运行源文件仍由已核验的候选恢复链提供；此包是诊断档案，不是新运行检查点。


上传补充：本包只读诊断证据，不是新运行增量，不提升任何验收。真实下载后逐项核验归档及固定依赖，并重新检查41个诊断输入字节。本轮不重跑探针、全工程哈希或Game，不另建完整运行目录，不重下历史全链。
