# Recover Hopebringer Beetle source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Eudora recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/b336f78e1d64771123369749b9135ff8c412cdd4/battlegrounds-backup/pending/20261108-hopebringer-eudora/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Eudora. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Eudora recovery directory must contain restored_hopebringer_eudora_runtime and hopebringer_eudora/extracted/hopebringer_eudora_20261108/SOURCE_MAP.json. Require exactly 27,763 files / 1,548,258,743 bytes; map SHA256 423e2cf3e18e4edef0949ce180fb7145e7e8b765d01eb5feeefb4f455ac6df1e.

Place HOPEBRINGER_EUDORA_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_EUDORA_REMOTE_CHAIN_VERIFICATION.json, SHA256 446e36387d5e018e2c7960aa325a275ab407784f4e40e89005dfdc9b0826e4c9.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Eudora source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_beetle.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_beetle.py --hopebringer-eudora-recovery /path/to/completed-hopebringer-eudora-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and seven binary parts from commit d0a949c65a2c7382c21e8ba83b3b610e90de87c7, path battlegrounds-backup/pending/20261108-hopebringer-beetle. Archive hopebringer_beetle_20261108.tar.xz: 1,566,900 bytes, SHA256 2b2ada55aac1bf886831f51946d274505166bb1b483f5be9ae725af1166ebd4f.

Every part, assembled archive and all 38 safe members are verified. Companion hashes and exact map differences must match five modifications, three additions and no removals. Hopebringer Eudora SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_beetle_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_BEETLE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,766 files / 1,548,266,883 bytes, no missing/mismatched/unexpected files, and target map SHA256 bfc7e02d881286df6d3db5000ef53245e0dc304422c6aab1cb19847828b65c76. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Beetle is freshly downloaded this round; historical source evidence and Hopebringer Eudora baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The eight delta files are exactly five modifications and three additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Eudora receipt establishes continuity through the intervening increments to the fully rehashed Eudora baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Beetle, not the historical chain.
