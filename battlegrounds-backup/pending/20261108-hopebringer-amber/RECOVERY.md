# Recover Hopebringer Amber source

This verifies source-byte recoverability only, not gameplay acceptance. Preserve all backups; never run Godot in verification baselines.

## Obtain the composed baseline

Restore the Blade runtime using its pinned recipe:
https://github.com/Ethsigema/AI_text01/blob/b225e1e290f5b36deb012b0009e51e018d13996f/battlegrounds-backup/pending/20261108-hopebringer-blade/RECOVERY.md

Follow the Mummifier scheduled whole-chain recipe and retain its downloaded increment directory:
https://github.com/Ethsigema/AI_text01/blob/684ce843421958a6961da3d709b829f3a1731226/battlegrounds-backup/pending/20261108-hopebringer-mummifier/RECOVERY.md

That recipe freshly obtains the original November 1 release ZIP, pinned recovery e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c and Bloodbound 32180d3af0db59fb3374f53100f9eaa5bb62d26a Git trees, and all 95 increments. It verifies complete byte composition rather than writing a Mummifier runtime. This Amber helper reuses that evidence and the retained Mummifier bytes; it does not redownload history.

Required inputs:
- Blade runtime: 27,776 files, source map f00667559104e5af8ac6015d5e52bb8d1ffd74742b312277b43cf6337d9a472f.
- Mummifier download directory: MANIFEST.json and its seven binary parts from commit cff6163b1cf4d18e7c43a29fd4378fccd0fde28f, folder battlegrounds-backup/pending/20261108-hopebringer-mummifier. Archive SHA256 9a7011f6ae7f94c887ebe29f1bb8e34a5343bffe1d8698aa967a06dfd90fad59.
- Evidence directory containing the accompanying MUMMIFIER_REMOTE_CHAIN_VERIFICATION.json, SHA256 c136e2ceb44ecc0a206822a947d68f2ea672e1b337f11e327667287db64bb8e3, and FRESH_WHOLE_CHAIN_VERIFICATION.json, SHA256 18f89636d4c2aa8750e54178454711ccda2c153fd745d808abd5c502aeacf98d.

## Restore

Place verify_and_restore_hopebringer_amber.py in a fresh directory. Use Python 3 standard library with about 2 GB free space after inputs exist:

```sh
python3 verify_and_restore_hopebringer_amber.py --blade-runtime /path/to/restored_blade_runtime --mummifier-download /path/to/fresh_chain/increments/hopebringer_mummifier --mummifier-evidence /path/to/evidence
```

The helper verifies every retained Mummifier part and member, safely extracts only its small package, and composes Blade plus its exact delta. It rehashes all 27,778 composed baseline files against Mummifier SOURCE_MAP 467c0fb627a95430f5c8bee36b81e9170f8700b9860e8d3ae244840173445cf3. No intermediate full Mummifier runtime is created.

It freshly downloads Amber MANIFEST.json, CHANGES.json, REMOVALS.json and seven parts from commit 8059a186387cf938481b9a7a7cf251865d524d03 at battlegrounds-backup/pending/20261108-hopebringer-amber. Archive hopebringer_amber_20261108.tar.xz: 1,569,900 bytes; SHA256 91986da71c66574c87f87a2b119344610fb2743c4ea2f4095a44ca6df1335e93. All 48 members and exact delta of five modifications/two additions/no removals are verified.

Require HOPEBRINGER_AMBER_REMOTE_CHAIN_VERIFICATION.json status PASS_EXACT_SOURCE_ONLY: 27,780 files / 1,548,313,647 bytes, map b561cff2dc05128e28ccdd6363c9116b0275ab3c3428b48e5f4db9979559ffc7. The independent restored_hopebringer_amber_runtime has no hardlinks or unexpected files; every output hash is checked and baseline bytes rehashed unchanged. RESTORE_PROVENANCE.json records each source origin.

Only Amber is freshly downloaded this round. No deletion, remote writes or gameplay execution occur. Existing destinations are not overwritten; preserve failed attempts before diagnosing.
