# 碎地者真实指令链候选：增量恢复

这是真实源码增量，不是完整游戏或默认发布版。以2026-11-11已核验的第14批合并增量为基线，新增7个文件、修改80个文件、删除0个文件。保留原Game、Catalog、Combat、工厂和_buff，仅加入碎地者有限链及必要来源pin，并修复金色原生pool_blocker注释的严格来源兼容。

## 恢复顺序

1. 先取得已核验基线包及原始Release，按该包RECOVERY.md恢复干净基线目录：
   https://github.com/Ethsigema/AI_text01/tree/5143e8fb41bc8332ce4ba196144172167a74318c/battlegrounds-backup/consolidated/20261111-batch14-restored
2. 保存该基线包里的SOURCE_MAP.json.gz。其解压后的SHA256必须为7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7。
3. 下载本候选目录全部文件，校验SHA256SUMS.txt，然后执行：

    python3 restore_increment.py --base-tree /路径/干净基线工程 --base-map /路径/基线包/SOURCE_MAP.json.gz --destination /路径/不存在的碎地者候选目录 --report /路径/不存在的报告.json

工具先逐文件核验基线，再从87份增量文件与未变基线重建新目录，随后重新读取全部目标文件核验。它不覆盖原基线，不执行游戏，也不运行证据包中的代码。成功状态为PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED。

## 已实际验证及边界

Godot 4.6.3完整Game和Catalog加载、受限房间开局、原工厂/入手、公开apply_command及原_buff实际执行通过。普通碎地者实际从6/4到7/5；随后连续不同卡打出，普通9/7、金色14/10。越域纳迦拒绝且手牌、两源属性不变。16项严格来源正反例通过。原失败日志全部保留在evidence.tar.xz，EVIDENCE_MANIFEST.json列出实际成员哈希。

候选仍仅支持原艾德温及明确的有限随从上下文，不适合通用默认池。活动工程保持已验证原基线，未推广本候选。法术计数为0，未验证3/6施法阈值增长、随机商店获取、三连/金色获取、同一命令重发、全组合、完整对局或旧存档。默认房间曾因已有未支持七级/衍生入池条目拒绝开局，不能声称该问题已经修复。

本增量及其基线不能保证原中断前未上传的修改已找回。旧备份保持不变，不强推。完整报告见REPORT.md，远端恢复核验结果另附。
