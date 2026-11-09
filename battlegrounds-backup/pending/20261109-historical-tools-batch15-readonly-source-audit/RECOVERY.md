# 证据恢复与复核

1. 从已公布的固定提交下载 MANIFEST.json 和其中按顺序列出的全部 .part 分片。逐个核对大小、SHA256，连接成 MANIFEST.json 指定的 .tar.xz，再核对整个归档 SHA256。
2. 使用随包 verify_evidence_backup.py：python3 -B verify_evidence_backup.py --local 下载目录。它验证分片、单一完整 XZ 流、安全普通文件成员、完整成员清单与白名单、原130项证据和源映射连续性，不执行历史生成器或游戏代码。
3. 需要重新下载验证时：python3 -B verify_evidence_backup.py --commit 固定提交 --folder battlegrounds-backup/pending/20261109-historical-tools-batch15-readonly-source-audit --manifest-sha256 已公布清单哈希 --out 不存在的新目录。它还实际下载第14批以及第14批清单中固定的第13批依赖，逐项核对两个归档与源映射衔接。要求网络可访问 GitHub；失败不代表已验证。
4. evidence/ 内路径保持原工作区相对布局。原始证据脚本的工作目录、内存上限和输入路径仍照其原始定义；仅核验证据包不需执行这些脚本。要重做所有历史搜索，还必须取得它们记录的历史原始归档并按哈希恢复到指定路径，本包不重复打包那些归档，也不声称搜索能脱离这些依赖独立复跑。
5. 游戏候选恢复从 DEPENDENCIES.json 固定的第14批备份及其完整依赖链按各批 RECOVERY.md 操作，恢复到新目录。不得把本证据包覆盖到游戏工程，或删除旧版本。SOURCE_MAP.json 是27,920个文件的完整映射，不等于包中包含这27,920个文件。

两份合同未找回、345项引用缺口、完整游戏和旧存档未验收的限制继续保留。当前封存的46项解析器控制、13项host控制及历史测试记录不等于本次重跑或游戏验收。本次新跑的仅为清单/归档/实际文件字节校验。
