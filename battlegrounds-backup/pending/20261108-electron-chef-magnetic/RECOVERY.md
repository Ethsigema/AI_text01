# Recover Electron Chef Magnetic source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Chef Choice recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/e4b93d79e3889e39de4584d8e173f2cd580335d7/battlegrounds-backup/pending/20261108-electron-chef-choice/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Chef Choice. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Chef Choice recovery directory must contain restored_chef_choice_runtime and chef_choice/extracted/electron_chef_choice_20261108/SOURCE_MAP.json. Require exactly 27,725 files / 1,548,126,797 bytes; map SHA256 e1a0a8cec47f9e58612f5e0e1533ea8ff01710b0487d09689a21509821f666bc.

Place these published receipts in that directory:
- CHEF_CHOICE_REMOTE_CHAIN_VERIFICATION.json, SHA256 b0037ef1e7dc19952915e78f49e03350b5c27e70f994cba4d48c3fecce343c80.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Chef Choice source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_chef_magnetic.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_chef_magnetic.py --chef-choice-recovery /path/to/completed-chef-choice-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 054dccd84590fc60323a8e6202fbb88d8ff39d39, path battlegrounds-backup/pending/20261108-electron-chef-magnetic. Archive electron_chef_magnetic_20261108.tar.xz: 1,085,628 bytes, SHA256 42cc923b5a7b2fc6c950a2f3b410ced70a984ce118dddb4875cf3b9a6fea3dba.

Every part, assembled archive and all 38 safe members are verified. Companion hashes and exact map differences must match six modifications, zero additions and no removals. Chef Choice SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_chef_magnetic_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require CHEF_MAGNETIC_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,725 files / 1,548,128,293 bytes, no missing/mismatched/unexpected files, and target map SHA256 696b48e489f4ed384fd2a65bad4e56436cc35b239bf55d5eacd2a920dcdde7af. Per-file origins are in RESTORE_PROVENANCE.json.

Only Chef Magnetic is freshly downloaded this round; historical source evidence and Chef Choice baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

Chef Magnetic gameplay implementation is partial. This verification establishes source-byte recoverability only, not gameplay completeness or acceptance.

The eight packaged delta files contain six actual modifications and two unchanged redundant files: research/electron_chef_choice/evidence.json and research/electron_chef_choice/BG28_518.native.xml. The helper verifies both redundant files equal their baseline and target hashes, separately from the six actual CHANGES entries. There are no additions or removals. The frozen archive remains unchanged.
