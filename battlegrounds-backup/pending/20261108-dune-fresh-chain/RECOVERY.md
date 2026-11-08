# Fresh complete-chain verification through Hopebringer Dune

This method freshly obtains every source archive dependency rather than relying on historical verification receipts. It verifies complete source-byte recoverability by hash-index composition without writing a full runtime directory. It does not execute gameplay or recover lost uncommitted work.

Copy RUN_FRESH_CHAIN.sh, verify_historical_bytes.py, verify_fresh_increment_chain.py PINNED_INCREMENT_CHAIN.json and create_dune_receipt.py into a new empty directory, then run:

```sh
sh RUN_FRESH_CHAIN.sh
```

Requirements: Python 3 standard library, Git, curl, tar, network access to GitHub and release assets, approximately 3 GB free disk and enough memory for archive decoding. Existing destinations are not overwritten. Preserve any failed attempt and diagnose before retrying; no deletion is performed.

The shell script freshly downloads the original November 1 release ZIP (SHA256 33b3a1a12185cf9035cec33da4fff7008c7680194eb045b37234fbb934803d65), clones/fetches recovery commit e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c and Bloodbound commit 32180d3af0db59fb3374f53100f9eaa5bb62d26a, and checks Git objects with git fsck. The clone is shallow: the complete pinned trees and their source blobs are obtained, not unrelated commit history.

The historical helper verifies archive part sizes and hashes, assembled archives, nested archives and exact source-byte hashes for all 27,463 Bloodbound files against its authoritative SOURCE_MAP (SHA256 9a517b7c2e0ba0c14308248884696b008e5a6f0b500a1d1d97bcd53c4b7a9c71). It records per-file archive origins in PROVENANCE.json and all scanned archives in ARCHIVE_SCANS.json. RESTORE_RESULT.json must have no missing files, mismatches or archive errors.

The increment helper then freshly downloads MANIFEST.json and every binary part for all 114 pinned increments listed in PINNED_INCREMENT_CHAIN.json. It verifies all part, archive and member sizes/hashes and safe member paths. Every BASE_MAP must exactly match the preceding source map; every changed source member must match the exact map difference. CHANGES.json and REMOVALS.json, where supplied, are freshly downloaded, hash-bound to the manifest and compared to actual differences. No removals are allowed in this chain.

The last increment is pinned to commit 7e1804464d9f703161883e9371358f0e4525881f at battlegrounds-backup/pending/20261108-hopebringer-dune. Archive SHA256: e09b9a16e325b39fffdc3359543d527ff364737f247191407915b984c57ba073. Expected final source: 27,821 files / 1,548,444,623 bytes; SOURCE_MAP SHA256 afcfedcc2db16afaa31e2007e32c39dd63d6efef20fdcdfd975d7c5a97c67ad7.

Success requires FRESH_WHOLE_CHAIN_VERIFICATION.json status PASS_FRESH_FULL_CHAIN_SOURCE_BYTES and the exact final counts/map. All unchanged files inherit provenance from freshly verified source bytes, and all changed files are verified from fresh archive member bytes. This is complete byte composition, not a second materialized runtime. No existing runtime, baseline, hardlink or backup is modified.

To materialize a runtime, follow the existing pinned recovery helpers in chronological order. This fresh verification does not itself create that directory or establish gameplay acceptance.

Chef Magnetic contains two redundant unchanged research files in its delta. Both are freshly member-hashed and verified equal to baseline and target: research/electron_chef_choice/evidence.json and research/electron_chef_choice/BG28_518.native.xml. Every other packaged delta equals the actual map difference.

The initial official release asset API request returned HTTP 403 because its unauthenticated GitHub rate limit was exhausted, with no ZIP bytes received. The run waits until the response's documented reset before retrying that same endpoint. The exact HTTP headers and body are retained locally; RUN.log and RESUME.log record the attempt and continuation. No historical bytes from previous runs substitute for this download. The portable recipe uses https://api.github.com/repos/Ethsigema/AI_text01/releases/assets/697440146 with Accept: application/octet-stream; respect any documented rate limit before retrying.

Increment retrieval uses four concurrent packages with at most four part/companion reads each. Every byte is freshly fetched in this invocation, then rehashed from that same-invocation download during ordered chain composition. Existing prior-run archives or receipts are not used as source evidence.

The final audit writes DUNE_REMOTE_CHAIN_VERIFICATION.json, validates all 114 pinned entries against the ordered receipts and checks the Dune baseline/target map hashes. This dedicated receipt explicitly records complete byte composition without a materialized directory.

For a materialized Dune runtime, the immutable ordinary recovery recipe is https://github.com/Ethsigema/AI_text01/blob/5d35dd88c83853681367c1e8aef16dcd95b0171a/battlegrounds-backup/pending/20261108-hopebringer-dune/RECOVERY.md . This scheduled check verifies all freshly obtained source-byte composition instead; it does not reuse that ordinary runtime as evidence.

Completed result: all 114 increments, 802 binary parts and 6,105 members freshly verified. Historical verification covered 70 archive-part manifests and 103 archives with all 27,463 Bloodbound source hashes found. Final Dune composition is 27,821 files / 1,548,444,623 bytes, with zero missing files, mismatches or archive errors. Git fsck exited successfully; its dangling Bloodbound commit notice is expected because that exact fetched tree was archived without moving HEAD. No gameplay tests were run.

PROVENANCE.json contains the complete historical per-file origin index and is retained locally; running this recipe reproduces it. It need not be duplicated in a publication. The failed rate-limited attempt downloaded zero ZIP bytes; the continuation reused only Git bytes freshly downloaded in this same scheduled check.
