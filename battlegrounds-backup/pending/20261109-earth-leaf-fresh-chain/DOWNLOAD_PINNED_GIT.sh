#!/bin/bash
set -eu
cd "$(dirname "$0")"
git init repository
git -C repository remote add origin https://github.com/Ethsigema/AI_text01.git
git -C repository fetch --depth 1 origin e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c
git -C repository checkout --detach FETCH_HEAD
git -C repository fetch --depth 1 origin 32180d3af0db59fb3374f53100f9eaa5bb62d26a
mkdir bloodbound
git -C repository archive 32180d3af0db59fb3374f53100f9eaa5bb62d26a | tar -x -C bloodbound
git -C repository fsck --full --no-reflogs > GIT_FSCK.log 2>&1
