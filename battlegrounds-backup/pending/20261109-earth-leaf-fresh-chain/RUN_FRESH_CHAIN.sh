#!/bin/bash
set -eu
cd "$(dirname "$0")"
test ! -e baseline_download && test ! -e repository && test ! -e increments
mkdir baseline_download
curl --fail --location 'https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip' -o baseline_download/baseline_direct.zip
bash DOWNLOAD_PINNED_GIT.sh > GIT_DOWNLOAD.log 2>&1
python3 -u verify_historical_bytes.py > HISTORICAL.log 2>&1
python3 -u prefetch.py > PREFETCH.log 2>&1
python3 -u verify_fresh_increment_chain.py > INCREMENTS.log 2>&1
