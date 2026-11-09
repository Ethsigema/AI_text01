# 第十一批只读审查证据恢复说明

本包仅为审查证据，没有runtime源码增量，不是独立完整游戏。六项发现材料均因行为或调用差异暂缓，349个原范围缺口不变。不得把审查目录中的重建文件安装到runtime/tools。

1. 下载固定提交目录的MANIFEST.json及八个.part000至.part007分片，校验大小与SHA256并依序连接为historical_tools_batch11_source_review_20261109.tar.xz。应为1,888,152字节，SHA256为3c841a46012974078fa46e722f61989ff1212647f32cf27539f3a8359055c393。
2. 在新目录解包，按外部清单校验334个成员，按FILE_MANIFEST.json校验333个被列入清单的文件。差额是清单本身。
3. 保持Python断言启用，禁止-O、-OO或非零PYTHONOPTIMIZE。python verify_review.py仅检查封存证据。python reconstruct_review_to_new.py /不存在的新审查目录重现两项历史载荷，禁止据此安装或运行其完整调用链。
4. 若需要完整审查树，准备精确匹配BASE_MAP的第十批上游树，再使用包内restore_to_new.py复制到新目录。它只复制未变基线，不安装六项暂缓工具。

固定运行基线：
https://github.com/Ethsigema/AI_text01/tree/1266c9d1c78bf3f388d2f695467d60af9807ac75/battlegrounds-backup/pending/20261109-historical-tools-batch10-overlay-candidate

本批BASE_MAP与SOURCE_MAP相同，SHA256为dc3968e2c02fc646100ad1a1745fe885414ad679250363c732f4ae4fae2920cb，对应27,916文件、1,549,279,351字节。

完整静态依赖审计、版本图和全部历史搜索的重做需要上游完整树及其他固定输入，不能仅凭小证据包重做，也不等同于本次备份验证。完整Game、Catalog、离线编译器及旧存档仍未验收。旧备份和源码保留，不覆盖、不强推。
