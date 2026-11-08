# Recover Electron Planar Telescope source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Type Refresh recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/7e97a154096c21bd8c5b7d2ab9c889ebc9ac5aa8/battlegrounds-backup/pending/20261108-electron-type-refresh/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Type Refresh. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Type Refresh recovery directory must contain restored_type_refresh_runtime and type_refresh/extracted/electron_type_refresh_20261108/SOURCE_MAP.json. Require exactly 27,717 files / 1,548,100,726 bytes; map SHA256 7d11fbb5e4f8f090bfb2592444e1e773434fe1a3ed08f4d6b3e90ad6a8c2036f.

Place these published receipts in that directory:
- TYPE_REFRESH_REMOTE_CHAIN_VERIFICATION.json, SHA256 f8d1a9a90d2671c7165a074cdd1e2e25c8e636050bdc9e89d98b4b11b68c5ec2.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Type Refresh source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_planar_telescope.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_planar_telescope.py --type-refresh-recovery /path/to/completed-type-refresh-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 2bfd33d26a82c894ed5552d3b75f1dd7b5dd9f1a, path battlegrounds-backup/pending/20261108-electron-planar-telescope. Archive electron_planar_telescope_20261108.tar.xz: 1,079,076 bytes, SHA256 46c5b8a89d88f1f6ddfa3319ee886f48fb818687789eee0bbd9332937c2613d2.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Type Refresh SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_planar_telescope_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require PLANAR_TELESCOPE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,719 files / 1,548,105,700 bytes, no missing/mismatched/unexpected files, and target map SHA256 8924681eebd90ccafc2b0ab1c9e6dac974a5a947936a3a7f12750e22d0464a2d. Per-file origins are in RESTORE_PROVENANCE.json.

Only Planar Telescope is freshly downloaded this round; historical source evidence and Type Refresh baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
