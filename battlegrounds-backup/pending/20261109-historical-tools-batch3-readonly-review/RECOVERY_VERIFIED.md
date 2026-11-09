# 第3批只读审查：新归档和固定依赖核验通过

这是审查证据，不是运行恢复候选。源码新增/修改/删除均为0，五项工具均未恢复，原367路径范围仍缺357项。四项记录历史工具与当前来源政策/验证边界差异，Partner的312脚本闭包未运行。差异探针通过不等于四文件通过恢复验收，也不是本轮新增运行回归。完整游戏、旧存档和最新版均未验收。

## 实际远端下载

新归档固定提交b78e979c5a64f79daa265196b50105b535953f27，1,258,348字节，SHA256 fa8ac41ae7131166487aebeecbd1d1b541ea259ebf8b2f00f438209ad1178663。

6片Git对象在fetch前均不在本地对象库，已从固定远端提交真实下载；辅助相同对象可被Git去重。BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE和ARCHIVE_PUBLICATION_RECEIPT记录来源。发布只新增12个文件，无覆盖、删除或强推。

逐片、整包、全部118成员和内部117项清单一致。没有delta、候选SOURCE_MAP或SOURCE.patch，外部CHANGES/REMOVALS均为空。原NO_SOURCE_CHANGES和当前BASE_MAP一致。

## 固定依赖与实际核验范围

输入提交8a675dc886b8686e6bdd9a47463366cafb9c020f：
https://github.com/Ethsigema/AI_text01/blob/8a675dc886b8686e6bdd9a47463366cafb9c020f/battlegrounds-backup/pending/20261109-historical-tools-batch2-four-candidate/RECOVERY_VERIFIED.md

重新从远端读取该提交MANIFEST和回执，分别核对SHA256：
- MANIFEST：26e1d37470f663358cc246c5a860d0d563b1eae60a3729f466f2080546ed678b。
- 回执：45c8d5c2837861e93d92c59df791c967a226d072decbaa34f59b6f5672f35b97。

复用第2批归档，实际重新哈希整包及全部282成员，其SHA256为51263c49a09a0a735a417e147e4f64f0529be4d5fa12529807653da7187693eb。实际归档SOURCE_MAP字节与本包BASE_MAP完全相同，SHA256为3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea。核验结束再次哈希依赖归档，未变。

对新包内69个唯一的历史原文/当前来源文件实际重哈希，共1,613,292字节，逐项同固定输入源码清单一致。56个探针输入中，53个是真实源码，另3个是严格限定名称与SHA的隔离配置。317个声明preload路径仅做元数据与输入映射对照，没有加载这些脚本，也没有重新读取整个历史工程。

输入映射记载27,908文件、1,548,971,251字节，但这不是本次全工程逐字节重新核验的计数。本次没有创建完整运行树，没有重新哈希完整1.55GB源码树，没有重新下载或重放历史全链，没有重新运行Godot、项目Python模块、真实Catalog、Game或旧存档。

原报告40项Python检查、完整输入两次30项Godot观察及初次失败报告只是保存并检查一致性，不充当本轮执行。before是初始不完整隔离输入，after是补齐后的隔离输入，均未安装五个工具；初始缺13个proof文件是探针输入遗漏，不是游戏源码缺失。

## 本轮核验脚本的一次分类修正

首次归档与依赖成员核验均通过，但脚本误把所有probe_inputs文件都当作游戏源码而退出1。已确认差异恰好为review_config.json、review_fixtures.json和136字节最小project.godot。没有包损坏或源码变动。

保留首次脚本、日志、过程记录和输出目录。修正后仅对这三个明确名称及固定SHA的配置分别核验，其余53个源码仍必须严格匹配输入清单，没有放宽一般检查。新输出目录重验通过，退出0，用时0.647秒，确切子进程峰值54512KiB。资源上限不变：192MiB RSS保护、512MiB地址空间、180秒超时。

成功脚本为verify_batch3_review.py。verify_batch3_review_initial.py只保留作失败证据，不应当作当前推荐验证器。详情见VERIFIER_INPUT_ROLE_CORRECTION、VERIFY_INITIAL、BOUNDED_INITIAL_PROCESS、VERIFY_SUCCESS和BOUNDED_RETRY_PROCESS。

## 成功回执

BATCH3_REVIEW_REMOTE_VERIFICATION.json
SHA256：671519fca12a0275d3b598672561f4d94dd03ffa5602621fdbc78ab262f330b0

EMBEDDED_SOURCE_FILES_VERIFIED列出69个实际重哈希并同固定映射匹配的文件。旧基线、旧归档、初始失败和所有未验证材料保留，无删除。

## 复现归档与依赖验证

Python3.9或以上标准库，准备已固定的第2批归档：

```sh
python3 verify_batch3_review.py \
  --input-archive /path/to/historical_tools_batch2_four_candidate_20261109.tar.xz \
  --output /path/to/a-new-batch3-evidence-check-directory
```

默认从固定提交下载本包和固定输入元数据。也可先下载同一提交MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY及6片，传--download-dir；用--input-manifest和--input-receipt指定本目录PINNED_INPUT副本。固定哈希约束不变。本轮采用Git预下载，因此increment_downloaded_by_this_helper:false只指Python不负责下载，真正下载证据见FETCH_PROVENANCE。

脚本仅解包并核验审查证据，不把它应用到游戏目录。需要游戏恢复时继续使用固定第2批恢复链，本审查包不改变源码链。不把零变更证据称作新候选或完整游戏验收。
