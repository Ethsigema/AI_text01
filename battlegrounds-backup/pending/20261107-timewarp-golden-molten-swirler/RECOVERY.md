# Recover Timewarp Golden Molten Swirler source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Timewarp Golden Swirler Combat recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/ae0da5151367a20801200475d21d7016d02b3ed1/battlegrounds-backup/pending/20261107-timewarp-golden-swirler-combat/RECOVERY.md

Follow each pinned prerequisite through Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Timewarp Golden Swirler Combat directory must contain restored_golden_swirler_combat_runtime and golden_swirler_combat/extracted/timewarp_golden_swirler_combat_20261107/SOURCE_MAP.json. Require exactly 27,656 files / 1,547,917,905 bytes, map SHA256 ebcdd31ae1a2d4b22fa9788fb904ada65e47ab8e05a68a591c4e4d8a6f6eeff4. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- GOLDEN_SWIRLER_COMBAT_REMOTE_CHAIN_VERIFICATION.json: SHA256 83734a9be2ed6406763cde25fceaa790b9b0f16d28b00381989292cfd551b23a.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Timewarp Golden Swirler Combat. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_golden_molten.py in a new directory and run:

```sh
python3 verify_and_restore_golden_molten.py --golden-swirler-combat-recovery /path/to/completed-golden-swirler-combat-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 499adb9ff6fec1c8fd7c4303a83912b3b73b8417, path battlegrounds-backup/pending/20261107-timewarp-golden-molten-swirler. Archive timewarp_golden_molten_swirler_20261107.tar.xz: 1,052,636 bytes, SHA256 ab111ac9fb74c547479b632742778e828acc7a9a3a0fd71475bc3eb045c442d0.

It verifies all part hashes, assembled archive and all 34 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: three modifications, zero additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_golden_molten_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require GOLDEN_MOLTEN_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,656 files / 1,547,918,193 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 3d562a0ccde4e3d74ec9794139497ac99378b5550971c73fac996cc7d2cfafd3. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
