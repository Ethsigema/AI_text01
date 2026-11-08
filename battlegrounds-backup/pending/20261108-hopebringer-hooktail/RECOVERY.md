# Recover Hopebringer Hooktail source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Weaver with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/3d1eae7e6efa5b58aff0f8f357f1db4b1dbca8dd/battlegrounds-backup/pending/20261108-hopebringer-weaver/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, Sylvar, Dune, and Weaver. Retain the Weaver recovery directory containing restored_hopebringer_weaver_runtime, hopebringer_weaver/extracted/hopebringer_weaver_20261108/SOURCE_MAP.json, and HOPEBRINGER_WEAVER_REMOTE_CHAIN_VERIFICATION.json.

Required Weaver map SHA256: bb941238bde7de43664ce830363307bf455fed7d4e1af587b31dd38876ebaf55. Required Weaver receipt SHA256: 93f5ae43858a00339f1e7212ac9b79d3bc1c9577d057d040f8a337c10f453bb0.

## Restore this increment

Place verify_and_restore_hopebringer_hooktail.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_hooktail.py --hopebringer-weaver-recovery /path/to/weaver_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 2b53de0c2d6e5f00417faf2ce0fc5e55a513f49a, folder battlegrounds-backup/pending/20261108-hopebringer-hooktail. Archive hopebringer_hooktail_20261108.tar.xz is 1,580,696 bytes, SHA256 eca4473dc6a5d191c0b5397775b8810d16faa5beb553363f36e0bd2937065706. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Weaver baseline file is fully rehashed before copying. The independent restored_hopebringer_hooktail_runtime must have exactly 27,827 files / 1,548,463,981 bytes, SOURCE_MAP SHA256 31ff2f5b844400593f57f8dce4423ea64ea9f9a6c9cba986b1110de20aab04a7. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Hooktail increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Weaver receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
