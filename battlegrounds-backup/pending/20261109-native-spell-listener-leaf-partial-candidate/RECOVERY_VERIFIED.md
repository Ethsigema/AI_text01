# Native spell listener部分候选：远端下载与流式字节重建核验通过

候选仍为PARTIAL_PURE_VALIDATION_AND_CANDIDATE_STOCK_PASS_ORIGINAL_HOST_BLOCKED，仅部分验证。旧真实入口SIGKILL，完整宿主及Game未验收。源码备份通过不提升游戏验收，不重跑Godot。此前a71d3e4ea64dc52264a3f789a48ddae2e4a043cd仅保留限定范围验收，不能描述成全机制回归通过。

## 真实执行结果

- 原包固定提交 `8056893fcb4181431e1bbd8a8866dfb2b2932df3`，只新增11个备份文件，无修改或删除旧文件，未强推。
- git fetch固定提交后读取同一提交全部上传文件。5个分片对象在下载前均不存在本地Git对象库，证明本次从远端重新下载，不沿用本地待上传包；相同辅助对象可能由Git去重。证明见BEFORE_FETCH_OBJECTS、FETCH_PROVENANCE及ARCHIVE_PUBLICATION_RECEIPT。
- 5片、1,155,064字节归档、247个归档成员及内部246项清单全部严格核对。内部清单自身由外部MANIFEST覆盖。
- 整包SHA256：`46ceb12b81c5db0c417933482d6572f3c89693d2ba3ef2d507ccebc5f0ed4ec7`。
- 固定依赖的MANIFEST及回执从远端新读取并核对SHA256；以前已下载的基线归档也重新核验。输入27,893个文件完整重哈希。
- 新增2、修改3、删除0，五个有效delta文件与实际来源差异严格相同，净增4533字节；测试篡改证据不应用。
- 对目标27,895个文件的全部1,548,719,055字节逐文件实际读取、按块重算SHA256，全部符合SOURCE_MAP。27,890文件来自已重哈希基线，5文件来自本次新下载delta。不是仅对照清单或检查5个变化文件。
- 缺失、多余、哈希不符均为0。完成后再次完整重哈希输入树，内容未变。
- 开始磁盘约2.6GiB，为保留余量采用流式重建，没有写出第二个完整运行目录，没有完整工程复制、运行游戏或删除旧备份。具体磁盘数值见DISK_PLAN及回执。

完整回执：`NATIVE_LISTENER_LEAF_PARTIAL_STREAM_VERIFICATION.json`，SHA256：`ba73c82db88ceaedbb57f395da246433deb89d55ddd3ff6296a871c9d03b3cda`。
流式目标映射SHA256：`9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111`。它含每个实际重建文件的字节数和SHA256，严格等于包内SOURCE_MAP的映射；脚本会在输出目录重新生成该JSON。
实际字节拼接摘要：`d778dde09696c622af7bf2a18fe31f747e4647f295028e0c973e341308cceee2`。计算顺序为排序路径UTF-8、NUL、ASCII字节数、NUL、实际文件字节，逐文件连续加入SHA256。

## 固定依赖和历史复用

直接依赖Harbinger identity候选提交26679da39e12f73907a9d15c325ca4028daf8474：
https://github.com/Ethsigema/AI_text01/blob/26679da39e12f73907a9d15c325ca4028daf8474/battlegrounds-backup/pending/20261109-harbinger-identity-leaf-candidate/RECOVERY_VERIFIED.md

输入归档SHA256：`b666e972100a402ae3b9fa92ab2126e5324f4327842ac88fecebcc204c6f4ee4`。
输入SOURCE_MAP SHA256：`e31eb74faca1a774b42a7c8bcef11b1592eae64ad350b08fa930f9a1d7cd64fe`。
输入MANIFEST SHA256：`180d5ebba796ffa9cde4a4afe2814604cba823a9bd5856f09bbf45cc8ca8ce1c`。
输入恢复回执SHA256：`a6d29ead3af28eb40c81bcc7b7a23a56ea5fb0f85c38125262e5b717c2bd14dc`。
目标SOURCE_MAP SHA256：`9c1faebcbc9c2edae3fbacd3de2d13e454c219bb4b9ad1938dd69496bdb5d111`。

本轮新下载本次native listener候选，历史基线及其所有依赖归档复用并重新哈希，历史整链没有重新下载。不能跳过Harbinger、catalog memory、女妖及更早运行增量。诊断档案没有运行改动，不插入运行增量链。之前的全链重下审计仅到女妖，没有包含这些后续实验。

## 重现低磁盘流式核验

Python3.9及以上标准库；先按固定输入说明准备完整Harbinger运行树及SOURCE_MAP，再下载本目录脚本执行：

```sh
python3 verify_native_listener_stream.py \
  --baseline-dir /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  --baseline-source-map /path/to/harbinger_identity_leaf_candidate_20261109/SOURCE_MAP.json \
  --output /path/to/a-new-native-listener-stream-evidence-directory
```

默认从固定提交下载新包及输入元数据，验证全部归档和依赖、完整输入、增量和删除清单，再读取全部目标文件实际字节并严格核对，最后复查输入未变。输出是证据、恢复配方和每文件重建映射，不是可运行的完整工程。

也可预下载同一固定提交MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY及5片后传入--download-dir。可通过--baseline-receipt、--baseline-manifest提供本目录固定依赖副本，通过--baseline-archive额外重哈希输入归档。所有固定SHA256检查仍执行。输出目录必须不存在，保留已有输出和旧备份。

本轮回执increment_bytes_freshly_downloaded_by_this_helper:false表示Git在Python脚本外完成下载；真实新下载证明见FETCH_PROVENANCE.json。complete_runtime_directory_created:false明确本次没有完整运行目录。

## 需要完整运行目录时

准备至少目标源码大小加目录及缓存余量，保留额外空闲空间。先通过上述全量基线和远端包校验，再使用解压包内restore_to_new.py（其hashlib.file_digest需要Python3.11及以上）：

```sh
python3 /path/to/extracted/native_spell_listener_leaf_partial_candidate_20261109/restore_to_new.py \
  /path/to/restored_harbinger_identity_leaf_candidate_runtime \
  /path/to/an-absent-new-native-listener-runtime
```

该脚本拒绝已有目标目录，独立复制并逐文件核对。恢复后仍须确认目标精确符合SOURCE_MAP且基线未变；不要使用硬链接、覆盖基线、应用tamper目录或删除旧备份。完整目录恢复和游戏运行是未来单独步骤，本轮未执行。

## 未验收范围

原文oracle不是完整原宿主，薄代理不是完整新版宿主；小入口只使用轻量catalog适配器。原入口SIGKILL没有完整报告，不能说其功能失败、断言OOM原因或计算正式内存降幅。事件调用接线、施法触发与效果执行、完整来源证据链、完整catalog/Game、存档、回放、UI及全局内存收益未验收。所有原成功与失败证据都按原字节保留。
