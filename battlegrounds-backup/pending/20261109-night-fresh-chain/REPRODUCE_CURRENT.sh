#!/bin/bash
set -eu
cd "$(dirname "$0")"
test ! -e remote_repo && test ! -e repository && test ! -e bloodbound
test ! -e baseline_download && test ! -e increments && test ! -e runtime_final_current
mkdir baseline_download
curl --fail --location 'https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip' -o baseline_download/baseline_direct.zip
git clone --no-checkout --single-branch --branch battlegrounds-recovery-20261103 https://github.com/Ethsigema/AI_text01.git remote_repo
git -C remote_repo fetch origin 32180d3af0db59fb3374f53100f9eaa5bb62d26a
git clone --shared --no-checkout "$PWD/remote_repo" repository
git -C repository checkout --detach e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c
mkdir bloodbound
git -C remote_repo archive 32180d3af0db59fb3374f53100f9eaa5bb62d26a | tar -x -C bloodbound
python3 -u materialize_historical_current.py > HISTORICAL_REPRODUCED.log 2>&1
python3 -u prefetch_from_fresh_git.py > PREFETCH_REPRODUCED.log 2>&1
cp -a restored_bloodbound_runtime runtime_final_current
python3 -u materialize_and_verify_increment_chain_retry.py > INCREMENTS_REPRODUCED.log 2>&1
