# Recover Hopebringer Bonehead source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Hopebringer Microbot recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/548852b456ceb993d28f0e7f7d1acde1bf369255/battlegrounds-backup/pending/20261108-hopebringer-microbot/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Hopebringer Microbot. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Hopebringer Microbot recovery directory must contain restored_hopebringer_microbot_runtime and hopebringer_microbot/extracted/hopebringer_microbot_20261108/SOURCE_MAP.json. Require exactly 27,752 files / 1,548,222,414 bytes; map SHA256 90e3daeb7358b1764b0871fb7b4ee9982609f502dbe985012bc27bd6bec94ae3.

Place HOPEBRINGER_MICROBOT_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- HOPEBRINGER_MICROBOT_REMOTE_CHAIN_VERIFICATION.json, SHA256 6da5761aabadd273e25832984ea7cde99aeb46e5e9b171ec632d23b34e30099d.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Hopebringer Microbot source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_bonehead.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_bonehead.py --hopebringer-microbot-recovery /path/to/completed-hopebringer-microbot-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and seven binary parts from commit d3a8bbfbc140795cf4fba6332fb821884bc8d48a, path battlegrounds-backup/pending/20261108-hopebringer-bonehead. Archive hopebringer_bonehead_20261108.tar.xz: 1,559,328 bytes, SHA256 abc589f4552edbbe06ee1575d94760a24ae2b0ba32172b032abccbffa59122ab.

Every part, assembled archive and all 36 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Hopebringer Microbot SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_bonehead_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_BONEHEAD_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,754 files / 1,548,228,427 bytes, no missing/mismatched/unexpected files, and target map SHA256 0f4533bc8e1e27446d0a6ddd84b24a33436cd904bf7fca593c9155ac2162baf4. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Bonehead is freshly downloaded this round; historical source evidence and Hopebringer Microbot baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Microbot receipt establishes continuity through the intervening increments to the fully rehashed Microbot baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Bonehead, not the historical chain.
