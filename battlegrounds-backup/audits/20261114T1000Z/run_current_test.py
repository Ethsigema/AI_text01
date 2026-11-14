from pathlib import Path
import subprocess,os,json,datetime,hashlib,re
r=Path(__file__).resolve().parent;home=r/'test_home';home.mkdir(exist_ok=False)
env=os.environ.copy()
for k,n in [('XDG_DATA_HOME','data'),('XDG_CONFIG_HOME','config'),('XDG_CACHE_HOME','cache')]:
 p=home/n;p.mkdir();env[k]=str(p)
project=r/'restored/project';version=subprocess.run(['godot','--version'],capture_output=True,text=True,check=True).stdout.strip();assert version.startswith('4.6.3.')
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
try:
 result=subprocess.run(['godot','--headless','--path',str(project),'--script','tests/shipwrecked_overflow_20261114/real_matrix.gd'],env=env,capture_output=True,text=True,timeout=240)
 log=result.stdout+result.stderr;code=result.returncode
except subprocess.TimeoutExpired as e:
 log=(e.stdout or b'').decode(errors='replace')+(e.stderr or b'').decode(errors='replace');code='timeout'
(r/'SCOPED_GAMEPLAY_CURRENT.log').write_text(log)
checks=len(re.findall(r'^PASS ',log,re.M));passed=code==0 and 'SHIPWRECKED_PASS checks=73' in log and checks==73 and not re.search(r'^(FAIL |ERROR:|SCRIPT ERROR:)',log,re.M)
record={'started_at_utc':start,'finished_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS' if passed else 'FAILED','godot':version,'exit_code':code,'passed_checks':checks,'fresh_restored_source_run':True,'source_commit':'5a1cd70bc1f818d5abde913d6482fb6573a15401','core_sha256':hashlib.sha256((project/'core/bulk_minion_activate.gd').read_bytes()).hexdigest(),'test_sha256':hashlib.sha256((project/'tests/shipwrecked_overflow_20261114/real_matrix.gd').read_bytes()).hexdigest(),'log_sha256':hashlib.sha256(log.encode()).hexdigest(),'scope':'normal/golden x 9/10 spell hand; 4 activations, 6 discovery choices; native factory/commands; fixture coin-only pool, board and initial gold; single source and no extra observers','full_gameplay_accepted':False,'golden_natural_acquisition_tested':False,'full_card_pool_tested':False,'old_save_tested':False,'new_complete_minion_credit':0}
(r/'SCOPED_GAMEPLAY_CURRENT.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record));raise SystemExit(0 if passed else 1)
