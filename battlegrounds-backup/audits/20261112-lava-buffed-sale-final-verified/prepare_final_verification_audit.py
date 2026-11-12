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
 for n in ['verify_final_publication.py','verify_failed_publication.py','packaging_common.py','run_remote_lava_buffed_sale.py','prepare_final_verification_audit.py','render_verified_slice.py']:
  put(p/n,(ROOT/'preparation'/n).read_bytes())
 text=f'''# 最终发布回读核验

发布 commit：{verified['commit']}；源码：{verified['source_commit']}。
结果：{a.outcome}；实际回读 {verified['files']} 文件、{verified['bytes']} bytes；所有归档成员数：{verified['archive_member_counts']}。

这里只证明发布字节与实际结果一致，不是再次运行Game。失败、未知和未运行必须分开。成功范围仅原Mini原token首cast原普通Lava永久4/5，再原生出售该buffed Lava。Mini留场，一次非空combat/nextrecruit发出原生新token但无Lava目标时cast held。未开放buffed Lava重买、金色、多个buff或新目标。暗潮的获取牌等级推进，不是随从星级变化。新pure实际计数为{runner.NEW_TEST_METADATA['pure_checks']}，旧11份纯合同3248项；未执行不得计入通过。旧source 610cad09/final 838043a与更早历史不改写。此审计包仍待上传和回读。
'''
 put(p/'README.md',text.encode());checksum(p);records=rows(p)
 put(ROOT/'FINAL_VERIFICATION_AUDIT_UPLOAD_METADATA.json',enc({'status':'LOCAL_AUDIT_READY_NOT_PUBLISHED','outcome':a.outcome,'source_commit':verified['source_commit'],'remote_folder':a.audit_remote_folder,'folder':a.audit_remote_folder,'files':len(records),'bytes':sum(row['bytes'] for row in records),'records':records}))
if __name__=='__main__':main()
