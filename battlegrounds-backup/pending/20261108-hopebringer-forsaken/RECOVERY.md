# Recover Hopebringer Forsaken source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Rat Leader recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/b7b5aaca089e723cee32c33e3ba6fa8b9d1acd97/battlegrounds-backup/pending/20261108-hopebringer-rat-leader/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Rat Leader. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Rat Leader recovery directory must contain restored_hopebringer_rat_leader_runtime and hopebringer_rat_leader/extracted/hopebringer_rat_leader_20261108/SOURCE_MAP.json. Require exactly 27,758 files / 1,548,242,863 bytes; map SHA256 131d581364ab21c0faa390ff33160d2652f8cd99475552195b704cb67b47e4a7.

Place HOPEBRINGER_RAT_LEADER_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_RAT_LEADER_REMOTE_CHAIN_VERIFICATION.json, SHA256 f07464f20a9beec5fb7ee5e86ea8e05d113ba228a8f3b8c3686916a00c09af1e.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Rat Leader source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_forsaken.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_forsaken.py --hopebringer-rat-leader-recovery /path/to/completed-hopebringer-rat-leader-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and seven binary parts from commit 3ab642882c9ed65e62e1aadb4a35ce543db969ba, path battlegrounds-backup/pending/20261108-hopebringer-forsaken. Archive hopebringer_forsaken_20261108.tar.xz: 1,565,968 bytes, SHA256 ad4ae5e962e671775262cfd563d3b8120d341d52dc036227954cb38eed5a4323.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, three additions and no removals. Hopebringer Rat Leader SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_forsaken_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_FORSAKEN_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,761 files / 1,548,252,047 bytes, no missing/mismatched/unexpected files, and target map SHA256 57a47c0f18da92d854dcfa8460c76668b93ea778c831d8ad0fac0ada329b7051. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Forsaken is freshly downloaded this round; historical source evidence and Hopebringer Rat Leader baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The eight delta files are exactly five modifications and three additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Rat Leader receipt establishes continuity through the intervening increments to the fully rehashed Rat Leader baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Forsaken, not the historical chain.
