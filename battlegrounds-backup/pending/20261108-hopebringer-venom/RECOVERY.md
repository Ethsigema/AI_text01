# Recover Hopebringer Venom source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Sindorei with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/fb89af905dfd627034e2eef8c634bccc8b00ca4d/battlegrounds-backup/pending/20261108-hopebringer-sindorei/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, and Sindorei. Retain the Sindorei recovery directory containing restored_hopebringer_sindorei_runtime, hopebringer_sindorei/extracted/hopebringer_sindorei_20261108/SOURCE_MAP.json, and HOPEBRINGER_SINDOREI_REMOTE_CHAIN_VERIFICATION.json.

Required Sindorei map SHA256: ba4a83a9e17a7721676468613b7f66415ff3a9835851752b68ecee8fe50fcfa9. Required Sindorei receipt SHA256: 0ea6e37101e9898a00dc647d17cbcfd9dc5ae0b4c9eb42fbc4c9537f83ab2228.

## Restore this increment

Place verify_and_restore_hopebringer_venom.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_venom.py --hopebringer-sindorei-recovery /path/to/sindorei_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit d9a6ceb1526e96f6a15acb3e854e0ad3feb73f6b, folder battlegrounds-backup/pending/20261108-hopebringer-venom. Archive hopebringer_venom_20261108.tar.xz is 1,579,900 bytes, SHA256 7c52cf4bcadac9d739d894e275e8854544ab8ec32137e5e1fe0d099417404095. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Sindorei baseline file is fully rehashed before copying. The independent restored_hopebringer_venom_runtime must have exactly 27,803 files / 1,548,385,518 bytes, SOURCE_MAP SHA256 942a26eeed2777253701d2aa30acc53a488945514aec151dc32127b8ec767527. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Venom increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
