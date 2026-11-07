# Recover Electron Spell Refresh source

Source-byte verification only, not gameplay acceptance or recovery of lost original work. Preserve all backups and never mutate the baseline.

## Obtain the prerequisite baseline

Follow the immutable Electron Enchanted Lasso recovery instructions and helper:
https://github.com/Ethsigema/AI_text01/blob/9a3d1cf82c5527e1300be32c0f74e309b6917567/battlegrounds-backup/pending/20261107-electron-enchanted-lasso/RECOVERY.md

Follow each pinned prerequisite through Electron Nearest Enemy, Electron Undead Army, Electron Corrupted Cupcakes, Electron Tomb Turning, Electron Tier1 Discover, Electron Golden Touch, Electron Scavenge Clock, Electron Alliance Choice, Timewarp Golden Ultraviolet Bridge, Electron Combat Spells, Electron Overconfidence, Electron Timed Choice, Electron Forest Choice, Timewarp Golden Molten Swirler, Timewarp Golden Swirler Combat, Timewarp Golden Swirler Air, Electron Tableware Bridge, Timewarp Swirler Golden Air, First Action Play Sequence, Swirler Ultraviolet, Swirler Air, Swirler Molten, Golden Scout and earlier increments to the Theotar recipe at e23df857427307b8a29675a62156e96040c72604. That recipe obtains the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and Wrathguard/Theotar increments. Use that archive hash-index reconstruction, not merely the older repository RESTORE.md. Requirements: Python 3, Git, curl, tar, fresh directories and sufficient space.

The completed Electron Enchanted Lasso directory must contain restored_enchanted_lasso_runtime and enchanted_lasso/extracted/electron_enchanted_lasso_20261107/SOURCE_MAP.json. Require exactly 27,689 files / 1,548,019,677 bytes, map SHA256 4cfd94bc3b414b3d55d0b827028bbfbe1e53c777321cac6c204b5c1d63ea0fec. Do not run Godot in that directory.

Place the published supporting receipts in that baseline directory:
- ENCHANTED_LASSO_REMOTE_CHAIN_VERIFICATION.json: SHA256 edeb4fce7e1b91b6faa0121bb2fa8f6175e0b8716c3bd80eda4935dcd660f03e.
- FRESH_WHOLE_CHAIN_VERIFICATION.json: SHA256 edf518f5ab565c4ef1990a2efe0985f6fe985054655cc3b43e9cbad2b38613d2.

The earlier fresh whole-chain byte check ends at Murky. Subsequent pinned receipts connect that endpoint through each later increment to Electron Enchanted Lasso. This helper pins both supporting receipt hashes and checks endpoint/continuity, then directly rehashes every supplied baseline file. Receipts do not replace source bytes or claim a new historical download.

## Restore the new increment

Place verify_and_restore_spell_refresh.py in a new directory and run:

```sh
python3 verify_and_restore_spell_refresh.py --enchanted-lasso-recovery /path/to/completed-enchanted-lasso-recovery
```

The helper freshly downloads MANIFEST.json, five binary parts, CHANGES.json and REMOVALS.json from immutable commit 673b2aa90334ba4b0a9ac728f69dccf97c4b2c8e, path battlegrounds-backup/pending/20261107-electron-spell-refresh. Archive electron_spell_refresh_20261107.tar.xz: 1,074,172 bytes, SHA256 8f9e8a61a8aff5484f3a65c96dd0189f2426942df80810296dffc9a6bfa89fda.

It verifies all part hashes, assembled archive and all 49 safe members; companion hashes/sizes must match MANIFEST.json and actual map differences: five modifications, two additions, zero removals. REMOVALS.json must also match removed_source_files. The supplied baseline SOURCE_MAP must byte-equal BASE_MAP and every baseline file must match its hash.

The helper creates restored_spell_refresh_runtime using independent copies, with no hardlinks. It hashes every output and rehashes the unchanged baseline. Require SPELL_REFRESH_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,691 files / 1,548,024,597 bytes, no missing/mismatched/unexpected files, and target SOURCE_MAP SHA256 cdf2bf2193b604df9f9214fd1ca16c9a1cc0a0edc1d4ed334d6d0687fd6ecc08. RESTORE_PROVENANCE.json records each file's source.

Existing destinations are never overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. Only this increment is freshly downloaded in this round; the baseline and historical evidence are reused, with all baseline bytes rehashed. The entire historical chain is not redownloaded. No gameplay is executed or accepted.
