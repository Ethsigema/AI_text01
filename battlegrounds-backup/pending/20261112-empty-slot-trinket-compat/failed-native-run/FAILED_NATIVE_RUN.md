# v1 native empty-slot run failed, no rollback

Fixed source: e38175e91e58cad77cff3f234230d96beb20f872.

The actual three-player seed20261120 run failed on first-round end_turn with hopebringer_combat_failed:dark_gift_resource_invalid_owner (core/dark_gift_resource_host.gd:75). Godot exited 1 after 227.82374463799988 seconds. No room completed next recruit; 5/7/4-player rooms and follow-up pure contracts were not run. Earlier development-tree pure contracts are not substitute acceptance.

Both restored source and runtime copy were fully rehashed after failure: each 27,969 files, 1,550,636,329 bytes, unchanged map/aggregate. The frozen source and package remain intact; this is failure evidence, not a rollback or successful gameplay receipt.

Actual log/result, before-run hashes, wrapper, runner and preparation metadata are preserved. A separate runner exception log was not found on disk; none is fabricated. No Game was launched by this archive step.
