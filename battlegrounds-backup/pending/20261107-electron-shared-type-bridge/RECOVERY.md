# Recover Electron shared-type bridge source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups. The exact verified Hooktusk double spell Discover baseline is required.

## Restore the prerequisite chain

Follow the immutable double spell Discover recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/0b5e2c9bf89a6d906a18d872922dc40aea44497a/battlegrounds-backup/pending/20261107-hooktusk-double-spell-discover/RECOVERY.md

Follow its linked spell Discover, stock Discover, Hooktusk base, Ultraviolet, Electron shop/targeted/economy bridges, Amalgam ALL, Drakkari, randomized Chimera/recruit bridges, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient space for retained archives and independent runtimes.

The completed double spell recovery directory must contain `restored_double_spell_runtime` and `double_spell/extracted/hooktusk_double_spell_discover_20261107/SOURCE_MAP.json`. Require 27,558 files / 1,546,775,169 bytes and SOURCE_MAP SHA256 `3ec6431e5bc7171a446013026cce91c62571b544ad3ebbc69ef7e9d145742b03`. Leave the verified baseline unmodified; do not launch Godot in it before verification.

Supporting receipts: `DOUBLE_SPELL_REMOTE_CHAIN_VERIFICATION.json` SHA256 `f25cbc438bab83122a4ec0abc8f2bae5947db23f8ee490d93eebbff6c1d78429`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records independent fresh historical recovery through Theotar. Receipts do not replace required source bytes.

## Download and restore shared-type bridge

Place `verify_and_restore_shared_type.py` in another new empty directory:

```sh
python3 verify_and_restore_shared_type.py --double_spell-recovery /path/to/completed-double-spell-recovery
```

The Python standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `595e7b564afc6919e6feeb9f6fd8babdd800b529`, directory `battlegrounds-backup/pending/20261107-electron-shared-type-bridge`. Archive: 1,056,452 bytes, SHA256 `ac47568765b24a0f2572d9cf0b5a045d3abeb547e4b9be18ae1202dc459a0f56`.

Every part, assembled archive and all 36 members are verified, rejecting unsafe paths/types. Both companions are hash/size checked against MANIFEST.json companion_files, and their arrays must equal actual map differences: 2 additions, 5 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. Baseline SOURCE_MAP must byte-equal increment BASE_MAP; every baseline file is rehashed.

The helper independently copies `restored_shared_type_runtime` without hardlinks, rehashes all outputs and the unchanged baseline, and records per-file RESTORE_PROVENANCE.json. Require `SHARED_TYPE_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,560 files / 1,546,780,587 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `4540582564ab747c5c284ca9f9cc60aeb7703a304c29ba0475d63f59d88d40e2`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads the shared-type increment only and rehashes the verified double spell baseline; use prerequisite recipes for fresh historical downloads. No gameplay is executed or accepted by this verification.
