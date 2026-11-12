# 最终发布回读核验

发布 commit：d914d66999536eb4250841488d09ae7ba3f82ccf；源码：a96a03307c43c5641793663b99e864877543d1b5。
结果：success；实际回读 30 文件、6465832 bytes；所有归档成员数：{'FIX_EVIDENCE.tar.xz': 84, 'GAMEPLAY_EVIDENCE.tar.xz': 151, 'TOOLS_EVIDENCE.tar.xz': 85, 'delta.tar.xz': 148}。

这里只证明发布字节与原始实际结果一致，不是再次运行 Game。失败不得升级为成功，未运行项目不得计为通过。若实际成功，有限范围仍仅为单 Mini 出售后既有原 token 对原 Lava 同回合首次施法，一次战斗/招募、无 Mini 再发；不覆盖售后 unused expiry；preview 不是发牌。新 pure 102 + 既有 3061 纯检查仅以实际执行回执为准。基线 source0b2962c / accepted final7f88ffc8 及更早失败证据保留，旧131项Game不重复。本审计包自身仍等待上传及回读。

附加证据：本次最终下载无HTTP403或字段兼容重试。封包前仅将renderer一句“暗潮成长至2级”澄清为“暗潮的获取牌等级推进至2（不是随从星级变化）”；旧文件、diff及SHA说明保留。此变更未触及source、技术字段、Game逻辑或实际日志。早期与最终实际新下载核验回执及本地最终包核验同时保留。旧TOOLS归档中的原冻结renderer未改；GAMEPLAY及本小包保留原/新版本。
