# 极紫外升腾者成长：当前源码定向验证

## 本期实际开发

基于已发布船难海盗增量的28,011文件恢复工程，在独立目录实现普通与金色紫外“使用其他元素后提升战斗开始增益”的缺失路径。此前直接返回 ultraviolet_growth_increment_unverified；现由原Game真实使用手牌后的监听派发成长，普通每次+4/+4、金色每次+8/+8。战斗仍走原Combat增益程序，招募阶段不改本体属性。

新增成长实体状态、真实上下文/重复派发保护、数值与JSON表示校验；未知普通/混合三连继承统一hold，元素磁力在任何消耗前hold，合法动作过滤同步；对达到上限的多个来源按自身状态顺序执行，不误扫前一来源的已完成状态。

5个主要逻辑文件变动：ultraviolet_host.gd、recruit_events.gd、game.gd、surprise_elemental_host.gd、triple_stat_rules.gd。其余源码差异主要是依赖完整性哈希随同一Game文件改动更新，以及普通/金色覆盖状态元数据；这些不是新增玩法数量。

## 规则证据

37.0.2官方补丁确证普通8/8和基础4/4：https://hs.blizzard.cn/news/24307311/index.html。
成长步长、自身排除和金色倍率根据AutoTavern固定提交1c2086a997afde46d68c6c5992cab194ddcfce88的公开实现，最小证据及blob SHA见evidence/rule_evidence.json。它是第三方模拟器代码证据，不是暴雪客户端/实机验收。没有据此声称最新完整卡池或整卡已完成。

## 最终源码实际执行

Godot4.6.3，Linuxheadless，最终runtime SHA清单见evidence/final_runtime_manifest.json。

- 紫外定向测试：59项断言通过，Godot进程退出码0。
- 同一最终源码上的船难海盗回归：73项断言通过，Godot进程退出码0。
- 紫外测试结束时Godot输出ObjectDB实例泄漏警告和“182 resources still in use”退出清理错误信息；断言均通过，但不能称无告警或全面验收。本次未处理独立Combat实例的资源释放问题。

真实Game测试包括普通/金色各两次连续元素手牌使用，增益计算12/12或24/24；实际Combat.resolve输出对应战斗增益事件，仅作用于两个其他元素，未给非元素或本体加成，也未回写招募本体。另验证非元素不成长、第二紫外自身不触发但原来源触发、沉默不触发、未授权内部回调只读拒绝、复制UID拒绝、JSON整数字面表示、普通和混合三连只读hold、元素磁力前置hold，以及双来源接近计数上限同时完成最后一次成长。

## Fixture及边界

初始来源由原工厂建立后直接放board、手牌通过原_add_hand加入、金币设为10，均为明确fixture。磁力负例用原生元素作结构输入，验证前置hold，未证明某张真实元素磁力牌的完整流程。上限测试人工设置1,000,000次前一计数及前一sequence，是边界fixture，不是自然执行百万次。JSON测试只证明实体数值表示可读，不是完整存档读写验收。

未验收自然购买、完整三连继承、复制/变金/其他变形、完整存档、全英雄/饰品交叉域、默认全池、GUI或完整对局。界面成长提示未更新。计数仍为“随从：已完成待核实／总计待核实”，247只为候选，完整随从计数本次不增加。法术与饰品未新增实现，数量与百分比同样待核实。

## 尝试记录

first_candidate_21_checks：早期真实玩法21项通过，非最终源码；second_candidate_test_event_key_failure：Combat日志键event误查type导致测试假失败；pre_review_49_checks：早期49项通过，后续审查加固后不能冒充最终验收；review_fixture_sequence_failure：边界fixture误把上一序号设为下一命令序号，被重复保护正确拒绝。最终日志final_59_checks与final_shipwrecked_regression_73才对应当前源码。

此报告不是上传或远端整链恢复成功回执。旧备份未删除；未知中断线程未上传成果未捕获。
