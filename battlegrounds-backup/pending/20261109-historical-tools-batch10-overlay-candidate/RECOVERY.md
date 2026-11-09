# 第十批历史来源修正助手候选恢复说明

本次只追加历史原件候选增量，不是独立完整游戏，不替换旧基线或旧备份。历史原件未证实实际安装过或为最新版。

必须保持Python断言启用。禁止-O、-OO或非零PYTHONOPTIMIZE；若不能保证断言启用，暂缓执行历史助手，不能据此放行完整编译器。本次不修改原件补写新实现。

1. 下载固定提交目录的MANIFEST.json和五个.part000至.part004分片，核对大小与SHA256，按数字顺序连接为historical_tools_batch10_overlay_candidate_20261109.tar.xz。应为1,187,512字节，SHA256为dd3fcc8a075443f871db47a264c5eda5d1188de121d571009bad39f20a62a631。
2. 在全新目录解包，按外部清单核对166个成员，按包内FILE_MANIFEST.json核对165个被列入清单的文件。差额是清单本身。
3. 在断言启用状态运行python verify_candidate.py和python verify_chain.py，核对限定证据与两段精确历史补丁链。不要运行完整游戏或编译器来替代这些限定核验。
4. 完整恢复需精确匹配BASE_MAP的27,915文件第九批完整上游树。运行python restore_to_new.py /上游树 /不存在的新候选树，拒绝覆盖或源内目标。只增加tools/final_source_overrides.py，3,984字节。

固定直接依赖：
https://github.com/Ethsigema/AI_text01/tree/3dd4db504ab9eba4c28088c1a72a6bbc3ed0e136/battlegrounds-backup/pending/20261109-historical-tools-batch9-trip-candidate

候选SOURCE_MAP SHA256为dc3968e2c02fc646100ad1a1745fe885414ad679250363c732f4ae4fae2920cb，对应27,916文件、1,549,279,351字节。

此文件是ZIP中已有的完整历史原件，不是推导的新后像；最早链条前像仍属反向重建。349个原范围引用路径缺口仍在，完整游戏与旧存档未验收。历史链复用及是否建立完整候选目录，以随后追加的核验凭证为准。
