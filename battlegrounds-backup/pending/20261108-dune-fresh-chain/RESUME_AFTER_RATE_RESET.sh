#!/bin/sh
set -eu
cd "$(dirname "$0")"
wait_seconds=$((1794151444-$(date +%s)))
if [ "$wait_seconds" -gt 0 ]; then echo "Waiting $wait_seconds seconds for documented GitHub API rate reset"; sleep "$wait_seconds"; fi
curl --fail --location -H 'Accept: application/octet-stream' 'https://api.github.com/repos/Ethsigema/AI_text01/releases/assets/697440146' -o baseline_download/baseline_api.zip
while [ ! -f GIT_FSCK.log ]; do sleep 5; done
python3 -u verify_historical_bytes.py > HISTORICAL.log 2>&1
python3 -u verify_fresh_increment_chain.py > INCREMENTS.log 2>&1
python3 create_dune_receipt.py > FINAL_AUDIT.log 2>&1
