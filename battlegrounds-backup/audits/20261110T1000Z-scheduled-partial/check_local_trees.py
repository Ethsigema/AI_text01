import json,hashlib,os,time
from pathlib import Path
out=Path(__file__).parent
pairs=[('batch14_runtime',Path('historical_tools_batch14_20261109T191857Z/runtime'),Path('backup_batch14_20261109/fresh_remote_verification/REBUILT_SOURCE_MAP.json')),('xml_isolated_candidate',Path('backup_batch16_20261109/fresh_remote_verification/isolated_restored_candidate'),Path('backup_batch16_20261109/fresh_remote_verification/RESTORED_SOURCE_MAP.json'))]
results=[]
for label,root,mp in pairs:
 start=time.time(); data=json.loads(mp.read_text()); issues=[]; total=0; found=set(); digest=hashlib.sha256()
 for key in sorted(data):
  p=root/key; exp=data[key]
  if not p.is_file() or p.is_symlink():issues.append({'path':key,'problem':'missing_or_nonregular'});continue
  h=hashlib.sha256(); n=p.stat().st_size; digest.update(key.encode()+b'\0'+str(n).encode()+b'\0')
  with p.open('rb') as f:
   while b:=f.read(1024*1024):h.update(b);digest.update(b)
  total+=n;found.add(key)
  if n!=exp['bytes'] or h.hexdigest()!=exp['sha256']:issues.append({'path':key,'problem':'byte_mismatch'})
 extras=[]; caches=[]
 for base,dirs,files in os.walk(root):
  for name in files:
   rel=str((Path(base)/name).relative_to(root))
   if rel not in data:
    (caches if rel.startswith('.godot/') else extras).append(rel)
 r={'label':label,'root':str(root),'source_map':str(mp),'expected_files':len(data),'verified_files':len(found)-len(issues),'bytes':total,'source_stream_sha256':digest.hexdigest(),'issues':issues,'unlisted_files':extras,'cache_count':len(caches),'seconds':round(time.time()-start,2),'network_used':False,'new_full_restore':False,'game_test_run':False}
 results.append(r);print(json.dumps(r,ensure_ascii=False),flush=True)
(out/'LOCAL_KNOWN_TREES_REHASH.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
