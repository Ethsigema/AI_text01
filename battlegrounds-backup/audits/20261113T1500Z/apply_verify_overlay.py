from pathlib import Path,PurePosixPath
import json,hashlib,gzip,zipfile,datetime
R=Path(__file__).resolve().parent;tree=R/'restored_current';sha=lambda b:hashlib.sha256(b).hexdigest();meta=lambda b:{'bytes':len(b),'sha256':sha(b)}
def safe(n):return n and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n
assert json.loads((R/'FRESH_DOWNLOAD_VERIFIED.json').read_text())['passed']==63
m=json.loads((R/'candidate/MANIFEST.json').read_text());expected=json.loads(gzip.decompress((R/'candidate/SOURCE_MAP.json.gz').read_bytes()));assert json.loads((R/'CANDIDATE_RESTORE_CURRENT.json').read_text())['aggregate_sha256']==m['aggregate_sha256']
for row in json.loads((R/'ledger/DEPENDENCIES.json').read_text())['dependencies']:
 p=R/row['file'].replace('base_package/','base/').replace('candidate_package/','candidate/');assert meta(p.read_bytes())=={'bytes':row['bytes'],'sha256':row['sha256']}
p=R/'ledger/minion_ledger_20261113_tooling_increment.zip';assert sha(p.read_bytes())=='bc94f25a2deeb2736fa541f88ffa3ea5cd4afe9dd3d7beeba50756b704a3a2c2'
adds={}
with zipfile.ZipFile(p) as z:
 assert len(z.namelist())==len(set(z.namelist()))
 for l in z.read('SHA256SUMS.txt').decode().splitlines():
  h,n=l.split('  ',1);assert safe(n) and sha(z.read(n))==h
 changes=json.loads(z.read('CHANGE_MANIFEST.json'));assert changes['removed_files']==[]
 for row in changes['added_files']:
  n=row['path'];b=z.read(n);assert len(b)==row['size'] and sha(b)==row['sha256']
  if not n.startswith('overlay/'):continue
  n=n[len('overlay/'):];assert safe(n) and n not in expected and not (tree/n).exists();adds[n]=meta(b);expected[n]=meta(b);q=tree/n;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(b)
actual={};agg=hashlib.sha256()
for p in sorted(tree.rglob('*')):
 assert not p.is_symlink()
 if not p.is_file():continue
 n=p.relative_to(tree).as_posix();b=p.read_bytes();actual[n]=meta(b);agg.update(n.encode()+b'\0'+str(len(b)).encode()+b'\0'+b)
assert actual==expected
raw=(json.dumps(actual,sort_keys=True,indent=2)+'\n').encode();(R/'FULL_SOURCE_MAP.json.gz').write_bytes(gzip.compress(raw,mtime=0))
report={'status':'PASS_NEW_DISK_RESTORE_BASE_CANDIDATE_AND_LEDGER_OVERLAY_ALL_FILES','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':'6a047aadfb2562c464bc06fd17777275c2a3b246','source_revision':'32a8b33abe2bfb980c5ec890e7950f6b5a9f1346','files':len(actual),'bytes':sum(v['bytes'] for v in actual.values()),'source_map_sha256':sha(raw),'aggregate_sha256':agg.hexdigest(),'overlay_added':adds,'removed':[],'missing':[],'extra':[],'mismatched':[],'unknown_unuploaded_work_captured':False,'gameplay_tested':False,'existing_tree_reused':False}
(R/'FULL_RESTORE_WITH_OVERLAY_VERIFIED.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
