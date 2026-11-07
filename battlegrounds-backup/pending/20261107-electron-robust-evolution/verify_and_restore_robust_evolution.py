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
packages=[('robust_evolution','d38e3502a2703839884e32855786913a0a514b57','20261107-electron-robust-evolution','cd625a1d580c75942e3b7a8f8fb39c773dad64fb1c85efdab1099dd1c8c5bc22',54)]
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--sale-transfer-recovery',type=Path,required=True,help='Directory containing the verified Electron Sale Transfer baseline')
args=parser.parse_args()
baseline_root=args.sale_transfer_recovery.resolve()
receipts=[]
for label,commit,folder,expected,count in packages:
 d=root/label;d.mkdir();url=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{commit}/battlegrounds-backup/pending/{folder}/'
 mb=get(url+'MANIFEST.json',d/'MANIFEST.json');m=json.loads(mb);assert m['sha256']==expected and len(m['files'])==count
 rb=get(url+'REMOVALS.json',d/'REMOVALS.json');rm=m['companion_files']['REMOVALS.json'];assert len(rb)==rm['bytes'] and sha(rb)==rm['sha256'];removals=json.loads(rb);assert removals==m['removed_source_files']==[]
 cb=get(url+'CHANGES.json',d/'CHANGES.json');cm=m['companion_files']['CHANGES.json'];assert len(cb)==cm['bytes'] and sha(cb)==cm['sha256'];change_manifest=json.loads(cb)
 def part(p):
  assert safe(p['name'])and'/'not in p['name'];b=get(url+p['name'],d/p['name']);assert len(b)==p['bytes']and sha(b)==p['sha256'];return b
 with concurrent.futures.ThreadPoolExecutor(max_workers=4)as ex:blocks=list(ex.map(part,m['parts']))
 b=b''.join(blocks);assert len(b)==m['bytes']and sha(b)==expected
 assert safe(m['archive']) and '/' not in m['archive']
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
b=baseline_root/'restored_sale_transfer_runtime'
bp=baseline_root/'sale_transfer/extracted/electron_sale_transfer_20261107/SOURCE_MAP.json'
e=root/'robust_evolution/extracted/electron_robust_evolution_20261107'
read=lambda p:json.loads(p.read_text())
bm=read(bp);eb=read(e/'BASE_MAP.json');em=read(e/'SOURCE_MAP.json')
assert bp.read_bytes()==(e/'BASE_MAP.json').read_bytes()
assert sha(bp.read_bytes())=='6f3b6db8269a0e7522b395b534b7ff0fc4bee76533c90e3a24856064737e6f1a'
assert sha((e/'SOURCE_MAP.json').read_bytes())=='7c6e3c37c5e2efe75c210b667a9e197f97bb8ae6cff6a9d17b5c9e7d66231297'
def inv(d):
 out={}
 for p in d.rglob('*'):
  assert not p.is_symlink(),str(p)
  if p.is_file():out[p.relative_to(d).as_posix()]={'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
 return out
actual=inv(b);assert actual==bm
ed=inv(e/'delta');assert ed==read(e/'SOURCE_DELTA.json')['changes']
assert ed=={n:v for n,v in em.items() if bm.get(n)!=v}
assert sorted(set(bm)-set(em))==removals
assert change_manifest['added']==sorted(set(em)-set(bm))
assert change_manifest['modified']==sorted(n for n in set(bm)&set(em) if bm[n]!=em[n])
assert change_manifest['removed']==removals
assert {**{n:v for n,v in bm.items() if n not in removals},**ed}==em
out=root/'restored_robust_evolution_runtime';assert not out.exists();out.mkdir();provenance={}
for n,v in em.items():
 assert safe(n);src=e/'delta'/n if n in ed else b/n;target=out/n;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target);provenance[n]='robust_evolution_remote_delta' if n in ed else 'verified_sale_transfer_baseline'
assert inv(out)==em;assert inv(b)==actual
assert all(p.stat().st_nlink==1 for p in out.rglob('*') if p.is_file())
support=baseline_root/'SALE_TRANSFER_REMOTE_CHAIN_VERIFICATION.json'
whole=baseline_root/'FRESH_WHOLE_CHAIN_VERIFICATION.json'
assert sha(whole.read_bytes())=='edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2'
wr=read(whole);prior=read(support);assert sha(support.read_bytes())=='e24d56d6b106897b3145cfa7d8f392da219a0581cff7b18572f4d6bfdebe6b98'
assert prior['source_map_sha256']['sale_transfer']==sha(bp.read_bytes())
assert prior['prior_whole_chain_via_molten_refresh_winds_to_sale_transfer_map_continuity'] is True
assert wr['final_source_map_sha256']=='2a72dcaf1d6166065182f3c40c2aadb115cd50b427a7687a667521719febd443'
assert prior['supporting_prior_fresh_whole_chain_receipt_sha256']==sha(whole.read_bytes())
receipt={'status':'PASS_EXACT_SOURCE_ONLY','remote_packages':receipts,'source_map_sha256':{'sale_transfer':sha(bp.read_bytes()),'robust_evolution':sha((e/'SOURCE_MAP.json').read_bytes())},'sale_transfer_source_byte_equals_robust_evolution_base':True,'baseline_files_rehashed':len(bm),'baseline_unchanged_after_restore':True,'changes_companion_verified':True,'changes_companion_sha256':sha(cb),'change_lists':change_manifest,'removals_companion_verified':True,'removals_companion_sha256':sha(rb),'removed_source_files':removals,'delta_files':len(ed),'new_files':len(set(em)-set(bm)),'modified_files':len(set(ed)&set(bm)),'removed_files':len(set(bm)-set(em)),'restored_files':len(em),'restored_bytes':sum(v['bytes'] for v in em.values()),'missing_files':[],'mismatched_files':[],'unexpected_files':[],'independent_copy_no_hardlinks':True,'historical_baseline_freshly_downloaded_by_this_helper':False,'supporting_prior_fresh_whole_chain_receipt_sha256':sha(whole.read_bytes()),'prior_whole_chain_via_molten_sale_transfer_to_robust_evolution_map_continuity':True,'supporting_sale_transfer_chain_receipt_sha256':sha(support.read_bytes()) if support.exists() else None,'historical_baseline_provenance':'The baseline is the verified Electron Sale Transfer baseline restored using the pinned recovery recipe referenced in RECOVERY.md. This helper freshly downloads the Electron Robust Evolution increment and rehashes every supplied baseline file.','implementation_scope':'Source-byte verification only; full gameplay acceptance is not claimed.','gameplay_test_run':False,'lost_november6_work_recovered':False,'all_prior_backups_preserved':True,'no_deletion_performed':True,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'ROBUST_EVOLUTION_REMOTE_CHAIN_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
(root/'RESTORE_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
