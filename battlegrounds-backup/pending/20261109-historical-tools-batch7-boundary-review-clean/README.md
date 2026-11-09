# 第七批只读边界证据：去缓存派生包

本目录发布的是去缓存派生包，不是原包。原包保持不动且未发布。已排除124个可重建字体缓存文件及4个重复运行日志，重新生成文件清单。保留的220个原始非清单文件逐字节不变，无凭据或私聊文件。新增DERIVATION.json记录变换范围，不公开缓存成员路径或哈希。

# 第七批：历史工具边界复核，无源码恢复增量

状态：READ_ONLY_REVIEW_TWO_INPUT_BOUNDARY_DIFFERENCES_NO_SOURCE_CANDIDATE。

本批先从独立核验树复制完整开发副本，27,912个文件、1,549,132,284字节全部重新读取并匹配。复制未使用硬链接。结束时再次重哈希原基线和开发副本，两树均完全未变。所有新脚本和报告只写入新目录，旧备份及证据未修改或删除。

固定输入是Devourer候选，SOURCE_MAP SHA256为9baabc104b5f2f93087dfec0e385d6cb9fceffbf3b1d4441ec91da463a727260。独立原始恢复记录见：
https://github.com/Ethsigema/AI_text01/blob/8e168c0c67b185a885c4e9251f728e3bde140cab/battlegrounds-backup/pending/20261109-night-fresh-chain/PUBLICATION_VERIFIED.md

## 两项实测结论

- tools/necrolyte_patterns.py，亡灵侍僧，14,936字节，SHA256 acec01cd401653fdde84ef84d4b542bd56b32afa8e399a94404ba0a6f71e4714。
- tools/taverngoer_patterns.py，无面酒客，15,017字节，SHA256 068d6e8582965c3e79d80e705fa008742345e3d20eb193d067ef3b395a91fc35。

两项历史原件、integration/shared manifest、当前RAW/EXPECTED均吻合。原始2026-11-01 ZIP完整重哈希为33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65，两个成员与当前历史副本逐字节相同。它们没有已知修改patch，原分类为单历史版本原件，但不证明是最新安装版本。

实测发现旧Python compile_card只核对传入card.id，再检查cards映射，不验证传入card本体。因此它接受改名card及仅有id的card。它使用Python普通字典相等比较，也接受布尔值被等值数字替换。当前Godot来源的raw_source_error明确拒绝以上输入。正常普通/金色输出、成对来源缺失/改名拒绝、深复制隔离及当前来源闭包另行检查通过。

这是具体的输入校验边界不同，不等于确认完整离线编译器一定以不安全方式调用，也不等于运行游戏已有漏洞。没有改写历史原件或当前来源来消除差异；两项都暂缓恢复。

## 旧分类的进一步静态筛选

原68项历史A类余55项，排除原11个暂缓对象后有44项。22项包含same与compile_card的严格card校验，但Python依赖表均额外含BG32_HERO_001，当前对应GD依赖表不含该英雄；其他同名依赖字面量相同。记录在STRICT_CANDIDATE_SCREEN.json，并保留逐字原源码输入供复核。

这22项只做静态筛查，未分别运行动态准入测试，不能称其全部已动态确认、已恢复或完整功能失效。其余22项也没有统一获准恢复；本轮只对其中上述两项做了独立动态核验。

原353个缺失路径仍全部缺失，原11个暂缓项保持不变，新增两项明确暂缓，共13项有本类审查记录。CHANGES与REMOVALS为空；没有delta或新的游戏SOURCE_MAP。

## 资源与可重复性

首次两模块Python检查50项通过，峰值12,288 KiB，地址空间上限128 MiB。最小Godot探针只加载两个来源及pool_identity，共3个实际脚本；两次独立输入目录各69项断言，报告相同。随后通过包内replay_to_new.py另建目录复现Python和两次Godot，同样一致。四次Godot峰值最大67,176 KiB，均正常退出且无Godot错误。

Godot串行运行，192 MiB RSS停止阈值、2 GiB地址空间上限、45秒超时，启动前至少1 GiB可用内存，系统余量低于640 MiB则停止。MiniCatalog是隔离夹具，不是完整Catalog。未加载Game、完整Catalog、完整离线编译器或旧存档。

82项初次静态交叉检查通过；补齐88份静态筛查输入后，最终扩展为170项通过。首次自编AST检查器把SOURCE_IDS=frozenset([...])误当非字面量，执行历史模块前即停止。初版脚本与说明保留，修正版仅允许该确切内建调用；原模块未改，初次失败不计通过。

## 在新目录复现

先校验FILE_MANIFEST.json中每项字节数及SHA256。可直接运行python verify_review.py只读检查封存报告和输入。

动态复现：python review_loose_compilers/replay_to_new.py /一个不存在的新目录。需要Python 3和/usr/local/bin/godot（本轮实际为4.6.3）。该脚本拒绝覆盖目标，复制验证过的最小输入，再执行限定的两模块检查及两次串行Godot探针。

screen_remaining.py使用完整开发副本；只有证据包时会使用screen_inputs。再次运行会写新的筛查报告，因此请先复制证据包到新的目录，勿覆盖封存原件。

本包是审查证据，不是独立游戏备份或恢复候选。完整玩法、随从/法术/饰品覆盖率、UI、旧存档兼容性以及原中断工作树都没有因此验收。四份原第六批核验文件仍未取回。
