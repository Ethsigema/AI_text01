# 恢复 Zesty 严格守卫累计审查包

从固定 GitHub 提交下载 MANIFEST.json、SHA256SUMS.txt、verify_package.py 和 .part000 至 .part024 共25片。按编号拼接应为 6,052,024 字节，SHA256 aa9a30adf5af12e94e0e74b0b8062d1eb7ee667cfb7d1d1d5937d2beb035537c。

可信 Python 3 环境可执行 python3 verify_package.py <下载目录> --write-archive --report verification.json。脚本读取分片，在内存核验436项成员、内外清单、两个 attempt 各204项交付白名单及报告边界，再写不存在的新归档。不覆盖已有归档、不联网、不下载依赖、不执行包内代码或重跑测试。

仅解包到新独立目录审查，不覆盖游戏树、不应用补丁或安装。首次 FAILED 与后次1580项局部 PASS 分别保留。原始来源库存清单不等于实际交付成员，不能按引用自动补下载。本包不是完整游戏树，不能凭这次备份保证整链可恢复。

候选未安装，完整 Game/Catalog/实际入手/等级4与存档仍未验收。旧依赖未复核，取消的第14批依赖下载不属于本任务。
