"""Prepare now; invoke --execute only after final publication has a fixed commit.
Freshly download and verify every final file and gameplay evidence member.
No source/package editing, upload or Game execution.
"""
from pathlib import Path,PurePosixPath
import argparse,json,subprocess,hashlib,concurrent.futures,datetime,re,tarfile,gzip
ROOT=Path(__file__).resolve().parent.parent
SOURCE_COMMIT='5d988875054ad4eea47d6615f8a9fdd65bfe7b4d'
FOLDER='battlegrounds-backup/pending/20261112-darkcrest-lava-native-board'
def sha(b):return hashlib.sha256(b).hexdigest()
def safe(n):return bool(n) and not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and '\\' not in n
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--execute',action='store_true',required=True);ap.parse_args()
 pub=json.loads((ROOT/'FINAL_PUBLICATION.json').read_text());files=json.loads((ROOT/'FINAL_PUBLICATION_FILES.json').read_text())
 assert re.fullmatch('[0-9a-f]{40}',pub['commit']) and pub['source_commit']==SOURCE_COMMIT and pub.get('folder',pub.get('remote_folder'))==FOLDER
 assert pub['commit']!=SOURCE_COMMIT and len(files)==30 and len({f['name'] for f in files})==len(files)
 if isinstance(pub.get('files'),list):assert pub['files']==files
 for f in files:assert safe(f['name']) and '/' not in f['name'] and re.fullmatch('[0-9a-f]{64}',f['sha256']) and re.fullmatch('[0-9a-f]{40}',f['git_sha'])
 out=ROOT/('final_remote_publication_'+pub['commit']);out.mkdir(exist_ok=False)
 def get(f):
  url=f"https://raw.githubusercontent.com/Ethsigema/AI_text01/{pub['commit']}/{FOLDER}/{f['name']}";p=out/f['name'];part=Path(str(p)+'.partial')
  subprocess.run(['curl','-fsSL','--retry','3','--connect-timeout','30','--max-time','300','--output',str(part),url],check=True)
  b=part.read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'] and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==f['git_sha'],f['name'];part.rename(p)
  return {**f,'url':url}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:records=list(ex.map(get,files))
 checked=set()
 for line in (out/'SHA256SUMS.txt').read_text().splitlines():
  h,n=line.split('  ',1);assert safe(n) and '/' not in n and n not in checked and n!='SHA256SUMS.txt'
  assert sha((out/n).read_bytes())==h,n;checked.add(n)
 assert checked=={f['name'] for f in files}-{'SHA256SUMS.txt'}
 # Independently compare immutable source payload/map to the verified source commit downloads.
 fixed=ROOT/'remote_snapshot_5d98887';original=json.loads((fixed/'FRESH_PACKAGE_DOWNLOAD_VERIFIED.json').read_text());assert original['source_commit']==SOURCE_COMMIT
 indexed={x['filename']:x for x in original['records']};unchanged={}
 for n in sorted(set(indexed)-{'SHA256SUMS.txt'}):
  b=(out/n).read_bytes();old=(fixed/'package'/n).read_bytes()
  assert len(old)==indexed[n]['bytes'] and sha(old)==indexed[n]['sha256'],n
  assert b==old,n;unchanged[n]=sha(b)
 manifest=json.loads((out/'MANIFEST.json').read_text())
 assert manifest['status']=='UNACCEPTED_DARKCREST_LAVA_BEFORE_GAME'
 assert manifest['source_map_sha256']=='e84edfaea8bf19ee8650f179cb48d9093915a99ef5d0a54adebb3a01fc9b33c3'
 assert sha(gzip.decompress((out/'SOURCE_MAP.json.gz').read_bytes()))==manifest['source_map_sha256']
 assert manifest['aggregate_sha256']=='1cbcbcc3a1c16f2271c2d27ba78b87ffad6009a07c4b0c2bb2d914f3ab01f814'
 evidence=json.loads((out/'GAMEPLAY_EVIDENCE_MANIFEST.json').read_text());assert evidence['source_commit']==SOURCE_COMMIT
 assert sha((out/'GAMEPLAY_EVIDENCE.tar.xz').read_bytes())==evidence['archive_sha256'];expected=evidence['members'];seen=set();total=0
 with tarfile.open(out/'GAMEPLAY_EVIDENCE.tar.xz','r:xz') as archive:
  for x in archive:
   assert x.isfile() and safe(x.name) and x.name not in seen and x.name in expected
   b=archive.extractfile(x).read();assert {'bytes':len(b),'sha256':sha(b)}==expected[x.name],x.name;seen.add(x.name);total+=len(b)
 assert seen==set(expected)
 # Preserve and independently verify the earlier bytes-only tool receipt too.
 tool_manifest=json.loads((out/'TOOLS_EVIDENCE_MANIFEST.json').read_text());assert tool_manifest['source_commit']==SOURCE_COMMIT
 assert sha((out/'TOOLS_EVIDENCE.tar.xz').read_bytes())==tool_manifest['archive_sha256'];tool_seen=set()
 with tarfile.open(out/'TOOLS_EVIDENCE.tar.xz','r:xz') as archive:
  for member in archive:
   assert member.isfile() and safe(member.name) and member.name not in tool_seen
   b=archive.extractfile(member).read();assert {'bytes':len(b),'sha256':sha(b)}==tool_manifest['members'][member.name];tool_seen.add(member.name)
 assert tool_seen==set(tool_manifest['members'])
 fix_expected=json.loads((out/'FIX_EVIDENCE_MANIFEST.json').read_text());fix_seen=set()
 with tarfile.open(out/'FIX_EVIDENCE.tar.xz','r:xz') as archive:
  for member in archive:
   assert member.isfile() and safe(member.name) and member.name not in fix_seen
   b=archive.extractfile(member).read();assert {'bytes':len(b),'sha256':sha(b)}==fix_expected[member.name];fix_seen.add(member.name)
 assert fix_seen==set(fix_expected) and len(fix_seen)==23 and len(tool_seen)==19 and len(seen)==len(expected)==50
 game_bytes=(out/'GAMEPLAY_INDEPENDENT_VERIFICATION.json').read_bytes()
 assert sha(game_bytes)==sha((fixed/'INDEPENDENT_GAME_VERIFICATION.json').read_bytes())
 game=json.loads(game_bytes);assert game['source_commit']==SOURCE_COMMIT
 assert game['source_map_sha256']==manifest['source_map_sha256']
 for tree in ['restored_snapshot','run_tree']:
  meta=game['trees'][tree];assert meta['files']==27972 and meta['bytes']==1550731770 and meta['aggregate_sha256']==manifest['aggregate_sha256']
  assert meta['missing']==meta['extra']==meta['mismatched']==[]
 assert game['status']=='PASS_FIXED_REMOTE_DARKCREST_LAVA_MATRIX_AND_CONTRACTS_POST_TEST_DOUBLE_REHASH'
 assert game['tests']['lava_real_matrix']['passed_checks']>0
 assert len(game['tests']['lava_real_matrix']['verified_scenario_fields']['cases'])==3
 assert {k:v['passed_checks'] for k,v in game['tests'].items() if k!='lava_real_matrix'}=={'lava_content_contract':211,'tier6_content_contract':966,'tier5_content_contract':810,'source_eot_contract':68,'hand_shape_contract':166,'seafloor_annotation_contract':267}
 assert not game['full_game_acceptance'] and not game['default_pool_promoted']

 report={'status':'PASS_FINAL_PUBLICATION_FRESH_BYTES_AND_ALL_GAMEPLAY_EVIDENCE_MEMBERS','commit':pub['commit'],'source_commit':SOURCE_COMMIT,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':len(records),'bytes':sum(f['bytes'] for f in records),'sha256sums_entries':len(checked),'sha256sums_sha256':sha((out/'SHA256SUMS.txt').read_bytes()),'records':records,'immutable_source_files_match_fixed_source_commit':unchanged,'source_evidence_members':len(fix_seen),'gameplay_receipt_sha256':sha(game_bytes),'post_game_double_tree_reports_match_source':True,'preserved_tools_evidence_members':len(tool_seen),'gameplay_evidence_members':len(seen),'gameplay_evidence_uncompressed_bytes':total,'gameplay_evidence_every_member_rehashed':True,'missing':[],'extra':[],'mismatched':[],'acceptance':'ordinary_darkcrest_single_ordinary_lava_native_board_compatibility_only','full_game_or_trinket_family_acceptance':False,'game_started_by_this_verifier':False,'uploaded':False}
 with (ROOT/'FINAL_PUBLICATION_VERIFIED.json').open('x') as f:json.dump(report,f,indent=2)
 print(json.dumps({k:v for k,v in report.items() if k!='records'},indent=2))
if __name__=='__main__':main()
