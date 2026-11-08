# Recover Hopebringer Caretaker source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Rattler with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/23eb64012ddc0257538f151f080742daf02722dc/battlegrounds-backup/pending/20261108-hopebringer-rattler/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, and Rattler. Retain the Rattler recovery directory containing restored_hopebringer_rattler_runtime, hopebringer_rattler/extracted/hopebringer_rattler_20261108/SOURCE_MAP.json, and HOPEBRINGER_RATTLER_REMOTE_CHAIN_VERIFICATION.json.

Required Rattler map SHA256: a5463a3bbad74c00b03aecde9ac7f60deee30caf3c6ba6c311229237357d911b. Required Rattler receipt SHA256: 358e0da438073af329ce0549f8205a5defa374bf2855c0d1aea8eb0c95e3d184.

## Restore this increment

Place verify_and_restore_hopebringer_caretaker.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_caretaker.py --hopebringer-rattler-recovery /path/to/rattler_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit 967d3225f09bde59489135cd160eebdc7c96198b, folder battlegrounds-backup/pending/20261108-hopebringer-caretaker. Archive hopebringer_caretaker_20261108.tar.xz is 1,577,664 bytes, SHA256 814a5a16242d0c655ee707ff97d04e8b11844efdc4d984744c0e62f06218b972. It verifies all part hashes, archive hash, 37 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/three additions/zero removals.

Every Rattler baseline file is fully rehashed before copying. The independent restored_hopebringer_caretaker_runtime must have exactly 27,791 files / 1,548,346,859 bytes, SOURCE_MAP SHA256 5d116ed6a31bcc512f6dbefeb2db194cc1bd56dfe321f8759bcb2afc85d0417d. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Caretaker increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
