# Recover Hopebringer Weaver source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Dune with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/5d35dd88c83853681367c1e8aef16dcd95b0171a/battlegrounds-backup/pending/20261108-hopebringer-dune/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, Sylvar, and Dune. Retain the Dune recovery directory containing restored_hopebringer_dune_runtime, hopebringer_dune/extracted/hopebringer_dune_20261108/SOURCE_MAP.json, and HOPEBRINGER_DUNE_REMOTE_CHAIN_VERIFICATION.json.

Required Dune map SHA256: afcfedcc2db16afaa31e2007e32c39dd63d6efef20fdcdfd975d7c5a97c67ad7. Required Dune receipt SHA256: a4dab7e378f6f79cfee6bc695c6b3ba8385866c500ec5d89594b6ee51b2a833f.

## Restore this increment

Place verify_and_restore_hopebringer_weaver.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_weaver.py --hopebringer-dune-recovery /path/to/dune_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit eca59f5c592b437972b3b989d439586b83b89191, folder battlegrounds-backup/pending/20261108-hopebringer-weaver. Archive hopebringer_weaver_20261108.tar.xz is 1,588,964 bytes, SHA256 9893c581e0aba12b3c6edd3fecd481ff3ff6f79b3fcd2e2b24423aa29f0722c3. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Dune baseline file is fully rehashed before copying. The independent restored_hopebringer_weaver_runtime must have exactly 27,824 files / 1,548,452,794 bytes, SOURCE_MAP SHA256 bb941238bde7de43664ce830363307bf455fed7d4e1af587b31dd38876ebaf55. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Weaver increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at the exact supplied Dune BASE_MAP. The older ordinary Dune receipt is also checked, but is not substituted for this latest proof.
