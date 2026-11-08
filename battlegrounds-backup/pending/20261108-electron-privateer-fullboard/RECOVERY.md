# Recover Electron Privateer Fullboard source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Privateer Four recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/2bc11405c254a7cc65ac73254d96aefb72431330/battlegrounds-backup/pending/20261108-electron-privateer-four/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Privateer Four. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Privateer Four recovery directory must contain restored_privateer_four_runtime and privateer_four/extracted/electron_privateer_four_20261108/SOURCE_MAP.json. Require exactly 27,744 files / 1,548,192,218 bytes; map SHA256 dbde059ed38c6620e3c693d323bdd403bdf8f499546c0d5b04dc29108625d36e.

Place PRIVATEER_FOUR_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- PRIVATEER_FOUR_REMOTE_CHAIN_VERIFICATION.json, SHA256 9748f5bf966b502afb84edf90acfbaef131ca12323736d645c46be3a13865f4b.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Privateer Four source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_privateer_fullboard.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_privateer_fullboard.py --privateer-four-recovery /path/to/completed-privateer-four-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 4635021efed8f1160f0e1a4e212eb6812446a081, path battlegrounds-backup/pending/20261108-electron-privateer-fullboard. Archive electron_privateer_fullboard_20261108.tar.xz: 1,087,900 bytes, SHA256 8cc9a2ac5a2bedcf06617be4cde59fb3d8225814f18d59a5aefd3aad0a4e719f.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, three additions and no removals. Privateer Four SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_privateer_fullboard_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require PRIVATEER_FULLBOARD_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,747 files / 1,548,202,857 bytes, no missing/mismatched/unexpected files, and target map SHA256 50e8c47af2573ca524bcdf96d8b654b6776f1659a0893ff8bcb6eeee96c25017. Per-file origins are in RESTORE_PROVENANCE.json.

Only Privateer Fullboard is freshly downloaded this round; historical source evidence and Privateer Four baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The eight delta files are exactly five modifications and three additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Four receipt establishes continuity through Leftmost to the fully rehashed Four baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Fullboard, not the historical chain.
