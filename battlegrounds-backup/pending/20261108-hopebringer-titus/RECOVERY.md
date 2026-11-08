# Recover Hopebringer Titus source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Nadina recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/61074906ec3d5bc7889fd03289dbf76eb27590e0/battlegrounds-backup/pending/20261108-hopebringer-nadina/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Nadina. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Nadina recovery directory must contain restored_hopebringer_nadina_runtime and hopebringer_nadina/extracted/hopebringer_nadina_20261108/SOURCE_MAP.json. Require exactly 27,770 files / 1,548,279,777 bytes; map SHA256 09e4acb1b56ca75044ced6b677807a2f5299c47f098f38c3dadd9efb0e362e75.

Place HOPEBRINGER_NADINA_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_NADINA_REMOTE_CHAIN_VERIFICATION.json, SHA256 b70bcdddfc3839a3de0bd6bb0c048a6a96bd4158228868b5402f00cbf452156a.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Nadina source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_titus.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_titus.py --hopebringer-nadina-recovery /path/to/completed-hopebringer-nadina-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and seven binary parts from commit b141aea8f2ca319dc7cab8f79ac8cee6bb9d2d3d, path battlegrounds-backup/pending/20261108-hopebringer-titus. Archive hopebringer_titus_20261108.tar.xz: 1,567,776 bytes, SHA256 380da0a402a28bb9d1efc80c16cf030e06a88c6c6eba06b7b5f35f7c088dd06e.

Every part, assembled archive and all 36 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Hopebringer Nadina SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_titus_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_TITUS_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,772 files / 1,548,288,014 bytes, no missing/mismatched/unexpected files, and target map SHA256 8e91bb42f29e491ac948ab8513292251b1cab19183f9eee783918dd67a1148be. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Titus is freshly downloaded this round; historical source evidence and Hopebringer Nadina baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Nadina receipt establishes continuity through the intervening increments to the fully rehashed Nadina baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Titus, not the historical chain.
