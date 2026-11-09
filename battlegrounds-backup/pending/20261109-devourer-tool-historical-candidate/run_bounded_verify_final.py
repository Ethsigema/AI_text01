from pathlib import Path
import subprocess,resource,time,os,json,datetime,signal
v=Path(__file__).resolve().parent
cmd=['python',str(v/'verify_devourer_stream.py'),'--historical-baseline','harbinger_leaf_remote_verify_20261109/verified_reconstruction/restored_harbinger_identity_leaf_candidate_runtime','--native-archive','native_listener_remote_verify_20261109/verified_stream/native_spell_listener_leaf_partial_candidate_20261109.tar.xz','--earth-archive','earth_leaf_remote_verify_20261109/verified_stream/earth_mother_helper_leaf_partial_candidate_20261109.tar.xz','--golden-archive','golden_leaf_remote_verify_20261109/verified_stream_final/native_golden_source_leaf_partial_candidate_20261109.tar.xz','--golden-tool-archive','tool_reconstruction_remote_verify_20261109/verified_stream/golden_arrow_tool_patch_reconstruction_candidate_20261109.tar.xz','--megasaur-archive','megasaur_remote_verify_20261109/verified_stream/megasaur_tool_fixed_pin_candidate_20261109.tar.xz','--batch1-archive','batch1_remote_verify_20261109/verified_stream/historical_tools_batch1_candidate_20261109.tar.xz','--batch2-archive','batch2_remote_verify_20261109/verified_stream/historical_tools_batch2_four_candidate_20261109.tar.xz','--batch4-archive','batch4_remote_verify_20261109/verified_stream/historical_tools_batch4_three_candidate_20261109.tar.xz','--baseline-receipt',str(v/'PINNED_INPUT_RECEIPT.json'),'--baseline-manifest',str(v/'PINNED_INPUT_MANIFEST.json'),'--download-dir',str(v/'downloaded'),'--output',str(v/'verified_stream_final')]
def limits():
 resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
start=time.monotonic();reason='process_exit';peak=0
with (v/'VERIFY_FINAL.log').open('x') as log:
 p=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits)
 while True:
  pid,status,usage=os.wait4(p.pid,os.WNOHANG)
  if pid:
   exit_code=os.waitstatus_to_exitcode(status);break
  try:
   rows=Path(f'/proc/{p.pid}/status').read_text().splitlines();rss=next(int(x.split()[1])*1024 for x in rows if x.startswith('VmRSS:'));peak=max(peak,rss)
   if rss>192*1024**2:reason='rss_guard_192MiB';p.kill()
  except (FileNotFoundError,StopIteration):pass
  if time.monotonic()-start>180:reason='timeout_180s';p.kill()
  time.sleep(.025)
 r={'exit':exit_code,'reason':reason,'seconds':time.monotonic()-start,'maxrss_kib_exact_child':usage.ru_maxrss,'sampled_peak_rss_bytes':peak,'address_space_limit_bytes':512*1024**2,'rss_guard_bytes':192*1024**2,'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 (v/'BOUNDED_PROCESS_FINAL.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2),flush=True)
 p.returncode=exit_code
 if exit_code:raise SystemExit(1)
