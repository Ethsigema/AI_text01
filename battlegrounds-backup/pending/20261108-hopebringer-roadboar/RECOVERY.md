# Recover Hopebringer Roadboar source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Venom with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/c27eb91f37d114351200b546c3c3205f06eae587/battlegrounds-backup/pending/20261108-hopebringer-venom/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, and Venom. Retain the Venom recovery directory containing restored_hopebringer_venom_runtime, hopebringer_venom/extracted/hopebringer_venom_20261108/SOURCE_MAP.json, and HOPEBRINGER_VENOM_REMOTE_CHAIN_VERIFICATION.json.

Required Venom map SHA256: 942a26eeed2777253701d2aa30acc53a488945514aec151dc32127b8ec767527. Required Venom receipt SHA256: f98b0ea4f9ec20bdbd302a8c06d13fcef26e5140d5807de5c0f971f6c4addcb6.

## Restore this increment

Place verify_and_restore_hopebringer_roadboar.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_roadboar.py --hopebringer-venom-recovery /path/to/venom_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 17df875e7558171f5605af0917425bc2e163b1c4, folder battlegrounds-backup/pending/20261108-hopebringer-roadboar. Archive hopebringer_roadboar_20261108.tar.xz is 1,635,880 bytes, SHA256 9ea0965aa5495c614d7cb8f221b9ce72b0d6282e3ebea2f517f2c69ef73fd8cd. It verifies all part hashes, archive hash, 64 safe members and companion hashes, exact BASE_MAP continuity, and seven modifications/three additions/zero removals.

Every Venom baseline file is fully rehashed before copying. The independent restored_hopebringer_roadboar_runtime must have exactly 27,806 files / 1,548,395,826 bytes, SOURCE_MAP SHA256 b71cabdcc391dff896e08ca9207f6dd667ed7bee71dac789fea1967cf5b0e8df. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Roadboar increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
