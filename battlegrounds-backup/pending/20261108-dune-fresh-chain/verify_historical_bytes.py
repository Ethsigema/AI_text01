from pathlib import Path,PurePosixPath
import json,hashlib,base64,tarfile,zipfile,io
r=Path(__file__).resolve().parent
assert not (r/'restored_bloodbound_runtime').exists(),'Use a new directory; never overwrite a runtime'
base_zips=list((r/'baseline_download').glob('*.zip'));assert len(base_zips)==1
assert hashlib.sha256(base_zips[0].read_bytes()).hexdigest()=='33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65'
import subprocess
assert subprocess.check_output(['git','-C',str(r/'repository'),'rev-parse','HEAD'],text=True).strip()=='e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c'
assembled=r/'assembled';assembled.mkdir(exist_ok=True);checks=[];errors=[]
sha=lambda b:hashlib.sha256(b).hexdigest()
for mpath in list((r/'repository').rglob('*.json'))+list((r/'bloodbound').rglob('*.json')):
 try:m=json.loads(mpath.read_text())
 except:continue
 records=([m]+m.get("archives",[]))if isinstance(m,dict)else[]
 for m in records:
  if not isinstance(m,dict)or not isinstance(m.get('parts'),list)or not m['parts']or not isinstance(m['parts'][0],dict):continue
  if not any(k in m['parts'][0]for k in ['name','path'])or not any(k in m for k in ['archive','archive_name','name']):continue
  try:
   name=m.get('archive',m.get('archive_name',m.get('name')));name=Path(name).name;blocks=[]
   for part in m['parts']:
    p=mpath.parent/part.get('name',part.get('path'));data=p.read_bytes()if p.exists()else base64.b64decode((p.parent/(p.name+'.b64')).read_bytes())
    assert len(data)==part.get('bytes',part.get('size'))and sha(data)==part['sha256'];blocks.append(data)
   data=b''.join(blocks);h=m.get('sha256',m.get('archive_sha256'));n=m.get('bytes',m.get('archive_bytes',m.get('size')));assert sha(data)==h and len(data)==n
   out=assembled/(h[:16]+'_'+name);out.write_bytes(data);checks.append({'manifest':str(mpath.relative_to(r)),'sha256':h,'bytes':len(data)})
  except Exception as e:errors.append({'manifest':str(mpath.relative_to(r)),'error':str(e)})
# Exact committed checkpoint is the target definition.
blood=next(assembled.glob('79e518052ef139e2*'));metadata=r/'bloodbound_metadata';metadata.mkdir(exist_ok=True)
with tarfile.open(blood)as t:
 for member in t.getmembers():
  if not member.isfile():continue
  rel=PurePosixPath(member.name);assert not rel.is_absolute()and'..'not in rel.parts
  p=metadata/member.name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.extractfile(member).read())
target=json.loads((metadata/'bloodbound_earrings_v1/SOURCE_MAP.json').read_text());assert sha((metadata/'bloodbound_earrings_v1/SOURCE_MAP.json').read_bytes())=='9a517b7c2e0ba0c14308248884696b008e5a6f0b500a1d1d97bcd53c4b7a9c71'
byhash={};sizes={v['bytes']for v in target.values()}
for rel,v in target.items():
 assert not PurePosixPath(rel).is_absolute() and '..'not in PurePosixPath(rel).parts and '\\'not in rel
 byhash.setdefault(v['sha256'],[]).append(rel)
out=r/'restored_bloodbound_runtime';found={};seen=set();archives=[];nested=r/'nested_archives';nested.mkdir(exist_ok=True)
def accept(data,origin):
 h=sha(data)
 for rel in byhash.get(h,[]):
  if rel in found:continue
  assert len(data)==target[rel]['bytes'];found[rel]=origin

def scan(path,origin,depth=0):
 h=sha(path.read_bytes())
 if h in seen:return
 seen.add(h);archives.append({'origin':origin,'sha256':h,'depth':depth})
 try:
  if zipfile.is_zipfile(path):
   with zipfile.ZipFile(path)as z:
    for m in z.infolist():
     if m.is_dir():continue
     is_archive=m.filename.endswith(('.zip','.tar.xz','.tar.gz','.tgz'))
     if m.file_size in sizes or is_archive:
      data=z.read(m);accept(data,origin+'!'+m.filename)
      if is_archive and depth<5:
       q=nested/(sha(data)[:16]+'_'+Path(m.filename).name);q.write_bytes(data);scan(q,origin+'!'+m.filename,depth+1)
  elif tarfile.is_tarfile(path):
   with tarfile.open(path)as t:
    for m in t:
     if not m.isfile():continue
     is_archive=m.name.endswith(('.zip','.tar.xz','.tar.gz','.tgz'))
     if m.size in sizes or is_archive:
      data=t.extractfile(m).read();accept(data,origin+'!'+m.name)
      if is_archive and depth<5:
       q=nested/(sha(data)[:16]+'_'+Path(m.name).name);q.write_bytes(data);scan(q,origin+'!'+m.name,depth+1)
 except Exception as e:errors.append({'archive':origin,'error':str(e)})
inputs=list((r/'baseline_download').glob('*.zip'))+list(assembled.iterdir())+[p for p in(r/'repository').rglob('*')if p.is_file()and p.name.endswith(('.zip','.tar.xz','.tar.gz','.tgz'))]
for p in inputs:
 scan(p,str(p.relative_to(r)));print('SCAN',len(archives),'FOUND',len(found),'/',len(target),p.name,flush=True)
# Some committed plain files may be exact source bytes.
for root in [r/'repository',metadata]:
 for p in root.rglob('*'):
  if p.is_file()and'.git'not in p.parts and p.stat().st_size in sizes:accept(p.read_bytes(),str(p.relative_to(r)))
missing=sorted(set(target)-set(found));mismatch=[]
result={'files':len(found),'expected':len(target),'missing':missing,'mismatch':mismatch,'archive_errors':errors,'checked_archives':len(archives),'part_manifests':checks,'source_map_sha256':'9a517b7c2e0ba0c14308248884696b008e5a6f0b500a1d1d97bcd53c4b7a9c71'}
(r/'RESTORE_RESULT.json').write_text(json.dumps(result,indent=2));(r/'PROVENANCE.json').write_text(json.dumps(found,indent=2));(r/'ARCHIVE_SCANS.json').write_text(json.dumps(archives,indent=2));print(json.dumps({k:v for k,v in result.items()if k!='part_manifests'},indent=2));assert not missing and not mismatch and not errors
