# Recover Hopebringer Strider source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Phantom with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/433398490d6dcb1f84046da644fc25decdfb87d5/battlegrounds-backup/pending/20261108-hopebringer-phantom/RECOVERY.md

That recipe links the complete pinned recovery chain back to the original November 1 release ZIP and recovery/Bloodbound Git sources. Retain the Phantom recovery directory containing restored_hopebringer_phantom_runtime, hopebringer_phantom/extracted/hopebringer_phantom_20261108/SOURCE_MAP.json, and HOPEBRINGER_PHANTOM_REMOTE_CHAIN_VERIFICATION.json.

Required Phantom map SHA256: 9617b0b0e4f823141049d41f0728b1aba2f306e729ae860bc16fd6647acd89ed. Required Phantom receipt SHA256: fdb19a2a819d6ea746e7e2c8138b09acf74606cd8706553aec3f35049b5a8153.

## Restore this increment

Place verify_and_restore_hopebringer_strider.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_strider.py --hopebringer-phantom-recovery /path/to/phantom_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit b4d5109cab57c33105e85b4e2b05eab7b0726f38, folder battlegrounds-backup/pending/20261108-hopebringer-strider. Archive hopebringer_strider_20261108.tar.xz is 1,620,316 bytes, SHA256 f4ad2938938b0a0d0db50dd203fcb77164100ea2c9ac0b0d5c85cf73761e7fa1. It verifies all part hashes, archive hash, 48 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Phantom baseline file is fully rehashed before copying. The independent restored_hopebringer_strider_runtime must have exactly 27,875 files / 1,548,634,283 bytes, SOURCE_MAP SHA256 3abb943757c53ed71ccec8b444fdcd7a458d6c96802086c1fa92190ed0ffcdc4. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Strider increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Phantom receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
