# 2026-11-11 已知候选的合并增量恢复

本次实际从 GitHub 重新下载原始 Release 与固定历史依赖，在新目录重建 160 层源码增量，并逐文件验证最终 27,920 个文件、1,549,340,406 字节。原中断工作目录没有找到，因此本包只代表当前可重建的第 14 批候选，不保证涵盖当时未上传的修改。

这是原始基包上的合并增量，不是独立全量包，也不是完成游戏。无需再逐层叠加 160 个旧包，但仍必须取得下列原始 ZIP。所有旧备份保持不变。

## 两项必需输入

1. 原始 ZIP：
   https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip
   大小 324,041,102 字节，SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65
2. 本目录中的 restore.py、MANIFEST.json、SOURCE_MAP.json.gz、BASE_MEMBERS.json.gz，以及全部 13 个 payload.tar.xz.part0000 至 part0012。

校验 SHA256SUMS.txt 后，在 Python 3.12 或更新版本运行：

    python3 restore.py --base-zip /路径/原始ZIP.zip --destination /路径/不存在的新工程目录 --report /路径/不存在的核验报告.json

脚本拒绝覆盖已有目录，校验原始 ZIP、全部分片、压缩包、文件清单和每个文件。完成写入后再次从磁盘读取每个文件，核对路径集、大小和 SHA256。成功报告为 PASS_ACTUAL_DISK_RESTORE_EVERY_FILE_REHASHED。不要只解包 payload 当完整工程。

Godot 工程入口在恢复目录的 project.godot。应使用 Godot 4.6.3。首次导入可能重建缓存，缓存不包含在本次源码清单中。

## 范围及限制

- 21,099 个目标文件从原始 ZIP 的匹配字节恢复，6,821 个目标文件从合并增量恢复；增量未压缩字节共 56,840,640。
- CHANGES_FROM_ORIGINAL.json 明确列出相对原始游戏目录的新增、修改和删除。最终清单决定文件集，不会恢复已删除文件。
- 最新 11 月 10 日审查包单独保留在原恢复分支的 pending 目录，未安装进本候选。PENDING_NOV10_PRESERVED.json 记录本次重新下载并逐成员核对的包。
- 仍有 345 个历史工具引用缺口，两份来源约定文件和四份历史证据未闭合。完整编译、完整游戏、界面及旧存档没有因备份成功而验收。
- 此次没有新增已验收随从、酒馆法术或饰品，不能用文件数、测试断言数换算完成率。
- 旧失败记录与旧备份不删除、不覆盖、不强推。原始基包的上游素材许可状态未因本次恢复而改变。

实际远端回读与新目录恢复结果会另附 REMOTE_RESTORE_VERIFIED.json。只有本地报告时不能声称远端核验完成。
