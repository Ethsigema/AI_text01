"""Fresh single-tree restoration. Never modifies an existing tree or retries a partial workspace."""
from pathlib import Path,PurePosixPath
import argparse,json,gzip,hashlib,tarfile,io,os,subprocess,datetime,fcntl,stat,shutil
BASE_MAP='7fec8d69e82de8bfcb7373549951f9456671b5c3980135d6ec6f983a3daf5ed7'
BASE_AGG='5ba04ef124fc78cf20e2a942a60589fb92dc76e6808155648226a534a4599e05'
BASE_RESTORE='bff945ef0ba2745f42db7335f621b3737745103dc0df5451c2a6c93cbbdc9e97'
RELEASE_SHA='33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def enc(o):return (json.dumps(o,indent=2,sort_keys=True)+'\n').encode()
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(data):
 def unique(pairs):
  result={}
  for k,v in pairs:require(k not in result,'Duplicate JSON key');result[k]=v
  return result
 return json.loads(data,object_pairs_hook=unique)
def safe(n):
 return isinstance(n,str) and bool(n) and '\\' not in n and '\x00' not in n and not PurePosixPath(n).is_absolute() and all(x not in {'','.','..'} for x in n.split('/'))
def no_links(p):
 for q in [p,*p.parents]:require(not q.is_symlink(),'Symlink path: '+str(q))
def digest_file(p):
 no_links(p);require(p.is_file(),'Missing regular file: '+str(p))
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write_new(p,data):
 with p.open('xb') as f:f.write(enc(data))
def validate_map(m):
 require(isinstance(m,dict) and bool(m),'Empty/invalid map')
 for n,v in m.items():
  require(safe(n),'Unsafe map path');require(isinstance(v,dict) and set(v)=={'bytes','sha256'},'Invalid map record')
  require(type(v['bytes']) is int and v['bytes']>=0,'Invalid length');require(isinstance(v['sha256'],str) and len(v['sha256'])==64 and all(c in '0123456789abcdef' for c in v['sha256']),'Invalid digest')
  require(not any(str(q) in m for q in PurePosixPath(n).parents if str(q)!='.'),'File/directory collision')
def scan(tree,expected,aggregate):
 no_links(tree);require(tree.is_dir(),'Tree missing');actual={};h=hashlib.sha256()
 for p in sorted(tree.rglob('*'),key=lambda x:x.relative_to(tree).as_posix()):
  mode=p.lstat().st_mode;require(not stat.S_ISLNK(mode),'Tree symlink');require(stat.S_ISDIR(mode) or stat.S_ISREG(mode),'Special tree member')
  if not stat.S_ISREG(mode):continue
  n=p.relative_to(tree).as_posix();b=p.read_bytes();actual[n]={'bytes':len(b),'sha256':sha(b)};h.update(n.encode()+b'\0'+str(len(b)).encode()+b'\0'+b)
 require(actual==expected,'Full tree missing/extra/changed');require(h.hexdigest()==aggregate,'Aggregate mismatch')
 return {'files':len(actual),'bytes':sum(x['bytes'] for x in actual.values()),'aggregate_sha256':h.hexdigest(),'missing':[],'extra':[],'mismatched':[]}
def sums(directory):
 no_links(directory);require(directory.is_dir(),'Package missing');files={}
 for p in directory.iterdir():
  no_links(p);require(p.is_file(),'Non-file package entry');files[p.name]=p
 require('SHA256SUMS.txt' in files,'Missing checksums');seen=set()
 for line in files['SHA256SUMS.txt'].read_text().splitlines():
  h,n=line.split('  ',1);require(safe(n) and '/' not in n and n not in seen and n!='SHA256SUMS.txt','Unsafe/duplicate checksum');require(n in files and digest_file(files[n])==h,'Package checksum mismatch');seen.add(n)
 require(seen==set(files)-{'SHA256SUMS.txt'},'Checksum file set mismatch')
 return {n:{'bytes':p.stat().st_size,'sha256':digest_file(p)} for n,p in files.items()}
def target_and_delta(base,package):
 m=load((package/'MANIFEST.json').read_bytes());require(m['base_map_sha256']==BASE_MAP,'Wrong base map')
 require(m['base_content_commit']=='5143e8fb41bc8332ce4ba196144172167a74318c','Wrong base commit')
 require(isinstance(m['removed'],list) and len(set(m['removed']))==len(m['removed']),'Duplicate removals');require(all(safe(n) and n in base for n in m['removed']),'Unknown removal')
 require(isinstance(m['changed_files'],dict),'Invalid changes');require(not set(m['removed'])&set(m['changed_files']),'Removed/changed overlap')
 target={n:v for n,v in base.items() if n not in m['removed']};target.update(m['changed_files']);validate_map(target)
 raw=gzip.decompress((package/'SOURCE_MAP.json.gz').read_bytes());require(raw==enc(target) and sha(raw)==m['source_map_sha256'],'Target map mismatch')
 require(len(target)==m['source_files'] and sum(x['bytes'] for x in target.values())==m['source_bytes'],'Target totals mismatch')
 expected={n for n in target if base.get(n)!=target[n]};require(expected==set(m['changed_files']),'Redundant/incomplete changes')
 data=(package/'delta.tar.xz').read_bytes();require(m['archive']=='delta.tar.xz' and len(data)==m['archive_bytes'] and sha(data)==m['archive_sha256'],'Archive mismatch');delta={}
 with tarfile.open(fileobj=io.BytesIO(data),mode='r:xz') as t:
  for x in t:
   require(x.isfile() and safe(x.name) and x.name not in delta and x.name in expected,'Unsafe/duplicate/extra tar member')
   require(x.size==target[x.name]['bytes'],'Tar declared size mismatch');b=t.extractfile(x).read();require({'bytes':len(b),'sha256':sha(b)}==target[x.name],'Tar member mismatch');delta[x.name]=b
 require(set(delta)==expected,'Missing delta member');return m,target,delta

def apply_validated(tree,base,target,delta,removed,staging):
 """Only called on this invocation's newly restored and fully checked tree."""
 require(not staging.exists(),'Staging exists');staging.mkdir()
 # All changed bytes are validated and staged before any source mutation.
 for i,(n,b) in enumerate(sorted(delta.items())):
  require(safe(n) and {'bytes':len(b),'sha256':sha(b)}==target[n],'Changed bytes mismatch')
  with (staging/str(i)).open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())
 for n in removed:
  q=tree/n;no_links(q);require(q.is_file() and {'bytes':q.stat().st_size,'sha256':digest_file(q)}==base[n],'Removal preimage mismatch');q.unlink()
 for i,n in enumerate(sorted(delta)):
  q=tree/n;no_links(q);q.parent.mkdir(parents=True,exist_ok=True);no_links(q.parent)
  require(not q.exists() or q.is_file(),'Replacement is not a file');os.replace(staging/str(i),q)
 staging.rmdir()

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--base-package',required=True,type=Path);ap.add_argument('--release',required=True,type=Path);ap.add_argument('--candidate-package',required=True,type=Path);ap.add_argument('--new-workspace',required=True,type=Path);ap.add_argument('--lock-file',required=True,type=Path);ap.add_argument('--execute',action='store_true',required=True);a=ap.parse_args()
 for p in [a.base_package,a.release,a.candidate_package,a.new_workspace,a.lock_file]:no_links(p.absolute())
 basep=a.base_package.resolve();cp=a.candidate_package.resolve();release=a.release.resolve();work=a.new_workspace.absolute();require(not work.exists() and work.parent.is_dir(),'Workspace must be new with existing parent')
 require(not any(work.is_relative_to(p) or p.is_relative_to(work) for p in [basep,cp]),'Workspace/input overlap')
 require(a.lock_file.is_file(),'Existing common lock required')
 with a.lock_file.open('r') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  inputs={'base':sums(basep),'candidate':sums(cp)};require(len(inputs['base'])==24,'Expected complete 24-file baseline')
  require(digest_file(basep/'restore.py')==BASE_RESTORE,'Untrusted baseline restore program');require(release.stat().st_size==324041102 and digest_file(release)==RELEASE_SHA,'Release mismatch')
  raw=gzip.decompress((basep/'SOURCE_MAP.json.gz').read_bytes());require(sha(raw)==BASE_MAP,'Wrong fixed baseline map');base=load(raw);validate_map(base)
  m,target,delta=target_and_delta(base,cp)
  require(shutil.disk_usage(work.parent).free>sum(v['bytes'] for v in base.values())+sum(len(b) for b in delta.values())+256*1024**2,'Insufficient disk reserve')
  work.mkdir();tree=work/'restored_snapshot';write_new(work/'STARTED.json',{'status':'STARTED_NOT_VERIFIED','utc':utc(),'source_map_sha256':m['source_map_sha256'],'new_workspace':str(work),'inputs':inputs,'game_started':False})
  try:
   with (work/'BASE_RESTORE.log').open('x') as log:subprocess.run(['python',str(basep/'restore.py'),'--base-zip',str(release),'--destination',str(tree),'--report',str(work/'BASE_RESTORE_CURRENT.json')],stdout=log,stderr=subprocess.STDOUT,check=True)
   baseline=scan(tree,base,BASE_AGG);write_new(work/'BASE_FULL_CHECKPOINT.json',{'status':'PASS_FRESH_BASE_COMPLETE_BEFORE_INPLACE_DELTA','utc':utc(),'tree':baseline,'source_map_sha256':BASE_MAP})
   # Detect any input drift; never reinterpret changed inputs after baseline creation.
   require(sums(basep)==inputs['base'] and sums(cp)==inputs['candidate'],'Input drift')
   write_new(work/'APPLY_STARTED.json',{'utc':utc(),'status':'TARGET_NOT_YET_VERIFIED','changed':len(delta),'removed':m['removed']})
   apply_validated(tree,base,target,delta,m['removed'],work/'staged_delta')
   final=scan(tree,target,m['aggregate_sha256']);second=scan(tree,target,m['aggregate_sha256']);require(final==second,'Second scan mismatch')
   write_new(work/'SINGLE_TREE_RESTORE_VERIFIED.json',{'status':'PASS_FRESH_SINGLE_TREE_CUMULATIVE_RESTORE','utc':utc(),'source_map_sha256':m['source_map_sha256'],'base_checkpoint':baseline,'target':final,'second_independent_read':second,'one_tree_reused_only_within_new_workspace':True,'old_tree_modified':False,'game_started':False})
   print('PASS_FRESH_SINGLE_TREE_CUMULATIVE_RESTORE',str(tree),flush=True)
  except BaseException as e:
   write_new(work/'FAILED_RESTORE.json',{'utc':utc(),'status':'INCOMPLETE_RESTORE_NO_ACCEPTANCE_NO_AUTOMATIC_DELETE_OR_RETRY','error_type':type(e).__name__,'error':str(e),'old_tree_modified':False});raise
if __name__=='__main__':main()
