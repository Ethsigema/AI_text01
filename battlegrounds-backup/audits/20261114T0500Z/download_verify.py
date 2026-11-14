from pathlib import Path
import concurrent.futures, datetime, hashlib, json, subprocess

root=Path(__file__).resolve().parent
requests=json.loads((root/'DOWNLOAD_REQUESTS.json').read_text())

def get(item):
    target=root/item['filename']
    assert not target.exists(), str(target)
    target.parent.mkdir(parents=True,exist_ok=True)
    temporary=target.with_name(target.name+'.partial')
    result=subprocess.run(['curl','--fail','--location','--silent','--show-error','--max-time','900','--output',str(temporary),item['url']],capture_output=True,text=True)
    if result.returncode:
        return {**item,'status':'DOWNLOAD_FAILED','exit_code':result.returncode,'stderr':result.stderr}
    size=temporary.stat().st_size
    sha=hashlib.sha256();git=hashlib.sha1();git.update(f'blob {size}\0'.encode())
    with temporary.open('rb') as stream:
        while chunk:=stream.read(1024*1024):sha.update(chunk);git.update(chunk)
    valid=size==item['bytes'] and ('git_sha' not in item or git.hexdigest()==item['git_sha']) and ('sha256' not in item or sha.hexdigest()==item['sha256'])
    record={**item,'status':'PASS_DOWNLOADED_AND_HASHED' if valid else 'HASH_MISMATCH','downloaded_bytes':size,'downloaded_sha256':sha.hexdigest(),'downloaded_git_sha':git.hexdigest()}
    if valid:temporary.rename(target)
    print(json.dumps({'filename':item['filename'],'status':record['status'],'bytes':size}),flush=True)
    return record

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(get,requests))
report={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':records,'passed':sum(r['status']=='PASS_DOWNLOADED_AND_HASHED' for r in records),'requested':len(requests)}
(root/'FRESH_DOWNLOAD_VERIFIED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='records'}))
raise SystemExit(0 if report['passed']==report['requested'] else 1)

