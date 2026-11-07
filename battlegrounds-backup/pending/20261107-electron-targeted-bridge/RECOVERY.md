# Recover the Electron targeted bridge source

Source-byte verification only. This is new reconstruction, not recovery of the lost original or gameplay acceptance. Preserve all backups. This increment requires the exact Electron economy bridge baseline.

## Restore the prerequisite chain

Follow the immutable Electron economy bridge recovery recipe and helper:

https://github.com/Ethsigema/AI_text01/blob/465b4101648eca6961675041d04dfe83940f4f64/battlegrounds-backup/pending/20261107-electron-economy-bridge/RECOVERY.md

Follow its linked Amalgam ALL, Drakkari, randomized Chimera bridge, recruit bridge, Rodeo, Chimera, Mythrax, Amalgam and Electron recipes to the complete Theotar recipe at commit `e23df857427307b8a29675a62156e96040c72604`. That recipe downloads the November 1 release ZIP, recovery commit `e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c`, Bloodbound commit `32180d3af0db59fb3374f53100f9eaa5bb62d26a`, and pinned Wrathguard/Theotar increments. Use its archive hash-index reconstruction, not only the older repository RESTORE.md. Use Python 3, Git, curl and tar, fresh directories and enough space for retained archives and independent runtime copies.

The completed economy bridge directory must contain `restored_economy_runtime` and `economy/extracted/electron_economy_bridge_20261107/SOURCE_MAP.json`. Require 27,531 files / 1,546,535,856 bytes and SOURCE_MAP SHA256 `faa285f0648287c779cefa6f185a22f6355eab160db752f05a2d10a7c459d133`. Leave the verified baseline unmodified; do not launch Godot in it before verification.

Supporting receipts: `ECONOMY_REMOTE_CHAIN_VERIFICATION.json` SHA256 `0e80e29ef085849ab9956960e83ad905780f8f4b721cc5953638a6e4313b07fc`, and `FRESH_FULL_CHAIN_VERIFICATION.json` SHA256 `add483d2bf9526bba19bbb9d6b53e4e7e86bc78d9c2a6826c6dfd071d7ffc53e`. The latter records independent fresh historical-chain recovery through Theotar. Receipts are evidence, not replacements for source bytes.

## Download and restore the targeted bridge

Place `verify_and_restore_targeted.py` in another new empty directory:

```sh
python3 verify_and_restore_targeted.py --economy-recovery /path/to/completed-economy-recovery
```

The Python standard-library helper freshly downloads MANIFEST.json, 5 binary parts, REMOVALS.json and CHANGES.json from immutable commit `fdf33eaeff8336ee4f25d48d901ec27f90cd1344`, directory `battlegrounds-backup/pending/20261107-electron-targeted-bridge`. Archive: 1,067,748 bytes, SHA256 `c3004f169e1ef8027c2d755545556badbc3bbf58e75f524d979c0780f3fb256f`.

It verifies every part, assembled archive and all 51 members, rejecting unsafe paths/types. Both companions are size/hash-checked against MANIFEST.json companion_files. Their added/modified/removed arrays must equal actual map differences: 6 additions, 5 modifications, no removals. REMOVALS.json must also match manifest removed_source_files. economy bridge SOURCE_MAP and targeted BASE_MAP must be byte-identical, and every baseline file is rehashed.

The helper independently copies `restored_targeted_runtime` without hardlinks, then rehashes every output file and the unchanged baseline. Require `TARGETED_REMOTE_CHAIN_VERIFICATION.json` status `PASS_EXACT_SOURCE_ONLY`, 27,537 files / 1,546,561,686 bytes, empty missing/mismatched/unexpected arrays, and SOURCE_MAP SHA256 `787d2084673b022681214fcf1a6764c5f0fb3fdd67235c2360e583be10bb814d`. Per-file origins are recorded in RESTORE_PROVENANCE.json.

Existing destinations are not overwritten. Preserve failed attempts and retry in a fresh directory. No deletion or remote writes occur. This helper freshly downloads only the Electron targeted bridge increment and rehashes the verified Electron economy baseline; use the prerequisite recipes for fresh historical downloads. Gameplay is not executed or accepted by this verification.
