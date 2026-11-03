#!/usr/bin/env python3
"""SHA-verified safe extraction for the game backup ZIP or solid TAR.XZ."""
import argparse,hashlib,pathlib,shutil,stat,tarfile,zipfile
p=argparse.ArgumentParser();p.add_argument('archive',type=pathlib.Path);p.add_argument('destination',type=pathlib.Path);p.add_argument('--sha256',required=True);a=p.parse_args()
h=hashlib.sha256()
with a.archive.open('rb') as f:
 for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
if h.hexdigest()!=a.sha256:raise SystemExit('Archive SHA256 mismatch')
if a.destination.exists():raise SystemExit('Destination exists; use a new path')
a.destination.mkdir(parents=True);seen=set();count=0

def target(name):
 q=pathlib.PurePosixPath(name)
 if not name or q.is_absolute() or '..' in q.parts or '\\' in name or name in seen:raise ValueError('Unsafe or duplicate archive path')
 seen.add(name);return a.destination/q

if a.archive.name.endswith('.zip'):
 with zipfile.ZipFile(a.archive) as z:
  for m in z.infolist():
   t=target(m.filename)
   if stat.S_ISLNK(m.external_attr>>16):raise ValueError('Symlinks rejected')
   if m.is_dir():t.mkdir(parents=True,exist_ok=True);continue
   t.parent.mkdir(parents=True,exist_ok=True)
   with z.open(m) as f,t.open('xb') as out:shutil.copyfileobj(f,out)
   count+=1
elif a.archive.name.endswith('.tar.xz'):
 with tarfile.open(a.archive,'r|xz') as tar:
  for m in tar:
   t=target(m.name)
   if m.isdir():t.mkdir(parents=True,exist_ok=True);continue
   if not m.isfile():raise ValueError('Only ordinary files and directories allowed')
   t.parent.mkdir(parents=True,exist_ok=True)
   with tar.extractfile(m) as f,t.open('xb') as out:shutil.copyfileobj(f,out)
   count+=1
else:raise ValueError('Unsupported archive format')
print('Verified extraction of',count,'files')
