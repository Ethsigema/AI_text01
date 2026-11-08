# Recover Hopebringer Nadina source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Skull recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/bf4d3265c9fad9bab79432ef795682a7dc9f2df3/battlegrounds-backup/pending/20261108-hopebringer-skull/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Skull. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Skull recovery directory must contain restored_hopebringer_skull_runtime and hopebringer_skull/extracted/hopebringer_skull_20261108/SOURCE_MAP.json. Require exactly 27,768 files / 1,548,273,482 bytes; map SHA256 8ca7c76e406b9900fec5c8f1e8fa9512d1809e8259b6a6829a989b079a3824be.

Place HOPEBRINGER_SKULL_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_SKULL_REMOTE_CHAIN_VERIFICATION.json, SHA256 d369c0d0e238f5b5d816ac636c2760af1629924183daf17b8ac2f8e35e39098f.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Skull source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_nadina.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_nadina.py --hopebringer-skull-recovery /path/to/completed-hopebringer-skull-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and fourteen binary parts from commit 2a61f7edab3cd6ce9826fae3263b9f0c80def62b, path battlegrounds-backup/pending/20261108-hopebringer-nadina. Archive hopebringer_nadina_20261108.tar.xz: 3,464,724 bytes, SHA256 259444bad147d818ae228aad515b05c4e106e2c927692da928bae89c5ea4c7e2.

Every part, assembled archive and all 60 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Hopebringer Skull SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_nadina_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_NADINA_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,770 files / 1,548,279,777 bytes, no missing/mismatched/unexpected files, and target map SHA256 09e4acb1b56ca75044ced6b677807a2f5299c47f098f38c3dadd9efb0e362e75. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Nadina is freshly downloaded this round; historical source evidence and Hopebringer Skull baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Skull receipt establishes continuity through the intervening increments to the fully rehashed Skull baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Nadina, not the historical chain.
