# Recover Electron Methodical Madness source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Gem Barrage recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/26e652062295c3b7be334efbbbd02a65c744f5a1/battlegrounds-backup/pending/20261108-electron-gem-barrage/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Gem Barrage. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Gem Barrage recovery directory must contain restored_gem_barrage_runtime and gem_barrage/extracted/electron_gem_barrage_20261108/SOURCE_MAP.json. Require exactly 27,721 files / 1,548,112,348 bytes; map SHA256 ab70bb0cf113fae82e898b4acb910b218453aad8a3a5981dcd06625b6a818941.

Place these published receipts in that directory:
- GEM_BARRAGE_REMOTE_CHAIN_VERIFICATION.json, SHA256 0c196a35b06699c354de8b9f19b5f2a7f1dff1b73fc50834103e9712283520ab.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Gem Barrage source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_methodical_madness.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_methodical_madness.py --gem-barrage-recovery /path/to/completed-gem-barrage-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit a158b3daab00d4f616abbb3db8307680981a7184, path battlegrounds-backup/pending/20261108-electron-methodical-madness. Archive electron_methodical_madness_20261108.tar.xz: 1,081,156 bytes, SHA256 afab517f4b0390f0e89fa0f00a3489f0f8f06691ced6d582d9c7f7848b878943.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Gem Barrage SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_methodical_madness_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require METHODICAL_MADNESS_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,723 files / 1,548,120,178 bytes, no missing/mismatched/unexpected files, and target map SHA256 125e50eccf1f9d59cb4e16f83d6fd1994cb56a423f9370690dca9502b7f02ab3. Per-file origins are in RESTORE_PROVENANCE.json.

Only Methodical Madness is freshly downloaded this round; historical source evidence and Gem Barrage baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.
