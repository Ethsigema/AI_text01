# Recover Electron Locked Discover source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Battlecry Discover recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/1a30f1b4d420ad60a55b2b91665fed91e7ec49bd/battlegrounds-backup/pending/20261108-electron-battlecry-discover/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Battlecry. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Battlecry recovery directory must contain restored_battlecry_discover_runtime and battlecry_discover/extracted/electron_battlecry_discover_20261108/SOURCE_MAP.json. Require exactly 27,705 files / 1,548,063,185 bytes; map SHA256 7e1eea7ffc224727525fef214a08ad6056563b332b95837910c423e7ca666787.

Place these published receipts in that directory:
- BATTLECRY_DISCOVER_REMOTE_CHAIN_VERIFICATION.json, SHA256 7ee3ac374e8e476009d114955ba328a5797432695909c7ea59a1b8e098992272.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Battlecry source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_locked_discover.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_locked_discover.py --battlecry-discover-recovery /path/to/completed-battlecry-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 5affa2537a0478a6eb8e0b468d88ace3a8cf0011, path battlegrounds-backup/pending/20261108-electron-locked-discover. Archive electron_locked_discover_20261108.tar.xz: 1,077,348 bytes, SHA256 474affa3545f2a935d37d7fc7133366397201bfcb9e2376783f80ebfe1ac36cd.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Battlecry SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_locked_discover_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require LOCKED_DISCOVER_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,707 files / 1,548,068,875 bytes, no missing/mismatched/unexpected files, and target map SHA256 c18e95627f7b1d7c754829f58a5364f77069c1e458c43eddde2b7251b9674297. Per-file origins are in RESTORE_PROVENANCE.json.

Only Locked Discover is freshly downloaded this round; historical source evidence and Battlecry baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
