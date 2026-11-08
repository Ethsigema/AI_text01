# Recover Electron Sludge Discard source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Sludge Hand recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/8a75602d368e7aa0df1bd5cff39894d09bb547bb/battlegrounds-backup/pending/20261108-electron-sludge-hand/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Sludge Hand. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Sludge Hand recovery directory must contain restored_sludge_hand_runtime and sludge_hand/extracted/electron_sludge_hand_20261108/SOURCE_MAP.json. Require exactly 27,733 files / 1,548,153,891 bytes; map SHA256 c17a48a665b20e1c65ed4dcd771f0d04e4d4686a12d595d3db1295d8c2a917e9.

Place these published receipts in that directory:
- SLUDGE_HAND_REMOTE_CHAIN_VERIFICATION.json, SHA256 a5ccf3ca2d1602cafa4380baada4921cef0c948d1a5485a17ef04781c3cbcb15.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Sludge Hand source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_sludge_discard.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_sludge_discard.py --sludge-hand-recovery /path/to/completed-sludge-hand-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 493a357019d4ee04727df6ad8eb5ea11f7811c18, path battlegrounds-backup/pending/20261108-electron-sludge-discard. Archive electron_sludge_discard_20261108.tar.xz: 1,097,864 bytes, SHA256 9e9c2d54e77b4433971ee1e4c505676385cde43739b6af5aab7cc8b8d100e1df.

Every part, assembled archive and all 38 safe members are verified. Companion hashes and exact map differences must match six modifications, two additions and no removals. Sludge Hand SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_sludge_discard_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require SLUDGE_DISCARD_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,735 files / 1,548,160,788 bytes, no missing/mismatched/unexpected files, and target map SHA256 10779ba8aa53ccf512d9ef0fad64be922ed0b1a0b85b4da0205389088dfe6cbb. Per-file origins are in RESTORE_PROVENANCE.json.

Only Sludge Discard is freshly downloaded this round; historical source evidence and Sludge Hand baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The eight delta files are exactly six modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.
