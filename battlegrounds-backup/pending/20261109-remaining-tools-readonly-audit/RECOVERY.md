# 恢复与核验本次证据包

1. 从固定 GitHub 提交中的本目录下载 MANIFEST.json、SHA256SUMS.txt、verify_package.py，以及 .part000 至 .part006 七份分片。不要从其他批次下载依赖。
2. 逐份核对 SHA256SUMS.txt 中的 SHA256 值；每个分片的精确大小和 SHA256 亦列于 MANIFEST.json。按分片编号拼接，可得到完整原始压缩包。
3. 可在可信 Python 3 环境执行：python3 verify_package.py <下载目录> --write-archive --report verify_result.json。脚本只读取分片、核对 SHA256、在内存中读取归档，并检查全部 102 个成员及内置白名单。它不连接网络、不导入历史工具、不启动 Godot 或 Game，也不覆盖已有归档。
4. 重建原包必须为 1,537,068 字节，SHA256 9eb4be705ee386167956350de3212845a70b664148f8dddeb3aed540da5c12ba。核验成功后仅在新的独立目录解包查看；不得覆盖当前游戏目录或将 13 项暂缓工具直接安装。

本次恢复只重建证据包，不能据此宣称游戏内容完整、依赖已复核或旧存档兼容。345 缺口和 13 项暂缓状态未变。此前被取消的依赖下载不属于本任务。
