# Recover Electron Corrupted Coin source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Beetle Blessing recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/be4ae90d64b63ec460030330f83cf7bff2c6f4a7/battlegrounds-backup/pending/20261108-electron-beetle-blessing/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Beetle Blessing. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Beetle Blessing recovery directory must contain restored_beetle_blessing_runtime and beetle_blessing/extracted/electron_beetle_blessing_20261108/SOURCE_MAP.json. Require exactly 27,729 files / 1,548,142,587 bytes; map SHA256 c91bbad9c9d37b2c27a6a2ab774b374c2ba5dafb60a331a94f7fe0b29f3952e7.

Place these published receipts in that directory:
- BEETLE_BLESSING_REMOTE_CHAIN_VERIFICATION.json, SHA256 1432bb9d874b7a00f67852159afd08c578af0e21d28d0a66026072e0032af27b.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Beetle Blessing source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_corrupted_coin.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_corrupted_coin.py --beetle-blessing-recovery /path/to/completed-beetle-blessing-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 60472112a7858d6569eff79b783146443d9f04ab, path battlegrounds-backup/pending/20261108-electron-corrupted-coin. Archive electron_corrupted_coin_20261108.tar.xz: 1,078,292 bytes, SHA256 03750aee5b546752f8d80456545b31afb7c367caf3815031b584b11d47269912.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Beetle Blessing SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_corrupted_coin_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require CORRUPTED_COIN_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,731 files / 1,548,148,085 bytes, no missing/mismatched/unexpected files, and target map SHA256 acfd9e487224daf05eb93e343f099fb26de584f3296c051a510fbb902736dce4. Per-file origins are in RESTORE_PROVENANCE.json.

Only Corrupted Coin is freshly downloaded this round; historical source evidence and Beetle Blessing baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.
