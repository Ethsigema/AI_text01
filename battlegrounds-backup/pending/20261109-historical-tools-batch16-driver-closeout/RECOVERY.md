# 证据恢复

1. 下载本目录MANIFEST.json、原.tar.xz和verify_closeout.py，核对SHA256SUMS.txt。原包必须是61,876字节、SHA256 58518fbc71c1af43e609e2f4b1ab3fd42dcb96491d156864dceec2ed3d799990。
2. python3 -B verify_closeout.py --local 下载目录。核验单一完整XZ流、安全文件路径、34项外部白名单、33项内部清单及全部文件哈希，不执行封存的调查脚本或编译器。
3. 远程复核：python3 -B verify_closeout.py --commit 公布的固定提交 --folder battlegrounds-backup/pending/20261109-historical-tools-batch16-driver-closeout --manifest-sha256 公布清单哈希 --out 不存在的新目录。
4. 脚本真实下载本包并将34项证据恢复到新的restored_evidence目录，再逐项回读；同时重下固定XML和第14批源码归档，逐成员核验，并回读固定XML核验报告。收口记录中的选定源码pin须与第14批SOURCE_MAP一致。
5. 证据恢复不是运行树恢复，不把restored_evidence覆盖进游戏。本次不再创建27,921文件游戏候选副本，不重跑历史链、驱动调查、完整编译器、游戏或存档测试。较早历史链和XML恢复回执如实标为复用。

如需重做原调查，必须另取原报告规定的历史归档、整本源码、补丁和索引。本包不是它们的完整副本；唯一当前驱动仍未知，不能按大小、文件名或图终点盲选版本。保留全部旧备份。
