# Recover Hopebringer Urzul source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Drakkari Devour with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/5a19a4ae428b671775a7e0b8a0a269abbd1475f6/battlegrounds-backup/pending/20261108-hopebringer-drakkari-devour/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Drakkari Devour recovery directory containing restored_hopebringer_drakkari_devour_runtime, hopebringer_drakkari_devour/extracted/hopebringer_drakkari_devour_20261108/SOURCE_MAP.json, and HOPEBRINGER_DRAKKARI_DEVOUR_REMOTE_CHAIN_VERIFICATION.json.

Required Drakkari Devour map SHA256: 2130f84b455c534c421306136727ca097327f4f9ccb08af6dfd914d4eca28def. Required Drakkari Devour receipt SHA256: 8b3bc46011ccbcce4fabc0f44325ce68fcb43eb37193aae31cd4d092be25a43a.

## Restore this increment

Place verify_and_restore_hopebringer_urzul.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_urzul.py --hopebringer-drakkari-devour-recovery /path/to/drakkari_devour_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 0eef14ca436bb963d289e1d06d8a100d3408ff1b, folder battlegrounds-backup/pending/20261108-hopebringer-urzul. Archive hopebringer_urzul_20261108.tar.xz is 1,599,964 bytes, SHA256 35a9a536ad7181f921289508375d1ae0777512d7a5ac7d76611388a42f34158d. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Drakkari Devour baseline file is fully rehashed before copying. The independent restored_hopebringer_urzul_runtime must have exactly 27,854 files / 1,548,557,641 bytes, SOURCE_MAP SHA256 c5be020f61efcc6b04383fb27090ff9c00d292233919fa9aadf4e1c5681f42cc. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Urzul increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Drakkari Devour receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
