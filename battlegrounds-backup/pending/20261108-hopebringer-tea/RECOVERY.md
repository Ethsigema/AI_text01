# Recover Hopebringer Tea source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Groundskeeper with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/8accb546d9a178470914a723d48ca1578a8687b6/battlegrounds-backup/pending/20261108-hopebringer-groundskeeper/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, Sylvar, Dune, Weaver, Hooktail, Hoarder, and Groundskeeper. Retain the Groundskeeper recovery directory containing restored_hopebringer_groundskeeper_runtime, hopebringer_groundskeeper/extracted/hopebringer_groundskeeper_20261108/SOURCE_MAP.json, and HOPEBRINGER_GROUNDSKEEPER_REMOTE_CHAIN_VERIFICATION.json.

Required Groundskeeper map SHA256: e95f0659426776c1484f3f317b5404b247e74c30b3ce747f47008bd00e48901b. Required Groundskeeper receipt SHA256: 5ccdfb7c3cbac787e2f22b18c623d35ff0a69acb062e8968ca45b9051a359fcc.

## Restore this increment

Place verify_and_restore_hopebringer_tea.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_tea.py --hopebringer-groundskeeper-recovery /path/to/groundskeeper_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit e553f3a7cfe35c13ab5ce764379a7a621bf302b2, folder battlegrounds-backup/pending/20261108-hopebringer-tea. Archive hopebringer_tea_20261108.tar.xz is 1,588,620 bytes, SHA256 a8a947451982dd052171960dd3afa3e9b0cef2b3749c7fa19540fc0f0869b906. It verifies all part hashes, archive hash, 46 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Groundskeeper baseline file is fully rehashed before copying. The independent restored_hopebringer_tea_runtime must have exactly 27,835 files / 1,548,493,187 bytes, SOURCE_MAP SHA256 f5208371d1d9a1eab19abdfab5e50756821236b7d3fece64ca223f11c80921ce. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Tea increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Groundskeeper receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
