# Recover Hopebringer Rat Leader source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Bonehead recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/d1951d7bf0ebbc1246211c302cfefb3815cd3f13/battlegrounds-backup/pending/20261108-hopebringer-bonehead/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Bonehead. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Bonehead recovery directory must contain restored_hopebringer_bonehead_runtime and hopebringer_bonehead/extracted/hopebringer_bonehead_20261108/SOURCE_MAP.json. Require exactly 27,754 files / 1,548,228,427 bytes; map SHA256 0f4533bc8e1e27446d0a6ddd84b24a33436cd904bf7fca593c9155ac2162baf4.

Place HOPEBRINGER_BONEHEAD_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_BONEHEAD_REMOTE_CHAIN_VERIFICATION.json, SHA256 f6049bfd6ab1c10ccd94feba93c1693b5f2f2ace73bf793ca20173a9c25f9662.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Bonehead source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_rat_leader.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_rat_leader.py --hopebringer-bonehead-recovery /path/to/completed-hopebringer-bonehead-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and seven binary parts from commit 9e7ce1b517594f4c95a6dabd40ff31beedd0900a, path battlegrounds-backup/pending/20261108-hopebringer-rat-leader. Archive hopebringer_rat_leader_20261108.tar.xz: 1,579,748 bytes, SHA256 122280fc22206c630dd2346ecdb1a184092fc52cfcda2c0a42ca5f27a239c8be.

Every part, assembled archive and all 38 safe members are verified. Companion hashes and exact map differences must match five modifications, four additions and no removals. Hopebringer Bonehead SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_rat_leader_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_RAT_LEADER_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,758 files / 1,548,242,863 bytes, no missing/mismatched/unexpected files, and target map SHA256 131d581364ab21c0faa390ff33160d2652f8cd99475552195b704cb67b47e4a7. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Rat Leader is freshly downloaded this round; historical source evidence and Hopebringer Bonehead baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The nine delta files are exactly five modifications and four additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Bonehead receipt establishes continuity through the intervening increments to the fully rehashed Bonehead baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Rat Leader, not the historical chain.
