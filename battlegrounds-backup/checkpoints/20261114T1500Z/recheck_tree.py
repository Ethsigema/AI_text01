from pathlib import Path
import json,gzip,hashlib,datetime
r=Path(__file__).resolve().parent;p=r/'package';m=json.loads((p/'MANIFEST.json').read_text());parts=[]
for x in m['manifest_parts']:
 b=(p/x['name']).read_bytes();assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'];parts.append(b)
raw=gzip.decompress(b''.join(parts));assert hashlib.sha256(raw).hexdigest()==m['target_manifest_sha256'];target=json.loads(raw);tree=r/'workspace/project';actual={};agg=hashlib.sha256()
for q in sorted(tree.rglob('*')):
 assert not q.is_symlink()
 if not q.is_file():continue
 n=q.relative_to(tree).as_posix();b=q.read_bytes();actual[n]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()};agg.update(n.encode()+b'\0'+str(len(b)).encode()+b'\0'+b)
assert actual==target
out={'status':'PASS_SECOND_INDEPENDENT_READ_ALL_SOURCE_FILES','files':len(actual),'bytes':sum(x['bytes'] for x in actual.values()),'aggregate_sha256':agg.hexdigest(),'manifest_sha256':hashlib.sha256(raw).hexdigest(),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'old_tree_reused':False,'gameplay_tested':False,'unknown_unuploaded_work_captured':False}
(r/'SECOND_SOURCE_RECHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
