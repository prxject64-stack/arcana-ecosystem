#!/bin/bash
# Phase 2, Day 17: Shadow-Mirror Proxy (Deceptive Defense Protocol)

MIRAGE_DIR="~/arcana-ecosystem/vault-backups"
eval MIRAGE_PATH=$MIRAGE_DIR

echo "--- CASTING THE SHADOW MIRROR ---"

# 1. Create the visible honey-pot
mkdir -p "$MIRAGE_PATH"

# 2. Populate with "Red Herrings"
# These look like real financial logs but contain random noise
for i in {1..5}; do
    FAKE_VAL=$((100 + RANDOM % 900))
    echo "DECOY_LOG|Source:Legacy_API|Value:$FAKE_VAL|Status:Archived" > "$MIRAGE_PATH/backup_log_00$i.txt"
done

# 3. Create a fake "Master Key" file (a harmless decoy)
echo "ENCRYPTION_LAYER: DISABLED (LOCAL_ONLY)" > "$MIRAGE_PATH/access_control.md"

echo "SUCCESS: Shadow-Mirror active. Decoy vault populated."
