# Recover Electron Tableware Bridge source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Timewarp Swirler Golden Air recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/5e29774a141b4817c6dec018f0cfe11143089ab3/battlegrounds-backup/pending/20261107-timewarp-swirler-golden-air/RECOVERY.md

Follow each pinned prerequisite through First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Timewarp Swirler Golden Air directory must contain restored_golden_air_runtime and golden_air/extracted/timewarp_swirler_golden_air_20261107/SOURCE_MAP.json. Require exactly 27,650 files / 1,547,857,831 bytes, map SHA256 e1f5d4fa719ca683553c6f641205fd33ea38382693ca8fa60b8cf95e070ce958. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- GOLDEN_AIR_REMOTE_CHAIN_VERIFICATION.json: SHA256 ccab244b2a9be81dff042536d5a6491f988e6a66a50a4baa1ed2a264ad5a583e.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Timewarp Swirler Golden Air. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_tableware.py in a new directory and run:

```sh
python3 verify_and_restore_tableware.py --golden-air-recovery /path/to/completed-golden-air-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 399b90e1dbed65acea5efc5f347f74694584f032, path battlegrounds-backup/pending/20261107-electron-tableware-bridge. Archive electron_tableware_bridge_20261107.tar.xz: 1,064,236 bytes, SHA256 5d3df83de68cfd5c93611e91101a97eb19f4db6de00164c8adfb36102e3ed548.

It verifies all part hashes, assembled archive and all 38 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_tableware_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require TABLEWARE_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,652 files / 1,547,862,908 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 1f165e821a4251c5e2770fe99c7268f55b757f397ac2134a8a6e3b97e1a4148b. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
