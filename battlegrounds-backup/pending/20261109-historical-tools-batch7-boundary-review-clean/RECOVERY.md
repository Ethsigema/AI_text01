# 第七批只读边界证据恢复说明

本次只追加去缓存派生证据，源码增加、修改、删除均为0，不替换任何旧备份，也不更新已验收游戏版本。这个压缩包本身不是独立游戏备份。

1. 从同一个固定提交目录下载本目录7个 .part000 至 .part006 分片、MANIFEST.json、SHA256SUMS.txt、DEPENDENCIES.json。
2. 校验每个分片的大小与SHA256，再按数字顺序连接为 historical_tools_batch7_boundary_review_nocache_20261109.tar.xz。完整包应为1,639,148字节，SHA256为11158be04088b7b681d0c43dbeca9cb33d2333a51bc0d6412c920a0ac2212aa8。
3. 在全新目录中解包，按MANIFEST.json校验全部222个归档成员，再按包内FILE_MANIFEST.json校验221个被列入清单的文件。两个清单的差额是FILE_MANIFEST.json自身。
4. 可运行包内verify_review.py，只读复核170项封存证据。需要动态复现时，依照包内README.md在另一个全新目录运行replay_to_new.py；不要覆盖封存证据。

固定源码候选：
https://github.com/Ethsigema/AI_text01/tree/3d41c7f71bdda146ed37930c7591b419b53e36a6/battlegrounds-backup/pending/20261109-devourer-tool-historical-candidate

固定最近全链恢复证据及恢复脚本：
https://github.com/Ethsigema/AI_text01/tree/8e168c0c67b185a885c4e9251f728e3bde140cab/battlegrounds-backup/pending/20261109-night-fresh-chain

恢复游戏源码必须继续使用上述固定依赖的官方基包及历史增量链，不能只解压本次证据包。本批BASE_MAP与固定源码候选SOURCE_MAP相同，SHA256为9baabc104b5f2f93087dfec0e385d6cb9fceffbf3b1d4441ec91da463a727260。

边界：两项工具暂缓恢复，353个原范围缺口未减少，四份原第六批核验文件尚未取回。备份验证只验证真实字节及证据一致性，不代表游戏玩法、完整内容、完整离线编译器或旧存档验收。此次备份工作不重跑游戏或整个历史链。

原包未发布且保持不动。派生包去除了128个自动生成文件（124个字体缓存和4个重复运行日志），其余原始非清单文件字节不变；新清单和DERIVATION.json明确记录变换，因此不能用原包SHA校验本派生包。
