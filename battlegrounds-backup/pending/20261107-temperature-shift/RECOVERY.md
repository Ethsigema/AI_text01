# Recover Temperature Shift source

Source-byte verification only, not gameplay acceptance or recovery of the lost original. Preserve all backups and shared hardlinks. The exact verified Snow Baller baseline is required.

## Restore the prerequisite chain

Follow the immutable Snow recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/011d4553c2f0e3fd9a09a7cab21b2497d2fdf06d/battlegrounds-backup/pending/20261107-snow-baller-base/RECOVERY.md

Follow its linked Fire Baller, dynamic spells, shared-type, double spell Discover, spell Discover, stock Discover, Hooktusk base, Ultraviolet, Electron shop/targeted/economy, Amalgam ALL, Drakkari, randomized Chimera/recruit, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient space for retained archives and independent runtimes.

The completed Snow recovery directory must contain `restored_snow_runtime` and `snow/extracted/snow_baller_base_20261107/SOURCE_MAP.json`. Require 27,582 files / 1,547,018,699 bytes and SOURCE_MAP SHA256 `d3fcbaad4f03524277aaae06d0c53339cff8e4ec1552646bb64eca1dc153a48e`. Do not modify the baseline or launch Godot in it before verification.

Supporting receipts: `SNOW_REMOTE_CHAIN_VERIFICATION.json` SHA256 `3a2894be816f0e1479ed6c9793d3977e1b59577fae42788afceb6a006cc6faa2`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter documents independent fresh historical recovery through Theotar; later pinned increment recipes and receipts connect that baseline through Snow. Receipts do not replace source bytes.

## Download and restore Temperature Shift

Place `verify_and_restore_temperature.py` in another new empty directory:

```sh
python3 verify_and_restore_temperature.py --snow-recovery /path/to/completed-snow-recovery
```

The Python standard-library helper freshly downloads MANIFEST.json, 6 binary parts, REMOVALS.json and CHANGES.json from immutable commit `ae498568fea3bee7ea7b703b6d2059ba7db3170a`, directory `battlegrounds-backup/pending/20261107-temperature-shift`. Archive: 1,280,680 bytes, SHA256 `51bd998e9340ae45dce247f70b968fa8fe8238c021bb019475edb9dae097e2f9`.

Every part, assembled archive and all 41 members are verified, rejecting unsafe paths/types. Both companions are hash/size checked against MANIFEST.json companion_files; their arrays must equal actual differences: 4 additions, 7 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. Snow SOURCE_MAP must byte-equal Temperature Shift BASE_MAP; every baseline file is rehashed.

The helper independently copies `restored_temperature_runtime` without hardlinks and never writes to baseline files. It rehashes every output and the unchanged baseline, recording per-file RESTORE_PROVENANCE.json. Require `TEMPERATURE_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,586 files / 1,547,065,227 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `c7e94e89019ab848f268c4b9cfa2bedebb747d50342b542b0cf8d0a3546b9215`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads Temperature Shift only and rehashes the already-verified Snow baseline; it does not redownload the historical chain. Use prerequisite recipes to download that chain anew. No gameplay is executed or accepted by source verification.
