# Recover Snow Baller partial base source

Source-byte verification only. This is partial Snow Baller base reconstruction, not scaling implementation, gameplay acceptance or recovery of the lost original. Preserve all backups. The exact Fire Baller partial base baseline is required.

## Restore the prerequisite chain

Follow the immutable Fire Baller recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/1b959163351c7fb492034a11d67217eb59285336/battlegrounds-backup/pending/20261107-fire-baller-base/RECOVERY.md

Follow its linked dynamic spells, shared-type, double spell Discover, spell Discover, stock Discover, Hooktusk base, Ultraviolet, Electron shop/targeted/economy, Amalgam ALL, Drakkari, randomized Chimera/recruit, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe obtains the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and sufficient space for archives and independent runtimes.

The completed fire recovery directory must contain `restored_fire_runtime` and `fire/extracted/fire_baller_base_20261107/SOURCE_MAP.json`. Require 27,573 files / 1,546,907,326 bytes and SOURCE_MAP SHA256 `8429c357fe845924347c1293f921c64e7143f4b4209d08dab2d51d7082e32120`. Leave the baseline unmodified; do not launch Godot in it before verification.

Supporting receipts: `FIRE_REMOTE_CHAIN_VERIFICATION.json` SHA256 `2913ad059116b50b3764c7a185c27bc352818783715e3c0726e2c8bb4bcdcf31`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records independent fresh historical recovery through Theotar. Receipts do not replace source bytes.

## Download and restore Snow Baller

Place `verify_and_restore_snow.py` in another new empty directory:

```sh
python3 verify_and_restore_snow.py --fire-recovery /path/to/completed-fire-recovery
```

The standard-library helper freshly downloads MANIFEST.json, 12 binary parts, REMOVALS.json and CHANGES.json from immutable commit `1d28247c526df73bc24efceda1d61d312093dcd4`, directory `battlegrounds-backup/pending/20261107-snow-baller-base`. Archive: 2,802,264 bytes, SHA256 `5575a1fae249d474e477156c64e95d08df7c0918b249cc45366712dfbd0260de`.

Every part, assembled archive and all 101 members are verified, rejecting unsafe paths/types. Both companions are hash/size checked against MANIFEST.json companion_files; their arrays must equal actual differences: 9 additions, 62 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. Baseline SOURCE_MAP must byte-equal increment BASE_MAP; every baseline file is rehashed.

The helper independently copies `restored_snow_runtime` without hardlinks, rehashes all outputs and the unchanged baseline, and records per-file RESTORE_PROVENANCE.json. Require `SNOW_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,582 files / 1,547,018,699 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `d3fcbaad4f03524277aaae06d0c53339cff8e4ec1552646bb64eca1dc153a48e`.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads Snow Baller only and rehashes the verified Fire Baller baseline; use prerequisite recipes for fresh historical downloads. No gameplay is executed or accepted. Partial base source verification does not establish scaling implementation.

The helper never mutates baseline files, including any shared hardlinked files. It uses independent copies for every restored output.
