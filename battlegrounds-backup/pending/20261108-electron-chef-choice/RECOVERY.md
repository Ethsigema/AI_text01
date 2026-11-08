# Recover Electron Chef Choice source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Methodical Madness recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/9b0f4fb28f0009cf95e0778339b1f0c4e9627b8e/battlegrounds-backup/pending/20261108-electron-methodical-madness/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Methodical Madness. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Methodical Madness recovery directory must contain restored_methodical_madness_runtime and methodical_madness/extracted/electron_methodical_madness_20261108/SOURCE_MAP.json. Require exactly 27,723 files / 1,548,120,178 bytes; map SHA256 125e50eccf1f9d59cb4e16f83d6fd1994cb56a423f9370690dca9502b7f02ab3.

Place these published receipts in that directory:
- METHODICAL_MADNESS_REMOTE_CHAIN_VERIFICATION.json, SHA256 986626fb2a987b8623a6bcf2001c75fd42415499dc1e1f5af2b40d6a9deaa837.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Methodical Madness source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_chef_choice.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_chef_choice.py --methodical-madness-recovery /path/to/completed-methodical-madness-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 32ffaa836630796372832deaa4b8441d9b82fe4a, path battlegrounds-backup/pending/20261108-electron-chef-choice. Archive electron_chef_choice_20261108.tar.xz: 1,085,872 bytes, SHA256 a16af8dc107c44fa558df23beef080198b08931b5d86abcee88b391d86bf9a20.

Every part, assembled archive and all 38 safe members are verified. Companion hashes and exact map differences must match six modifications, two additions and no removals. Methodical Madness SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_chef_choice_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require CHEF_CHOICE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,725 files / 1,548,126,797 bytes, no missing/mismatched/unexpected files, and target map SHA256 e1a0a8cec47f9e58612f5e0e1533ea8ff01710b0487d09689a21509821f666bc. Per-file origins are in RESTORE_PROVENANCE.json.

Only Chef Choice is freshly downloaded this round; historical source evidence and Methodical Madness baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

Chef Choice gameplay implementation is partial. This verification establishes source-byte recoverability only, not gameplay completeness or acceptance.
