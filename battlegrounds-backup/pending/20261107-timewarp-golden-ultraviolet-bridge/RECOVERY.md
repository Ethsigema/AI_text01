# Recover Timewarp Golden Ultraviolet Bridge source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Combat Spells recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/094957ee47f52dfee428f5424d67aa3cc4220e83/battlegrounds-backup/pending/20261107-electron-combat-spells/RECOVERY.md

Follow each pinned prerequisite through Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Combat Spells directory must contain restored_combat_spells_runtime and combat_spells/extracted/electron_combat_spells_20261107/SOURCE_MAP.json. Require exactly 27,669 files / 1,547,960,044 bytes, map SHA256 5c30800c28a7f49dab7a5d2a48e2836451db05827ddde077a9b206654f8852ee. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- COMBAT_SPELLS_REMOTE_CHAIN_VERIFICATION.json: SHA256 6911f047420ccef8d461f331cae2026fea863523fdc0c42f191657eb6d52bad2.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Combat Spells. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_golden_ultraviolet.py in a new directory and run:

```sh
python3 verify_and_restore_golden_ultraviolet.py --combat-spells-recovery /path/to/completed-combat-spells-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 67459fd7cb493d9a84e956efd867fc7cd32ca3f2, path battlegrounds-backup/pending/20261107-timewarp-golden-ultraviolet-bridge. Archive timewarp_golden_ultraviolet_bridge_20261107.tar.xz: 1,059,228 bytes, SHA256 66714f169d488e8400132bfe692c38e5676573903e04057cbe9eca9ef66aeedc.

It verifies all part hashes, assembled archive and all 32 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: three modifications, zero additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_golden_ultraviolet_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require GOLDEN_ULTRAVIOLET_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,669 files / 1,547,960,474 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 ad387f3dd43e4f2239efa641f9eb4168de901331342741a36ffe85cf924aef6d. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
