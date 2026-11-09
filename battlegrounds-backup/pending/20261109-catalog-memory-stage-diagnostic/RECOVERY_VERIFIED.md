# 分阶段内存诊断：远端证据与固定依赖核验通过

本包仅为诊断证据，不是运行源码增量，也不改变任何已验收状态。输入工程仍固定于4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1，其完整Game仍未验收。源码新增、修改、删除均为0。

## 已完成检查

- 原档案提交 `54e5f406ef75bfe7864bbe4947d803de4b1a6525`，仅新增11个备份文件，未修改或删除旧文件，未强推。
- 真实git fetch固定提交下载后，读取全部上传文件。5个分片对象在下载前均不存在本地Git对象库，证明本次档案不是沿用本地待上传包；相同的辅助文件对象可能由Git去重复用。证明见FETCH_PROVENANCE、BEFORE_FETCH_OBJECTS及ARCHIVE_PUBLICATION_RECEIPT。
- 5个分片、1,101,148字节整包与67个归档文件的大小/SHA256全部匹配，内部清单66项逐一核对，清单自身由外部MANIFEST覆盖。编码夹具中的非法UTF-8及NUL等原字节完整保留。
- 整包SHA256：`b5b03999c2cee2e995c56267cf2327786e3585187c061cf944a0088664a603a6`。
- 从固定远端提交新读取输入候选MANIFEST和恢复回执，分别验证SHA256，确认输入归档、来源清单与实验状态相互一致；此前已下载输入归档也重新核对整包SHA256。
- 对全部27,892个输入运行文件重新哈希，共1,548,714,104字节，严格符合INPUT_SOURCE_MAP；缺失、多余、不符均为0，前后核验内容未变。
- 恢复的是独立诊断证据目录，没有创建新运行树，没有执行包内探针、load_catalog或Game，没有删除任何旧备份。

完整回执：`DIAGNOSTIC_REMOTE_VERIFICATION.json`，SHA256：`1cfd7034bbb727ab1d777aa99d954452dc243c53b106c97ac820df14c5319fd1`。

## 固定输入及复用边界

输入恢复说明：
https://github.com/Ethsigema/AI_text01/blob/4ebbc2e1276f678c8a9e91e45d0fe24f036f66c1/battlegrounds-backup/pending/20261109-catalog-memory-candidate/RECOVERY_VERIFIED.md

输入归档SHA256：`e5272cc3556bf626d353993b142a75d40ea26c4522eb94bcb2f5a55994f7f7d6`。
输入SOURCE_MAP SHA256：`e52121d24d2b21f75af73521362928a2da449f7f42915fb692cfcb3d425ab0a0`。
输入MANIFEST SHA256：`2218f998a299ee221fb31ee06c123737d8cc53c07d6a2c3eb6e122c744c87ad6`。
输入恢复回执SHA256：`45d53273107a8411727d9d2e1462810ac6e685c4e1f62727eb55fdfd81a4d384`。

本轮重新下载本次诊断档案，并新读取固定依赖元数据。输入候选归档和运行树复用此前远端恢复结果，本轮重新哈希；历史全链及输入归档没有重新下载，不把依赖复用说成全链重下。

## 重现证据恢复与依赖检查

使用Python3.9及以上标准库，先按输入恢复说明准备其运行树，然后下载本目录脚本：

```sh
python3 verify_stage_diagnostic.py \
  --input-runtime /path/to/restored_catalog_memory_candidate_runtime \
  --input-source-map /path/to/catalog_memory_candidate_20261109/SOURCE_MAP.json \
  --input-archive /path/to/catalog_memory_candidate_20261109.tar.xz \
  --output /path/to/a-new-diagnostic-evidence-directory
```

脚本默认从固定提交下载诊断档案及固定输入元数据，验证归档全部成员后，仅安全解压证据并逐文件检查输入运行树。不会覆盖或补丁任何工程文件。--input-source-map及--input-archive可省略；传入时分别加强独立清单和归档检查。输出目录必须不存在，保留已有目录和旧备份。

如果已从相同固定提交预下载MANIFEST、CHANGES、REMOVALS、SHA256SUMS、README、RECOVERY与5个分片，可加 `--download-dir /path/to/downloaded`。输入元数据可使用本目录PINNED_INPUT_MANIFEST.json及PINNED_INPUT_RECEIPT.json，分别通过--input-manifest和--input-receipt传入，固定SHA256检查仍执行。本次采用Git预下载模式，diagnostic_download_by_this_python_helper:false表示下载在Python脚本之外完成；本轮真实下载证明在FETCH_PROVENANCE.json。

INPUT_SOURCE_MAP是固定依赖清单，不是新版本运行树。诊断包不应插入游戏源码增量叠加链。包内原诊断脚本绑定执行时路径及输出目录，恢复证据不等于再次执行它们。

## 未验收与风险边界

原预载试验在848项完成后、combat预载阶段被SIGKILL，完整catalog与Game未启动；内核/cgroup终止原因未知。小探针结果不是完整加载修复或游戏验收。文本哈希和原字节哈希在部分编码用例不等价，未替换源码；短函数作用域未证明RSS峰值下降。回读任务没有提升资源阈值、重跑高内存预载、修改工程或宣称新游戏验收。最后已验收基线仍为a71d3e4ea64dc52264a3f789a48ddae2e4a043cd。
