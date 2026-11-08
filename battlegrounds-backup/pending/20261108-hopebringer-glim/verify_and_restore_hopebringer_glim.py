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
packages=[('hopebringer_glim','171a5d0ed41f3b1d2b897bd4107eca5804c496ce','20261108-hopebringer-glim','23d9b34f6db77f0bbf928ed7cd53f9b7cc80cd64586d4c889969de253103dcb7',36)]
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--hopebringer-bat-recovery',type=Path,required=True,help='Directory containing the verified Hopebringer Bat baseline')
args=parser.parse_args()
baseline_root=args.hopebringer_bat_recovery.resolve()
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
b=baseline_root/'restored_hopebringer_bat_runtime'
bp=baseline_root/'hopebringer_bat/extracted/hopebringer_bat_20261108/SOURCE_MAP.json'
e=root/'hopebringer_glim/extracted/hopebringer_glim_20261108'
read=lambda p:json.loads(p.read_text())
bm=read(bp);eb=read(e/'BASE_MAP.json');em=read(e/'SOURCE_MAP.json')
assert bp.read_bytes()==(e/'BASE_MAP.json').read_bytes()
assert sha(bp.read_bytes())=='55bfec869fd2b4c1868b7d61028118375ae2eac626f8624b2c8ebee640e2dd80'
assert sha((e/'SOURCE_MAP.json').read_bytes())=='6317c4fa555653bb258ce726b19dbfd2881980bc082e5f406bee60921357af90'
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
out=root/'restored_hopebringer_glim_runtime';assert not out.exists();out.mkdir();provenance={}
for n,v in em.items():
 assert safe(n);src=e/'delta'/n if n in ed else b/n;target=out/n;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target);provenance[n]='hopebringer_glim_remote_delta' if n in ed else 'verified_hopebringer_bat_baseline'
assert inv(out)==em;assert inv(b)==actual
assert all(p.stat().st_nlink==1 for p in out.rglob('*') if p.is_file())
support=baseline_root/'HOPEBRINGER_BAT_REMOTE_CHAIN_VERIFICATION.json'
whole=root/'FRESH_WHOLE_CHAIN_VERIFICATION.json'
assert sha(whole.read_bytes())=='18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d'
wr=read(whole);prior=read(support);assert sha(support.read_bytes())=='a742fc36f702934b4e7911048c30d263556c17a16529e7680fcfe599725bbbe3'
assert prior['source_map_sha256']['hopebringer_bat']==sha(bp.read_bytes())
assert prior['prior_whole_chain_via_hopebringer_wolf_to_hopebringer_bat_map_continuity'] is True
assert wr['final_source_map_sha256']=='467c0fb627a95430f5c8bee36b81e9170f8700b9860e8d3ae244840173445cf3'
assert wr['status']=='PASS_FRESH_FULL_CHAIN_SOURCE_BYTES' and wr['final_files']==27778 and wr['final_bytes']==1548305970
assert prior['source_map_sha256']['hopebringer_wolf']=='ebb7c3b356e7f04caecdd0839354579d1c98d6a38bed50be642c3a1e91d33282'
assert prior['supporting_prior_fresh_whole_chain_receipt_sha256']==sha(whole.read_bytes())
receipt={'status':'PASS_EXACT_SOURCE_ONLY','remote_packages':receipts,'source_map_sha256':{'hopebringer_bat':sha(bp.read_bytes()),'hopebringer_glim':sha((e/'SOURCE_MAP.json').read_bytes())},'hopebringer_bat_source_byte_equals_hopebringer_glim_base':True,'baseline_files_rehashed':len(bm),'baseline_unchanged_after_restore':True,'changes_companion_verified':True,'changes_companion_sha256':sha(cb),'change_lists':change_manifest,'removals_companion_verified':True,'removals_companion_sha256':sha(rb),'removed_source_files':removals,'delta_files':len(ed),'new_files':len(set(em)-set(bm)),'modified_files':len(set(actual_changes)&set(bm)),'redundant_unchanged_delta_files':sorted(redundant),'actual_changed_files':len(actual_changes),'removed_files':len(set(bm)-set(em)),'restored_files':len(em),'restored_bytes':sum(v['bytes'] for v in em.values()),'missing_files':[],'mismatched_files':[],'unexpected_files':[],'independent_copy_no_hardlinks':True,'historical_baseline_freshly_downloaded_by_this_helper':False,'supporting_prior_fresh_whole_chain_receipt_sha256':sha(whole.read_bytes()),'prior_whole_chain_via_hopebringer_bat_to_hopebringer_glim_map_continuity':True,'supporting_hopebringer_bat_chain_receipt_sha256':sha(support.read_bytes()) if support.exists() else None,'historical_baseline_provenance':'The baseline is the verified Hopebringer Bat baseline restored using the pinned recovery recipe referenced in RECOVERY.md. This helper freshly downloads the Hopebringer Glim increment and rehashes every supplied baseline file.','implementation_scope':'Source-byte verification only; Full gameplay acceptance is not claimed.','gameplay_test_run':False,'lost_november6_work_recovered':False,'all_prior_backups_preserved':True,'no_deletion_performed':True,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'HOPEBRINGER_GLIM_REMOTE_CHAIN_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
(root/'RESTORE_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
