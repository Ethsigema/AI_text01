# Ordinary Lava native sale final verification audit

Final fixed commit c3873696df2d384a833bc78a6a58897faa810dce; source fixed commit 73ef3f42e2a52b71aacd29fac2d6392731015d9d.

The verifier already supported publication `remote_folder`; this batch had no publication-field compatibility failure. It actually freshly downloaded all 30 files, 3,960,877 bytes, checked length/Git blob SHA/SHA256 and all 29 checksum entries, and safely read and rehashed all 103 evidence members (FIX29 + TOOLS19 + GAMEPLAY55). All 16 original non-checksum source-package files remained identical; existing post-Game double-tree reports matched source map/aggregate. The actual finite-slice test total is 2,950 (Game322 + pure140/211/966/810/68/166/267), not whole-game acceptance. No Game rerun or new full source-tree copy was performed by final publication verification.

Scope: single ordinary Lava native sale/departure and later Darkcrest EOT in two fixed four-player headless rooms. Coin funding is a fixture before source ownership. Pure predicates/unbound rejection calls do not establish live partial-native-failure or capacity saturation coverage. Retired UID limit128/no eviction/pre-consumption hold is separate from Darkcrest Tier6 progression cap. No permanent Mini/active rebuy/empty-slot or whole-family promotion.

This audit stores the exact verifier and actual publication metadata/results. It is not standalone: the verifier expects its stage layout, including remote_snapshot_73ef3f4/package, the original download receipt and INDEPENDENT_GAME_VERIFICATION.json. Place verifier under preparation/ and FINAL_*.json in its parent. A repeat `python preparation/verify_final_publication.py --execute` needs a new workspace with no existing final_remote_publication_<commit> directory or FINAL_PUBLICATION_VERIFIED.json; preserve this actual receipt instead of overwriting it. No execution is needed to inspect this archive.

The source17, early24 and final30 packages and all old evidence remain unchanged. This audit's own upload and fresh-download verification were pending at freeze time and are separate from the completed final package verification.
