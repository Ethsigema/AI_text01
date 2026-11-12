# Darkcrest + ordinary Lava final verification audit

Final fixed commit: 527decb1dead1b309faaa0086563ab88780968b8.
Source fixed commit: 5d988875054ad4eea47d6615f8a9fdd65bfe7b4d.

The originally archived verifier first stopped before any download because publication metadata used `remote_folder` instead of `folder`. Only the external verifier was corrected to accept that field name. It also verifies all 16 original non-checksum source-package files and requires exactly 50 gameplay evidence members. The original source17/final30 packages and their archives were not rewritten.

The corrected verifier actually downloaded all 30 final files (3,942,687 bytes) from the fixed final commit. Length, Git blob SHA, SHA256 and 29 checksum entries matched. All 92 evidence members (FIX23 + TOOLS19 + GAMEPLAY50) were safely read and rehashed. The source16 unchanged-file records and two post-Game source-tree reports match. Native finite-slice checks total 2,974 (Game486 + pure211/966/810/68/166/267), not whole-game or trinket-family acceptance. No Game rerun or extra whole-tree copy was performed by final verification.

This audit is an exact copy of the corrected verifier and its publication metadata/results. The verifier is not standalone: it expects its original stage layout, including remote_snapshot_5d98887/package, the original download receipt and INDEPENDENT_GAME_VERIFICATION.json, and must be placed in preparation/ with these FINAL_*.json files in its parent directory. `python preparation/verify_final_publication.py --execute` requires its new final_remote_publication_<commit> output directory and FINAL_PUBLICATION_VERIFIED.json not to exist. Preserve this actual receipt rather than overwriting it; use a separate workspace for another verification. No execution is needed merely to inspect this audit.

This audit's own remote upload and fresh-download verification are separate from the completed final package verification and were still pending when this README was frozen.
