# Recover Hopebringer Mindmuck source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Urzul with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/e09921add489a2815542108afa3b673b899d034a/battlegrounds-backup/pending/20261108-hopebringer-urzul/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Urzul recovery directory containing restored_hopebringer_urzul_runtime, hopebringer_urzul/extracted/hopebringer_urzul_20261108/SOURCE_MAP.json, and HOPEBRINGER_URZUL_REMOTE_CHAIN_VERIFICATION.json.

Required Urzul map SHA256: c5be020f61efcc6b04383fb27090ff9c00d292233919fa9aadf4e1c5681f42cc. Required Urzul receipt SHA256: dc21c7fa71618627378fee323037ca4c65c82ef1bb8b11df247f29ae98bf4a51.

## Restore this increment

Place verify_and_restore_hopebringer_mindmuck.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_mindmuck.py --hopebringer-urzul-recovery /path/to/urzul_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit d09a1225eaccbb14a9ff1f6d15cab185464a67bc, folder battlegrounds-backup/pending/20261108-hopebringer-mindmuck. Archive hopebringer_mindmuck_20261108.tar.xz is 1,602,212 bytes, SHA256 8885ba8e22842280c5bd4f870a7455448a5ddd99fface31c4f3be4937018902c. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Urzul baseline file is fully rehashed before copying. The independent restored_hopebringer_mindmuck_runtime must have exactly 27,856 files / 1,548,565,248 bytes, SOURCE_MAP SHA256 d18852cb8aa7c99d31e6d9ebb297f6151e4a1a8639e3401292c601470bf7a0e7. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Mindmuck increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Urzul receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
