# Recover Electron Privateer Leftmost source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Privateer Wealth recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/1a8c1381a5b94ee1b82b198bc8f21bb8bfbd6c04/battlegrounds-backup/pending/20261108-electron-privateer-wealth/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Privateer Wealth. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Privateer Wealth recovery directory must contain restored_privateer_wealth_runtime and privateer_wealth/extracted/electron_privateer_wealth_20261108/SOURCE_MAP.json. Require exactly 27,739 files / 1,548,173,496 bytes; map SHA256 170be091073bebc2381da4f748262098c1093008f5f35f9ae97971f557817c5b.

Place PRIVATEER_WEALTH_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- PRIVATEER_WEALTH_REMOTE_CHAIN_VERIFICATION.json, SHA256 685375738ba465c91a89392f8e5a4b7b86e91539fb6c5a4774eec451c3b0e966.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Privateer Wealth source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_privateer_leftmost.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_privateer_leftmost.py --privateer-wealth-recovery /path/to/completed-privateer-wealth-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 7b5370f9df09d0d78cce56a475779499bd888e11, path battlegrounds-backup/pending/20261108-electron-privateer-leftmost. Archive electron_privateer_leftmost_20261108.tar.xz: 1,083,320 bytes, SHA256 f618937b1f4428b65f7c136e6647563e1ce41451f666d123b4c9f02307796536.

Every part, assembled archive and all 36 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Privateer Wealth SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_privateer_leftmost_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require PRIVATEER_LEFTMOST_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,741 files / 1,548,179,617 bytes, no missing/mismatched/unexpected files, and target map SHA256 86a0b68f46f7cfb9ee7680324cc510074e8f794257291851788ea94f1a70ff4e. Per-file origins are in RESTORE_PROVENANCE.json.

Only Privateer Leftmost is freshly downloaded this round; historical source evidence and Privateer Wealth baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

Use the latest whole-chain receipt published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0. Its exact endpoint is the supplied Wealth baseline. The older Wealth increment receipt refers to an earlier scheduled proof; both receipt hashes are pinned separately, and the new whole-chain endpoint is directly compared with the rehashed baseline. This run does not download historical source bytes again.
