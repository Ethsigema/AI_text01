from pathlib import Path
import json,gzip,hashlib,tarfile,zipfile,io,datetime
R=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def meta(b):return {'bytes':len(b),'sha256':sha(b)}
def enc(x):return (json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
def j(p):return json.loads(p.read_bytes())
def sums(p):
 names=set()
 for l in (p/'SHA256SUMS.txt').read_text().splitlines():
  h,n=l.split('  ',1);assert '/' not in n and n not in names;names.add(n);assert sha((p/n).read_bytes())==h
 assert names=={x.name for x in p.iterdir()}-{'SHA256SUMS.txt'}
def tar(b,expected):
 d={}
 with tarfile.open(fileobj=io.BytesIO(b),mode='r:xz') as t:
  for m in t:
   assert m.isfile() and m.name not in d and m.name in expected
   v=t.extractfile(m).read();assert meta(v)==expected[m.name];d[m.name]=v
 return d
receipt=j(R/'FRESH_DOWNLOAD_VERIFIED.json');assert receipt['files']==42
for r in receipt['records']:assert meta((R/r['filename']).read_bytes())=={'bytes':r['bytes'],'sha256':r['sha256']}
bp=R/'base_package';cp=R/'candidate_package';sums(bp);sums(cp)
bm=j(bp/'MANIFEST.json');cm=j(cp/'MANIFEST.json')
raw=gzip.decompress((bp/'SOURCE_MAP.json.gz').read_bytes());assert sha(raw)==bm['source_map_sha256']==cm['base_map_sha256'];base=json.loads(raw)
raw=gzip.decompress((bp/'BASE_MEMBERS.json.gz').read_bytes());assert sha(raw)==bm['base_members_sha256'];members=json.loads(raw)
blocks=[]
for p in bm['parts']:
 b=(bp/p['name']).read_bytes();assert meta(b)=={'bytes':p['bytes'],'sha256':p['sha256']};blocks.append(b)
b=b''.join(blocks);assert meta(b)=={'bytes':bm['archive_bytes'],'sha256':bm['archive_sha256']};payload=tar(b,base);assert set(payload)==set(base)-set(members)
assert meta((R/'original_release.zip').read_bytes())=={'bytes':bm['baseline_bytes'],'sha256':bm['baseline_sha256']}
target={k:v for k,v in base.items() if k not in cm['removed']};target.update(cm['changed_files']);assert len(set(cm['removed']))==len(cm['removed']) and set(cm['removed'])<=set(base)
assert not set(cm['removed'])&set(cm['changed_files']);assert {k for k in target if base.get(k)!=target[k]}==set(cm['changed_files'])
raw=gzip.decompress((cp/'SOURCE_MAP.json.gz').read_bytes());assert raw==enc(target) and sha(raw)==cm['source_map_sha256']
b=(cp/cm['archive']).read_bytes();assert meta(b)=={'bytes':cm['archive_bytes'],'sha256':cm['archive_sha256']};delta=tar(b,target);assert set(delta)==set(cm['changed_files'])
def verify(mapping,changed):
 h=hashlib.sha256();count=0
 with zipfile.ZipFile(R/'original_release.zip') as z:
  assert len(z.namelist())==len(set(z.namelist()))
  for n,m in sorted(mapping.items()):
   b=changed[n] if n in changed else z.read(members[n]) if n in members else payload[n]
   assert meta(b)==m,n;h.update(n.encode()+b'\0'+str(len(b)).encode()+b'\0'+b);count+=len(b)
 return {'files':len(mapping),'bytes':count,'aggregate_sha256':h.hexdigest()}
a=verify(base,{});assert a['files']==bm['source_files'] and a['bytes']==bm['source_bytes'];assert a['aggregate_sha256']=='5ba04ef124fc78cf20e2a942a60589fb92dc76e6808155648226a534a4599e05'
b=verify(target,delta);assert b['files']==cm['source_files'] and b['bytes']==cm['source_bytes'] and b['aggregate_sha256']==cm['aggregate_sha256']
out={'status':'PASS_FRESH_REMOTE_STREAMED_RECONSTRUCTION_ALL_FILE_BYTES','source_commit':'0b2962c294aa4c0e4354bdc119f2fecd732d3c03','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fresh_input_files':42,'fresh_input_bytes':receipt['bytes'],'base':a,'target':b,'source_map_sha256':cm['source_map_sha256'],'delta_sha256':cm['archive_sha256'],'changed_files':len(cm['changed_files']),'removed_files':cm['removed'],'new_complete_directory_created':False,'existing_source_tree_read':False,'gameplay_tested_by_this_audit':False,'old_backups_deleted':False,'missing':[],'mismatched':[]}
(R/'STREAM_RECONSTRUCTION_VERIFIED.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
