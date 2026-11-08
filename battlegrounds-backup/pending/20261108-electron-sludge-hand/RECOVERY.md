# Recover Electron Sludge Hand source

Source-byte verification only, not gameplay acceptance or recovery of lost uncommitted work. Preserve all backups and never run Godot in verification baselines.

## Obtain the prerequisite baseline

Follow the immutable Corrupted Coin recipe and tested helper:
https://github.com/Ethsigema/AI_text01/blob/25172c8c72f83df112ef81000c4af70f08044c97/battlegrounds-backup/pending/20261108-electron-corrupted-coin/RECOVERY.md

That recipe describes obtaining Recruitment and composing Deathrattle before independently restoring Corrupted Coin. Follow its pinned prerequisites to the complete historical recovery recipe, including the November 1 ZIP, recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c, Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and subsequent increments. The scheduled Deathrattle whole-chain check freshly verified all those source bytes; this helper reuses its evidence rather than redownloading the entire history.

The completed Corrupted Coin recovery directory must contain restored_corrupted_coin_runtime and corrupted_coin/extracted/electron_corrupted_coin_20261108/SOURCE_MAP.json. Require exactly 27,731 files / 1,548,148,085 bytes; map SHA256 acfd9e487224daf05eb93e343f099fb26de584f3296c051a510fbb902736dce4.

Place these published receipts in that directory:
- CORRUPTED_COIN_REMOTE_CHAIN_VERIFICATION.json, SHA256 f13b7832136e98f1e2b56bf46b204992d30e42a97093635d190fe04eb60a7c99.
- FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 47f9232e818c42246c1932cebfdb71dce791bb42b0b82cf5beb9614655bdd5b7.

The helper pins those hashes, checks the prior chain endpoint and continuity, and directly rehashes every Corrupted Coin source file. Receipts are supporting evidence, not substitutes for source bytes.

## Download and restore

Place verify_and_restore_sludge_hand.py in a fresh directory. Python 3 standard library and about 2 GB free disk are needed once the baseline exists.

```sh
python3 verify_and_restore_sludge_hand.py --corrupted-coin-recovery /path/to/completed-corrupted-coin-recovery
```

The helper freshly downloads MANIFEST.json, CHANGES.json, REMOVALS.json and five binary parts from commit 0479d2585fbd6132bbc47c16fee77e578308d76f, path battlegrounds-backup/pending/20261108-electron-sludge-hand. Archive electron_sludge_hand_20261108.tar.xz: 1,080,420 bytes, SHA256 d9b490f000fd675332dcabd9ed6effa826a47d9ca379b1dfc31ae01a95ab46a9.

Every part, assembled archive and all 37 safe members are verified. Companion hashes and exact map differences must match five modifications, two additions and no removals. Corrupted Coin SOURCE_MAP must byte-equal BASE_MAP. The helper independently copies restored_sludge_hand_runtime, verifies every output hash, and rehashes the baseline unchanged. No hardlinks are created.

Require SLUDGE_HAND_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY, 27,733 files / 1,548,153,891 bytes, no missing/mismatched/unexpected files, and target map SHA256 c17a48a665b20e1c65ed4dcd771f0d04e4d4686a12d595d3db1295d8c2a917e9. Per-file origins are in RESTORE_PROVENANCE.json.

Only Sludge Hand is freshly downloaded this round; historical source evidence and Corrupted Coin baseline are reused, with all baseline bytes rehashed. Existing destinations are not overwritten. Preserve failed attempts and diagnose before retrying in a fresh directory. No deletion, remote writes or gameplay execution occur.

The seven delta files are exactly five modifications and two additions. No redundant delta files or removals are present. Source-byte verification does not establish gameplay acceptance.
