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
packages=[('hopebringer_groundskeeper','3edd9d3870863a80bd4b5bebb96710ccc99c0029','20261108-hopebringer-groundskeeper','bfdc4dfd995abbe0f21c28b9b53f74a0786075aab175d4d26d3a63c45e3a8743',37)]
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--hopebringer-hoarder-recovery',type=Path,required=True,help='Directory containing the verified Hopebringer Hoarder baseline')
args=parser.parse_args()
baseline_root=args.hopebringer_hoarder_recovery.resolve()
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
b=baseline_root/'restored_hopebringer_hoarder_runtime'
bp=baseline_root/'hopebringer_hoarder/extracted/hopebringer_hoarder_20261108/SOURCE_MAP.json'
e=root/'hopebringer_groundskeeper/extracted/hopebringer_groundskeeper_20261108'
read=lambda p:json.loads(p.read_text())
bm=read(bp);eb=read(e/'BASE_MAP.json');em=read(e/'SOURCE_MAP.json')
assert bp.read_bytes()==(e/'BASE_MAP.json').read_bytes()
assert sha(bp.read_bytes())=='4f5ca51d64dfdc38e5d86c685b345a6eb45d133ab4b29c027b5df841de01394b'
assert sha((e/'SOURCE_MAP.json').read_bytes())=='e95f0659426776c1484f3f317b5404b247e74c30b3ce747f47008bd00e48901b'
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
out=root/'restored_hopebringer_groundskeeper_runtime';assert not out.exists();out.mkdir();provenance={}
for n,v in em.items():
 assert safe(n);src=e/'delta'/n if n in ed else b/n;target=out/n;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target);provenance[n]='hopebringer_groundskeeper_remote_delta' if n in ed else 'verified_hopebringer_hoarder_baseline'
assert inv(out)==em;assert inv(b)==actual
assert all(p.stat().st_nlink==1 for p in out.rglob('*') if p.is_file())
support=baseline_root/'HOPEBRINGER_HOARDER_REMOTE_CHAIN_VERIFICATION.json'
whole=root/'FRESH_WHOLE_CHAIN_VERIFICATION.json'
assert sha(whole.read_bytes())=='0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f'
wr=read(whole);prior=read(support);assert sha(support.read_bytes())=='70906205fd4767b90a5d45b399d525708ce85ea49c86cb4f796557ba75ef5c76'
assert prior['source_map_sha256']['hopebringer_hoarder']==sha(bp.read_bytes())
assert prior['prior_whole_chain_via_hopebringer_hooktail_to_hopebringer_hoarder_map_continuity'] is True
assert wr['final_source_map_sha256']=='afcfedcc2db16afaa31e2007e32c39dd63d6efef20fdcdfd975d7c5a97c67ad7'
assert wr['status']=='PASS_FRESH_FULL_CHAIN_SOURCE_BYTES' and wr['final_files']==27821 and wr['final_bytes']==1548444623
assert prior['source_map_sha256']['hopebringer_hooktail']=='31ff2f5b844400593f57f8dce4423ea64ea9f9a6c9cba986b1110de20aab04a7'
assert prior['supporting_prior_fresh_whole_chain_receipt_sha256']==sha(whole.read_bytes())
assert wr['increments'][-1]['commit']=='7e1804464d9f703161883e9371358f0e4525881f'
assert len(wr['increments'])==114
receipt={'status':'PASS_EXACT_SOURCE_ONLY','remote_packages':receipts,'source_map_sha256':{'hopebringer_hoarder':sha(bp.read_bytes()),'hopebringer_groundskeeper':sha((e/'SOURCE_MAP.json').read_bytes())},'hopebringer_hoarder_source_byte_equals_hopebringer_groundskeeper_base':True,'baseline_files_rehashed':len(bm),'baseline_unchanged_after_restore':True,'changes_companion_verified':True,'changes_companion_sha256':sha(cb),'change_lists':change_manifest,'removals_companion_verified':True,'removals_companion_sha256':sha(rb),'removed_source_files':removals,'delta_files':len(ed),'new_files':len(set(em)-set(bm)),'modified_files':len(set(actual_changes)&set(bm)),'redundant_unchanged_delta_files':sorted(redundant),'actual_changed_files':len(actual_changes),'removed_files':len(set(bm)-set(em)),'restored_files':len(em),'restored_bytes':sum(v['bytes'] for v in em.values()),'missing_files':[],'mismatched_files':[],'unexpected_files':[],'independent_copy_no_hardlinks':True,'historical_baseline_freshly_downloaded_by_this_helper':False,'supporting_prior_fresh_whole_chain_receipt_sha256':sha(whole.read_bytes()),'prior_whole_chain_via_hopebringer_hoarder_to_hopebringer_groundskeeper_map_continuity':True,'supporting_hopebringer_hoarder_chain_receipt_sha256':sha(support.read_bytes()) if support.exists() else None,'historical_baseline_provenance':'The baseline is the verified Hopebringer Hoarder baseline restored using the pinned recovery recipe referenced in RECOVERY.md. This helper freshly downloads the Hopebringer Groundskeeper increment and rehashes every supplied baseline file.','implementation_scope':'Source-byte verification only; Full gameplay acceptance is not claimed.','gameplay_test_run':False,'lost_november6_work_recovered':False,'all_prior_backups_preserved':True,'no_deletion_performed':True,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'HOPEBRINGER_GROUNDSKEEPER_REMOTE_CHAIN_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
(root/'RESTORE_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
