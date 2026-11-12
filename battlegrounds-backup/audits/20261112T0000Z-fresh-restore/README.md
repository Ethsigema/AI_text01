# 2026-11-12 北京时间 08:00 备份核验

本轮从 GitHub 重新下载原始 Release 和所需增量，在两个不存在的新目录实际恢复并逐文件重读核验。基线 27,920 个文件、1,549,340,406 字节通过；独立碎地者候选 27,927 个文件、1,549,517,087 字节通过。两份恢复结果的缺失、多余和哈希不符均为 0。

**原活动工程仍不可见，因此本轮不能保证原工程所有当前变化均已备份。** 可见的两个昨晚恢复副本已重新逐文件核对，均无新增、缺失或内容修改；它们不是原活动工程。本轮没有伪造新游戏源码增量，新增内容只有本次核验记录。无法排除不可见原工作树仍有未上传修改，也不据此断言永久丢失。

## 本轮实际执行

- 核验前恢复分支固定在 b3619a13d2c0b50fc25e929d358cdbd69818dd31，和上次回执一致；main 为 32180d3af0db59fb3374f53100f9eaa5bb62d26a，其最近提交日期为 11 月 6 日。没有发现更新的远端游戏源码。
- 46 份输入重新下载：原始 ZIP 为 324,041,102 字节，另外 45 份仓库文件的大小及 Git blob 身份全部吻合。未用本地旧包充当重新下载。
- 两个包的 SHA256SUMS.txt 和 VERIFICATION_SHA256SUMS.txt 全部通过。
- 原始 ZIP 加 13 片合并增量，恢复基线全部 27,920 个文件，再从磁盘核对路径集、大小及 SHA256。21,099 个目标文件来自原始 ZIP，6,821 个来自合并增量。
- 在上述干净基线上应用 87 份候选增量，新增 7、修改 80、删除 0，重建全部 27,927 个文件并再次逐文件重读核验。
- 碎地者证据包 24 个成员逐项哈希通过。仅验证历史证据字节，没有执行证据内代码，没有运行 Godot、完整对局、界面或存档测试。
- 原基线及碎地者候选均不推广、不覆盖默认工程。旧备份、旧审计和旧失败记录均保留，不强推、不清理。

## 随从、酒馆法术、饰品进度及依据

- 随从：本轮新增完整验收 0，可靠完成百分比未知。碎地者仍是受限独立候选，未变成通用默认池已完成项。
- 酒馆法术：本轮新增完整验收 0，可靠完成百分比未知。当前范围清单中的四法术切片仍为 candidate_not_engine_tested。
- 饰品：本轮新增完整验收 0，可靠完成百分比未知，没有新验收证据。

本轮读取并记录了当前恢复树的 data/current_scope_manifest.json、data/runtime_coverage.json、data/effect_coverage.json 及其哈希。范围清单仍为 written_unverified。runtime_coverage.json 自带生成时间为 2026-10-17，其计数混合普通、金色和衍生实体，文件也明确说明能力校验不等于穷尽组合验证。因此这些旧能力数、文件数、断言数和历史样本都不是当前完成率的可信分子/分母。详细可复核依据见 PROGRESS_BASIS_CURRENT.json。

11 月 11 日碎地者已存证但本轮未重跑的测试包括真实 Game/Catalog、受限房间开局、原工厂和入手、公开 apply_command 及原 _buff。普通 6/4→7/5，连续不同卡打出后普通 9/7、金色 14/10，越域纳迦拒绝且状态不变，16 项来源合同正反例通过。这些不计作本轮新增测试。随机商店获取、金色获取/三连、3/6 施法阈值、同一命令重复、通用默认房间、完整对局和旧存档仍未验收。

本轮再次检查，Piranha、Hand Murloc 两份 SOURCE_CONTRACT.md 和 tools/build_effect_catalog.py 仍不存在。345 个历史工具引用缺口及四份旧证据缺口沿用原记录，本轮未重新完整分类盘点，不能把文件恢复成功当作缺口消失。保持娜迦，排除畸变怪；英雄和额外机制没有新增。

## 恢复入口与精确哈希

1. [原始 ZIP](https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip)，SHA256：33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65。
2. [合并增量及恢复说明](https://github.com/Ethsigema/AI_text01/tree/b3619a13d2c0b50fc25e929d358cdbd69818dd31/battlegrounds-backup/consolidated/20261111-batch14-restored)。合并归档 SHA256：eb3a81406cf04ce629d001a72e8f0f099c8a1db07f28713e2818898f2faf7e12；解压后完整源码清单 SHA256：7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7。
3. 可选的[碎地者独立候选及恢复说明](https://github.com/Ethsigema/AI_text01/tree/b3619a13d2c0b50fc25e929d358cdbd69818dd31/battlegrounds-backup/pending/20261111-shatterer-real-command-candidate)。增量 SHA256：b333fd28f7be6d93c36b7c650611de8f99465d6f4dc3f592e363f8e99a7afb71；完整候选清单 SHA256：a2661c3968082e0708b2ab8c9b95ec31ed36eb72295f477f58fdad69a716f5c9。

严格按各目录 RECOVERY.md 操作，输出必须为不存在的新目录。增量不能单独作为完整游戏。旧 LATEST.json、LATEST_DEVELOPMENT.json 和 RECOVERY_STATUS.md 是早期历史索引，不能替代上述恢复入口。

本目录仅为本轮新核验记录，不是新游戏源码包。核心回执为 AUDIT_SUMMARY.json、FRESH_DOWNLOAD_VERIFIED.json、BASE_RESTORE_CURRENT.json、CANDIDATE_RESTORE_CURRENT.json、PREEXISTING_RESTORED_TREES_CURRENT.json 及 EVIDENCE_CURRENT.json。
