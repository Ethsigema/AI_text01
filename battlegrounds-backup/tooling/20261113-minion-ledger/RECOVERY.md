# 随从逐卡台账工具增量交接

本包仅新增台账生成工具、工具单测及其输出，不修改游戏规则或旧备份。
基于已发布源码 32a8b33abe2bfb980c5ec890e7950f6b5a9f1346：
https://github.com/Ethsigema/AI_text01/blob/0632e9bf414b669a7f860cd9de4a640a0e575425/battlegrounds-backup/pending/20261112-lava-carried-sale/RECOVERY.md

先按上面的固定恢复链说明恢复游戏，再将 overlay/ 的内容添加到工程根目录。
若目标中存在同名文件，先比较内容，禁止覆盖未核验或唯一成果。
本增量不包含游戏基包，不是独立完整游戏备份，也未捕获中断线程的未知未上传文件。

## 执行与验证

Python 3 标准库，无外部依赖。游戏本身恢复要求 Godot 4.6.3，本工具未运行 Godot。

    python -m unittest discover -s tests/ledger -v
    python tools/build_minion_acceptance_ledger.py --project . --source-revision <精确源码版本> --output <新的不存在的输出目录>

输出拒绝覆盖既有目录。输入的 2182 个数据/代码/测试文件均记录大小与 SHA256。
全部 247 行的完成状态为待验收，完整完成数及最新版总数为 null，而不是 0。
数据映射不是运行时最终状态：core/catalog.gd 存在覆盖逻辑，本工具不模拟加载执行。
因此 18 个普通 ID 未在静态 catalog.json 映射中出现，绝不等于 18 个完全没实现。
代码/测试里的精确 ID 命中只用于导航，不能证明处理器被调用、执行过测试或测试通过。
未扫描所有 research 历史证据包；后续逐卡核验时应保留来源版本及测试适用范围。

## 本次成果

- 247 种候选，普通及金色各一列；排除畸变怪，含 20 种娜迦。
- 229 种普通和 229 种金色有静态 supported 标记，绝不据此计完成。
- 8 项 Python 工具单元测试通过，不代表 8 项游戏玩法验收。
- 本次未做游戏功能修复，也未认证任何随从完整完成。
- 原恢复树未修改，所有旧成果保留。本目录发布台账工具新增文件，未覆盖任何旧备份；后续完整工程备份需将 overlay 中的新增文件纳入全量清单。

## 本次远端工具包

文件：`minion_ledger_20261113_tooling_increment.zip`，268553 字节。
SHA256：`bc94f25a2deeb2736fa541f88ffa3ea5cd4afe9dd3d7beeba50756b704a3a2c2`。
固定依赖链接与 SHA256 详见 DEPENDENCIES.json。包内的“尚未发布”是打包时历史状态，不覆盖本目录发布回执。
