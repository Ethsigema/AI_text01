# 第16批聚合 XML 原件隔离候选备份

这是按用户指示保存到 Ethsigema/AI_text01 的恢复资料，不是完整游戏验收。原归档逐字节不变，SHA256 为 3d37a9d1a0ee2d61939e88f8ced995622ca22fd84ba7f9dabe8c4f2df6bafa7d，共 1,804,348 字节、49 个文件。为保持原证据，没有重写其中的历史报告。

唯一拟新增的游戏根相对路径是 evidence/portable_legacy/CardDefs.Bacon_latest.xml。原件来自 HearthSim/hsdata 固定提交 27fbd2323aec20cab1c6ecc7d5f55cf12729f956，版本 36.6.3.253932，15,824,602 字节，SHA256 c385e3d67bfc2c52408059fbb0399b41164c8d1b78d3dd1619a6fb1882116690。不是今天的 latest，也不覆盖其他版本。

源码基线固定为第14批 3b0061fcf3a55850eeda689818f7cc1700700750。第15批 758e26e1ecefaebfbcc7166912da412eb7197994 是只读调查证据，不是新源码基线。保留全部旧备份，不强推。

## 当前范围

- 原包只含单文件覆盖层和调查证据，没有完整运行树。现存运行树未安装该文件。发布后恢复核验只在新的独立验证目录进行，不晋升、覆盖或启用现存游戏。
- 完整编译驱动、两份 SOURCE_CONTRACT.md、原范围内345项运行时工具引用缺口仍未解决。另一路径 research/supplemental/CardDefs.Bacon_latest.xml 历史缓存也未恢复。
- 未执行编译驱动、历史生成器、Game、Catalog、Godot、游戏或存档测试。执行指纹未重算，完整游戏与旧存档兼容性未验收。
- XML 完整解析及5份原生实体字节对照只证明输入身份，不证明游戏行为正确。历史报告和封存测试不是本次重跑。

## 原证据与许可

包内 publication_performed=false、未远端发布等措辞是封包前的历史状态；最新发布及核验状态以本目录 PUBLICATION_VERIFIED.md 和 REMOTE_RESTORE_VERIFIED.json 为准。原有“未获得原件”的有界调查已由包内补充证据更新，但原文保留。

上游固定提交无明确 LICENSE/COPYING，再分发许可未确认；其 README 说明这是从 Hearthstone 客户端提取的数据。公开下载不等于获授再分发权，也不能套用其他代码许可。本次按用户授权保存在指定仓库，仍不表示第三方数据权利已确认。

仅按49项原文件清单保存，排除缓存、私聊、凭据和环境目录。必要技术文件名及排除记录不代表上传了对应数据。恢复与验证方法见 RECOVERY.md。
