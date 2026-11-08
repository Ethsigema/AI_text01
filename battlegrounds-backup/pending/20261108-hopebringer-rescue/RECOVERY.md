# Recover Hopebringer Rescue source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Tea with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/2dfb76fc74bc31e090486dda4429f4775d5af98b/battlegrounds-backup/pending/20261108-hopebringer-tea/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, Sylvar, Dune, Weaver, Hooktail, Hoarder, Groundskeeper, and Tea. Retain the Tea recovery directory containing restored_hopebringer_tea_runtime, hopebringer_tea/extracted/hopebringer_tea_20261108/SOURCE_MAP.json, and HOPEBRINGER_TEA_REMOTE_CHAIN_VERIFICATION.json.

Required Tea map SHA256: f5208371d1d9a1eab19abdfab5e50756821236b7d3fece64ca223f11c80921ce. Required Tea receipt SHA256: a0fbf3d6389a55de1d473435e1218019222fad985fb249cc5360d7536015c2f1.

## Restore this increment

Place verify_and_restore_hopebringer_rescue.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_rescue.py --hopebringer-tea-recovery /path/to/tea_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit ebf988e556315e3e682724349f38192e5be6d237, folder battlegrounds-backup/pending/20261108-hopebringer-rescue. Archive hopebringer_rescue_20261108.tar.xz is 1,586,104 bytes, SHA256 878aac7ba694e9f7f34306f79c708a0c4adf88269c7ea1c59bf69b36e6868074. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Tea baseline file is fully rehashed before copying. The independent restored_hopebringer_rescue_runtime must have exactly 27,838 files / 1,548,503,171 bytes, SOURCE_MAP SHA256 979a05605467202a36d51225807fa162cdd53fb1c449c1573bc5347fadd6aec2. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Rescue increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Tea receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
