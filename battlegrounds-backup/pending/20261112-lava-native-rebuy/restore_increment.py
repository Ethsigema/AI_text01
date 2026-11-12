"""Restore the isolated Shatterer candidate from the fixed, verified base tree."""
from pathlib import Path,PurePosixPath
import argparse,gzip,hashlib,io,json,tarfile,datetime,os
def check(ok,message):
 if not ok:raise ValueError(message)
def h(b):return hashlib.sha256(b).hexdigest()
def safe(n):return bool(n) and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--base-tree',type=Path,required=True);p.add_argument('--base-map',type=Path,required=True);p.add_argument('--destination',type=Path,required=True);p.add_argument('--report',type=Path,required=True);a=p.parse_args();r=Path(__file__).resolve().parent
 check(a.base_tree.is_dir(),'Base tree missing');check(not a.destination.exists(),'Destination must not exist');check(not a.report.exists(),'Report must not exist')
 m=json.loads((r/'MANIFEST.json').read_text());bb=gzip.decompress(a.base_map.read_bytes());check(h(bb)==m['base_map_sha256'],'Base map mismatch');base=json.loads(bb);target=dict(base)
 for n in m['removed']:check(n in target,'Unknown removed path');target.pop(n)
 target.update(m['changed_files']);tb=(json.dumps(target,indent=2,sort_keys=True)+'\n').encode();check(h(tb)==m['source_map_sha256'],'Target map mismatch')
 check(all(safe(n) for n in set(base)|set(target)),'Unsafe map path')
 for n,v in base.items():
  q=a.base_tree/n;check(q.is_file() and not q.is_symlink(),'Base file missing: '+n);b=q.read_bytes();check({'bytes':len(b),'sha256':h(b)}==v,'Base file mismatch: '+n)
 archive=(r/'delta.tar.xz').read_bytes();check(len(archive)==m['archive_bytes'] and h(archive)==m['archive_sha256'],'Delta archive mismatch');delta={}
 with tarfile.open(fileobj=io.BytesIO(archive),mode='r:xz') as t:
  for x in t:
   check(x.isfile() and safe(x.name) and x.name not in delta,'Unsafe or duplicate member');b=t.extractfile(x).read();check(x.name in target and {'bytes':len(b),'sha256':h(b)}==target[x.name],'Delta member mismatch');delta[x.name]=b
 expected={n for n in target if target[n]!=base.get(n)};check(set(delta)==expected,'Delta file set mismatch')
 a.destination.mkdir(parents=True)
 for n,v in sorted(target.items()):
  b=delta[n] if n in delta else (a.base_tree/n).read_bytes();check({'bytes':len(b),'sha256':h(b)}==v,'Source bytes changed during restore');q=a.destination/n;q.parent.mkdir(parents=True,exist_ok=True)
  with q.open('xb') as f:f.write(b)
 actual={};aggregate=hashlib.sha256()
 for n,v in sorted(target.items()):
  q=a.destination/n;check(q.is_file() and not q.is_symlink(),'Invalid restored file');b=q.read_bytes();actual[n]={'bytes':len(b),'sha256':h(b)};check(actual[n]==v,'Restored file mismatch: '+n);aggregate.update(n.encode()+b'\0'+str(len(b)).encode()+b'\0'+b)
 check({q.relative_to(a.destination).as_posix() for q in a.destination.rglob('*') if q.is_file()}==set(target),'Unexpected restored files')
 report={'status':'PASS_INCREMENT_RESTORED_AND_EVERY_FILE_REHASHED','verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_files_verified':len(base),'target_files_verified':len(target),'target_bytes':sum(v['bytes'] for v in target.values()),'delta_files':len(delta),'source_map_sha256':h(tb),'aggregate_sha256':aggregate.hexdigest(),'missing':[],'mismatched':[],'extra':[],'gameplay_rerun_by_restore':False,'default_pool_promoted':False};a.report.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
