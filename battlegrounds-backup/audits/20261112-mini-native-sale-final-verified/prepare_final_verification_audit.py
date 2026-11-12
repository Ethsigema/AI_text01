"""Freeze actual success OR failure publication verification receipt, without uploading."""
from packaging_common import *
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--execute',action='store_true',required=True);ap.add_argument('--audit-remote-folder',required=True);ap.add_argument('--outcome',choices=['success','failure'],required=True);a=ap.parse_args()
 assert safe(a.audit_remote_folder) and a.audit_remote_folder.startswith('battlegrounds-backup/audits/')
 prefix='FINAL' if a.outcome=='success' else 'FAILED_RUN'
 verified=read(ROOT/(prefix+'_PUBLICATION_VERIFIED.json'));assert verified['status']=='PASS_FINAL_PUBLICATION_FRESH_BYTES_ALL_ARCHIVE_MEMBERS'
 assert verified['outcome']==a.outcome and verified['gameplay_accepted']==(a.outcome=='success') and verified['game_started_by_this_verifier'] is False
 assert verified['source_commit']==runner.FROZEN_SOURCE_COMMIT
 p=ROOT/'final_verification_audit';p.mkdir(exist_ok=False)
 for n in ['SOURCE_PUBLICATION.json',prefix+'_PUBLICATION.json',prefix+'_PUBLICATION_VERIFIED.json',prefix+'_UPLOAD_METADATA.json']:
  put(p/n,(ROOT/n).read_bytes())
 optional=ROOT/(prefix+'_PUBLICATION_FILES.json')
 if optional.exists():put(p/optional.name,optional.read_bytes())
 for n in ['verify_final_publication.py','verify_failed_publication.py','packaging_common.py','run_remote_mini_sale.py','prepare_final_verification_audit.py','render_verified_slice.py']:
  put(p/n,(ROOT/'preparation'/n).read_bytes())
 text=f'''# 最终发布回读核验

发布 commit：{verified['commit']}；源码：{verified['source_commit']}。
结果：{a.outcome}；实际回读 {verified['files']} 文件、{verified['bytes']} bytes；所有归档成员数：{verified['archive_member_counts']}。

这里只证明发布字节与原始实际结果一致，不是再次运行 Game。失败不得升级为成功，未运行项目不得计为通过。若实际成功，有限范围仍仅为单 Mini 出售后既有原 token 对原 Lava 同回合首次施法，一次战斗/招募、无 Mini 再发；不覆盖售后 unused expiry；preview 不是发牌。新 pure {runner.NEW_TEST_METADATA['pure_checks']} + 既有 3061 纯检查仅以实际执行回执为准。基线 source0b2962c / accepted final7f88ffc8 及更早失败证据保留，旧131项Game不重复。本审计包自身仍等待上传及回读。
'''
 put(p/'README.md',text.encode());checksum(p);records=rows(p)
 put(ROOT/'FINAL_VERIFICATION_AUDIT_UPLOAD_METADATA.json',enc({'status':'LOCAL_AUDIT_READY_NOT_PUBLISHED','outcome':a.outcome,'source_commit':verified['source_commit'],'remote_folder':a.audit_remote_folder,'folder':a.audit_remote_folder,'files':len(records),'bytes':sum(row['bytes'] for row in records),'records':records}))
if __name__=='__main__':main()
