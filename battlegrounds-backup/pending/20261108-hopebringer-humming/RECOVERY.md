# Recover Hopebringer Humming source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Banana with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/b3e57db6cd419cbb92ce8f467012e858cdbaf5a5/battlegrounds-backup/pending/20261108-hopebringer-banana/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, and Banana. Retain the Banana recovery directory containing restored_hopebringer_banana_runtime, hopebringer_banana/extracted/hopebringer_banana_20261108/SOURCE_MAP.json, and HOPEBRINGER_BANANA_REMOTE_CHAIN_VERIFICATION.json.

Required Banana map SHA256: 801ee9d585dbf6b6bc51b57f89ec3dc769c644d23799867cd600db71f1791d28. Required Banana receipt SHA256: 435bd80d14d81a27e7cae4e8cbf3e8be8dc046a02c59de9c82008c3239db609a.

## Restore this increment

Place verify_and_restore_hopebringer_humming.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_humming.py --hopebringer-banana-recovery /path/to/banana_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit f7919f28d466cb2cf3b4ac463659937351b01777, folder battlegrounds-backup/pending/20261108-hopebringer-humming. Archive hopebringer_humming_20261108.tar.xz is 1,577,040 bytes, SHA256 8e1b9fd84a1b144c551b07f633e6c2fd02d91773786389399240895522373d54. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Banana baseline file is fully rehashed before copying. The independent restored_hopebringer_humming_runtime must have exactly 27,784 files / 1,548,326,479 bytes, SOURCE_MAP SHA256 75ab1ea4ff1dcd8e57495841c0f1e17c7ace505645eea9d0b8abd4b9f8becdc6. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Humming increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
