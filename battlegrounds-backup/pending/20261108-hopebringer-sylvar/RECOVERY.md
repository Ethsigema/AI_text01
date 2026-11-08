# Recover Hopebringer Sylvar source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Sellemental with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/7a128751a4c424400983a6b8fee2ae7e585c3fcb/battlegrounds-backup/pending/20261108-hopebringer-sellemental/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, and Sellemental. Retain the Sellemental recovery directory containing restored_hopebringer_sellemental_runtime, hopebringer_sellemental/extracted/hopebringer_sellemental_20261108/SOURCE_MAP.json, and HOPEBRINGER_SELLEMENTAL_REMOTE_CHAIN_VERIFICATION.json.

Required Sellemental map SHA256: 7d5e3a682dc9dcaeab6de97d84d11769cbc13996c47b3b9b0f3e47fe91ef2d1c. Required Sellemental receipt SHA256: cf79568d678a4b44176ecfa4fe09f919a80b459fac6e40288aa3b6d2e9d2fce5.

## Restore this increment

Place verify_and_restore_hopebringer_sylvar.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_sylvar.py --hopebringer-sellemental-recovery /path/to/sellemental_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 28b81230c71515f7a1a44cfbb83d7af959eb4043, folder battlegrounds-backup/pending/20261108-hopebringer-sylvar. Archive hopebringer_sylvar_20261108.tar.xz is 1,583,432 bytes, SHA256 1b33f25fff556a0a6b33b1e3929822780fd340bdbbd7962cd28194f57cc2dfb4. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Sellemental baseline file is fully rehashed before copying. The independent restored_hopebringer_sylvar_runtime must have exactly 27,819 files / 1,548,438,006 bytes, SOURCE_MAP SHA256 4342a26be4032b422da1599de730f3b4634ef902954cc3eea82556fbfa8df88a. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Sylvar increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
