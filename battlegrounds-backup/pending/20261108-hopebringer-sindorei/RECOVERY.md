# Recover Hopebringer Sindorei source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Glim with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/beb72d314eab8b4f87f2371b9d64c8a43c59aa8c/battlegrounds-backup/pending/20261108-hopebringer-glim/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, and Glim. Retain the Glim recovery directory containing restored_hopebringer_glim_runtime, hopebringer_glim/extracted/hopebringer_glim_20261108/SOURCE_MAP.json, and HOPEBRINGER_GLIM_REMOTE_CHAIN_VERIFICATION.json.

Required Glim map SHA256: 6317c4fa555653bb258ce726b19dbfd2881980bc082e5f406bee60921357af90. Required Glim receipt SHA256: ccfcbed48586158788bcef413786b4119e47dede25b8b508e8be20a5227d559a.

## Restore this increment

Place verify_and_restore_hopebringer_sindorei.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_sindorei.py --hopebringer-glim-recovery /path/to/glim_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit ccd190d55787bb0a4943c48a9163ce65e79c2600, folder battlegrounds-backup/pending/20261108-hopebringer-sindorei. Archive hopebringer_sindorei_20261108.tar.xz is 1,576,640 bytes, SHA256 b7b4f91ca93dfc673f1a6a3c45b2597456e2de376d6651d835e88c75898eddb3. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Glim baseline file is fully rehashed before copying. The independent restored_hopebringer_sindorei_runtime must have exactly 27,800 files / 1,548,375,078 bytes, SOURCE_MAP SHA256 ba4a83a9e17a7721676468613b7f66415ff3a9835851752b68ecee8fe50fcfa9. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Sindorei increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
