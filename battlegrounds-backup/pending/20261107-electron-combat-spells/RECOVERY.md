# Recover Electron Combat Spells source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Overconfidence recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/d0d56f6ffa294aaf84b9785fefe834993df7009b/battlegrounds-backup/pending/20261107-electron-overconfidence/RECOVERY.md

Follow each pinned prerequisite through Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Overconfidence directory must contain restored_overconfidence_runtime and overconfidence/extracted/electron_overconfidence_20261107/SOURCE_MAP.json. Require exactly 27,666 files / 1,547,950,530 bytes, map SHA256 7a139b4f1834493fa7fb32ad3ffdeda86e6a6660ece3fa5cc2399146e3e6960c. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- OVERCONFIDENCE_REMOTE_CHAIN_VERIFICATION.json: SHA256 fa219f716c8e507e7f373024073d3e45913cd6ce8336a62ecc30d5604896d913.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Overconfidence. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_combat_spells.py in a new directory and run:

```sh
python3 verify_and_restore_combat_spells.py --overconfidence-recovery /path/to/completed-overconfidence-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit d6322dd73a4c95b1a7f7c849be98e85427db96bf, path battlegrounds-backup/pending/20261107-electron-combat-spells. Archive electron_combat_spells_20261107.tar.xz: 1,075,956 bytes, SHA256 5878d10a22d4c6ee9833e15aa4e3e2e64cdbf3ad855fea7349b624839921c291.

It verifies all part hashes, assembled archive and all 39 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, three additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_combat_spells_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require COMBAT_SPELLS_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,669 files / 1,547,960,044 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 5c30800c28a7f49dab7a5d2a48e2836451db05827ddde077a9b206654f8852ee. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
