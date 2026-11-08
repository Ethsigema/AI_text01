# Recover Hopebringer Eudora source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Forsaken recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/bf629d63258373402b89dae856bfbf61e89b85df/battlegrounds-backup/pending/20261108-hopebringer-forsaken/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Forsaken. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Forsaken recovery directory must contain restored_hopebringer_forsaken_runtime and hopebringer_forsaken/extracted/hopebringer_forsaken_20261108/SOURCE_MAP.json. Require exactly 27,761 files / 1,548,252,047 bytes; map SHA256 57a47c0f18da92d854dcfa8460c76668b93ea778c831d8ad0fac0ada329b7051.

Place HOPEBRINGER_FORSAKEN_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_FORSAKEN_REMOTE_CHAIN_VERIFICATION.json, SHA256 298433f323a99a234700f059b5eed51217be76c371399092f33172c9ddc95fc7.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Forsaken source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_eudora.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_eudora.py --hopebringer-forsaken-recovery /path/to/completed-hopebringer-forsaken-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and eleven binary parts from commit 9f5721df03f45b20926e8e6c5e097f90348cdb39, path battlegrounds-backup/pending/20261108-hopebringer-eudora. Archive hopebringer_eudora_20261108.tar.xz: 2,591,092 bytes, SHA256 c65a461ad8f8636cfe77c704bfbcf1ce997abc1a3f879b47d4e6a15a3338807d.

Every part, assembled archive and all 48 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Hopebringer Forsaken SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_eudora_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_EUDORA_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,763 files / 1,548,258,743 bytes, no missing/mismatched/unexpected files, and target map SHA256 423e2cf3e18e4edef0949ce180fb7145e7e8b765d01eb5feeefb4f455ac6df1e. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Eudora is freshly downloaded this round; historical source evidence and Hopebringer Forsaken baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Forsaken receipt establishes continuity through the intervening increments to the fully rehashed Forsaken baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Eudora, not the historical chain.
