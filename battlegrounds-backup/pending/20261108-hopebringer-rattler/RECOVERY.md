# Recover Hopebringer Rattler source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Recruiter with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/b8bc506164c488fd22f6c5b04ce7420251a4ec6d/battlegrounds-backup/pending/20261108-hopebringer-recruiter/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, and Recruiter. Retain the Recruiter recovery directory containing restored_hopebringer_recruiter_runtime, hopebringer_recruiter/extracted/hopebringer_recruiter_20261108/SOURCE_MAP.json, and HOPEBRINGER_RECRUITER_REMOTE_CHAIN_VERIFICATION.json.

Required Recruiter map SHA256: 708c6bc362cee806ec1932409db9da7f08ccf1430f9b0562a201d653e2027205. Required Recruiter receipt SHA256: 2aa3d707953cda9e4280bec408f0d1bc80dd8be3f1f9d3791eb569f3ce5def5c.

## Restore this increment

Place verify_and_restore_hopebringer_rattler.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_rattler.py --hopebringer-recruiter-recovery /path/to/recruiter_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit fcf9ebbfff0086613ecf417d621831da5b8ba107, folder battlegrounds-backup/pending/20261108-hopebringer-rattler. Archive hopebringer_rattler_20261108.tar.xz is 1,572,072 bytes, SHA256 ed340e38a54deb732a5b320ea2e964cbdab826d16d6998a717a9e1f5fb9f8d1d. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Recruiter baseline file is fully rehashed before copying. The independent restored_hopebringer_rattler_runtime must have exactly 27,788 files / 1,548,339,020 bytes, SOURCE_MAP SHA256 a5463a3bbad74c00b03aecde9ac7f60deee30caf3c6ba6c311229237357d911b. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Rattler increment is freshly downloaded by this helper. Historical dependencies and the Mummifier full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.
