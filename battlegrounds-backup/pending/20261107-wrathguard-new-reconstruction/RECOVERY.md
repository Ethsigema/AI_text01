# Verified new Wrathguard reconstruction

This is new work, not recovery of either lost checkpoint. The card remains partially supported; see the archived README and VALIDATION.json for bounded tests and limitations.

Download MANIFEST.json and all six .part000 through .part005 files at content commit cf0a57917c570773382f8bcad5e33f86d141846f. Concatenate parts in manifest order as binary bytes (not base64). The resulting tar.xz is 1,371,400 bytes with SHA256 9e96a7b8f3a182975bd1237a4e68259568a38530be3738478883f3b8d5943432. Verify each part, whole archive and all42 member hashes before safe extraction into a NEW directory. Reject absolute paths, .. paths and links.

This archive is a delta, not a standalone game. Restore exact Bloodbound first from November1 baseline and preserved recovery commits e11b3d7e759cc96b75a86b4c1de2e0cd192ab27c and32180d3af0db59fb3374f53100f9eaa5bb62d26a. Bloodbound source-map SHA256:9a517b7c2e0ba0c14308248884696b008e5a6f0b500a1d1d97bcd53c4b7a9c71. Follow the archived materialize.py instructions, using a new runtime destination and Godot4.6.3. Never modify hardlinked assets/research in place.

Remote download verification passed all6 parts and42 members. This is backup integrity verification, not a new full gameplay or clean-machine restore test. Older backups were preserved because safe historical recovery after deletion is not established; the dependency chain must remain.
