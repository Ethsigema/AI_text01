#!/usr/bin/env python3
"""Low-disk baseline overlay capture and streamed reconstruction verification.
Verification reads every reconstructed file byte, but does not materialize or run a game.
"""
import argparse,hashlib,io,json,lzma,os,pathlib,re,stat,tarfile,zipfile
BASE_SHA='33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65'
BASE_URL='https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip'
BASE_ROOT='酒馆战棋_新范围半成品交接包_20261101'
SKIP={'.git','.godot','__pycache__'}
def safe(s):
 p=pathlib.PurePosixPath(s)
 if not s or s=='.' or '\x00' in s or p.is_absolute() or '..' in p.parts or '\\' in s or ':' in s or p.as_posix()!=s:raise ValueError('Unsafe/noncanonical path')
 return p

def digest(f):
 h=hashlib.sha256();n=0
 for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
 return {'size':n,'sha256':h.hexdigest()}
def filemeta(p):
 with open(p,'rb') as f:return digest(f)
def inventory(root):
 out={}
 for p in sorted(root.rglob('*')):
  rel=p.relative_to(root).as_posix()
  if any(x in SKIP for x in p.relative_to(root).parts) or p.name=='.DS_Store' or p.suffix=='.pyc':continue
  safe(rel)
  if p.is_symlink():raise ValueError('Symlink source')
  if p.is_dir():continue
  if not p.is_file():raise ValueError('Nonregular source')
  if p.name.lower() in {'.env','credentials','credentials.json','id_rsa','id_ed25519','hosts.yml'} or p.name.lower().startswith('.env.'):raise ValueError('Potential secret filename')
  out[rel]=filemeta(p)
 return out

def baseline(p):
 if filemeta(p)['sha256']!=BASE_SHA:raise ValueError('Wrong baseline SHA')
 z=zipfile.ZipFile(p)
 if len(z.namelist())!=len(set(z.namelist())):raise ValueError('Duplicate baseline entries')
 regular=set()
 for zi in z.infolist():
  name=zi.filename.rstrip('/') if zi.is_dir() else zi.filename
  q=safe(name)
  if not name.startswith(BASE_ROOT+'/'):raise ValueError('Baseline outside expected root')
  mode=stat.S_IFMT(zi.external_attr>>16)
  if zi.is_dir():
   if mode not in {0,stat.S_IFDIR}:raise ValueError('Invalid baseline directory type')
  else:
   if mode not in {0,stat.S_IFREG}:raise ValueError('Nonregular baseline entry')
   regular.add(name)
 for name in z.namelist():
  if any(p.as_posix() in regular for p in pathlib.PurePosixPath(name.rstrip('/')).parents):raise ValueError('Baseline parent conflict')
 return z

def build(a):
 root=a.root.resolve();out=a.archive.resolve()
 if not root.is_dir():raise ValueError('Source root must exist and be a directory')
 if out.exists() or out==root or root in out.parents:raise ValueError('Output exists or inside source')
 before=inventory(root);changed=[]
 with baseline(a.base_zip) as z:
  names=set(z.namelist())
  for rel,meta in before.items():
   name=BASE_ROOT+'/'+rel;identical=False
   if name in names:
    zi=z.getinfo(name)
    if stat.S_ISLNK(zi.external_attr>>16):raise ValueError('Baseline symlink')
    if zi.file_size==meta['size']:
     with z.open(zi) as f:identical=digest(f)==meta
   if not identical:changed.append(rel)
 m={'format':'battlegrounds-baseline-overlay-v1','created_utc':a.created_utc,'baseline':{'url':BASE_URL,'sha256':BASE_SHA,'zip_root':BASE_ROOT},'excluded_directory_names':sorted(SKIP),'files':before,'payload_paths':changed,'note':'All current files. Historical evidence is not fresh execution. Stream capture; derived caches excluded. Secret pattern scan covers changed payload only; unchanged baseline is already public.'}
 mb=(json.dumps(m,ensure_ascii=False,indent=2)+'\n').encode();prefix='battlegrounds-backup/snapshots/'+a.timestamp+'/'
 patterns=[re.compile(p) for p in [rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',rb'gh[pousr]_[A-Za-z0-9]{30,}',rb'github_pat_[A-Za-z0-9_]{40,}',rb'AKIA[0-9A-Z]{16}']]
 partial=out.with_name(out.name+'.partial')
 if partial.exists():raise ValueError('Partial capture already exists')
 with tarfile.open(partial,'x:xz',preset=1,dereference=True) as t:
  ti=tarfile.TarInfo(prefix+'manifest.json');ti.size=len(mb);t.addfile(ti,io.BytesIO(mb))
  for rel in changed:
   p=root/rel
   # Chunked secret scan with overlapping boundary; never prints matching bytes.
   tail=b''
   with p.open('rb') as f:
    for b in iter(lambda:f.read(1048576),b''):
     scan=tail+b
     if any(q.search(scan) for q in patterns):raise ValueError('Secret pattern in '+rel)
     tail=scan[-256:]
   if filemeta(p)!=before[rel]:raise ValueError('Changed before archive '+rel)
   t.add(p,arcname=prefix+'payload/'+rel,recursive=False)
  for name in ['snapshot.py','extract_backup.py','assemble_backup.py','stream_snapshot.py']:
   t.add(pathlib.Path(__file__).parent/name,arcname='battlegrounds-backup/tools/'+name,recursive=False)
  t.add(pathlib.Path(__file__).parent/'RESTORE.md',arcname='battlegrounds-backup/RESTORE.md',recursive=False)
 if inventory(root)!=before:raise ValueError('Changed during capture; do not publish')
 os.link(partial,out) # Atomic no-replace publication; retain own partial hardlink for audit.
 print(json.dumps({'files':len(before),'payload_files':len(changed),'payload_bytes':sum(before[x]['size'] for x in changed),'manifest_sha256':hashlib.sha256(mb).hexdigest(),'archive':filemeta(out)}))

def strict_json(raw):
 def pairs(items):
  d={}
  for k,v in items:
   if k in d:raise ValueError('Duplicate JSON key')
   d[k]=v
  return d
 return json.loads(raw,object_pairs_hook=pairs)

def strict_xz(path):
 d=lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
 with open(path,'rb') as f:
  while True:
   chunk=f.read(1048576)
   if not chunk:break
   if d.eof:raise ValueError('Trailing XZ data')
   d.decompress(chunk,max_length=1048576)
   while not d.needs_input and not d.eof:d.decompress(b'',max_length=1048576)
   if d.unused_data:raise ValueError('Trailing XZ data')
 if not d.eof:raise ValueError('Truncated XZ stream')

def verify(a):
 if filemeta(a.archive)['sha256']!=a.sha256:raise ValueError('Wrong archive SHA')
 strict_xz(a.archive)
 prefix='battlegrounds-backup/snapshots/'+a.timestamp+'/'
 m=None;mb=None;payload={};seen=set();runtime=None
 allowed_helpers={'battlegrounds-backup/tools/'+x for x in ['snapshot.py','extract_backup.py','assemble_backup.py','stream_snapshot.py']}|{'battlegrounds-backup/RESTORE.md'}
 with tarfile.open(a.archive,'r|xz') as t:
  for member in t:
   name=member.name;safe(name)
   if name in seen or not member.isfile():raise ValueError('Duplicate or nonregular archive entry')
   seen.add(name)
   with t.extractfile(member) as f:
    if name==prefix+'manifest.json':
     if m is not None:raise ValueError('Duplicate manifest')
     mb=f.read();m=strict_json(mb)
    elif name.startswith(prefix+'payload/'):
     rel=name[len(prefix+'payload/'):];safe(rel)
     if rel==a.runtime_manifest:
      b=f.read();runtime=b;payload[rel]={'size':len(b),'sha256':hashlib.sha256(b).hexdigest()}
     else:payload[rel]=digest(f)
    elif name in allowed_helpers or name in {prefix+'local_restore_verification.json',prefix+'source_integrity_restore_verification.json'}: digest(f)
    else:raise ValueError('Unexpected archive entry')
  if t.fileobj.tell()!=t.offset+512:raise ValueError('Missing first TAR end marker')
  padding=0
  for b in iter(lambda:t.fileobj.read(1048576),b''):
   if any(b):raise ValueError('Nonzero data after TAR end')
   padding+=len(b)
  if padding<512 or padding%512:raise ValueError('Missing or malformed TAR end padding')
 if m is None or m['format']!='battlegrounds-baseline-overlay-v1' or m['baseline']!={'url':BASE_URL,'sha256':BASE_SHA,'zip_root':BASE_ROOT}:raise ValueError('Invalid manifest')
 if set(m)!={'format','created_utc','baseline','excluded_directory_names','files','payload_paths','note'}:raise ValueError('Unknown manifest fields')
 if not isinstance(m['note'],str) or not isinstance(m['created_utc'],str):raise ValueError('Invalid manifest text types')
 if m['excluded_directory_names']!=sorted(SKIP):raise ValueError('Unknown exclusions')
 files=m['files'];expected=m['payload_paths']
 if not isinstance(files,dict) or not isinstance(expected,list):raise ValueError('Invalid files/payload types')
 if len(expected)!=len(set(expected)) or set(expected)!=set(payload) or not set(expected).issubset(files):raise ValueError('Missing/extra payload')
 for rel,meta in files.items():
  q=safe(rel)
  if any(p.as_posix() in files for p in q.parents if p.as_posix()!='.'):raise ValueError('File-parent conflict')
  if not isinstance(meta,dict) or set(meta)!={'size','sha256'} or type(meta['size']) is not int or meta['size']<0 or not re.fullmatch('[0-9a-f]{64}',meta['sha256']):raise ValueError('Invalid file metadata')
 actual={}
 with baseline(a.base_zip) as z:
  for rel,meta in files.items():
   if rel in payload:got=payload[rel]
   else:
    zi=z.getinfo(BASE_ROOT+'/'+rel)
    if stat.S_ISLNK(zi.external_attr>>16):raise ValueError('Baseline symlink')
    with z.open(zi) as f:
     if rel==a.runtime_manifest:
      runtime=f.read();got={'size':len(runtime),'sha256':hashlib.sha256(runtime).hexdigest()}
     else:got=digest(f)
   if got!=meta:raise ValueError('Reconstructed file mismatch '+rel)
   actual[rel]=got
 if runtime is None or hashlib.sha256(runtime).hexdigest()!=a.runtime_sha:raise ValueError('Runtime manifest mismatch')
 entries=strict_json(runtime);paths=set()
 for e in entries:
  if not isinstance(e,dict) or set(e)!={'path','size','sha256'} or type(e['size']) is not int or e['size']<0 or not isinstance(e['sha256'],str) or not re.fullmatch('[0-9a-f]{64}',e['sha256']):raise ValueError('Invalid runtime row')
  safe(e['path']);rel='游戏工程/'+e['path'];safe(rel)
  if rel in paths or actual.get(rel)!={'size':e['size'],'sha256':e['sha256']}:raise ValueError('Runtime source mismatch '+rel)
  paths.add(rel)
 scope={rel for rel in actual if rel.startswith(tuple('游戏工程/'+x+'/' for x in ['core','data','research','ui'])) or rel in {'游戏工程/project.godot','游戏工程/main.tscn'}}
 if scope!=paths:raise ValueError('Runtime file-set mismatch')
 print(json.dumps({'passed':True,'verification_mode':'streamed baseline+overlay reconstruction; no full tree materialized or game executed','verified_files':len(actual),'runtime_checked_files':len(paths),'manifest_sha256':hashlib.sha256(mb).hexdigest(),'runtime_manifest_sha256':a.runtime_sha,'archive_sha256':a.sha256,'payload_files':len(payload)}))

def main():
 p=argparse.ArgumentParser();s=p.add_subparsers(dest='command',required=True)
 b=s.add_parser('build');b.add_argument('--root',type=pathlib.Path,required=True);b.add_argument('--created-utc',required=True)
 v=s.add_parser('verify');v.add_argument('--sha256',required=True);v.add_argument('--runtime-manifest',required=True);v.add_argument('--runtime-sha',required=True)
 for q in [b,v]:q.add_argument('--base-zip',type=pathlib.Path,required=True);q.add_argument('--archive',type=pathlib.Path,required=True);q.add_argument('--timestamp',required=True)
 a=p.parse_args();safe(a.timestamp);{'build':build,'verify':verify}[a.command](a)
if __name__=='__main__':main()
