# Recover Hopebringer Groundskeeper source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Hoarder with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/f1d2bd283daef6af8ee234eee52ca55e451cf432/battlegrounds-backup/pending/20261108-hopebringer-hoarder/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, Sylvar, Dune, Weaver, Hooktail, and Hoarder. Retain the Hoarder recovery directory containing restored_hopebringer_hoarder_runtime, hopebringer_hoarder/extracted/hopebringer_hoarder_20261108/SOURCE_MAP.json, and HOPEBRINGER_HOARDER_REMOTE_CHAIN_VERIFICATION.json.

Required Hoarder map SHA256: 4f5ca51d64dfdc38e5d86c685b345a6eb45d133ab4b29c027b5df841de01394b. Required Hoarder receipt SHA256: 70906205fd4767b90a5d45b399d525708ce85ea49c86cb4f796557ba75ef5c76.

## Restore this increment

Place verify_and_restore_hopebringer_groundskeeper.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_groundskeeper.py --hopebringer-hoarder-recovery /path/to/hoarder_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 3edd9d3870863a80bd4b5bebb96710ccc99c0029, folder battlegrounds-backup/pending/20261108-hopebringer-groundskeeper. Archive hopebringer_groundskeeper_20261108.tar.xz is 1,588,648 bytes, SHA256 bfdc4dfd995abbe0f21c28b9b53f74a0786075aab175d4d26d3a63c45e3a8743. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Hoarder baseline file is fully rehashed before copying. The independent restored_hopebringer_groundskeeper_runtime must have exactly 27,832 files / 1,548,482,938 bytes, SOURCE_MAP SHA256 e95f0659426776c1484f3f317b5404b247e74c30b3ce747f47008bd00e48901b. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Groundskeeper increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Hoarder receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
