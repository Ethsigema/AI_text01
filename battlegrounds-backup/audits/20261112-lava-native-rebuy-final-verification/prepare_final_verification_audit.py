"""Freeze actual final-publication verification receipt; no prefilled result or upload."""
from packaging_common import *
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--execute',action='store_true',required=True);ap.add_argument('--audit-remote-folder',required=True);a=ap.parse_args()
 assert safe(a.audit_remote_folder) and a.audit_remote_folder.startswith('battlegrounds-backup/audits/')
 verified=read(ROOT/'FINAL_PUBLICATION_VERIFIED.json');assert verified['status']=='PASS_FINAL_PUBLICATION_FRESH_BYTES_ALL_ARCHIVE_MEMBERS'
 assert verified['outcome'] in ['success','failure'] and verified['gameplay_accepted']==(verified['outcome']=='success') and verified['game_started_by_this_verifier'] is False
 p=ROOT/'final_verification_audit';p.mkdir(exist_ok=False)
 for n in ['SOURCE_PUBLICATION.json','FINAL_PUBLICATION.json','FINAL_PUBLICATION_VERIFIED.json','CN_SLICE_ADDITION_VERIFIED.json','LOCAL_FINAL_PACKAGE_VERIFIED.json']:
  put(p/n,(ROOT/n).read_bytes())
 for n in ['FINAL_UPLOAD_METADATA.json','FINAL_PUBLICATION_FILES.json','FAILED_RUN_UPLOAD_METADATA.json','FAILED_RUN_PUBLICATION_FILES.json']:
  if (ROOT/n).exists():put(p/n,(ROOT/n).read_bytes())
 for n in ['verify_final_publication.py','packaging_common.py','run_remote_lava_rebuy.py','prepare_final_verification_audit.py','add_verified_cn_slice.py']:put(p/n,(ROOT/'preparation'/n).read_bytes())
 put(p/'README.md',f'# Actual final verification audit\n\nPublished commit {verified["commit"]}; source {verified["source_commit"]}. Outcome {verified["outcome"]}; actual downloaded files {verified["files"]}, bytes {verified["bytes"]}, archive member counts {verified["archive_member_counts"]}. Verification is bytes/evidence, not another Game run. One active purchase after a pre-source first buy only; second offer existed before sale. Coin fixture disclosed. No broad game acceptance. The Chinese slice addition script was created after the original GAMEPLAY archive; this audit now preserves its actual bytes plus CN_SLICE_ADDITION_VERIFIED and LOCAL_FINAL_PACKAGE_VERIFIED, not merely its hash. Final source/gameplay packages remain unchanged. Tools require original stage metadata and remote snapshot layout; do not overwrite existing attempt evidence. This audit upload is not yet verified.\n'.encode())
 checksum(p);records=rows(p);put(ROOT/'FINAL_VERIFICATION_AUDIT_UPLOAD_METADATA.json',enc({'status':'LOCAL_AUDIT_READY_NOT_PUBLISHED','remote_folder':a.audit_remote_folder,'folder':a.audit_remote_folder,'files':len(records),'bytes':sum(x['bytes'] for x in records),'records':records}))
if __name__=='__main__':main()
