#!/bin/sh
set -eu
# Place this script, both Python helpers, and PINNED_INCREMENT_CHAIN.json in a new directory.
cd "$(dirname "$0")"
mkdir baseline_download
curl --fail --location 'https://github.com/Ethsigema/AI_text01/releases/download/battlegrounds-handoff-20261101/battlegrounds_new_scope_handoff_20261101.zip' -o baseline_download/baseline.zip
git clone --branch battlegrounds-recovery-20261103 https://github.com/Ethsigema/AI_text01.git repository
git -C repository checkout --detach e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c
git -C repository fetch origin 32180d3af0db59fb3374f53100f9eaa5bb62d26a
mkdir bloodbound
git -C repository archive 32180d3af0db59fb3374f53100f9eaa5bb62d26a | tar -x -C bloodbound
git -C repository fsck --full --no-reflogs
python3 verify_historical_bytes.py
python3 verify_fresh_increment_chain.py
