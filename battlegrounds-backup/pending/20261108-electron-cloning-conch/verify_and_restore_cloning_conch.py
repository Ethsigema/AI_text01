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
packages=[('cloning_conch','730a84f6e10bd6debdb3cc144ca46fa527bdbce2','20261108-electron-cloning-conch','20427fe9c99003c39932cf902669651703e936b6b24d99c9f0cc9bb297968f77',56)]
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--recruitment-runtime',type=Path,required=True)
parser.add_argument('--deathrattle-package',type=Path,required=True)
parser.add_argument('--deathrattle-evidence',type=Path,required=True)
args=parser.parse_args()
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

read=lambda p:json.loads(p.read_text())
b=args.recruitment_runtime.resolve();d=args.deathrattle_package.resolve();e=root/'cloning_conch/extracted/electron_cloning_conch_20261108'
bp=d/'SOURCE_MAP.json';bm=read(bp);em=read(e/'SOURCE_MAP.json')
assert sha(bp.read_bytes())=='64db47233c38a84eae77365374b1f834172c21b5cdafd2ec6c596a38c2cd0a5f'
assert bp.read_bytes()==(e/'BASE_MAP.json').read_bytes()
assert sha((e/'SOURCE_MAP.json').read_bytes())=='4af4961f1d1b1f67ab9981f92bcd202553c8a35a9f2faa9a1f69bd47627883dd'
def inv(path):
 out={}
 for p in path.rglob('*'):
  assert not p.is_symlink()
  if p.is_file():out[p.relative_to(path).as_posix()]={'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
 return out
actual=inv(b);assert actual==read(d/'BASE_MAP.json')
dd=inv(d/'delta');assert dd==read(d/'SOURCE_DELTA.json')['changes'];assert {**actual,**dd}==bm
assert dd=={n:v for n,v in bm.items() if actual.get(n)!=v}
ed=inv(e/'delta');assert ed==read(e/'SOURCE_DELTA.json')['changes']=={n:v for n,v in em.items() if bm.get(n)!=v}
assert {**bm,**ed}==em and sorted(set(bm)-set(em))==removals==[]
assert change_manifest=={'added':sorted(set(em)-set(bm)),'modified':sorted(n for n in set(bm)&set(em) if bm[n]!=em[n]),'removed':[]}
def source(n):return d/'delta'/n if n in dd else b/n
for n,v in bm.items():
 assert safe(n);p=source(n);assert not p.is_symlink();data=p.read_bytes();assert {'bytes':len(data),'sha256':sha(data)}==v
support=args.deathrattle_evidence/'DEATHRATTLE_DISCOVER_REMOTE_CHAIN_VERIFICATION.json';whole=args.deathrattle_evidence/'FRESH_WHOLE_CHAIN_VERIFICATION.json'
assert sha(support.read_bytes())=='0d0a749024680d5e855fcc906bc445a7469dc484a84329dd4f6ecec72ef821d1'
assert sha(whole.read_bytes())=='47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7'
assert read(whole)['final_source_map_sha256']==sha(bp.read_bytes()) and read(whole)['status']=='PASS_FRESH_FULL_CHAIN_SOURCE_BYTES'
out=root/'restored_cloning_conch_runtime';out.mkdir();provenance={}
for n,v in em.items():
 assert safe(n);src=e/'delta'/n if n in ed else source(n);p=out/n;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,p);provenance[n]='fresh_conch_delta' if n in ed else ('reused_deathrattle_delta' if n in dd else 'reused_recruitment_runtime')
assert inv(out)==em and inv(b)==actual and inv(d/'delta')==dd
assert all(p.stat().st_nlink==1 for p in out.rglob('*') if p.is_file())
receipt={'status':'PASS_EXACT_SOURCE_ONLY','remote_packages':receipts,'source_map_sha256':{'deathrattle_discover':sha(bp.read_bytes()),'cloning_conch':sha((e/'SOURCE_MAP.json').read_bytes())},'baseline_files_rehashed':len(bm),'baseline_unchanged_after_restore':True,'baseline_composition':'Recruitment runtime plus Deathrattle delta; no pre-existing Deathrattle runtime directory','delta_files':len(ed),'new_files':len(set(em)-set(bm)),'modified_files':len(set(ed)&set(bm)),'removed_files':0,'change_lists':change_manifest,'changes_companion_sha256':sha(cb),'removals_companion_sha256':sha(rb),'restored_files':len(em),'restored_bytes':sum(v['bytes'] for v in em.values()),'missing_files':[],'mismatched_files':[],'unexpected_files':[],'independent_copy_no_hardlinks':True,'supporting_deathrattle_receipt_sha256':sha(support.read_bytes()),'supporting_prior_fresh_whole_chain_receipt_sha256':sha(whole.read_bytes()),'prior_whole_chain_to_cloning_conch_map_continuity':True,'historical_baseline_freshly_downloaded_by_this_helper':False,'historical_baseline_provenance':'Prior fresh full-chain proof through Deathrattle is reused. Only Cloning Conch is freshly downloaded this round; every composed baseline byte is rehashed.','gameplay_test_run':False,'no_deletion_performed':True,'all_prior_backups_preserved':True,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'CLONING_CONCH_REMOTE_CHAIN_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n')
(root/'RESTORE_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
