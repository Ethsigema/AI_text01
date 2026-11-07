# Recover Electron Robust Evolution source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Sale Transfer recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/d2997511f4e63d56ced5f8d97bbe80c9ba034793/battlegrounds-backup/pending/20261107-electron-sale-transfer/RECOVERY.md

Follow each pinned prerequisite through Electron Refresh Winds, Electron Spell Refresh, Electron Enchanted Lasso, Electron Nearest Enemy, Electron Undead Army, Electron Corrupted Cupcakes, Electron Tomb Turning, Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Sale Transfer directory must contain restored_sale_transfer_runtime and sale_transfer/extracted/electron_sale_transfer_20261107/SOURCE_MAP.json. Require exactly 27,695 files / 1,548,036,752 bytes, map SHA256 6f3b6db8269a0e7522b395b534b7ff0fc4bee76533c90e3a24856064737e6f1a. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- SALE_TRANSFER_REMOTE_CHAIN_VERIFICATION.json: SHA256 e24d56d6b106897b3145cfa7d8f392da219a0581cff7b18572f4d6bfdebe6b98.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Sale Transfer. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_robust_evolution.py in a new directory and run:

```sh
python3 verify_and_restore_robust_evolution.py --sale-transfer-recovery /path/to/completed-sale-transfer-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit d38e3502a2703839884e32855786913a0a514b57, path battlegrounds-backup/pending/20261107-electron-robust-evolution. Archive electron_robust_evolution_20261107.tar.xz: 1,100,380 bytes, SHA256 cd625a1d580c75942e3b7a8f8fb39c773dad64fb1c85efdab1099dd1c8c5bc22.

It verifies all part hashes, assembled archive and all 54 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: eight modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_robust_evolution_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require ROBUST_EVOLUTION_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,697 files / 1,548,042,693 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 7c6e3c37c5e2efe75c210b667a9e197f97bb8ae6cff6a9d17b5c9e7d66231297. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
