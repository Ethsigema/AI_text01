# Recover Hopebringer Hoarder source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Hooktail with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/f20826d2b537d76f2658c256616bb8348a48f988/battlegrounds-backup/pending/20261108-hopebringer-hooktail/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, Sylvar, Dune, Weaver, and Hooktail. Retain the Hooktail recovery directory containing restored_hopebringer_hooktail_runtime, hopebringer_hooktail/extracted/hopebringer_hooktail_20261108/SOURCE_MAP.json, and HOPEBRINGER_HOOKTAIL_REMOTE_CHAIN_VERIFICATION.json.

Required Hooktail map SHA256: 31ff2f5b844400593f57f8dce4423ea64ea9f9a6c9cba986b1110de20aab04a7. Required Hooktail receipt SHA256: 7ab0cc2546c8cb6c6eb6fb6f0b8173f9fa120add91d087a73fe06507476a5c82.

## Restore this increment

Place verify_and_restore_hopebringer_hoarder.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_hoarder.py --hopebringer-hooktail-recovery /path/to/hooktail_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 035ed1f9416e1fc2317e95dda62ca4193c425f78, folder battlegrounds-backup/pending/20261108-hopebringer-hoarder. Archive hopebringer_hoarder_20261108.tar.xz is 1,581,820 bytes, SHA256 e4271a74f442eaccf807e2cc0130a915eb352f233e2f8aa6113489620606d7a9. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Hooktail baseline file is fully rehashed before copying. The independent restored_hopebringer_hoarder_runtime must have exactly 27,829 files / 1,548,470,700 bytes, SOURCE_MAP SHA256 4f5ca51d64dfdc38e5d86c685b345a6eb45d133ab4b29c027b5df841de01394b. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Hoarder increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Hooktail receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
