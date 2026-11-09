# Fresh full-chain byte verification: Golden Banshee candidate

This run freshly downloaded the official Release baseline (SHA256 33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65), fixed historical Git commits and all 143 later increments. No historical downloaded source bytes or prior verification receipt replaced a fresh download.

The historical scanner inspected 103 archives and established every one of 27,463 Bloodbound source files from newly downloaded bytes. Ordered increment verification checked every archive part and member size/SHA256, exact base-map continuity, changed bytes and removals. Final virtual reconstruction contains 27,892 files and 1,548,713,672 bytes; source-map SHA256 45dcd76fe50c5e2e03cea65032189b15cca35894cac08b2e704c17139b7fd6a8. Missing, extra and mismatching files: zero.

This is streaming source-byte reconstruction, not a newly materialized complete Godot project. No gameplay test was run by this audit. All backup archives and original sources were retained.

## Fixed candidate

Archive commit: c6e62f2af2277b43b139b8049936008772df979d
Final separate single-package verification publication: 35c7fc04e0cb85c4ec9435bf4d2861b65c057971
Path: battlegrounds-backup/pending/20261109-hopebringer-banshee-golden-candidate
Archive SHA256: a20b6c427a1219903df1d4a927693d3e553a337236f509408eff651318297433

The candidate is unfinished. Its isolated native combat passed 20 checks, but four complete Game attempts exited -9/SIGKILL with no gameplay report; termination cause was not established. Hopebringer co-play/permanent growth, full saves/replay, natural acquisition and UI remain unverified. Do not promote it over accepted baseline a71d3e4ea64dc52264a3f789a48ddae2e4a043cd.

## Repeat

Place RUN_FRESH_CHAIN.sh, DOWNLOAD_PINNED_GIT.sh, verify_historical_bytes.py, prefetch.py, verify_fresh_increment_chain.py and PINNED_INCREMENT_CHAIN.json in a new empty working directory; run bash RUN_FRESH_CHAIN.sh. It requires public GitHub access, git, curl, Python3 and disk for downloaded compressed archives. It deliberately does not create a second full runtime directory. On failure preserve the logs and report failure; do not substitute an old receipt.

The original API download encountered an exhausted unauthenticated quota. The official direct Release link in fixed RESTORE.md worked normally and produced the exact expected hash. A preliminary increment check stopped while downloads were incomplete; another exposed the old helper assumption that all companion files were JSON. The helper now hashes every companion and parses only .json files. Final ordered verification reran from the start and passed.

## Progress reporting

No authoritative current completion ledger/denominator was found in the candidate runtime or freshly fetched remote repository. Minions, Tavern Spells and latest fully released trinkets each have unknown reliable completed count, denominator and percentage. Bounded fixtures are not exhaustive item acceptance. Scope retains Naga, excludes explicit Aberrations and excludes hero/extra-system development.
