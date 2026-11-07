# Recover Timewarp Golden Swirler Air source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Tableware Bridge recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/3ac8532eacd5d814986ddc3b254bc618bc2e6f76/battlegrounds-backup/pending/20261107-electron-tableware-bridge/RECOVERY.md

Follow each pinned prerequisite through Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Tableware Bridge directory must contain restored_tableware_runtime and tableware/extracted/electron_tableware_bridge_20261107/SOURCE_MAP.json. Require exactly 27,652 files / 1,547,862,908 bytes, map SHA256 1f165e821a4251c5e2770fe99c7268f55b757f397ac2134a8a6e3b97e1a4148b. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- TABLEWARE_REMOTE_CHAIN_VERIFICATION.json: SHA256 988cb51aa7c7c8fe124af9a00a7901e7c350a534b634fb63d44caf5d3c2c3a1f.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Tableware Bridge. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_golden_swirler_air.py in a new directory and run:

```sh
python3 verify_and_restore_golden_swirler_air.py --tableware-recovery /path/to/completed-tableware-recovery
```

The helper freshly downloads MANIFEST.json, six binary parts, CHANGES.json and REMOVALS.json from immutable commit 9ae2032d3cc240c71ed96058a2a463c1393a1dbc, path battlegrounds-backup/pending/20261107-timewarp-golden-swirler-air. Archive timewarp_golden_swirler_air_20261107.tar.xz: 1,287,548 bytes, SHA256 04bb78cd91c1eacfbbb94939b64350e17d7e84da667d47db410d5d8eadaac486.

It verifies all part hashes, assembled archive and all 40 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: three modifications, four additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_golden_swirler_air_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require GOLDEN_SWIRLER_AIR_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,656 files / 1,547,917,931 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 045c431ca600e3f0cce20c766d498bdec6ae88f372ea0e23e0a9af8288cd6384. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
