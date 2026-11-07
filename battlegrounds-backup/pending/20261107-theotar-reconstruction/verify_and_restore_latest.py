from pathlib import Path,PurePosixPath
import json,hashlib,urllib.request,tarfile,concurrent.futures,datetime,shutil
root=Path(__file__).resolve().parent;workspace=root
sha=lambda b:hashlib.sha256(b).hexdigest()
def safe(s):
 p=PurePosixPath(s);return bool(s)and not p.is_absolute()and'..'not in p.parts and'\\'not in s

def get(url,path):
 with urllib.request.urlopen(url,timeout=90)as r:b=r.read()
 with path.open('xb')as f:f.write(b)
 return b
packages=[('wrathguard','cf0a57917c570773382f8bcad5e33f86d141846f','20261107-wrathguard-new-reconstruction','9e96a7b8f3a182975bd1237a4e68259568a38530be3738478883f3b8d5943432',42),('theotar','8a746239fec90cbc37983da1e2c4e271a1b05bbc','20261107-theotar-reconstruction','ac02652611912136525b97bc1d309c4a0d4193c972933dedef572ac39ab16800',103)]
receipts=[]
for label,commit,folder,expected,count in packages:
 d=root/label;d.mkdir();url=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{commit}/battlegrounds-backup/pending/{folder}/'
 mb=get(url+'MANIFEST.json',d/'MANIFEST.json');m=json.loads(mb);assert m['sha256']==expected and len(m['files'])==count
 def part(p):
  assert safe(p['name'])and'/'not in p['name'];b=get(url+p['name'],d/p['name']);assert len(b)==p['bytes']and sha(b)==p['sha256'];return b
 with concurrent.futures.ThreadPoolExecutor(max_workers=4)as ex:blocks=list(ex.map(part,m['parts']))
 b=b''.join(blocks);assert len(b)==m['bytes']and sha(b)==expected
 archive=d/m['archive'];archive.write_bytes(b);dest=d/'extracted';dest.mkdir();seen={}
 with tarfile.open(archive)as t:
  for x in t:
   assert safe(x.name),x.name
   if x.isdir():continue
   assert x.isfile()and x.name not in seen,x.name
   v=t.extractfile(x).read();assert x.name in m['files'];meta=m['files'][x.name];assert len(v)==meta['bytes']and sha(v)==meta['sha256'],x.name
   p=dest/x.name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(v);seen[x.name]=meta
 assert seen==m['files']
 receipt={'package':label,'commit':commit,'repository_path':'battlegrounds-backup/pending/'+folder,'manifest_sha256':sha(mb),'archive':m['archive'],'archive_sha256':expected,'archive_bytes':len(b),'parts_verified':len(blocks),'members_verified':len(seen),'status':'FRESH_REMOTE_DOWNLOAD_AND_ALL_MEMBER_HASHES_VERIFIED'};receipts.append(receipt)
 (d/'REMOTE_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)
b=workspace/'restored_bloodbound_runtime';bp=workspace/'bloodbound_metadata/bloodbound_earrings_v1/SOURCE_MAP.json'
w=root/'wrathguard/extracted/wrathguard_rebuild_retry_20261107';t=root/'theotar/extracted/timewarp_theotar_rebuild_20261107'
read=lambda p:json.loads(p.read_text())
bm=read(bp);wb=read(w/'BASE_MAP.json');wm=read(w/'SOURCE_MAP.json');tb=read(t/'BASE_MAP.json');tm=read(t/'SOURCE_MAP.json');assert bm==wb and wm==tb
assert sha(bp.read_bytes())=='9a517b7c2e0ba0c14308248884696b008e5a6f0b500a1d1d97bcd53c4b7a9c71';assert sha((w/'SOURCE_MAP.json').read_bytes())=='e16ce2b99917f46f9492c0ad14f36060e0d90d19b76ae702fd13ebb9a51bfcd9';assert sha((t/'SOURCE_MAP.json').read_bytes())=='23c1cd9b8f037c39c7b748348312f3c5e327d35a471f9ded31b4e186574d0c8e'
def inv(d):
 out={}
 for p in d.rglob('*'):
  assert not p.is_symlink(),str(p)
  if p.is_file():out[p.relative_to(d).as_posix()]={'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
 return out
actual=inv(b);assert all(actual.get(n)==v for n,v in bm.items());extra=sorted(set(actual)-set(bm));assert all(n.startswith('.godot/')or n.endswith('.gd.uid')for n in extra)
wd=inv(w/'delta');td=inv(t/'delta');assert{**bm,**wd}==wm and{**wm,**td}==tm
out=root/'restored_theotar_runtime';assert not out.exists();out.mkdir();provenance={}
for n,v in tm.items():
 assert safe(n);src=t/'delta'/n if n in td else w/'delta'/n if n in wd else b/n;target=out/n;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target);provenance[n]='theotar_remote_delta'if n in td else'wrathguard_remote_delta'if n in wd else'previously_verified_bloodbound_baseline'
assert inv(out)==tm;assert inv(b)==actual
receipt={'status':'EXACT_SOURCE_RESTORED_FROM_FRESH_REMOTE_INCREMENTS_AND_PREVIOUSLY_VERIFIED_BASELINE','remote_packages':receipts,'source_map_sha256':{'bloodbound':sha(bp.read_bytes()),'wrathguard':sha((w/'SOURCE_MAP.json').read_bytes()),'theotar':sha((t/'SOURCE_MAP.json').read_bytes())},'map_equalities':{'bloodbound_source_equals_wrathguard_base':True,'wrathguard_source_equals_theotar_base':True},'baseline_manifest_files_verified':len(bm),'baseline_ignored_generated_extras':len(extra),'baseline_unchanged_after_restore':True,'restored_files':len(tm),'restored_bytes':sum(v['bytes']for v in tm.values()),'missing_files':[],'mismatched_files':[],'unexpected_files':[],'historical_baseline_freshly_downloaded_this_check':False,'historical_baseline_provenance':'Previously restored from November1 ZIP SHA25633b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c and Bloodbound main snapshot32180d3af0db59fb3374f53100f9eaa5bb62d26a; prior receipt checked27463files and70part manifests/103archive scans. Every baseline source byte rehashed during this check.','gameplay_test_run':False,'lost_november6_work_recovered':False,'all_prior_backups_preserved':True,'no_deletion_performed':True,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'REMOTE_CHAIN_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n');(root/'RESTORE_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n');(root/'IGNORED_BASELINE_GENERATED_FILES.json').write_text(json.dumps(extra,indent=2)+'\n');print(json.dumps(receipt),flush=True)
