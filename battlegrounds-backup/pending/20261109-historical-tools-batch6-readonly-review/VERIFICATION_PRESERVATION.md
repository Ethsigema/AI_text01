# 第6批只读审查：核验回执保全，发布材料未齐

有效包已完整备份于提交8097e8aec613f3d2c606a299f2cb7c505cff16ab。SHA256：297778bcc5e851bb3e3a0f306be05e7cd7e96e632871ed2e46a4d5b11f658e8d。

[原归档与恢复说明](https://github.com/Ethsigema/AI_text01/blob/8097e8aec613f3d2c606a299f2cb7c505cff16ab/battlegrounds-backup/pending/20261109-historical-tools-batch6-readonly-review/RECOVERY.md)

## 中断前已实际完成

2026-11-09 09:08:15 UTC，独立核验正常退出0。6片真实远端下载，整包173成员、内部172项清单一致。固定Devourer依赖的137成员重新哈希通过，SOURCE_MAP与本包BASE_MAP逐字节一致。固定输入元数据从远端重新读取。

126个唯一嵌入源码文件共756,811字节与输入映射一致；109个探针输入中106个是原源码，3个为明确隔离夹具。64项现有proof pin、五份历史工具105,845字节及封存依赖边界报告已交叉核对。

[原成功回执](https://github.com/Ethsigema/AI_text01/blob/170777528947389f76e04c04eb572be4bcd0b894/battlegrounds-backup/pending/20261109-historical-tools-batch6-readonly-review/BATCH6_REVIEW_REMOTE_VERIFICATION.json)
回执SHA256：03ba2e85367764f7faf9750f23a789cfa86565c1c494e2ed50c3e5a7db12d3ab。

源码变更0，五项暂缓，353条原范围引用缺口不变。没有重跑游戏、存档、候选Python或Godot，没有重新下载/重放全链，没有全树重新哈希或创建完整工程。历史版本及完整游戏/存档未验收。

## 环境中断与保全范围

发布验证文件时执行环境断连。重连后同一云电脑的原工作目录只剩只读配置目录，工程及本地输出不在；随后再次断连，原因未知。本任务没有删除文件，也未将空目录当作原基线。

断连前确已创建GitHub blob的8份原始证据已从远端取回，原字节数及Git对象SHA全部精确相同，再原样追加提交170777528947389f76e04c04eb572be4bcd0b894。包括成功回执、进程记录、下载来源、嵌入源码逐项结果、输入元数据。成功回执并非凭记忆重写。

8份原始证据与新增ENVIRONMENT_INTERRUPTION说明，共9文件，均已从固定提交完整回读，内容与原blob完全一致。见PRESERVATION_REMOTE_READBACK.json。

另4份原计划材料未上传成功，Git blob查询404，当前未取回：RECOVERY_VERIFIED.md、VERIFICATION_SHA256SUMS.txt、VERIFY.log、verify_batch6_review.py。不声称这些文件已恢复，不伪造缺失日志或独立核验脚本。因此原计划的完整验证材料尚未发布齐全。

本说明和PRESERVATION_REMOTE_READBACK是环境中断后新写的说明及真实远端回读记录，不是缺失文件的替代原件，也不代表在新环境重新跑过核验。

## 仍可使用

原归档、完整成员清单、恢复说明和原研究复现脚本已在固定归档提交，仍可下载。该包仅作审查证据，不应用到游戏运行树。游戏恢复继续沿用固定Devourer依赖链。

全部既有远端备份保留，提交仅追加，不强推。原本地文件当前不可见的事实不改写为已恢复完整工程。
