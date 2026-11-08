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
packages=[('sludge_hand','0479d2585fbd6132bbc47c16fee77e578308d76f','20261108-electron-sludge-hand','d9b490f000fd675332dcabd9ed6effa826a47d9ca379b1dfc31ae01a95ab46a9',37)]
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--corrupted-coin-recovery',type=Path,required=True,help='Directory containing the verified Electron Corrupted Coin baseline')
args=parser.parse_args()
baseline_root=args.corrupted_coin_recovery.resolve()
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
b=baseline_root/'restored_corrupted_coin_runtime'
bp=baseline_root/'corrupted_coin/extracted/electron_corrupted_coin_20261108/SOURCE_MAP.json'
e=root/'sludge_hand/extracted/electron_sludge_hand_20261108'
read=lambda p:json.loads(p.read_text())
bm=read(bp);eb=read(e/'BASE_MAP.json');em=read(e/'SOURCE_MAP.json')
assert bp.read_bytes()==(e/'BASE_MAP.json').read_bytes()
assert sha(bp.read_bytes())=='acfd9e487224daf05eb93e343f099fb26de584f3296c051a510fbb902736dce4'
assert sha((e/'SOURCE_MAP.json').read_bytes())=='c17a48a665b20e1c65ed4dcd771f0d04e4d4686a12d595d3db1295d8c2a917e9'
def inv(d):
 out={}
 for p in d.rglob('*'):
  assert not p.is_symlink(),str(p)
  if p.is_file():out[p.relative_to(d).as_posix()]={'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
 return out
actual=inv(b);assert actual==bm
ed=inv(e/'delta');assert ed==read(e/'SOURCE_DELTA.json')['changes']
actual_changes={n:v for n,v in em.items() if bm.get(n)!=v}
redundant={n:v for n,v in ed.items() if bm.get(n)==v}
assert redundant=={}
assert all(em.get(n)==v for n,v in redundant.items())
assert ed=={**actual_changes,**redundant}
assert sorted(set(bm)-set(em))==removals
assert change_manifest['added']==sorted(set(em)-set(bm))
assert change_manifest['modified']==sorted(n for n in set(bm)&set(em) if bm[n]!=em[n])
assert change_manifest['removed']==removals
assert {**{n:v for n,v in bm.items() if n not in removals},**ed}==em
out=root/'restored_sludge_hand_runtime';assert not out.exists();out.mkdir();provenance={}
for n,v in em.items():
 assert safe(n);src=e/'delta'/n if n in ed else b/n;target=out/n;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target);provenance[n]='sludge_hand_remote_delta' if n in ed else 'verified_corrupted_coin_baseline'
assert inv(out)==em;assert inv(b)==actual
assert all(p.stat().st_nlink==1 for p in out.rglob('*') if p.is_file())
support=baseline_root/'CORRUPTED_COIN_REMOTE_CHAIN_VERIFICATION.json'
whole=baseline_root/'FRESH_WHOLE_CHAIN_VERIFICATION.json'
assert sha(whole.read_bytes())=='47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7'
wr=read(whole);prior=read(support);assert sha(support.read_bytes())=='f13b7832136e98f1e2b56bf46b204992d30e42a97093635d190fe04eb60a7c99'
assert prior['source_map_sha256']['corrupted_coin']==sha(bp.read_bytes())
assert prior['prior_whole_chain_via_beetle_blessing_to_corrupted_coin_map_continuity'] is True
assert wr['final_source_map_sha256']=='64db47233c38a84eae77365374b1f834172c21b5cdafd2ec6c596a38c2cd0a5f'
assert prior['supporting_prior_fresh_whole_chain_receipt_sha256']==sha(whole.read_bytes())
receipt={'status':'PASS_EXACT_SOURCE_ONLY','remote_packages':receipts,'source_map_sha256':{'corrupted_coin':sha(bp.read_bytes()),'sludge_hand':sha((e/'SOURCE_MAP.json').read_bytes())},'corrupted_coin_source_byte_equals_sludge_hand_base':True,'baseline_files_rehashed':len(bm),'baseline_unchanged_after_restore':True,'changes_companion_verified':True,'changes_companion_sha256':sha(cb),'change_lists':change_manifest,'removals_companion_verified':True,'removals_companion_sha256':sha(rb),'removed_source_files':removals,'delta_files':len(ed),'new_files':len(set(em)-set(bm)),'modified_files':len(set(actual_changes)&set(bm)),'redundant_unchanged_delta_files':sorted(redundant),'actual_changed_files':len(actual_changes),'removed_files':len(set(bm)-set(em)),'restored_files':len(em),'restored_bytes':sum(v['bytes'] for v in em.values()),'missing_files':[],'mismatched_files':[],'unexpected_files':[],'independent_copy_no_hardlinks':True,'historical_baseline_freshly_downloaded_by_this_helper':False,'supporting_prior_fresh_whole_chain_receipt_sha256':sha(whole.read_bytes()),'prior_whole_chain_via_corrupted_coin_to_sludge_hand_map_continuity':True,'supporting_corrupted_coin_chain_receipt_sha256':sha(support.read_bytes()) if support.exists() else None,'historical_baseline_provenance':'The baseline is the verified Electron Corrupted Coin baseline restored using the pinned recovery recipe referenced in RECOVERY.md. This helper freshly downloads the Electron Sludge Hand increment and rehashes every supplied baseline file.','implementation_scope':'Source-byte verification only; Full gameplay acceptance is not claimed.','gameplay_test_run':False,'lost_november6_work_recovered':False,'all_prior_backups_preserved':True,'no_deletion_performed':True,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'SLUDGE_HAND_REMOTE_CHAIN_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
(root/'RESTORE_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
