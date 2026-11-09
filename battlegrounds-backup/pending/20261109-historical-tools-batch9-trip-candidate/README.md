# 第九批：Trip Vouchers历史补丁重建候选

状态：ONE_PATCH_RECONSTRUCTED_CANDIDATE_NOT_PROVEN_LATEST。

在第八批候选基础上新增tools/trip_vouchers_patterns.py，58,891字节。只修改全新独立副本，没有硬链接；第八批及此前树、备份均未更改。输入固定备份提交为24034fe9f1c068880f0792b88a434845d3df78d6。

## 精确来源

- 历史原件SHA256：791f2ba5bfb770fa9f6d065471093955edaf0cf9db0d3f5e639617c2fe6d2982，58,909字节。
- 后续paid-choices patch SHA256：31d7a74cd340b9bba21db20ad21c22b868c6998588e220907e39143b8ae6f1a1。
- 重建结果SHA256：9923f0a449576165a59fd568dc31328ef186a23744a0fc5e689dd4c9e09b2adf，58,891字节。

原件、patch、历史integration/shared manifest均核对SHA。原始ZIP此次完整重哈希为33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65，相关成员逐字相同。补丁仅一处hunk，严格按原行号、上下文和行数应用，无偏移或模糊匹配；独立GNU patch --fuzz=0结果一致，反向应用也恢复原件。

没有找到独立历史完整postimage或补丁后SHA manifest。此结果是有证据的补丁重建候选，不是已证实最新安装原件，不是根据当前GD编造代码。

## 当前规则与测试范围

补丁把编译准入从RAW+DEPENDENCY_RAW收窄到SOURCE_IDS，严格检查传入card本体及cards中对应来源。历史演示依赖常量仍留在原文件中，但不再参与该编译入口。

唯一编译来源BG30_MagicItem_891的RAW投影和EXPECTED与当前GD相等。**完整RAW字典不相等**：GD另外含BG30_MagicItem_970t、BG30_MagicItem_984t两个选中大型饰品目标，它们不是该Python编译入口。当前来源闭包只要求自身，目标在target_error中验证。

Python只执行该字面常量与copy.deepcopy、same、compile_card组成的已审阅模块，135项检查通过：正常输出、每个顶层字段缺失、额外字段、card与cards分别篡改、布尔/数字类型区别、深复制隔离、忽略历史非拥有依赖、拒绝把两个目标当编译入口。

Godot只加载Trip来源、phase_undead_army_sources和pool_identity三个实际脚本。缺失、恢复、追加注释三态各108项断言，再在独立输入目录复现，报告相同；包内portable replay又在新目录完整复现。总计两轮Python、12次Godot。Python峰值15,104 KiB；Godot峰值69,080 KiB。全部正常退出，无Godot错误。

21个当前固定proof输入及实际proof_error在三态均通过。该工具不在这些固定准入pin中，所以本批不是新的准入阻断修复；追加注释不被proof拒绝，但改变Catalog指纹片段中工具自身一项。未计算完整execution_fingerprint，旧存档兼容性未知。

选中目标的正常、改名、额外字段、未知ID接受/拒绝边界已直接验证，但没有执行真实购买、倒计时、支付、替换、选择交互或完整对局。

Godot串行运行，192 MiB RSS停止阈值、2 GiB地址空间上限、45秒超时；启动前要求至少1 GiB可用内存，系统余量低于640 MiB则停止。Python地址空间上限128 MiB。MiniCatalog仅为隔离夹具。

## 两项继续暂缓

Battlecry Swap现存候选已经是旧shared_changes.patch的afterimage，不能再次正向套补丁。此次以零偏移、零fuzz反向得到manifest记录的before SHA 24dd2488e4e200dbb04abf5f56ae5240f635645f301b9adfff5bf2a19e517026，再正向逐字返回after SHA 9697e9fa88a9bd545d62614b3cdec05a46193c07bc75c33aca56f931e559185a。尽管来源链闭合，两条编译分支仍忽略传入card本体并使用普通Python字典相等，当前GD严格校验，故不恢复。

Souvenir Stand原件SHA 7a4b587a24a3d523647225c60fd3e84049a6095170f70badcd115e9900c71da0，双manifest、ZIP、来源投影和EXPECTED均相符，Python也使用严格same。但当前GD closure_error额外要求970t/984t两个目标，Python只检查888，仍有准入范围差异，故不恢复。

上述两项只有静态审查和字节补丁往返验证，没有执行其Python或Godot；不得把来源一致说成行为已验收。原14项暂缓保留，新增这两项静态暂缓。

## 实际树与缺口

输入SOURCE_MAP SHA256：5e7e06673ff9a6b9eaf0668af1327b5ea3b86cf7f1ea866a105edbf2afd32e10。
候选SOURCE_MAP SHA256：d4d9c436df5aa851412f8a2457a7e11128bc66d6f4313a46b42679d14f51e29b。
候选实际整树字节流SHA256：ed0a7b545e0fc5339619cd7b735f426962e7a47874e9908e75b9ea9fb9e6c519。

输入27,914文件、1,549,216,476字节保持不变；候选27,915文件、1,549,275,367字节。两树都逐文件实际重哈希，候选仅新增一个文件、修改0、删除0。原范围缺失路径在新候选中351→350；旧第八批基线仍保持351，未改旧清单。原68项历史A类余55未恢复，本次来自B类补丁链。不是项目全部潜在缺口统计。

126项静态证据检查通过。完整Game、完整Catalog、完整离线编译器、真实UI、全部玩法、随从/法术/饰品覆盖率、旧存档与原中断工作树均未因此验收；第六批四份原核验文件未找回。

## 复现与备份

首先验证FILE_MANIFEST.json逐项字节数和SHA256。python verify_candidate.py可在证据包内检查限定证据与delta。

python reconstruct_to_new.py /不存在的新目录：从原件+patch重建单文件delta，已实际复现。
python replay_to_new.py /另一个不存在的新目录：复制验证过的最小输入，复现限定Python与六次Godot检查，已实际复现。需要Python 3及/usr/local/bin/godot，本轮为Godot4.6.3。
python restore_to_new.py /精确匹配BASE_MAP的完整输入树 /不存在的新树：拒绝不匹配输入和已有目标，复制后逐文件核验。该附带入口未额外重跑；本轮实际独立全树复制核验已完成。

本包是单文件增量候选及限定审查证据，不是独立完整游戏备份。完整恢复仍需要匹配BASE_MAP的上游树。封存采用明确文件白名单，不含测试HOME、字体/编辑器缓存、.godot、__pycache__、私聊、凭据或无关文件；旧备份及证据原样保留。
