# Recover Hopebringer Skull source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Beetle recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/313d69fc217e15e3da41308996f23a23be2e7b9a/battlegrounds-backup/pending/20261108-hopebringer-beetle/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Beetle. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Beetle recovery directory must contain restored_hopebringer_beetle_runtime and hopebringer_beetle/extracted/hopebringer_beetle_20261108/SOURCE_MAP.json. Require exactly 27,766 files / 1,548,266,883 bytes; map SHA256 bfc7e02d881286df6d3db5000ef53245e0dc304422c6aab1cb19847828b65c76.

Place HOPEBRINGER_BEETLE_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_BEETLE_REMOTE_CHAIN_VERIFICATION.json, SHA256 b08bd88b991803cda2342245909cb9b092dd566559daabb09c8fce2a9393429c.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Beetle source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_skull.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_skull.py --hopebringer-beetle-recovery /path/to/completed-hopebringer-beetle-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and twenty-one binary parts from commit a188379c97a9827f0fe1d71b048c889d7229a00e, path battlegrounds-backup/pending/20261108-hopebringer-skull. Archive hopebringer_skull_20261108.tar.xz: 5,066,124 bytes, SHA256 40f4dfad032026457ce06ffc7d10ef707b3c81fef4096a17722c33ecfa16be39.

Every part, assembled archive and all 72 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Hopebringer Beetle SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_skull_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_SKULL_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,768 files / 1,548,273,482 bytes, no missing/mismatched/unexpected files, and target map SHA256 8ca7c76e406b9900fec5c8f1e8fa9512d1809e8259b6a6829a989b079a3824be. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Skull is freshly downloaded this round; historical source evidence and Hopebringer Beetle baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Beetle receipt establishes continuity through the intervening increments to the fully rehashed Beetle baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Skull, not the historical chain.
