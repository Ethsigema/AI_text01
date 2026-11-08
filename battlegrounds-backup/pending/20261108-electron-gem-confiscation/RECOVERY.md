# Recover Electron Gem Confiscation source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Chef Magnetic recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/a56f5199e2892c4f8299afeeb34c43121e97901d/battlegrounds-backup/pending/20261108-electron-chef-magnetic/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Chef Magnetic. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Chef Magnetic recovery directory must contain restored_chef_magnetic_runtime and chef_magnetic/extracted/electron_chef_magnetic_20261108/SOURCE_MAP.json. Require exactly 27,725 files / 1,548,128,293 bytes; map SHA256 696b48e489f4ed384fd2a65bad4e56436cc35b239bf55d5eacd2a920dcdde7af.

Place these published receipts in that directory:
- CHEF_MAGNETIC_REMOTE_CHAIN_VERIFICATION.json, SHA256 790a8eec70c02936f2dc38dfc190831b1c5544f8f0f219218ba178adf16464df.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Chef Magnetic source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_gem_confiscation.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_gem_confiscation.py --chef-magnetic-recovery /path/to/completed-chef-magnetic-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 27a54e4c5b1f69ae21047c5c39e6601dfd31cbc1, path battlegrounds-backup/pending/20261108-electron-gem-confiscation. Archive electron_gem_confiscation_20261108.tar.xz: 1,119,340 bytes, SHA256 7455e9dec32cdcb55a1824e271f7c3be02b0c11b57ea185bcb218cbab20211df.

Every part, assembled archive and all 52 safe members are verified. Companion hashes and exact map differences must match seven modifications, two additions and no removals. Chef Magnetic SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_gem_confiscation_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require GEM_CONFISCATION_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,727 files / 1,548,135,510 bytes, no missing/mismatched/unexpected files, and target map SHA256 d08421c3d32fd5f07e583b10e64a85b56ef39b596944fc0023ffaa617d05f93a. Per-file origins are in RESTORE_PROVENANCE.json.

Only Gem Confiscation is freshly downloaded this round; historical source evidence and Chef Magnetic baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The nine delta files are exactly seven modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.
