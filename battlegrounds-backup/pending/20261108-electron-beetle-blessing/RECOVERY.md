# Recover Electron Beetle Blessing source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Gem Confiscation recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/da0e22c7eb889bc039c423f6073b798e27397c54/battlegrounds-backup/pending/20261108-electron-gem-confiscation/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Gem Confiscation. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Gem Confiscation recovery directory must contain restored_gem_confiscation_runtime and gem_confiscation/extracted/electron_gem_confiscation_20261108/SOURCE_MAP.json. Require exactly 27,727 files / 1,548,135,510 bytes; map SHA256 d08421c3d32fd5f07e583b10e64a85b56ef39b596944fc0023ffaa617d05f93a.

Place these published receipts in that directory:
- GEM_CONFISCATION_REMOTE_CHAIN_VERIFICATION.json, SHA256 194cf34c4fc26e6ec8942f6dc8889b8389407649d4c814d8fbb8a0f0a3b613d4.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Gem Confiscation source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_beetle_blessing.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_beetle_blessing.py --gem-confiscation-recovery /path/to/completed-gem-confiscation-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit e83d646f0f6add67e2d971df07f70ec0ea2fcf04, path battlegrounds-backup/pending/20261108-electron-beetle-blessing. Archive electron_beetle_blessing_20261108.tar.xz: 1,087,648 bytes, SHA256 d95dfe8dd2a7c537208674ff86e1b516fc441927e9375b37ca2d6b86d6e50d30.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Gem Confiscation SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_beetle_blessing_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require BEETLE_BLESSING_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,729 files / 1,548,142,587 bytes, no missing/mismatched/unexpected files, and target map SHA256 c91bbad9c9d37b2c27a6a2ab774b374c2ba5dafb60a331a94f7fe0b29f3952e7. Per-file origins are in RESTORE_PROVENANCE.json.

Only Beetle Blessing is freshly downloaded this round; historical source evidence and Gem Confiscation baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.
