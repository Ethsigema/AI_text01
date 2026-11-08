# Recover Hopebringer Blade source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Leeroy recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/1fd3d13e4b6a46cb2b1eabdf453f165f31ae56b0/battlegrounds-backup/pending/20261108-hopebringer-leeroy/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Leeroy. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Leeroy recovery directory must contain restored_hopebringer_leeroy_runtime and hopebringer_leeroy/extracted/hopebringer_leeroy_20261108/SOURCE_MAP.json. Require exactly 27,774 files / 1,548,293,852 bytes; map SHA256 934cdd469da4a27c3ed3a9bfd659bd6d8595f112138b47e5807997ef6c512030.

Place HOPEBRINGER_LEEROY_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_LEEROY_REMOTE_CHAIN_VERIFICATION.json, SHA256 c91f43bbfae1a60c0925dc427008c4e7e89c05f4ff18ccf08acf7ae8c25cef86.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Leeroy source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_blade.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_blade.py --hopebringer-leeroy-recovery /path/to/completed-hopebringer-leeroy-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and seven binary parts from commit baf5c3464f35a76b199ba95129322858b5e59507, path battlegrounds-backup/pending/20261108-hopebringer-blade. Archive hopebringer_blade_20261108.tar.xz: 1,560,936 bytes, SHA256 f79d268466298d2b67fe117c5f9879f4cedbc195959d4281126515d78dc21b11.

Every part, assembled archive and all 36 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Hopebringer Leeroy SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_blade_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_BLADE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,776 files / 1,548,299,466 bytes, no missing/mismatched/unexpected files, and target map SHA256 f00667559104e5af8ac6015d5e52bb8d1ffd74742b312277b43cf6337d9a472f. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Blade is freshly downloaded this round; historical source evidence and Hopebringer Leeroy baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Leeroy receipt establishes continuity through the intervening increments to the fully rehashed Leeroy baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Blade, not the historical chain.
