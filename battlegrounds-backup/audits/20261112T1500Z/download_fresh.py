from pathlib import Path
import json,hashlib,subprocess,concurrent.futures,datetime
R=Path(__file__).resolve().parent
rows=json.loads((R/'REMOTE_FILES.json').read_text())
rows.append({'filename':'original_release.zip','size':324041102,'sha256':'33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65','download_url':'https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip'})
def download(row):
 p=R/row['filename'];p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists()
 partial=Path(str(p)+'.partial');assert not partial.exists()
 subprocess.run(['curl','-fsSL','--retry','3','--connect-timeout','30','--max-time','600',row['download_url'],'-o',str(partial)],check=True)
 b=partial.read_bytes();sha=hashlib.sha256(b).hexdigest();git=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
 assert len(b)==row['size'],row['filename']
 if 'sha' in row:assert git==row['sha'],row['filename']
 if 'sha256' in row:assert sha==row['sha256'],row['filename']
 partial.rename(p)
 out={'filename':row['filename'],'url':row['download_url'],'bytes':len(b),'sha256':sha,'git_sha':git,'git_sha_checked':'sha' in row,'status':'PASS_FRESH_DOWNLOAD_SIZE_AND_HASH'}
 print(out['filename'],out['status'],flush=True);return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:records=list(executor.map(download,rows))
report={'status':'PASS_CURRENT_ENVIRONMENT_FRESH_DOWNLOADS','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':len(records),'bytes':sum(x['bytes'] for x in records),'records':records,'old_download_bytes_reused':False,'old_restore_reports_reused':False}
with (R/'FRESH_DOWNLOAD_VERIFIED.json').open('x') as f:json.dump(report,f,indent=2)
print(report['status'],report['files'],report['bytes'],flush=True)
