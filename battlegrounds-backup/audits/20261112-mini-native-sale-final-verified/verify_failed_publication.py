"""Fresh-download fixed publication and every archive member; never Game or upload."""
import subprocess,concurrent.futures
from packaging_common import *
def main():
 ap=parser(__doc__);ap.add_argument('--publication',type=Path,default=ROOT/'FAILED_RUN_PUBLICATION.json');ap.add_argument('--files-metadata',type=Path,default=ROOT/'FAILED_RUN_UPLOAD_METADATA.json');a=ap.parse_args()
 r,commit,folder,m,expected,d=context(a);pub=read(a.publication);files=read(a.files_metadata)
 if isinstance(files,dict):files=files['records']
 assert re.fullmatch('[0-9a-f]{40}',pub['commit']) and pub['commit']!=commit and pub['source_commit']==commit
 assert pub.get('remote_folder',pub.get('folder'))==folder
 assert len(files)==len({x['name'] for x in files}) and len(files)>0
 for row in files:assert safe(row['name']) and '/' not in row['name'] and re.fullmatch('[0-9a-f]{64}',row['sha256']) and re.fullmatch('[0-9a-f]{40}',row['git_sha'])
 out=ROOT/('failed_remote_publication_'+pub['commit']);out.mkdir(exist_ok=False)
 def download(row):
  url=f"https://raw.githubusercontent.com/Ethsigema/AI_text01/{pub['commit']}/{folder}/{row['name']}";p=out/row['name'];partial=Path(str(p)+'.partial')
  subprocess.run(['curl','-fsSL','--retry','3','--connect-timeout','30','--max-time','300','--output',str(partial),url],check=True)
  b=partial.read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256'] and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_sha'];partial.rename(p);return {**row,'url':url}
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(download,files))
 sums={}
 for line in (out/'SHA256SUMS.txt').read_text().splitlines():
  h,n=line.split('  ',1);assert safe(n) and '/' not in n and n not in sums and n!='SHA256SUMS.txt';assert sha((out/n).read_bytes())==h;sums[n]=h
 assert set(sums)=={x['name'] for x in files}-{'SHA256SUMS.txt'}
 immutable={}
 for row in d['records']:
  n=row['filename']
  if n=='SHA256SUMS.txt':continue
  b=(out/n).read_bytes();assert b==(r/'package'/n).read_bytes() and sha(b)==row['sha256'];immutable[n]=sha(b)
 assert read(out/'MANIFEST.json')==m
 archives={}
 for f in out.glob('*.tar.xz'):
  meta={'archive_sha256':m['archive_sha256'],'members':m['changed_files']} if f.name==m.get('archive') else read(out/(f.name.removesuffix('.tar.xz')+'_MANIFEST.json'))
  archives[f.name]=verify_archive(f.read_bytes(),meta)
 assert 'FIX_EVIDENCE.tar.xz' in archives and 'TOOLS_EVIDENCE.tar.xz' in archives and 'GAMEPLAY_EVIDENCE.tar.xz' in archives
 with tarfile.open(out/'GAMEPLAY_EVIDENCE.tar.xz','r:xz') as t:
  def archived(n):return json.loads(t.extractfile(n).read())
  summary=archived('independent_tests/ATTEMPT_SUMMARY.json');audit=archived('POST_ATTEMPT_SOURCE_AUDIT.json')
  names=t.getnames();final=archived('INDEPENDENT_GAME_VERIFICATION.json') if 'INDEPENDENT_GAME_VERIFICATION.json' in names else None
  outcome=outcome_metadata(summary,audit,final)
 post=read(out/'GAMEPLAY_OUTCOME.json');assert post['source_commit']==commit and post['source_map_sha256']==m['source_map_sha256'] and post['outcome']==outcome
 assert post['source_integrity_ok']==all(tree['matches'] is True for tree in post['trees'].values())
 if outcome=='success':
  for tree in post['trees'].values():assert tree['matches'] and tree['aggregate_sha256']==m['aggregate_sha256'] and tree['files']==m['source_files'] and tree['bytes']==m['source_bytes'] and not any(tree[k] for k in ['missing','extra','mismatched'])
 if outcome=='success':
  b=(out/'GAMEPLAY_INDEPENDENT_VERIFICATION.json').read_bytes();assert b==(r/'INDEPENDENT_GAME_VERIFICATION.json').read_bytes() and json.loads(b)==final
  scenario=read(out/'GAMEPLAY_MATRIX_RESULT.json');assert scenario==final['tests']['mini_sale_real_matrix']['verified_scenario_fields']
  actual_count,actual_scenario=runner.validate_mini_sale_full((r/'independent_tests/mini_sale_real_matrix.log').read_text(),r/'independent_tests')
  assert actual_scenario==scenario and actual_count==final['tests']['mini_sale_real_matrix']['passed_checks']
 else:assert not (out/'GAMEPLAY_INDEPENDENT_VERIFICATION.json').exists()
 assert outcome=='failure', 'Failure verifier must not publish success'
 report={'status':'PASS_FINAL_PUBLICATION_FRESH_BYTES_ALL_ARCHIVE_MEMBERS','outcome':outcome,'commit':pub['commit'],'source_commit':commit,'remote_folder':folder,'verified_at_utc':runner.utc(),'files':len(records),'bytes':sum(x['bytes'] for x in records),'records':records,'archive_member_counts':archives,'immutable_source_files_match_fixed_source_commit':immutable,'gameplay_accepted':outcome=='success','full_game_acceptance':False,'game_started_by_this_verifier':False,'uploaded':False}
 put(ROOT/'FAILED_RUN_PUBLICATION_VERIFIED.json',enc(report))
if __name__=='__main__':main()
