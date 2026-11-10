# November 10, 2026 18:00 Beijing backup audit

This directory contains audit evidence, not a game backup or source delta. No new game package was generated: both known local source trees match their existing manifests, and the latest candidate evidence package was already published.

Actual work this round: rehashed every byte in the two known local trees (27,920 and 27,921 files); freshly fetched 28 files of the latest optional-field evidence package from fixed commit 9c3e01bc0f30ad4627d0fa0068edacaadaf83bde; verified file sizes, SHA256 and Git blob SHA; reconstructed 22 parts and verified 908 archive files and the 893-entry fixture whitelist. Rehashed 28 retained older archives against their sealed hashes.

Only the latest evidence package was newly downloaded. The prior cancelled batch14 dependency network action was not retried, directly or indirectly. Full base-plus-dependency-chain download and rebuild were NOT attempted. These checks do not establish complete game recoverability.

345 entries in the existing missing-reference list remain absent. Two named SOURCE_CONTRACT.md files also remain absent. Candidate tests do not supply reliable completion numerators or denominators for minions, Tavern spells or trinkets. No engine, gameplay or save test ran in this audit.

The latest evidence archive is 5,393,436 bytes, SHA256 00097718164f6665867f6ee79d5f033cf99e112f921cfc6b2040ba6760d53a70. It contains review material and uninstalled candidates, not a standalone game. Its fixed recovery instructions are at https://github.com/Ethsigema/AI_text01/blob/9c3e01bc0f30ad4627d0fa0068edacaadaf83bde/battlegrounds-backup/pending/20261110-darkcrest-frost-seafloor-optional-review/RECOVERY.md .

All existing backups and source trees were preserved. This audit publication only adds its own records.
