# 第十批：最终来源修正助手的历史原件候选

状态：ONE_EXACT_HISTORICAL_ORIGINAL_CANDIDATE_WITH_ASSERTIONS_REQUIRED。此处“原件”指历史候选目录中现存的完整文件，不表示曾实际安装或已证实最新版。

本批从第九批完整候选另复制新树，没有硬链接。仅新增 tools/final_source_overrides.py，3,984字节，SHA256 f05bd591950b6267db19458936fa29fe3cbbd70a8dff745160aa8cf971a2a810。来源是 research/sparring_partner_native_recovery/candidates/tools/final_source_overrides.py，未重写代码。

## 来源与版本边界

输入固定备份提交：3dd4db504ab9eba4c28088c1a72a6bbc3ed0e136。

两份完整历史文件、两份manifest、两份patch均与实际输入SOURCE_MAP和原始ZIP逐字相符。ZIP本轮重新计算完整SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65。

精确补丁链：149ac6e247dda2d72a2614523f2666f39cc60e0a8707f79d9fa3fc3c18250393 → e40eb11c09569178e741ae2fe131496a69fa261230b5cc3f29febcb64dab5780 → f05bd591950b6267db19458936fa29fe3cbbd70a8dff745160aa8cf971a2a810。两个patch各4个hunk，按原行号、上下文和行数正反向闭合，零偏移、零fuzz。最早前像是反向重建值，未找到独立完整原件；本次选中的后一版本则是ZIP里已有的完整历史原件，不是推导的postimage。

前一完整版本只覆盖17项且pin旧清单；后一版是本次定位的两份完整副本中唯一匹配当前19项及清单SHA者。不能由图的末端、时间或文件大小推定最新版。

**原Python助手的保护使用assert。必须开启Python断言，禁止使用-O、-OO或非零PYTHONOPTIMIZE。** 本包复现/校验入口用不可被-O删除的显式条件拦截优化模式。若未来调用不能保证断言开启，应暂缓执行，而不能把本批文件恢复视为完整编译器放行。未修改历史原件来补写新实现。

## 限定实际验证

当前清单 data/final_bg_source_overrides.json SHA256为1f61cc86718d6e0fcba3091b9213823c8c25804cb6a2849e66946a7cafb63c27。Python与当前GD均pin此文件及19个ID；Python直接依赖仅标准库与此清单。未执行原件的main分支、完整离线编译器、Game或Catalog。

从固定SHA的30,883,879字节catalog_raw.json流式读取3,879行，仅保存19条实际来源夹具，解析缓冲峰值74,479字符。另一遍独立审查复核这19条及预期输出。固定原始修正字段为27个字符串、8个字符串列表和2个整数星级。

共79种场景：19项正常修正；逐项缺失、种类改变、37个原始字段漂移；重复应用；无关行保留；清单追加换行破坏pin。Python每轮252项检查，两个完整轮次通过。GD只加载实际来源修正、Battlecry来源及pool_identity三个脚本，每态249项检查；缺失、恢复、追加注释三态，各重复一次，再在全新portable目录重现，总计12次Godot正常退出。Python峰值12,612 KiB，Godot峰值65,872 KiB。

测试确认限定输入下两边结果与接受/拒绝一致，失败前不部分修改，supported/effects保持不变。这里只证明已列举的解析后JSON场景，不证明任意畸形输入一致，也不声称两门语言的运行时数值类型完全相同。

所有测试串行，Godot RSS停止阈值192 MiB、地址空间上限2 GiB、45秒超时，启动前至少1 GiB可用内存，低于640 MiB余量则停止；Python夹具测试地址空间上限128 MiB。

Battlecry的8项固定proof及实际proof_error在三态均通过。新增助手不属于这些固定pin，Battlecry工具本身仍缺失。追加注释仅改变该助手的指纹条目，不会被此proof拒绝；未计算完整execution_fingerprint，不说明旧存档兼容，也不是新增玩法准入修复。

两次测试脚本问题均留证：首次Python用重复完整夹具序列化触及128 MiB限制，改为保存一次原始行及稀疏变更描述后成功，未提高限制或修改候选；独立补丁核验首次错误假定两份manifest都为数组，按原始一份对象files、一份数组修正读取后通过。首次未完成的运行不计为完整成功。

## 其余版本继续暂缓

原16项暂缓保留。本轮静态筛查12项有单副本的B类工具：10项忽略传入card本体且采用普通相等，spellteach_murloc_native虽检查card仍采用普通相等；Old Murk-Eye严格Python类型比较会拒绝等值float，而当前GD允许有限int/float等值。历史调用从raw经共享mutators/overrides构建输入，不能保证全链类型，因此不强行恢复。Old Murk-Eye输出删除三个字段符合历史emit契约，但这不消除输入准入差异。上述12项未执行动态验收。

Kerrigan只定位到manifest元数据，未找到可验证的完整原件或创建/修改补丁，不据此编造源码。

完整build_effect_catalog定位179份副本、98个不同SHA、95条manifest边，其中92条获精确补丁验证，另有2条精确跨分量连接。合并仍有4个分量、分支及pending/冲突记录，不能选定唯一当前兼容版本。输入树各版本静态缺772–856个直接内部导入；本次加入助手后仍缺771–855个，联合856、共同771。此统计扫描全部AST嵌套层，未证明每个导入必执行、传递闭包或内容兼容，且与367项原始引用路径范围不同。没有运行完整编译器。

static_evidence保留来源/哈希、全部版本路径、manifest和补丁核验、模块清单及版本图的事实投影；完整原审查报告在本地原样保留，其SHA亦记录。完整图审查的重做需要上游完整树，不能只靠此小包。

## 实际树与缺口

输入树逐文件实际重哈希：27,915文件、1,549,275,367字节，未改变。
候选逐文件实际重哈希：27,916文件、1,549,279,351字节。新增1，修改0，删除0。

输入SOURCE_MAP：d4d9c436df5aa851412f8a2457a7e11128bc66d6f4313a46b42679d14f51e29b。
候选SOURCE_MAP：dc3968e2c02fc646100ad1a1745fe885414ad679250363c732f4ae4fae2920cb。
候选实际整树字节流SHA256：f159ef6f456e8cade1b5d8eebc84e8833b95659af2a5ef6f7bd5911d3e95074b。

原367项引用路径范围，在候选树中缺失350→349，累计有18条恢复；旧第九批仍保持350。余55项历史A、17项B、277项C；C是原限定调查未定位重建材料，不是本轮重新穷尽所有远端历史。缺失路径统计不是全部项目缺口，更不是玩法覆盖率。

完整Game、Catalog、编译器、真实UI、全部对局及卡牌/法术/饰品覆盖率、旧存档、原中断工作树均未验收。第六批四份原核验文件仍未找回。所有此前树、证据、备份原样保留。

## 复现与封存

先按FILE_MANIFEST.json核验每个文件字节数及SHA256。python verify_candidate.py检查限定证据、delta、映射和已记录测试；python verify_chain.py重做自包含精确历史链校验。

python replay_to_new.py /不存在的新目录：重做19条Python及六次Godot限定试验，已实际运行。需要Python 3和/usr/local/bin/godot；本轮Godot为4.6.3。

python restore_to_new.py /严格匹配BASE_MAP的完整输入树 /不存在的新树：拒绝不匹配输入、已有目标和源内目标，独立复制后完整重哈希。该交付入口未额外重跑；本轮实际完整新树复制与核验已完成。

此包为单文件增量候选和限定证据，不是独立完整游戏备份。白名单仅包括相关代码、夹具、审查结果和运行记录，排除HOME、字体/编辑器缓存、.godot、__pycache__、私聊、凭据及无关文件；测试生成目录留在本地，不整目录打包。
