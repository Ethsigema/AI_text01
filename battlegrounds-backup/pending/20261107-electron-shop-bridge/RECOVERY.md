# Recover the Electron shop bridge source

Source-byte verification only. This is new reconstruction, not recovery of the lost original or gameplay acceptance. Preserve all backups. This increment requires the exact Electron targeted bridge baseline.

## Restore the prerequisite chain

Follow the immutable Electron targeted bridge recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/6db3c8925df72316a23b41fe7f7304b1bc70f025/battlegrounds-backup/pending/20261107-electron-targeted-bridge/RECOVERY.md

Follow its linked Electron economy, Amalgam ALL, Drakkari, randomized Chimera bridge, recruit bridge, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe downloads the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and enough space for retained archives and independent runtime copies.

The completed targeted bridge directory must contain `restored_targeted_runtime` and `targeted/extracted/electron_targeted_bridge_20261107/SOURCE_MAP.json`. Require 27,537 files / 1,546,561,686 bytes and SOURCE_MAP SHA256 `787d2084673b022681214fcf1a6764c5f0fb3fdd67235c2360e583be10bb814d`. Leave the verified baseline unmodified; do not launch Godot in it before verification.

Supporting receipts: `TARGETED_REMOTE_CHAIN_VERIFICATION.json` SHA256 `e22de2b7998a012cc9616d534e5111a4b83833de8a268bd0850dcbec24ecbcc9`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records independent fresh historical-chain recovery through Theotar. Receipts are evidence, not replacements for source bytes.

## Download and restore the shop bridge

Place `verify_and_restore_shop.py` in another new empty directory:

```sh
python3 verify_and_restore_shop.py --targeted-recovery /path/to/completed-targeted-recovery
```

The Python standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `121772afa065621f29d4931172d4d7325edc9ee8`, directory `battlegrounds-backup/pending/20261107-electron-shop-bridge`. Archive: 1,059,076 bytes, SHA256 `df7bb3f2ba43c53d23a348e3ec9f824a4b920e8f149c8fd1a0c01bea15341620`.

It verifies every part, assembled archive and all 50 members, rejecting unsafe paths/types. Both companions are size/hash-checked against MANIFEST.json companion_files. Their added/modified/removed arrays must equal actual map differences: 3 additions, 5 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. targeted bridge SOURCE_MAP and shop BASE_MAP must be byte-identical, and every baseline file is rehashed.

The helper independently copies `restored_shop_runtime` without hardlinks, then rehashes every output file and the unchanged baseline. Require `SHOP_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,540 files / 1,546,568,776 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `9bd31a5351f2adc91dcad6c34e42a259844e4bfcab0173d0e9cee3ad54758574`. Per-file origins are recorded in RESTORE_PROVENANCE.json.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads only the Electron shop bridge increment and rehashes the verified Electron targeted baseline; use the prerequisite recipes for fresh historical downloads. Gameplay is not executed or accepted by this verification.
