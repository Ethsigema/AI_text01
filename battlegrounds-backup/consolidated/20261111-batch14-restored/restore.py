"""Restore this pinned incremental snapshot into a new directory. Python 3.12+."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,io,json,tarfile,zipfile,datetime,os,gzip
def check(ok,message):
 if not ok:raise ValueError(message)
def digest(data):return hashlib.sha256(data).hexdigest()
def file_digest(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def safe(name):
 p=PurePosixPath(name)
 return bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name
def main():
 a=argparse.ArgumentParser(description=__doc__)
 a.add_argument('--base-zip',type=Path,required=True)
 a.add_argument('--destination',type=Path,required=True)
 a.add_argument('--report',type=Path,required=True)
 args=a.parse_args();folder=Path(__file__).resolve().parent
 check(not args.destination.exists(),'Destination must not exist; nothing will be overwritten.')
 check(not args.report.exists(),'Report must not exist.')
 manifest=json.loads((folder/'MANIFEST.json').read_text())
 source_bytes=gzip.decompress((folder/'SOURCE_MAP.json.gz').read_bytes());base_bytes=gzip.decompress((folder/'BASE_MEMBERS.json.gz').read_bytes())
 check(digest(source_bytes)==manifest['source_map_sha256'],'Source map digest mismatch')
 check(digest(base_bytes)==manifest['base_members_sha256'],'Baseline map digest mismatch')
 source=json.loads(source_bytes);base=json.loads(base_bytes)
 check(set(base)<=set(source),'Baseline map has unknown target')
 check(all(safe(n) for n in source),'Unsafe target path')
 check(args.base_zip.stat().st_size==manifest['baseline_bytes'],'Baseline ZIP size mismatch')
 check(file_digest(args.base_zip)==manifest['baseline_sha256'],'Baseline ZIP digest mismatch')
 blocks=[]
 for p in manifest['parts']:
  check(safe(p['name']) and '/' not in p['name'],'Unsafe part path')
  b=(folder/p['name']).read_bytes();check(len(b)==p['bytes'] and digest(b)==p['sha256'],'Part mismatch: '+p['name']);blocks.append(b)
 archive=b''.join(blocks);check(len(archive)==manifest['archive_bytes'] and digest(archive)==manifest['archive_sha256'],'Archive mismatch')
 payload={}
 with tarfile.open(fileobj=io.BytesIO(archive),mode='r:xz') as t:
  for member in t:
   check(member.isfile() and safe(member.name) and member.name not in payload,'Unsafe or duplicate archive member')
   b=t.extractfile(member).read();check(member.name in source and {'bytes':len(b),'sha256':digest(b)}==source[member.name],'Payload mismatch: '+member.name);payload[member.name]=b
 check(set(payload)==set(source)-set(base),'Payload target set mismatch')
 args.destination.mkdir(parents=True)
 with zipfile.ZipFile(args.base_zip) as z:
  check(len(z.namelist())==len(set(z.namelist())),'Duplicate ZIP names')
  for name,meta in sorted(source.items()):
   data=z.read(base[name]) if name in base else payload[name]
   check({'bytes':len(data),'sha256':digest(data)}==meta,'Restored input mismatch: '+name)
   p=args.destination/name;p.parent.mkdir(parents=True,exist_ok=True)
   with p.open('xb') as f:f.write(data)
 # Re-read every output file from disk, independently of in-memory bytes.
 actual={};aggregate=hashlib.sha256()
 for name,meta in sorted(source.items()):
  p=args.destination/name;check(p.is_file() and not p.is_symlink(),'Missing or unsafe output: '+name)
  data=p.read_bytes();actual[name]={'bytes':len(data),'sha256':digest(data)}
  check(actual[name]==meta,'Disk output mismatch: '+name)
  aggregate.update(name.encode()+b'\0'+str(len(data)).encode()+b'\0'+data)
 paths=set()
 for root,dirs,files in os.walk(args.destination):
  for name in dirs:check(not (Path(root)/name).is_symlink(),'Symlink directory')
  paths.update((Path(root)/name).relative_to(args.destination).as_posix() for name in files)
 check(paths==set(source),'Output file set mismatch')
 report={'status':'PASS_ACTUAL_DISK_RESTORE_EVERY_FILE_REHASHED','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':len(actual),'bytes':sum(v['bytes'] for v in actual.values()),'source_map_sha256':digest(source_bytes),'aggregate_sha256':aggregate.hexdigest(),'baseline_sha256':manifest['baseline_sha256'],'payload_sha256':manifest['archive_sha256'],'parts':len(blocks),'payload_members':len(payload),'missing':[],'mismatched':[],'extra':[],'gameplay_tested':False,'old_save_tested':False}
 args.report.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
