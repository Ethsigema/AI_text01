"""Restore original baseline + complete previous chain + this increment into a new directory. Python 3.12+."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,gzip,tarfile,io,zipfile,subprocess

def sha(b): return hashlib.sha256(b).hexdigest()
def safe(n): return bool(n) and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n

def main():
 p=argparse.ArgumentParser();p.add_argument('--inputs',type=Path,required=True);p.add_argument('--workspace',type=Path,required=True);a=p.parse_args();pkg=Path(__file__).resolve().parent
 assert not a.workspace.exists(),'Never overwrite an existing workspace'
 deps=json.loads((pkg/'DEPENDENCIES.json').read_text())
 for r in deps:
  q=a.inputs/r['filename'];b=q.read_bytes();assert len(b)==r['bytes'],r['filename'];assert sha(b)==r['sha256'],r['filename']
 m=json.loads((pkg/'MANIFEST.json').read_text())
 blobs=[]
 for entry in m['manifest_parts']:
  b=(pkg/entry['name']).read_bytes();assert len(b)==entry['bytes'] and sha(b)==entry['sha256'];blobs.append(b)
 target_raw=gzip.decompress(b''.join(blobs));assert sha(target_raw)==m['target_manifest_sha256'];target=json.loads(target_raw)
 archive=(pkg/'delta.tar.xz').read_bytes();assert sha(archive)==m['delta_sha256'] and len(archive)==m['delta_bytes']
 for n in target: assert safe(n)
 a.workspace.mkdir(parents=True)
 subprocess.run(['python3',str(a.inputs/'growth/restore.py'),'--inputs',str(a.inputs),'--workspace',str(a.workspace/'growth_restore')],check=True)
 root=a.workspace/'project';(a.workspace/'growth_restore/project').rename(root)
 before={q.relative_to(root).as_posix():{'bytes':q.stat().st_size,'sha256':sha(q.read_bytes())} for q in root.rglob('*') if q.is_file()}
 before_raw=(json.dumps(before,sort_keys=True,indent=2)+'\n').encode();assert sha(before_raw)==m['base_manifest_sha256']
 for n in m['removed']:
  assert safe(n) and n in before and n not in target;(root/n).unlink()
 expected={n for n in target if target[n]!=before.get(n)};seen=set()
 with tarfile.open(fileobj=io.BytesIO(archive),mode='r:xz') as t:
  for member in t:
   n=member.name;assert member.isfile() and safe(n) and n in expected and n not in seen;seen.add(n);b=t.extractfile(member).read();assert target[n]=={'bytes':len(b),'sha256':sha(b)};q=root/n;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b)
 assert seen==expected
 actual={q.relative_to(root).as_posix():{'bytes':q.stat().st_size,'sha256':sha(q.read_bytes())} for q in root.rglob('*') if q.is_file()}
 assert actual==target,'Restored path/size/SHA256 differs from target'
 report={'status':'PASS_FRESH_COMPLETE_CHAIN_RESTORED_AND_EVERY_FILE_REHASHED','files':len(actual),'bytes':sum(v['bytes'] for v in actual.values()),'changed':len(expected),'removed':len(m['removed']),'missing':[],'extra':[],'mismatched':[],'gameplay_accepted':False,'unknown_unuploaded_work_captured':False}
 (a.workspace/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':main()
