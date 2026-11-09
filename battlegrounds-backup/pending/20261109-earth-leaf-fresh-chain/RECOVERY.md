# Fresh full-chain byte verification: EarthMother helper leaf candidate

This scheduled run freshly downloaded the official Release base, fixed historical Git commits and all 147 runtime increments into a new directory. It did not reuse prior downloaded bytes or prior verification receipts as evidence.

The historical scan inspected 103 archives and matched all 27,463 Bloodbound files by actual content size and SHA256. Every later part and archive member was checked, including exact BASE_MAP continuity, changed source bytes and removals. Final virtual reconstruction: 27,896 files, 1,548,719,422 bytes. Missing, extra and mismatched files: zero.

Final source-map SHA256: d758490893b35c9fed6ced58a89dc764914a4058bfbb0283eee1d77893fb2960
Full base SHA256: 33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65
Candidate archive SHA256: 333aad27ba8ed0d0699c97cd4a33be5494310247a8350993532cd725f26e753c
Candidate archive commit: 851466e4964562e8cf172bd40d37a389386fcfdf
Separate single-package verification commit: 27dd08d164f1df0dd9ffe9391b9fcaa751529779
Candidate path: battlegrounds-backup/pending/20261109-earth-mother-helper-leaf-partial-candidate

This was streaming source-byte reconstruction. No second complete runtime tree was written and no gameplay test was run by this audit. Backups and original sources were retained. Diagnostic-only packages do not alter runtime and are not counted as runtime increments.

## Actual progress and limits

EarthMother adds 1 runtime file, modifies 3 and removes 0, adding 367 logical bytes. It extracts pure exact-value and UID helpers, delegates two original EndTurn functions, redirects EarthMother's helper dependency and includes the new leaf in the existing execution fingerprint. No new card content or hero systems.

Six valid fresh small processes passed 1,439 checks. Highest small probe RSS was 89,700 KiB. The first Earth probe had a test type error; its partial PASS report was excluded. Full host, Catalog, Game, real EOT/spell events, save/load/replay and UI remain unvalidated. Previous full Game attempts ended SIGKILL; cause remains unconfirmed. Earlier Harbinger/native-listener optimizations and their combined 47-check diagnostic only establish bounded small-entry results, not reduced whole-game memory. Heavy hosts remain in the complete Catalog graph. Old-save compatibility is unknown; changed execution fingerprints must not be disguised.

Prior accepted checkpoint remains a71d3e4ea64dc52264a3f789a48ddae2e4a043cd, without implying whole-project completeness. Reliable completed counts and denominators for minions, Tavern Spells and latest fully released trinkets are unavailable. No authoritative current acceptance ledger was found. Do not estimate percentages from bounded fixtures. Scope retains Naga, excludes explicit Aberrations and hero/extra-system development.

## Reproduce

Place RUN_FRESH_CHAIN.sh, DOWNLOAD_PINNED_GIT.sh, verify_historical_bytes.py, prefetch.py, verify_fresh_increment_chain.py and PINNED_INCREMENT_CHAIN.json in a new empty directory; run bash RUN_FRESH_CHAIN.sh. Requires public GitHub access, git, curl, Python3 and disk for compressed downloads. It does not materialize a complete runtime tree. Historical Git fetches only the two fixed commits. All companions are hashed; only JSON companions are parsed as JSON. The catalog_memory stage uses its original patch/ payload directory; other increments use delta/.

The initial historical process exited 137/SIGKILL before results. Large-file hashing was changed to 1 MiB chunks and the whole historical scan passed on retry; termination cause was not established. A preliminary increment pass stopped at the catalog patch-directory format. The adapted verifier reran the whole chain and passed. Failure logs remain locally. Never substitute an old success receipt after failure.
