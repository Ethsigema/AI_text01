#!/usr/bin/env python3
"""Join authenticated archive parts without overwriting an existing output."""
import argparse,hashlib,json,pathlib,os
p=argparse.ArgumentParser();p.add_argument('parts_manifest',type=pathlib.Path);p.add_argument('output',type=pathlib.Path);a=p.parse_args()
m=json.loads(a.parts_manifest.read_text());root=a.parts_manifest.resolve().parent
if a.output.exists():raise SystemExit('Output already exists; choose another filename')
if m['format']!='sha256-split-archive-v1':raise SystemExit('Unsupported format')
seen=set();total=0;all_hash=hashlib.sha256()
with a.output.open('xb') as out:
 for item in m['parts']:
  n=item['name'];q=pathlib.PurePosixPath(n)
  if len(q.parts)!=1 or n in seen or q.is_absolute() or '..' in q.parts:raise ValueError('Unsafe/duplicate part name')
  seen.add(n);f=root/n
  if f.is_symlink():raise ValueError('Symlink part')
  h=hashlib.sha256();size=0
  with f.open('rb') as inp:
   for b in iter(lambda:inp.read(1024*1024),b''):h.update(b);all_hash.update(b);size+=len(b);out.write(b)
  if size!=item['bytes'] or h.hexdigest()!=item['sha256']:raise ValueError('Part integrity mismatch: '+n)
  total+=size
 if total!=m['archive_bytes'] or all_hash.hexdigest()!=m['archive_sha256']:raise ValueError('Archive integrity mismatch')
print(json.dumps({'verified_archive_bytes':total,'verified_archive_sha256':all_hash.hexdigest(),'parts':len(m['parts'])}))
