"""Add Chinese explanation from actual verified receipts, preserving before-CN metadata."""
from packaging_common import *
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--execute',action='store_true',required=True);ap.add_argument('--remote-root',type=Path,required=True);a=ap.parse_args()
 r=a.remote_root.resolve();p=ROOT/'final_package';e=r/'independent_tests';final=read(r/'INDEPENDENT_GAME_VERIFICATION.json');scenario=read(p/'GAMEPLAY_MATRIX_RESULT.json');case=scenario['cases'][0]
 assert final['status']==runner.FINAL_STATUS and len(final['tests'])==9 and len(scenario['cases'])==1
 assert sha((r/'INDEPENDENT_GAME_VERIFICATION.json').read_bytes())=='eff52588c9d106c971e1155c0e5569a1be19024e214bbaf8c67d1253e0eee5ce'
 sale=case['sale_effects'][0];buy=case['purchases'][0]
 assert case['first_buy_before_source'] is True and case['active_purchase_count']==1 and case['offer_created_after_first_sale'] is False
 assert sale['uid']=='u68' and sale['index']==0 and [sale['gold_before'],sale['gold_after'],sale['stock_before'],sale['stock_after']]==[5,6,12,13]
 assert sale['uid_before']==sale['uid_after']==301 and sale['rng_before']==sale['rng_after']
 assert buy['uid']=='u267' and buy['source_uid']=='u268' and buy['source_tier']==3 and [buy['gold_before'],buy['gold_after']]==[6,3]
 assert buy['next_uid_before']==buy['next_uid_after']==302 and buy['rng_before']==buy['rng_after']
 log=(e/'lava_rebuy_real_matrix.log').read_text();assert sha(log.encode())=='bf7a190086ada61f55d4fbd95a74fbb838872ce150d3918109e7aad0afc31257'
 acquisitions=[json.loads(line.removeprefix('ACQUIRED ')) for line in log.splitlines() if line.startswith('ACQUIRED ')]
 assert len(acquisitions)==1 and acquisitions[0]=={'id':'BG23_007','pool_after':12,'pool_before':13,'source_uid':'u268','tier':3,'token_uid':'u288','uid':'u301'}
 for marker in ['PASS purchase_no_second_stock_uid_rng_change','PASS distinct_uid_new_play_record_old_retirement_preserved','PASS actual_nonempty_enemy_combat','PASS next_recruit_original_lava_2_5_kept0_after_combat']:assert marker in log.splitlines()
 counts={k:v['passed_checks'] for k,v in final['tests'].items()};assert counts['lava_rebuy_real_matrix']==190 and sum(counts.values())==2907
 game=final['tests']['lava_rebuy_real_matrix']['result'];script_sha=sha(Path(__file__).read_bytes())
 text=f'''# 普通熔岩潜伏者：成熟暗潮下售后重购的有限验证

固定源码提交：{final['source_commit']}。源码 MANIFEST 保留原“未验收源码冻结”状态，不以文档改写它；本文件只记录随后实际完成的有限测试结果。

## 实际通过

- 一场四人真实房间，seed {case['seed']}。首次找 Lava 刷新 {case['pre_source_first_lava_rolls']} 次，随后找暗潮与另一 Lava 同店刷新 {case['pre_source_cooffer_rolls']} 次。首次购买 u68 发生在拥有暗潮前，不计作 active purchase。
- 暗潮 u268 成熟至3级仍在场。原生出售 index0 的 u68：金币5→6、该卡库存12→13、出售数0→1；UID游标301保持301，RNG保持不变。原 play 记录退休，退休凭证为 {sale['retirement']}。
- 当前暗潮 token 先公开施放：唯一新随从 BG23_007 / u301，库存13→12，UID游标变为302。这是正常 cast3 分配，不是出售或购买额外生成。
- 随后公开购买另一原始 shop 对象 u267：金币6→3，购买数2→3；UID游标302不变、RNG及原生库存无额外变化。只验证了 **1次成熟暗潮下的 active purchase**。
- 新 u267 的 play 认证记录与旧 u68 退休记录分离，旧引用不能重用。之后经过实际非空敌方战斗与下一招募，Lava仍为原始2/5、kept0，暗潮真实成长至4级。
- 已拥有 Lava、当前 token 尚在手的两次购买均消费前拒绝，完整状态不变。真实独立投影还验证了共享 stats/effects 引用拒绝，以及直接发证、施法、EOT、Generation和低层出售的权限拒绝。

Game实际190项；8项纯合同合计2717项（89/140/211/966/810/68/166/267），总计2907项。Game耗时 {game['elapsed']} 秒；采样进程组峰值RSS {game['sampled_process_group_peak_rss']} 字节，并非cgroup硬上限。最终独立审计9项 executed_validated、无遗漏。candidate与唯一独立恢复运行树均再次逐文件SHA核验一致；未创建第二run_tree。

## 明确保留的边界

第二offer u267在暗潮购买前已由原生商店创建并冻结保留；**没有验证售后刷新产生新offer**。本批使用原factory/add_hand及公开Coin施放的源前资金夹具，不是完全自然、无夹具的对局。激活后不改金币、RNG、库存、UID、等级或手牌来选择结果。

未重复旧三场Lava、八场Tier6等完整矩阵；不宣称当前token购买、多Lava、金色/三连、永久塑造法术、存档、UI、默认池、整个随从/法术/饰品家族或整局已验收。未注入真实容量128耗尽或原生半失败场景。旧备份及源码状态原样保留。

依据：GAMEPLAY_MATRIX_RESULT.json、GAMEPLAY_INDEPENDENT_VERIFICATION.json、GAMEPLAY_EVIDENCE.tar.xz内原始日志/审计。生成脚本 add_verified_cn_slice.py SHA256 {script_sha}。此时最终远端发布及新下载验证仍待执行。
'''
 put(p/'GAMEPLAY_VERIFIED_SLICE.md',text.encode())
 for n in ['FINAL_UPLOAD_METADATA.json','FINAL_PUBLICATION_FILES.json']:put(ROOT/(n.removesuffix('.json')+'_BEFORE_CN.json'),(ROOT/n).read_bytes())
 checksum(p);records=rows(p);oldmeta=read(ROOT/'FINAL_UPLOAD_METADATA_BEFORE_CN.json');early=read(ROOT/'RESTORE_RECEIPT_UPLOAD_METADATA.json');old={x['name']:x for x in early['records']}
 for n,row in old.items():
  b=(ROOT/'restore_receipt_package'/n).read_bytes();assert sha(b)==row['sha256'] and len(b)==row['bytes']
  if n!='SHA256SUMS.txt':assert (p/n).read_bytes()==b
 changed=[x for x in records if x['name'] not in old or x['sha256']!=old[x['name']]['sha256']]
 assert [x['name'] for x in changed if x['name'] in old]==['SHA256SUMS.txt']
 finalmeta={**oldmeta,'records':records,'changed_records':changed,'files':len(records),'bytes':sum(x['bytes'] for x in records),'cn_slice_script_sha256':script_sha}
 (ROOT/'FINAL_UPLOAD_METADATA.json').write_bytes(enc(finalmeta));(ROOT/'FINAL_PUBLICATION_FILES.json').write_bytes(enc(records))
 put(ROOT/'CN_SLICE_ADDITION_VERIFIED.json',enc({'status':'ACTUAL_RECEIPT_BACKED_CN_SLICE_ADDED','script_sha256':script_sha,'document_sha256':sha(text.encode()),'files':len(records),'bytes':finalmeta['bytes'],'early_nonchecksum_bytes_unchanged':True,'source_manifest_unchanged':True,'uploaded':False}))
 print(json.dumps({'files':len(records),'bytes':finalmeta['bytes'],'script_sha256':script_sha}))
if __name__=='__main__':main()
