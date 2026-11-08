# Recover Hopebringer Leeroy source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Titus recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/7a643b3b7aa23d5028d8f49ca410a9e2b1fb337f/battlegrounds-backup/pending/20261108-hopebringer-titus/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Titus. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Titus recovery directory must contain restored_hopebringer_titus_runtime and hopebringer_titus/extracted/hopebringer_titus_20261108/SOURCE_MAP.json. Require exactly 27,772 files / 1,548,288,014 bytes; map SHA256 8e91bb42f29e491ac948ab8513292251b1cab19183f9eee783918dd67a1148be.

Place HOPEBRINGER_TITUS_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_TITUS_REMOTE_CHAIN_VERIFICATION.json, SHA256 e69c09d237a35c646b3a26ff23616bfc482bc0372e2bad691ef21de2f2b5ba48.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Titus source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_leeroy.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_leeroy.py --hopebringer-titus-recovery /path/to/completed-hopebringer-titus-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and seven binary parts from commit 188ec8047ade8f5d4662a1005e9498d3bae63094, path battlegrounds-backup/pending/20261108-hopebringer-leeroy. Archive hopebringer_leeroy_20261108.tar.xz: 1,555,196 bytes, SHA256 b1a364c79881a7520cb3abe0c428d7140386c785a2643e5718c90d8f69b28aff.

Every part, assembled archive and all 36 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Hopebringer Titus SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_leeroy_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_LEEROY_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,774 files / 1,548,293,852 bytes, no missing/mismatched/unexpected files, and target map SHA256 934cdd469da4a27c3ed3a9bfd659bd6d8595f112138b47e5807997ef6c512030. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Leeroy is freshly downloaded this round; historical source evidence and Hopebringer Titus baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Titus receipt establishes continuity through the intervening increments to the fully rehashed Titus baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Leeroy, not the historical chain.
