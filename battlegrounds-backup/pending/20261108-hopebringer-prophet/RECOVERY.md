# Recover Hopebringer Prophet source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Rescue with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/25e6df4971f482fbe01c3a696913f6e73604dede/battlegrounds-backup/pending/20261108-hopebringer-rescue/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, Sylvar, Dune, Weaver, Hooktail, Hoarder, Groundskeeper, Tea, and Rescue. Retain the Rescue recovery directory containing restored_hopebringer_rescue_runtime, hopebringer_rescue/extracted/hopebringer_rescue_20261108/SOURCE_MAP.json, and HOPEBRINGER_RESCUE_REMOTE_CHAIN_VERIFICATION.json.

Required Rescue map SHA256: 979a05605467202a36d51225807fa162cdd53fb1c449c1573bc5347fadd6aec2. Required Rescue receipt SHA256: 80c51e52b66726d2158cef04b6813c8225d528397cc31d54c43d067d627731cb.

## Restore this increment

Place verify_and_restore_hopebringer_prophet.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_prophet.py --hopebringer-rescue-recovery /path/to/rescue_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 1b5f4754faa7d68500e950d0ac3d3f3bcbabe686, folder battlegrounds-backup/pending/20261108-hopebringer-prophet. Archive hopebringer_prophet_20261108.tar.xz is 1,590,368 bytes, SHA256 c661b638dd4e1247b0fee0ccb88205bb5060a1ad59f47b744acbc04ab3e8433e. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Rescue baseline file is fully rehashed before copying. The independent restored_hopebringer_prophet_runtime must have exactly 27,840 files / 1,548,509,804 bytes, SOURCE_MAP SHA256 8d101d811bb61f6dfdb7ede936562fdacfb142e567d69316a1f477037f7bc190. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Prophet increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Rescue receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
