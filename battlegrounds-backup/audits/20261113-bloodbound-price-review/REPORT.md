# 血缚耳环获取价格复核（2026-11-13）

结论：未发现小型饰品价格遗漏，无需修正游戏源码。官方 37.0.2 明确小型由 1 调整为 2 金币：https://hearthstone.blizzard.com/en-us/news/24307311 。历史 catalog_raw 保留 1 是原始证据，不是运行时最终价格；现有专用 overlay 的有效 cost 为 2。

固定核查版本：32a8b33abe2bfb980c5ec890e7950f6b5a9f1346。最新完整恢复目录在本执行环境不可见，所以不是测试当前完整工程。另行下载该固定版本 SOURCE_MAP.json.gz，其解压 SHA256 与 RECOVERY.md 的 a20b935157ef28e0fd8e2953e4e121824ba2fc665c0df851554892ca6cd7e9ef 一致。9 个局部输入与该清单逐字节哈希匹配；旧 core/catalog.gd 不同，未复制或声称其为当前版本。具体见 SOURCE_COMPARISON.json。

从匹配的输入复制至独立目录，在 Godot 4.6.3 实际调用 acquisition overlay，10 项断言通过：有效价格2、历史原始值1、真实apply结果2、旧价格被拒、变更前像被拒、大型输入价格6且不被小型overlay改变等。大型6金币由固定版本的原生XML COST=6与独立卡行交叉核查；网页搜索的独立wiki也显示6，但官方37.0.2仅列小型改价，未建立大型当前全量状态或完整效果验收。

这不是完整 catalog 初始化、金币扣费界面或施法效果验收，也不是恢复整链核验。首次测试因 XDG_DATA_HOME 未指定导致不可写日志目录崩溃；设置独立外部数据/配置/缓存后重试通过。保留两份原始日志，未修改冻结工程、旧备份或未知未上传成果。

## 复现
在按匹配清单准备的独立测试树（core、data、research同项目相对路径）中放置 check.gd 与 project.godot，设置 XDG_DATA_HOME、XDG_CONFIG_HOME、XDG_CACHE_HOME 指向可写外部目录，执行 godot --headless --path TREE --script res://check.gd。本审查包仅含新增测试与审查材料，不是游戏增量或完整备份。实际依赖清单在 SOURCE_COMPARISON.json；core/catalog.gd 的不匹配项不参与测试。
