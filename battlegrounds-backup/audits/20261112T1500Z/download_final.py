from pathlib import Path
import json,hashlib,subprocess,concurrent.futures,datetime
R=Path(__file__).resolve().parent;stage=R.parent/'develop_lava_permanent_v2_20261112'; rows=json.loads((stage/'FINAL_PUBLICATION_FILES.json').read_text());p=json.loads((stage/'FINAL_PUBLICATION.json').read_text());dest=R/'final_evidence_verified_attempt2';dest.mkdir();records=[]
def f(r):
 url='https://raw.githubusercontent.com/Ethsigema/AI_text01/'+p['commit']+'/'+p['remote_folder']+'/'+r['name'];q=dest/r['name'];subprocess.run(['curl','-fsSL','--retry','3','--max-time','300',url,'-o',str(q)],check=True);b=q.read_bytes();assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'];return dict(r,url=url)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:records=list(ex.map(f,rows))
for l in (dest/'SHA256SUMS.txt').read_text().splitlines():
 h,n=l.split('  ',1);assert hashlib.sha256((dest/n).read_bytes()).hexdigest()==h
for n in ['MANIFEST.json','SOURCE_MAP.json.gz','delta.tar.xz']:assert (dest/n).read_bytes()==(R/'candidate_package'/n).read_bytes()
(R/'FINAL_EVIDENCE_FRESH_VERIFIED.json').write_text(json.dumps({'status':'PASS_FRESH_FINAL_30_FILES_SHA_MATCH_AND_SOURCE_UNCHANGED','commit':p['commit'],'files':len(records),'bytes':sum(x['bytes'] for x in records),'records':records,'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
print('PASS',p['commit'],len(records))
