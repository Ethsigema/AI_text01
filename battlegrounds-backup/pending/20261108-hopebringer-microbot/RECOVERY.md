# Recover Hopebringer Microbot source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Privateer Majority recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/7fc9fbbba750a0c9852291954ba8554801749943/battlegrounds-backup/pending/20261108-electron-privateer-majority/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Privateer Majority. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The latest scheduled Privateer Wealth whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Privateer Majority recovery directory must contain restored_privateer_majority_runtime and privateer_majority/extracted/electron_privateer_majority_20261108/SOURCE_MAP.json. Require exactly 27,750 files / 1,548,215,949 bytes; map SHA256 8d7ebfc803f3f410b8cffea9de3710c5bba7ad6173ad706bc5018a855618b6d0.

Place PRIVATEER_MAJORITY_REMOTE_CHAIN_VERIFICATION.json in the baseline directory and the latest FRESH_WHOLE_CHAIN_VERIFICATION.json beside this helper:
- PRIVATEER_MAJORITY_REMOTE_CHAIN_VERIFICATION.json, SHA256 fd00d5ce155c729422d1a1748e825bf7aa85248110f982f3e77676ce836d32b6.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 fd25b27e3113830b7d692beab0f02d85568bc579c5b995e663fe3fa1feb2a319.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Privateer Majority source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_hopebringer_microbot.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_hopebringer_microbot.py --privateer-majority-recovery /path/to/completed-privateer-majority-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and seven binary parts from commit c76147ebcce76c78e58a93612a927571307d6f68, path battlegrounds-backup/pending/20261108-hopebringer-microbot. Archive hopebringer_microbot_20261108.tar.xz: 1,566,588 bytes, SHA256 937b8ec1050b57df2b4517768b28584a61da026d6e78893be744eddd4b305e87.

Every part, assembled archive and all 55 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Privateer Majority SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_hopebringer_microbot_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require HOPEBRINGER_MICROBOT_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,752 files / 1,548,222,414 bytes, no missing/mismatched/unexpected files, and target map SHA256 90e3daeb7358b1764b0871fb7b4ee9982609f502dbe985012bc27bd6bec94ae3. Per-file origins are in RESTORE_PROVENANCE.json.

Only Hopebringer Microbot is freshly downloaded this round; historical source evidence and Privateer Majority baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.

The latest whole-chain receipt, published at commit f6b1ae512e2796a6e3b0f0b7b9ce7b717da458a0, ends at Wealth. The pinned Majority receipt establishes continuity through the intervening increments to the fully rehashed Majority baseline, and is bound to that same whole-chain receipt. This run freshly downloads only Hopebringer Microbot, not the historical chain.
