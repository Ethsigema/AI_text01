# Recover Electron Type Refresh source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Earth Mother recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/031d6bfb1cb044c9e7c69f3d6acf04d852dac2f2/battlegrounds-backup/pending/20261108-electron-earth-mother/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Earth Mother. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Earth Mother recovery directory must contain restored_earth_mother_runtime and earth_mother/extracted/electron_earth_mother_20261108/SOURCE_MAP.json. Require exactly 27,715 files / 1,548,093,832 bytes; map SHA256 05dbcc97097782b408b73e9cb2e55e018739a6063dd82ef66efdf92ba3c61b3f.

Place these published receipts in that directory:
- EARTH_MOTHER_REMOTE_CHAIN_VERIFICATION.json, SHA256 09decd982730bc39dc6e4b5e65085d3bdfe34d7233eaceafade6f84cdd710542.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Earth Mother source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_type_refresh.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_type_refresh.py --earth-mother-recovery /path/to/completed-earth-mother-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 39b1e73b5b362915b1151bbc623464cd86defbb8, path battlegrounds-backup/pending/20261108-electron-type-refresh. Archive electron_type_refresh_20261108.tar.xz: 1,078,324 bytes, SHA256 69931527bea9114d3f7ad196c6c5f17898e585d4a6e0595d580e1bbf8c233582.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Earth Mother SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_type_refresh_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require TYPE_REFRESH_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,717 files / 1,548,100,726 bytes, no missing/mismatched/unexpected files, and target map SHA256 7d11fbb5e4f8f090bfb2592444e1e773434fe1a3ed08f4d6b3e90ad6a8c2036f. Per-file origins are in RESTORE_PROVENANCE.json.

Only Type Refresh is freshly downloaded this round; historical source evidence and Earth Mother baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
