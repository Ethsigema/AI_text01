# 第九批Trip Vouchers补丁重建候选恢复说明

本次只追加单文件候选增量，不是独立完整游戏，不替换旧基线或任何旧备份。

1. 下载固定提交目录中的MANIFEST.json及五个.part000至.part004分片。逐项核对大小和SHA256后按数字顺序连接为historical_tools_batch9_trip_candidate_20261109.tar.xz。应为1,117,320字节，SHA256为1153a89cfbc84c89310d83627d2f2c764ad45665dbe11ed12dcd3218c6ac6b0d。
2. 在全新目录解包，按外部清单校验178个成员，再按内部FILE_MANIFEST.json校验177个被列入清单的文件。差额是清单自身。
3. python verify_candidate.py检查只读证据。python reconstruct_to_new.py /不存在的新目录从历史原件和补丁独立重建tools/trip_vouchers_patterns.py，58,891字节。
4. 完整恢复需精确匹配BASE_MAP.json的27,914文件第八批上游树。运行python restore_to_new.py /上游树 /不存在的新候选树；它拒绝不匹配输入或覆盖已有目录。

固定直接依赖：
https://github.com/Ethsigema/AI_text01/tree/24034fe9f1c068880f0792b88a434845d3df78d6/battlegrounds-backup/pending/20261109-historical-tools-batch8-patch-candidate

原始历史全链恢复证据：
https://github.com/Ethsigema/AI_text01/tree/8e168c0c67b185a885c4e9251f728e3bde140cab/battlegrounds-backup/pending/20261109-night-fresh-chain

候选SOURCE_MAP SHA256为d4d9c436df5aa851412f8a2457a7e11128bc66d6f4313a46b42679d14f51e29b，对应27,915文件、1,549,275,367字节。

本工具是历史原件加补丁重建，未找到独立安装后原件，最新版未证实。350个原引用范围缺口仍在，完整游戏及旧存档未验收。本次备份验证不运行完整游戏，不把封存测试报告当成本轮新运行。历史链复用与是否建立完整候选树，见随后追加的核验凭证。
