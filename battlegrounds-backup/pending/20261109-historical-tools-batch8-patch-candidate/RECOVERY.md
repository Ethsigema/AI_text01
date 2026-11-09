# 第八批补丁重建候选恢复说明

此目录只追加一个两文件候选增量，不是独立完整游戏，不替换旧基线或任何旧备份。

1. 下载同一个固定提交目录中的MANIFEST.json和六个.part000至.part005分片。逐项核对大小和SHA256后按数字顺序连接为historical_tools_batch8_patch_candidate_20261109.tar.xz。应为1,294,952字节，SHA256为a0e9d546f812b08d015a0279e83223a6cee6953313129c02ad4004dfb1342092。
2. 在新目录解包，先按外部清单核对234个成员，再按包内FILE_MANIFEST.json核对233个被列入清单的文件。差额是清单自身。
3. 运行python verify_candidate.py只读检查证据；运行python reconstruct_to_new.py /不存在的新目录，可从历史原件和补丁重新生成两个delta文件。
4. 完整候选目录需要精确匹配BASE_MAP.json的27,912文件上游源码树。使用下方固定依赖及其历史恢复链准备上游树，再运行python restore_to_new.py /上游树 /不存在的新候选树。它拒绝不匹配输入或覆盖已有目录。两项只增加tools/aggramar_patterns.py和tools/mystery_cube_patterns.py，共84,192字节。

固定源码基线：
https://github.com/Ethsigema/AI_text01/tree/3d41c7f71bdda146ed37930c7591b419b53e36a6/battlegrounds-backup/pending/20261109-devourer-tool-historical-candidate

固定上游全链恢复证据及入口：
https://github.com/Ethsigema/AI_text01/tree/8e168c0c67b185a885c4e9251f728e3bde140cab/battlegrounds-backup/pending/20261109-night-fresh-chain

第七批审查上下文：
https://github.com/Ethsigema/AI_text01/tree/ca902d3bc382190a5e2b3d19b057ea10c6712f00/battlegrounds-backup/pending/20261109-historical-tools-batch7-boundary-review-clean

候选SOURCE_MAP SHA256为5e7e06673ff9a6b9eaf0668af1327b5ea3b86cf7f1ea866a105edbf2afd32e10，对应27,914文件、1,549,216,476字节。

这两份文件是历史原件加补丁精确重建，不是找到独立安装后原件，也未证明是最新版。351个原引用范围缺口、完整游戏及旧存档未验收的限制继续保留。本次备份验证不运行完整游戏，不把限定历史测试报告视为新执行结果。全链是否复用、是否建立完整目录，以随后追加的远端核验凭证为准。
