# Recover Electron Privateer Majority source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Privateer Fullboard recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/8c5eccbac30b600ac18b0a97628c42948a3d4d5e/battlegrounds-backup/pending/20261108-electron-privateer-fullboard/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Privateer Fullboard. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Privateer Fullboard recovery directory must contain restored_privateer_fullboard_runtime and privateer_fullboard/extracted/electron_privateer_fullboard_20261108/SOURCE_MAP.json. Require exactly 27,747 files / 1,548,202,857 bytes; map SHA256 50e8c47af2573ca524bcdf96d8b654b6776f1659a0893ff8bcb6eeee96c25017.

Place PRIVATEER_FULLBOARD_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- PRIVATEER_FULLBOARD_REMOTE_CHAIN_VERIFICATION.json, SHA256 d162891b1a799f192a78efac24e09fa69502d309d7a84d35d2863e438ab32a90.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Privateer Fullboard source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_privateer_majority.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_privateer_majority.py --privateer-fullboard-recovery /path/to/completed-privateer-fullboard-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 8ffc8d09705f00f14702d9f0958b26d3fc0a91dc, path battlegrounds-backup/pending/20261108-electron-privateer-majority. Archive electron_privateer_majority_20261108.tar.xz: 1,121,216 bytes, SHA256 fb9636147cc301bdd2a987fd38bb4ab25b36187883fd14b35f94c0616831f136.

Every part, assembled archive and all 63 safe members are verified. Companion hashes and exact map differences must match five modifications, three additions and no removals. Privateer Fullboard SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_privateer_majority_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require PRIVATEER_MAJORITY_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,750 files / 1,548,215,949 bytes, no missing/mismatched/unexpected files, and target map SHA256 8d7ebfc803f3f410b8cffea9de3710c5bba7ad6173ad706bc5018a855618b6d0. Per-file origins are in RESTORE_PROVENANCE.json.

Only Privateer Majority is freshly downloaded this round; historical source evidence and Privateer Fullboard baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The eight delta files are exactly five modifications and three additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Fullboard receipt establishes continuity through the intervening increments to the fully rehashed Fullboard baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Majority, not the historical chain.
