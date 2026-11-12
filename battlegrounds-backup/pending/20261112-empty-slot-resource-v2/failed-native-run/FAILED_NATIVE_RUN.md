# v2 native empty-slot run failed, no rollback

Fixed source: aae0cf4c9f3325bc6a98ca34700059d25d235534.

The actual three-player seed20261120 run failed on first-round end_turn with hopebringer_combat_failed:apexis_wrong_real_owner (core/apexis_guardian_host.gd:43). Godot exited 1 after 225.16315811799996 seconds. No room completed next recruit; 5/7/4-player rooms and follow-up pure contracts were not run. Earlier development-tree pure contracts are not substitute acceptance.

Both restored source and runtime copy were fully rehashed after failure: each 27,971 files, 1,550,655,219 bytes, unchanged map/aggregate. The frozen source and package remain intact; this is failure evidence, not a rollback or successful gameplay receipt.

Actual log/result, before-run hashes, wrapper, runner and preparation metadata are preserved. A separate runner exception log was not found on disk; none is fabricated. No Game was launched by this archive step.
