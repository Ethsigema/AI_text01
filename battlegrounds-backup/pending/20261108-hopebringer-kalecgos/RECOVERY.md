# Recover Hopebringer Kalecgos source

This is source-byte recovery verification, not gameplay acceptance. Preserve all backups and do not run Godot in a verification baseline.

## Obtain the baseline

First restore Hopebringer Prophet with its immutable recipe:
https://github.com/Ethsigema/AI_text01/blob/49ac922df9660f2eea0ad6b30906fd0ee2a3c0c3/battlegrounds-backup/pending/20261108-hopebringer-prophet/RECOVERY.md

That recipe links the complete pinned recovery chain, including the original November 1 release ZIP, recovery and Bloodbound Git sources, the complete Mummifier chain, Amber, Banana, Humming, Recruiter, Rattler, Caretaker, Wolf, Bat, Glim, Sindorei, Venom, Roadboar, Refreshing, Brann, Geomancer, Lullabot, Sellemental, Sylvar, Dune, Weaver, Hooktail, Hoarder, Groundskeeper, Tea, Rescue, and Prophet. Retain the Prophet recovery directory containing restored_hopebringer_prophet_runtime, hopebringer_prophet/extracted/hopebringer_prophet_20261108/SOURCE_MAP.json, and HOPEBRINGER_PROPHET_REMOTE_CHAIN_VERIFICATION.json.

Required Prophet map SHA256: 8d101d811bb61f6dfdb7ede936562fdacfb142e567d69316a1f477037f7bc190. Required Prophet receipt SHA256: ee4e2189df0b89a928b6c663d5fde2688daefbd02e3d6db2bd032c67298f0cac.

## Restore this increment

Place verify_and_restore_hopebringer_kalecgos.py and the accompanying FRESH_WHOLE_CHAIN_VERIFICATION.json in a new empty recovery directory. The historical receipt SHA256 must be 0d8a735b6656ec5fa63fc1a0696b1b8a14d8ea4ce40b50e2640fb6eaf5cb285f. Use Python 3 standard library and approximately 2 GB free space after baseline inputs exist:

```sh
python3 verify_and_restore_hopebringer_kalecgos.py --hopebringer-prophet-recovery /path/to/prophet_recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and all seven binary parts from commit f68b91196fc88be95da99aec8a00912c1c1ce439, folder battlegrounds-backup/pending/20261108-hopebringer-kalecgos. Archive hopebringer_kalecgos_20261108.tar.xz is 1,598,368 bytes, SHA256 0e3aab2f76a4e345a7e12edf0834a4ce1ec29df914f5612c90744575e6011970. It verifies all part hashes, archive hash, 36 safe members and companion hashes, exact BASE_MAP continuity, and five modifications/two additions/zero removals.

Every Prophet baseline file is fully rehashed before copying. The independent restored_hopebringer_kalecgos_runtime must have exactly 27,842 files / 1,548,516,555 bytes, SOURCE_MAP SHA256 c7b7e6e47b59346f7c2e1f9799ad631c2e074c802f46b21a1ba444abcb645c71. Every output hash and exact inventory is verified; the baseline is rehashed unchanged afterward. No hardlinks are created. Require receipt status PASS_EXACT_SOURCE_ONLY, empty missing/mismatched/unexpected lists, and baseline_unchanged_after_restore true.

Only the Kalecgos increment is freshly downloaded by this helper. Historical dependencies and the 23:00 Dune full-chain receipt are explicitly reused, not freshly redownloaded this round. No files are deleted, no remote state is changed, and gameplay is not executed. Existing download/output directories cause the helper to stop rather than overwrite them. Keep any failed attempt for diagnosis and use a new recovery directory when retrying.

The reused latest full-chain proof and reproducible fresh verification recipe are pinned at https://github.com/Ethsigema/AI_text01/blob/c76196558a0f5c6ce41420b1782b95f6590ff94e/battlegrounds-backup/pending/20261108-dune-fresh-chain/RECOVERY.md . Its 114 freshly verified increments terminate at Dune; the verified Prophet receipt links that exact map to this baseline. The helper verifies both receipt hashes and map continuity. This round does not redownload those historical dependencies.
