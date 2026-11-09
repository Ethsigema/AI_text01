from pathlib import Path, PurePosixPath
import json, hashlib, tarfile, io, urllib.request, time, concurrent.futures, datetime, subprocess
R=Path(__file__).resolve().parent
OUT=R/'fresh_remote_readback'; OUT.mkdir(exist_ok=False)
PLAN=json.loads('{"folder": "battlegrounds-backup/pending/20261109-historical-tools-batch7-boundary-review-clean", "branch": "battlegrounds-recovery-20261103", "parent": "8e168c0c67b185a885c4e9251f728e3bde140cab", "tree": "705a8802a8c3f8f508941e0f8b048c2c39d9e105", "files": [{"name": "CHANGES.json", "bytes": 53, "sha256": "27223135250f2a76068e8147ec88a9d2b8fce0cf65d8e5fc4c7b09d179185a91", "git_sha": "e18672dcfb2b5a220575029f832aead3c5d5b254"}, {"name": "DEPENDENCIES.json", "bytes": 803, "sha256": "280dae5c0df857d22577a009f0295ef8b73f4f945925dcf4bf36f11313847e45", "git_sha": "1e809723e425d402a58567a2cf9c5d16550aced2"}, {"name": "DERIVATION.json", "bytes": 946, "sha256": "0882916128ed8962d287730c76dad8119056acae35a10f9210a96777b69f0703", "git_sha": "f53d1c6f324d9e5732d1be4d687644cbcccb0f9b"}, {"name": "MANIFEST.json", "bytes": 57467, "sha256": "7096fe066f7e08d2cac29753f689407fe0498167eb7864840b727fe30924e590", "git_sha": "c436110b35330f8d07a4d0223112bd1e836c40af"}, {"name": "README.md", "bytes": 5162, "sha256": "b9975e1c7573733c04e01423f6ced1bc6293b2a549934a6bf9f267b849bd5693", "git_sha": "dfad12ea67f54bc23d00b169d8f333a72f197af3"}, {"name": "RECOVERY.md", "bytes": 2207, "sha256": "25979ff6bddb5067c88e8a31f953ff4bd77f7df12ebd68242daaa109e40409d9", "git_sha": "391f26865e28b1a0858e6d4c02a6b28bd53912d8"}, {"name": "REMOVALS.json", "bytes": 3, "sha256": "37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570", "git_sha": "fe51488c7066f6687ef680d6bfaa4f7768ef205c"}, {"name": "SHA256SUMS.txt", "bytes": 1096, "sha256": "1920979d4fe71d42aa3bb6f3f706c112a3ae3a3b347c80283171e7512a73fbc8", "git_sha": "1ea52a0ab297638ced786919375a71f2549f5ae0"}, {"name": "historical_tools_batch7_boundary_review_nocache_20261109.tar.xz.part000", "bytes": 250000, "sha256": "2db2ca7c38506cb628bcfb60b929a6b69ee7522232009ce0cda656ea42375a1d", "git_sha": "3f1858f779ac9d72eebcb0cb0e4fc05f7a7748fe"}, {"name": "historical_tools_batch7_boundary_review_nocache_20261109.tar.xz.part001", "bytes": 250000, "sha256": "9245a8a24162b3239a8d7178d2ad142a125c2cf27eba9e201a4d2fc163174e95", "git_sha": "bc406432ab80d79b8258fcbc87f0ee4b97a9d259"}, {"name": "historical_tools_batch7_boundary_review_nocache_20261109.tar.xz.part002", "bytes": 250000, "sha256": "94caa8635f34804623bdfb277cd4c5a5620fc9cd82e78d118a167bbdb4f87b89", "git_sha": "18b2001baf5453d82207fcbf71e0a6260fedb11a"}, {"name": "historical_tools_batch7_boundary_review_nocache_20261109.tar.xz.part003", "bytes": 250000, "sha256": "56e40db477945162d01bbe35d35d9ae7951238c73d0554352c451a09fea4e876", "git_sha": "b93dbe856faf15c2d3b1e863f45ead8291c7e296"}, {"name": "historical_tools_batch7_boundary_review_nocache_20261109.tar.xz.part004", "bytes": 250000, "sha256": "6a0edafd0ef7fc6d7e103d3cadd0d79218d2e6e33ce17caeb7c5b603feeffa94", "git_sha": "0cd15c919837cd311295f730df85fb3f4cb53877"}, {"name": "historical_tools_batch7_boundary_review_nocache_20261109.tar.xz.part005", "bytes": 250000, "sha256": "b2099149b2b60d3216acc4427bb3541f754f61ca5ef1c3a0c2b3bc7d3b286c49", "git_sha": "5f0b8dbbc480395c6015a49e1596dccd89582a1d"}, {"name": "historical_tools_batch7_boundary_review_nocache_20261109.tar.xz.part006", "bytes": 139148, "sha256": "a7d1cfa7c279d7d2f0dbb7b575cb57657fb8fc40eb8c3e4ab4321d77a5b653e8", "git_sha": "e19f664d35f4aedb4ac46c4a899cf55113c14c68"}]}')
COMMIT='4608a9d229b7528b813bc8c4f5aaa23f025c0da0'
REPO='https://raw.githubusercontent.com/Ethsigema/AI_text01/'
downloads=[]
def meta(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def fetch(commit,folder,name,dest,expected=None):
 url=REPO+commit+'/'+folder+'/'+name
 for attempt in range(3):
  try:
   with urllib.request.urlopen(url,timeout=60) as r:b=r.read()
   break
  except Exception:
   if attempt==2:raise
   time.sleep(2*(attempt+1))
 value=meta(b)
 if expected:
  assert value=={k:expected[k] for k in ['bytes','sha256']},name
  if 'git_sha' in expected:assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==expected['git_sha']
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
 downloads.append({'url':url,'name':name,**value,'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
 return b
def batch(commit,folder,files,dest):
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:
  return list(e.map(lambda f:fetch(commit,folder,f['name'],dest/f['name'],f),files))
def read_archive(b,prefix,expected):
 actual={};content={}
 with tarfile.open(fileobj=io.BytesIO(b),mode='r:xz') as tf:
  for t in tf:
   assert t.isfile() and t.name not in actual
   p=PurePosixPath(t.name);assert not p.is_absolute() and '..' not in p.parts and p.parts[0]==prefix
   data=tf.extractfile(t).read();actual[t.name]=meta(data);content[t.name]=data
 assert actual==expected,{'missing':sorted(set(expected)-set(actual)),'extra':sorted(set(actual)-set(expected))}
 return content
def get_archive(commit,folder,manifest,dest):
 parts=batch(commit,folder,manifest['parts'],dest)
 b=b''.join(parts);assert meta(b)=={k:manifest[k] for k in ['bytes','sha256']}
 (dest/manifest['archive']).write_bytes(b)
 return b
batch(COMMIT,PLAN['folder'],PLAN['files'],OUT/'batch7')
m=json.loads((OUT/'batch7/MANIFEST.json').read_text());b=b''.join((OUT/'batch7'/p['name']).read_bytes() for p in m['parts'])
assert meta(b)=={k:m[k] for k in ['bytes','sha256']};(OUT/'batch7'/m['archive']).write_bytes(b)
prefix=m['archive'].removesuffix('.tar.xz');contents=read_archive(b,prefix,m['files'])
internal=json.loads(contents[prefix+'/FILE_MANIFEST.json']);assert {prefix+'/'+n:v for n,v in internal.items()}=={n:meta(v) for n,v in contents.items() if n!=prefix+'/FILE_MANIFEST.json'}
assert len(contents)==222 and len(internal)==221
assert all('/home/' not in n and '__pycache__' not in n and '/.godot/' not in n for n in contents)
ex=OUT/'extracted';ex.mkdir()
for name,data in contents.items():p=ex/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
r=subprocess.run(['python',str(ex/prefix/'verify_review.py')],capture_output=True,text=True,check=True);static=json.loads(r.stdout);assert static['checks']==170
dump(OUT/'STATIC_VERIFICATION.json',static)
print('PASS: fresh batch7 archive, 7 parts, 222 members, 221 internal manifest entries, 170 read-only checks',flush=True)
deps=m['dependencies'];d=deps['source_candidate'];cdir=OUT/'source_candidate'
mb=fetch(d['commit'],d['folder'],'MANIFEST.json',cdir/'MANIFEST.json');assert meta(mb)['sha256']==d['manifest_sha256'];cm=json.loads(mb)
cb=get_archive(d['commit'],d['folder'],cm,cdir);assert meta(cb)['sha256']==d['archive_sha256']
cp=cm['archive'].removesuffix('.tar.xz');cc=read_archive(cb,cp,cm['files']);ci=json.loads(cc[cp+'/PACKAGE_MANIFEST.json'])
assert {cp+'/'+n:v for n,v in ci.items()}=={n:meta(v) for n,v in cc.items() if n!=cp+'/PACKAGE_MANIFEST.json'}
source_map=cc[cp+'/SOURCE_MAP.json'];assert meta(source_map)['sha256']==d['source_map_sha256'] and source_map==contents[prefix+'/BASE_MAP.json']
receipt=json.loads(fetch(d['commit'],d['folder'],'DEVOURER_HISTORICAL_TOOL_STREAM_VERIFICATION.json',cdir/'DEVOURER_HISTORICAL_TOOL_STREAM_VERIFICATION.json'))
assert receipt['source_map_sha256']==d['source_map_sha256'] and receipt['remaining_missing_within_inventory_scope']==353 and receipt['full_game_validation_passed'] is False
print('PASS: fixed candidate archive, 11 parts, 137 members, 136 internal entries; exact source-map matches batch7 baseline',flush=True)
d=deps['previous_whole_chain_audit'];adir=OUT/'previous_audit'
mb=fetch(d['commit'],d['folder'],'ARCHIVE_MANIFEST.json',adir/'ARCHIVE_MANIFEST.json');assert meta(mb)['sha256']==d['manifest_sha256'];am=json.loads(mb)
eb=fetch(d['commit'],d['folder'],'EVIDENCE_MANIFEST.json',adir/'EVIDENCE_MANIFEST.json');assert meta(eb)['sha256']=='67366c26701e5e6cf182b2768c71a58e8bf4466eb2f28a2dde1df0587b5b0f37';em=json.loads(eb)
ab=get_archive(d['commit'],d['folder'],am,adir);assert meta(ab)['sha256']==d['archive_sha256']
ac=read_archive(ab,'night_backup_verification_evidence',{**{'night_backup_verification_evidence/'+n:v for n,v in em.items()},'night_backup_verification_evidence/EVIDENCE_MANIFEST.json':meta(eb)})
assert len(ac)==30 and ac['night_backup_verification_evidence/REBUILT_SOURCE_MAP_CURRENT.json']==source_map
audit=json.loads(ac['night_backup_verification_evidence/FRESH_WHOLE_CHAIN_VERIFICATION.json']);assert audit['status']=='PASS_FRESH_FULL_CHAIN_SOURCE_BYTES' and len(audit['increments'])==154
publication=fetch(d['commit'],d['folder'],'PUBLICATION_VERIFIED.md',adir/'PUBLICATION_VERIFIED.md')
missing=json.loads(fetch(d['commit'],d['folder'],'MISSING_ORIGINAL_BLOBS_CURRENT.json',adir/'MISSING_ORIGINAL_BLOBS_CURRENT.json'));assert missing['original_files_recovered'] is False
print('PASS: fixed preceding audit archive, 7 parts, 30 members; exact source map matches both packages',flush=True)
report={'status':'PASS_FRESH_REMOTE_READBACK_SANITIZED_BATCH7_AND_TWO_FIXED_DEPENDENCIES','commit':COMMIT,'folder':PLAN['folder'],'new_published_files_downloaded':len(PLAN['files']),'archive_name':m['archive'],**meta(b),'archive_parts_verified':len(m['parts']),'archive_members_verified':len(contents),'internal_manifest_entries_verified':len(internal),'read_only_static_checks':170,'dependency_source_candidate':{'commit':deps['source_candidate']['commit'],'archive_sha256':meta(cb)['sha256'],'parts_verified':len(cm['parts']),'members_verified':len(cc),'internal_manifest_entries_verified':len(ci)},'dependency_previous_audit':{'commit':d['commit'],'archive_sha256':meta(ab)['sha256'],'parts_verified':len(am['parts']),'members_verified':len(ac)},'all_three_source_maps_byte_identical':True,'source_map_sha256':meta(source_map)['sha256'],'source_map_files':len(json.loads(source_map)),'source_map_bytes':sum(x['bytes'] for x in json.loads(source_map).values()),'game_source_changes':{'added':0,'modified':0,'deleted':0},'removed_generated_files':128,'original_archive_preserved_not_published':True,'derived_archive_byte_identical_to_original':False,'remaining_missing_paths_within_original_scope':353,'newly_deferred_tools':2,'full_game_test_rerun':False,'whole_history_chain_rerun':False,'full_game_verified':False,'old_save_compatibility_verified':False,'older_154_layer_chain_evidence_reverified_but_not_rerun':True,'all_prior_backups_preserved':True,'downloads':sorted(downloads,key=lambda x:x['url']),'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
dump(R/'REMOTE_READBACK_VERIFIED.json',report)
print(json.dumps({k:v for k,v in report.items() if k!='downloads'},indent=2),flush=True)
