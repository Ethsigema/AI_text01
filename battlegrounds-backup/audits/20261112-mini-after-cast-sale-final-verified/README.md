# 最终发布回读核验

发布 commit：838043a91d995a93bf916846e960465ee05966e7；源码：610cad09b7d19fe2615201f054a68c6e1a31d79d。
结果：success；实际回读 30 文件、5661321 bytes；所有归档成员数：{'FIX_EVIDENCE.tar.xz': 61, 'GAMEPLAY_EVIDENCE.tar.xz': 162, 'TOOLS_EVIDENCE.tar.xz': 86, 'delta.tar.xz': 151}。

这里只证明发布字节与实际结果一致，不是再次运行Game。失败、未知和未运行必须分开。成功范围仅原Mini原token先cast原Lava永久4/5，再在无child手牌时原生sellMini，一次非空combat/nextrecruit保留4/5并重置kept0，且不再发牌。新pure实际计数为85，旧10份纯合同3163项；未执行不得计入通过。旧source a96a033/final d914d669与更早历史不改写。此审计包仍待上传和回读。

附加说明：最终fresh30/460成员核验通过，原source16及early22非SUMS字节不变。实际总3351项；顺序严格先cast原token、确认消费、再sell原Mini、最后combat/recruit。本次无HTTP403续传或字段兼容修补。晚改仅解释“获取牌等级2而非随从星级”并明确未测售后unusedexpiry，不是代码或Game重验。原renderer/旧说明、当前renderer、14项措辞synthetic及校验回执保留，旧TOOLS归档原字节未改。
