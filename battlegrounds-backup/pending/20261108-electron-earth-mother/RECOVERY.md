# Recover Electron Earth Mother source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Choose Discover recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/fc8abc7268715470cc040d1a5849220143f36da0/battlegrounds-backup/pending/20261108-electron-choose-discover/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Choose Discover. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Choose Discover recovery directory must contain restored_choose_discover_runtime and choose_discover/extracted/electron_choose_discover_20261108/SOURCE_MAP.json. Require exactly 27,713 files / 1,548,087,620 bytes; map SHA256 3d185d5cfdc669d2400d683609b64237749e8eac4612741f36b6d23120e62dc0.

Place these published receipts in that directory:
- CHOOSE_DISCOVER_REMOTE_CHAIN_VERIFICATION.json, SHA256 bc67ecc955b21ef1986ff3225a38cfa5b903d6dde3372774d852dc9550dfddb8.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Choose Discover source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_earth_mother.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_earth_mother.py --choose-discover-recovery /path/to/completed-choose-discover-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 6838920a590e88061333ecb4bab8a6dbc1f70d72, path battlegrounds-backup/pending/20261108-electron-earth-mother. Archive electron_earth_mother_20261108.tar.xz: 1,075,876 bytes, SHA256 26b44068ca393b359000a8677aa4c3e8d415482aea4163ee5cb8c712bd012225.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Choose Discover SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_earth_mother_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require EARTH_MOTHER_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,715 files / 1,548,093,832 bytes, no missing/mismatched/unexpected files, and target map SHA256 05dbcc97097782b408b73e9cb2e55e018739a6063dd82ef66efdf92ba3c61b3f. Per-file origins are in RESTORE_PROVENANCE.json.

Only Earth Mother is freshly downloaded this round; historical source evidence and Choose Discover baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
