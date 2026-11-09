# 恢复与验证

1. 从公布的固定提交下载 MANIFEST.json 和按顺序列出的8份 .part000 至 .part007，逐份核对大小和 SHA256，顺序拼成原 .tar.xz。原包 SHA256 必须为 3d37a9d1a0ee2d61939e88f8ced995622ca22fd84ba7f9dabe8c4f2df6bafa7d。
2. 运行 python3 -B verify_backup.py --local 下载目录。脚本验证单一完整XZ流、安全普通成员、全部49文件及48项内部清单、XML SHA256/Git blob、5,786个Entity和5份原生实体逐字节相同。它不执行包内游戏或历史脚本。
3. 完整复核：python3 -B verify_backup.py --commit 固定提交 --folder battlegrounds-backup/pending/20261109-historical-tools-batch16-xml-original-candidate --manifest-sha256 已公布清单哈希 --out 不存在的新目录 --baseline13 第13批完整基线目录。
4. 脚本真实下载第16/14/13批全部分片和清单，核验每个归档成员与 SOURCE_MAP 衔接。第13批完整基线须来自其原依赖链，并严格匹配远程固定 SOURCE_MAP 的27,918文件。脚本会重新逐项哈希，不接受只有清单没有实际文件。
5. 恢复写入仅发生在新目录 isolated_restored_candidate：复制并校验第13批基线，用刚下载的第14批两份delta补齐第14批候选，再加入刚下载的XML。最终逐项校验27,921文件、1,565,165,008字节；原基线在前后重新哈希，不能有缺失、多余、变化或硬链接。
6. 此步骤复用较早历史链及其本地恢复树，不重新下载或重跑第13批以前的完整链。完整游戏源、二进制依赖、存档和运行行为仍可能有未知缺口。远程恢复成功仅指清单覆盖的字节可恢复，不代表完整游戏可运行或存档兼容。

包内原 RECOVERY.md 原样保留；本页补充发布阶段的当前恢复方式。现存运行树不覆盖；若以后需要应用到现存游戏，必须先验证基线及目标缺失，并另做行为/指纹/存档验收。旧备份不得删除。
