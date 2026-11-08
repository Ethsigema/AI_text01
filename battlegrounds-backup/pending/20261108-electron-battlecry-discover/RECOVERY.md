# Recover Electron Battlecry Discover source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Cloning Conch recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/2f56cbcf1ac5816edc88fc99fe090c81d1cfd39f/battlegrounds-backup/pending/20261108-electron-cloning-conch/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Conch. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Conch recovery directory must contain restored_cloning_conch_runtime and cloning_conch/extracted/electron_cloning_conch_20261108/SOURCE_MAP.json. Require exactly 27,703 files / 1,548,057,670 bytes; map SHA256 4af4961f1d1b1f67ab9981f92bcd202553c8a35a9f2faa9a1f69bd47627883dd.

Place these published receipts in that directory:
- CLONING_CONCH_REMOTE_CHAIN_VERIFICATION.json, SHA256 01bf6488c25a1170c8b09331485e3f85c98f7bae0f0bfff6a584b259a6a56606.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Conch source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_battlecry_discover.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_battlecry_discover.py --cloning-conch-recovery /path/to/completed-conch-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit f0653df584e12d274ca689f6384b3a45f1efe060, path battlegrounds-backup/pending/20261108-electron-battlecry-discover. Archive electron_battlecry_discover_20261108.tar.xz: 1,076,612 bytes, SHA256 d8de842db29100276342e4fbc0a9c9c29e4d8b6a31423eb77c642ef165489ba7.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Conch SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_battlecry_discover_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require BATTLECRY_DISCOVER_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,705 files / 1,548,063,185 bytes, no missing/mismatched/unexpected files, and target map SHA256 7e1eea7ffc224727525fef214a08ad6056563b332b95837910c423e7ca666787. Per-file origins are in RESTORE_PROVENANCE.json.

Only Battlecry Discover is freshly downloaded this round; historical source evidence and Conch baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
