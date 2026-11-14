from pathlib import Path, PurePosixPath
import json, hashlib, gzip, tarfile, zipfile, datetime
R=Path(__file__).resolve().parent
def h(b):return hashlib.sha256(b).hexdigest()
def safe(n):return n and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n
evidence=[]
for stem in ['FIX_EVIDENCE','GAMEPLAY_EVIDENCE','TOOLS_EVIDENCE']:
 m=json.loads((R/'candidate'/f'{stem}_MANIFEST.json').read_text());members=m.get('members',m);archive=R/'candidate'/f'{stem}.tar.xz';actual={}
 if 'archive_sha256' in m:assert h(archive.read_bytes())==m['archive_sha256']
 with tarfile.open(archive,'r:xz') as t:
  for e in t:
   assert e.isfile() and safe(e.name) and e.name not in actual
   b=t.extractfile(e).read();actual[e.name]={'bytes':len(b),'sha256':h(b)}
 assert actual==members
 evidence.append({'archive':archive.name,'members':len(actual),'sha256':h(archive.read_bytes())})
parts=sorted((R/'published_map').glob('FULL_SOURCE_MAP.json.gz.part*'));assert len(parts)==6
published=b''.join(p.read_bytes() for p in parts)
assert h(published)=='a28a85fbd61e75546ac906223166709bf9e0d564847f5fa65971195888ea8c32'
assert published==(R/'FULL_SOURCE_MAP.json.gz').read_bytes()
expected=json.loads(gzip.decompress(published));actual={};agg=hashlib.sha256()
for p in sorted((R/'restored_current').rglob('*')):
 assert not p.is_symlink()
 if p.is_file():
  n=p.relative_to(R/'restored_current').as_posix();b=p.read_bytes();actual[n]={'bytes':len(b),'sha256':h(b)};agg.update(n.encode()+b'\0'+str(len(b)).encode()+b'\0'+b)
assert actual==expected
ledger=json.loads((R/'restored_current/docs/minion_acceptance/minion_acceptance_ledger.json').read_text())
report={'status':'PASS_FRESH_INPUTS_AND_NEW_FULL_DISK_RESTORE_MATCH_PUBLISHED_FROZEN_MAP','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_head':'2b69f534430148d2048903056448c838e4b9d7d9','files':len(actual),'bytes':sum(x['bytes'] for x in actual.values()),'aggregate_sha256':agg.hexdigest(),'compressed_map_sha256':h(published),'evidence_archives':evidence,'evidence_members':sum(x['members'] for x in evidence),'missing':[],'extra':[],'mismatched':[],'game_tested':False,'unknown_unuploaded_work_captured':False}
with (R/'FULL_CHAIN_CURRENT_VERIFIED.json').open('x') as f:f.write(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));print('LEDGER_TOP_LEVEL_KEYS',list(ledger))
