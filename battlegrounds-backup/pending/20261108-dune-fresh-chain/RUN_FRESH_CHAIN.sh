#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir baseline_download
curl --fail --location -H 'Accept: application/octet-stream' 'https://api.github.com/repos/Ethsigema/AI_text01/releases/assets/697440146' -o baseline_download/baseline_api.zip
git clone --depth 1 --branch battlegrounds-recovery-20261103 https://github.com/Ethsigema/AI_text01.git repository
git -C repository fetch --depth 1 origin e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c
git -C repository checkout --detach e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c
git -C repository fetch --depth 1 origin 32180d3af0db59fb3374f53100f9eaa5bb62d26a
mkdir bloodbound
git -C repository archive 32180d3af0db59fb3374f53100f9eaa5bb62d26a | tar -x -C bloodbound
git -C repository fsck --full --no-reflogs > GIT_FSCK.log 2>&1
python3 -u verify_historical_bytes.py > HISTORICAL.log 2>&1
python3 -u verify_fresh_increment_chain.py > INCREMENTS.log 2>&1
python3 create_dune_receipt.py > FINAL_AUDIT.log 2>&1
