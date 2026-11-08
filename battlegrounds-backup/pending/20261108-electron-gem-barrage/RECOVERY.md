# Recover Electron Gem Barrage source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Planar Telescope recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/ef3c4ba0d3558976a68d5b64f2bcf6cca5c54e74/battlegrounds-backup/pending/20261108-electron-planar-telescope/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Planar Telescope. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Planar Telescope recovery directory must contain restored_planar_telescope_runtime and planar_telescope/extracted/electron_planar_telescope_20261108/SOURCE_MAP.json. Require exactly 27,719 files / 1,548,105,700 bytes; map SHA256 8924681eebd90ccafc2b0ab1c9e6dac974a5a947936a3a7f12750e22d0464a2d.

Place these published receipts in that directory:
- PLANAR_TELESCOPE_REMOTE_CHAIN_VERIFICATION.json, SHA256 6e27e8448041d0cf80dc9ea46b499762e6c9e7b20718c35ff9826751f775dfbc.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Planar Telescope source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_gem_barrage.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_gem_barrage.py --planar-telescope-recovery /path/to/completed-planar-telescope-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit fc4cbad5bd60f0aa81baca615e708555c6e4a1cb, path battlegrounds-backup/pending/20261108-electron-gem-barrage. Archive electron_gem_barrage_20261108.tar.xz: 1,079,548 bytes, SHA256 1e0bc7bede79f981036f0843a258cfe8f8ac61cbdbbd92e68f4f66fdf7f5d47c.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Planar Telescope SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_gem_barrage_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require GEM_BARRAGE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,721 files / 1,548,112,348 bytes, no missing/mismatched/unexpected files, and target map SHA256 ab70bb0cf113fae82e898b4acb910b218453aad8a3a5981dcd06625b6a818941. Per-file origins are in RESTORE_PROVENANCE.json.

Only Gem Barrage is freshly downloaded this round; historical source evidence and Planar Telescope baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
