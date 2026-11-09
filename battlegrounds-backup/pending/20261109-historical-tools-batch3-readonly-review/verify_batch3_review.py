#!/usr/bin/env python3
"""Verify pinned readonly review archive and fixed input dependency. No runtime reconstruction, full-chain rerun, candidate Python execution or gameplay."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,tarfile,os,datetime,urllib.request,shutil
COMMIT='b78e979c5a64f79daa265196b50105b535953f27'
REPO_PATH='battlegrounds-backup/pending/20261109-historical-tools-batch3-readonly-review'
PACKAGE='historical_tools_batch3_review_20261109'
BASE_URL=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{COMMIT}/{REPO_PATH}/'
ARCHIVE_SHA='fa8ac41ae7131166487aebeecbd1d1b541ea259ebf8b2f00f438209ad1178663'
MANIFEST_SHA='1a1fbd4339a32ecd3c93f804d99b2f121eb20acbe7958114708fb6595cfd98d3'
INPUT_COMMIT='8a675dc886b8686e6bdd9a47463366cafb9c020f'
INPUT_ROOT='historical_tools_batch2_four_candidate_20261109'
INPUT_ARCHIVE_SHA='51263c49a09a0a735a417e147e4f64f0529be4d5fa12529807653da7187693eb'
INPUT_MANIFEST_SHA='26e1d37470f663358cc246c5a860d0d563b1eae60a3729f466f2080546ed678b'
INPUT_RECEIPT_SHA='45c8d5c2837861e93d92c59df791c967a226d072decbaa34f59b6f5672f35b97'
INPUT_MAP_SHA='3581d683af1a208f00c3dd853e268d799abc5e2811847954a339cad2a68434ea'
INPUT_URL=f'https://raw.githubusercontent.com/Ethsigema/AI_text01/{INPUT_COMMIT}/battlegrounds-backup/pending/20261109-historical-tools-batch2-four-candidate/'
def require(ok,message):
 if not ok: raise ValueError(message)
def sha(b):return hashlib.sha256(b).hexdigest()
def meta(b):return {'bytes':len(b),'sha256':sha(b)}
def safe(name):
 p=PurePosixPath(name);return bool(name) and not p.is_absolute() and '..' not in p.parts and '\\' not in name and str(p)==name

def file_meta(path):
 require(path.is_file() and not path.is_symlink(),'Not a regular file: '+str(path));digest=hashlib.sha256();count=0
 with path.open('rb') as h:
  for b in iter(lambda:h.read(1024*1024),b''):digest.update(b);count+=len(b)
 return {'bytes':count,'sha256':digest.hexdigest()}
def read_json(p):return json.loads(p.read_text())
def get(url,path):
 with urllib.request.urlopen(url,timeout=120) as r:path.write_bytes(r.read())
def check_tree(root,expected,label):
 require(root.is_dir() and not root.is_symlink(),'Invalid historical tree');count=0
 for folder,dirs,files in os.walk(root):
  folder=Path(folder)
  for name in dirs:require(not (folder/name).is_symlink(),'Historical directory symlink')
  for name in files:
   p=folder/name;rel=p.relative_to(root).as_posix();require(rel in expected and file_meta(p)==expected[rel],'Historical byte mismatch: '+rel);count+=1
 require(count==len(expected),'Historical file count mismatch');print('PASS:',label,count,'actual files',flush=True)

def archive_verify(path,expected_sha,root,external=None,extract=None):
 require(file_meta(path)['sha256']==expected_sha,'Archive hash mismatch: '+str(path));members={};keep={};internal=None
 with tarfile.open(path,'r:xz') as t:
  for m in t:
   require(m.isfile() and safe(m.name) and m.name.startswith(root+'/') and m.name not in members,'Unsafe/duplicate archive member')
   retain=m.name.startswith(root+'/delta/') or m.name in [root+'/'+n for n in ['BASE_MAP.json','SOURCE_MAP.json','PACKAGE_MANIFEST.json','REMOVALS.json']]
   if extract:
    dst=extract/m.name;dst.parent.mkdir(parents=True,exist_ok=True);writer=dst.open('xb')
   else:writer=None
   digest=hashlib.sha256();count=0;chunks=[]
   with t.extractfile(m) as h:
    for b in iter(lambda:h.read(1024*1024),b''):
     digest.update(b);count+=len(b)
     if retain and not extract:chunks.append(b)
     if writer:writer.write(b)
   if writer:writer.close()
   members[m.name]={'bytes':count,'sha256':digest.hexdigest()}
   if retain:
    body=(extract/m.name).read_bytes() if extract else b''.join(chunks)
    if m.name==root+'/PACKAGE_MANIFEST.json':internal=json.loads(body)
    elif m.name==root+'/REMOVALS.json':require(json.loads(body)==[],'Unexpected deletion')
    elif not extract:keep[m.name.removeprefix(root+'/')]=body
 if external is not None:require(members==external['files'],'External member manifest mismatch')
 require(internal=={n.removeprefix(root+'/'):v for n,v in members.items() if n!=root+'/PACKAGE_MANIFEST.json'},'Internal manifest mismatch')
 print('PASS: archive',root,len(members),'members',flush=True);return members,keep

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input-archive',required=True,type=Path);p.add_argument('--input-manifest',type=Path);p.add_argument('--input-receipt',type=Path);p.add_argument('--download-dir',type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
 out=a.output.resolve();require(not out.exists(),'Use a new output directory');out.mkdir(parents=True);fresh=a.download_dir is None;d=a.download_dir.resolve() if a.download_dir else out/'downloaded'
 if fresh:d.mkdir();get(BASE_URL+'MANIFEST.json',d/'MANIFEST.json')
 require(file_meta(d/'MANIFEST.json')['sha256']==MANIFEST_SHA,'Pinned manifest mismatch');m=read_json(d/'MANIFEST.json');require(m['sha256']==ARCHIVE_SHA and m['bytes']==1258348 and len(m['files'])==118 and len(m['parts'])==6,'Archive metadata mismatch')
 for name,expected in m['companion_files'].items():
  require(safe(name) and '/' not in name,'Unsafe companion name')
  if fresh:get(BASE_URL+name,d/name)
  require(file_meta(d/name)==expected,'Companion mismatch')
 require(read_json(d/'CHANGES.json')=={'added':[],'modified':[],'removed':[]} and read_json(d/'REMOVALS.json')==m['removed_source_files']==m['runtime_delta_files']==[],'Unexpected source changes')
 require((d/'SHA256SUMS.txt').read_text().strip()==ARCHIVE_SHA+'  '+m['archive'],'Archive checksum record mismatch');require(safe(m['archive']) and '/' not in m['archive'],'Unsafe archive name')
 archive=out/m['archive']
 with archive.open('xb') as h:
  for part in m['parts']:
   name=part['name'];require(safe(name) and '/' not in name,'Unsafe part')
   if fresh:get(BASE_URL+name,d/name)
   require(file_meta(d/name)=={'bytes':part['bytes'],'sha256':part['sha256']},'Part mismatch');h.write((d/name).read_bytes())
 members,_=archive_verify(archive,ARCHIVE_SHA,PACKAGE,m,out/'extracted');pkg=out/'extracted'/PACKAGE
 require(not any(n.startswith(PACKAGE+'/delta/') or n in [PACKAGE+'/SOURCE_MAP.json',PACKAGE+'/SOURCE.patch'] for n in members),'Review must not add a candidate delta/map/patch')
 require(file_meta(pkg/'BASE_MAP.json')['sha256']==INPUT_MAP_SHA,'Input source map mismatch');base=read_json(pkg/'BASE_MAP.json');require(len(base)==27908 and sum(v['bytes'] for v in base.values())==1548971251,'Input map counts mismatch')
 for n in base:require(safe(n),'Unsafe input source path')
 result=read_json(pkg/'RESULT.json');zero=read_json(pkg/'NO_SOURCE_CHANGES.json');require(result['status']==m['status']=='REVIEW_SEALED_NO_NEW_RECOVERY_CANDIDATE' and result['input_commit']==INPUT_COMMIT and result['reviewed']==5 and result['remaining_original_367_scope']==357,'Review status/scope mismatch')
 require(result['added']==result['modified']==result['deleted']==zero['added']==zero['modified']==zero['deleted']==m['source_changes']==0,'Source change counter mismatch')
 for key in ['new_restore_candidate_created','historical_versions_proven_latest','current_full_Catalog_loaded','full_Game_tested','full_compiler_run','old_save_compatibility_verified','source_fingerprint_changed_by_this_work']:require(result[key] is False,'Scope limitation missing: '+key)
 for supplied,name,urlname,expected in [(a.input_manifest,'PINNED_INPUT_MANIFEST.json','MANIFEST.json',INPUT_MANIFEST_SHA),(a.input_receipt,'PINNED_INPUT_RECEIPT.json','HISTORICAL_TOOLS_BATCH2_STREAM_VERIFICATION.json',INPUT_RECEIPT_SHA)]:
  dest=out/name
  if supplied:dest.write_bytes(supplied.read_bytes())
  else:get(INPUT_URL+urlname,dest)
  require(file_meta(dest)['sha256']==expected,'Pinned input metadata mismatch')
 dependency=read_json(out/'PINNED_INPUT_MANIFEST.json');prior=read_json(out/'PINNED_INPUT_RECEIPT.json')
 require(m['depends_on']['recovery_commit']==INPUT_COMMIT and m['depends_on']['archive_sha256']==dependency['sha256']==INPUT_ARCHIVE_SHA and m['depends_on']['receipt_sha256']==INPUT_RECEIPT_SHA and m['depends_on']['manifest_sha256']==INPUT_MANIFEST_SHA,'Dependency pointer mismatch')
 require(prior['status']=='PASS_EXACT_STREAMED_SOURCE_MAP_BYTES_WITH_FOUR_HISTORICAL_TOOLS_AND_SINSTONE_DEFERRED' and prior['source_map_sha256']==INPUT_MAP_SHA and prior['full_game_validation_passed'] is False,'Input receipt scope mismatch')
 old_members,keep=archive_verify(a.input_archive,INPUT_ARCHIVE_SHA,INPUT_ROOT,dependency);require(len(old_members)==282,'Input archive member count mismatch');require(keep['SOURCE_MAP.json']==(pkg/'BASE_MAP.json').read_bytes(),'Actual dependency target map differs from review input')
 cfg=read_json(pkg/'REVIEW_CONFIG.json');require(cfg['input_commit']==INPUT_COMMIT and len(cfg['records'])==5,'Review config mismatch');checked={};closure_map_paths=set()
 for row in cfg['records']:
  require(row['target'] not in base and row['latest_installed_version_proven'] is False,'Deferred target/version changed')
  for name,expected in row['preserved_evidence'].items():
   require(safe(name) and base[name]==expected and file_meta(pkg/'evidence/historical'/name)==expected,'Embedded historical/source evidence mismatch');checked[name]=expected
  for name,expected in row['preload_closure_map'].items():require(safe(name) and base[name]==expected,'Declared closure map mismatch');closure_map_paths.add(name)
 probe_count=0;harness_inputs={}
 harness_hashes={'review_config.json':'0b055b076bec16f47c843dd9f5c5fd661f2ae67b944d1204c11cf37020cb9627','review_fixtures.json':'65d89aa02e0114fdb4885730b5e7f209fbfbc08174b3afbab3b4a255aadc487a','project.godot':'efee3e87caf41e3a1f227252c53dd071fd9a5fc2e599e316f85c24b7ff6161c5'}
 for name,value in members.items():
  prefix=PACKAGE+'/probe_inputs/'
  if name.startswith(prefix):
   relative=name.removeprefix(prefix);actual=file_meta(pkg/'probe_inputs'/relative);require(actual==value,'Probe input differs from sealed archive');probe_count+=1
   if relative in harness_hashes:
    require(actual['sha256']==harness_hashes[relative],'Known isolated harness hash mismatch');harness_inputs[relative]=actual
    if relative=='review_config.json':require((pkg/'probe_inputs'/relative).read_bytes()==(pkg/'REVIEW_CONFIG.json').read_bytes(),'Harness review config differs')
   else:
    require(relative in base and actual==base[relative],'Embedded source probe input differs from pinned source map');checked[relative]=value
 require(probe_count==56 and set(harness_inputs)==set(harness_hashes),'Probe input count/role mismatch')
 before=read_json(pkg/'before/report.json');after=read_json(pkg/'after/report.json');portable=read_json(pkg/'portable_report/report.json')
 require(len(before['failures'])==1 and before['findings'][0]['actual_current_closure_error_without_fixtures'].startswith('wishbone_active_native_binding_changed:'),'Initial incomplete probe failure missing')
 require(after['status']=='PASS_EVIDENCE_OF_DIFFERENCES_NO_RESTORATION' and after['failures']==[] and len(after['findings'])==4 and after==portable and after['Partner_source_loaded'] is False,'Complete evidence reports inconsistent')
 partner=next(x for x in cfg['records'] if x['target']=='tools/partner_in_crime_patterns.py');require(partner['preload_closure_count']==312 and result['partner']['actual_runtime_tests_not_run'] is True,'Partner scope mismatch')
 py=read_json(pkg/'PYTHON_REVIEW.json');require(py['checks']==40 and all(x['pass'] for x in py['results']),'Saved Python review evidence inconsistent')
 require(file_meta(a.input_archive)['sha256']==INPUT_ARCHIVE_SHA,'Input archive changed during verification')
 (out/'EMBEDDED_SOURCE_FILES_VERIFIED.json').write_text(json.dumps(checked,indent=2,sort_keys=True)+'\n')
 receipt={'status':'PASS_READONLY_REVIEW_ARCHIVE_AND_PINNED_DEPENDENCY','review_status':result['status'],'archive_commit':COMMIT,'repository_path':REPO_PATH,'archive_sha256':ARCHIVE_SHA,'archive_bytes':1258348,'manifest_sha256':MANIFEST_SHA,'parts_verified':6,'members_verified':118,'internal_manifest_members_verified':117,'input_verified_commit':INPUT_COMMIT,'input_archive_sha256':INPUT_ARCHIVE_SHA,'input_archive_members_reverified':282,'input_manifest_sha256':INPUT_MANIFEST_SHA,'input_receipt_sha256':INPUT_RECEIPT_SHA,'unchanged_source_map_sha256':INPUT_MAP_SHA,'input_source_map_files':len(base),'input_source_map_bytes':sum(x['bytes'] for x in base.values()),'input_source_map_counts_are_not_a_fresh_full_tree_byte_verification':True,'embedded_historical_and_current_source_files_rehashed_against_pinned_map':len(checked),'embedded_source_file_bytes_checked':sum(x['bytes'] for x in checked.values()),'probe_input_files_verified':probe_count,'probe_source_files_matching_base_map':probe_count-len(harness_inputs),'isolated_harness_inputs_not_game_source':harness_inputs,'retry_after_initial_harness_role_misclassification':True,'declared_preload_paths_compared_as_metadata_only':len(closure_map_paths),'source_changes':0,'runtime_delta_created':False,'new_candidate_created':False,'reviewed_and_deferred_targets':5,'remaining_missing_in_original_367_scope':357,'initial_incomplete_probe_failure_preserved':True,'complete_saved_evidence_reports_match':True,'saved_reports_are_observations_not_new_gameplay_acceptance':True,'Partner_312_script_closure_not_loaded':True,'candidate_Python_or_Godot_executed_by_verifier':False,'whole_runtime_rehashed_or_reconstructed_this_round':False,'complete_runtime_directory_created':False,'historical_full_chain_downloaded_or_replayed_this_round':False,'input_archive_reused_and_rehashed':True,'increment_downloaded_by_this_helper':fresh,'increment_input_mode':'fresh immutable URLs' if fresh else 'Pre-fetched pinned Git bytes; six archive-part objects absent before fetch, see FETCH_PROVENANCE.json','full_game_verified':False,'old_save_compatibility_verified':False,'all_prior_backups_preserved':True,'no_deletion_performed':True,'input_archive_unchanged':True,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 (out/'BATCH3_REVIEW_REMOTE_VERIFICATION.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2),flush=True)
if __name__=='__main__':main()
