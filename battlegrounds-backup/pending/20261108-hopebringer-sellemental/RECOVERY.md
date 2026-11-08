# Recover Hopebringer Sellemental source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Lullabot with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/dc96f05b52ec6a03cb5bf94f0d93aacf615e8ab2/battlegrounds-backup/pending/20261108-hopebringer-lullabot/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, and Lullabot. Retain the Lullabot recovery directory containing restored_hopebringer_lullabot_runtime, hopebringer_lullabot/extracted/hopebringer_lullabot_20261108/SOURCE_MAP.json, and HOPEBRINGER_LULLABOT_REMOTE_CHAIN_VERIFICATION.json.

Required Lullabot map SHA256: 0416cdda6d96751509c39dc3dcfe60983fede6130615ba68df1eefa1dea4eb9e. Required Lullabot receipt SHA256: bbb8204fa4f9c487788a04b2aee608e8d6d00230901df1350baf0578e5ec60e2.

## Restore this increment

Place verify_and_restore_hopebringer_sellemental.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_sellemental.py --hopebringer-lullabot-recovery /path/to/lullabot_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 3220028538fe202520e659d0a9f24471baa4b70f, folder battlegrounds-backup/pending/20261108-hopebringer-sellemental. Archive hopebringer_sellemental_20261108.tar.xz is 1,577,732 bytes, SHA256 164633e86dcdb33ec19d6441b7867a289b483422254c508d7dd8b2b17663e723. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Lullabot baseline file is fully rehashed before copying. The independent restored_hopebringer_sellemental_runtime must have exactly 27,817 files / 1,548,428,923 bytes, SOURCE_MAP SHA256 7d5e3a682dc9dcaeab6de97d84d11769cbc13996c47b3b9b0f3e47fe91ef2d1c. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Sellemental increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
