# Recover Electron Privateer Four source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Privateer Leftmost recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/60099bcf2be4fdee4ad9a7b1deba69a720d7c0fa/battlegrounds-backup/pending/20261108-electron-privateer-leftmost/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Privateer Leftmost. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Privateer Leftmost recovery directory must contain restored_privateer_leftmost_runtime and privateer_leftmost/extracted/electron_privateer_leftmost_20261108/SOURCE_MAP.json. Require exactly 27,741 files / 1,548,179,617 bytes; map SHA256 86a0b68f46f7cfb9ee7680324cc510074e8f794257291851788ea94f1a70ff4e.

Place PRIVATEER_LEFTMOST_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- PRIVATEER_LEFTMOST_REMOTE_CHAIN_VERIFICATION.json, SHA256 efa0d65d32a10bff952220270fe715bec7c2ebb4b3e3950ba9ce559de75a448b.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Privateer Leftmost source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_privateer_four.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_privateer_four.py --privateer-leftmost-recovery /path/to/completed-privateer-leftmost-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 23b40eb02342825ba9e96fd8ed408b1443890314, path battlegrounds-backup/pending/20261108-electron-privateer-four. Archive electron_privateer_four_20261108.tar.xz: 1,131,480 bytes, SHA256 0fcb1dca43e0f7565365f3911d25afd1d55317463655e461cddb24f4debbeff5.

Every part, assembled archive and all 52 safe members are verified. Companion hashes and exact map differences must match seven modifications, three additions and no removals. Privateer Leftmost SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_privateer_four_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require PRIVATEER_FOUR_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,744 files / 1,548,192,218 bytes, no missing/mismatched/unexpected files, and target map SHA256 dbde059ed38c6620e3c693d323bdd403bdf8f499546c0d5b04dc29108625d36e. Per-file origins are in RESTORE_PROVENANCE.json.

Only Privateer Four is freshly downloaded this round; historical source evidence and Privateer Leftmost baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The ten delta files are exactly seven modifications and three additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. Its endpoint is pinned and matched to the preceding Leftmost receipt’s Wealth source map. That pinned receipt establishes the next step to the fully rehashed Leftmost baseline. This run freshly downloads only Four, not the historical chain.
