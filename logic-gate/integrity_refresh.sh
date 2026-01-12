#!/bin/bash
# Phase 2, Day 28: Integrity-Mirror Refresh (Final Audit Protocol)

MANIFEST_FILE="~/arcana-ecosystem/.integrity_manifest.sha256"
eval MANIFEST_PATH=$MANIFEST_FILE

echo "--- INITIATING DEEP INTEGRITY REFRESH ---"

# 1. Generate new SHA-256 hashes for every file in the ecosystem
# Excluding the manifest itself and the hidden .git directory
find ~/arcana-ecosystem -type f -not -path '*/.*' -not -name "*.sha256" -exec sha256sum {} + > "$MANIFEST_PATH.tmp"

# 2. Compare with previous manifest (if it exists)
if [ -f "$MANIFEST_PATH" ]; then
    echo "Comparing against 12D Blueprint..."
    DIFF=$(diff "$MANIFEST_PATH" "$MANIFEST_PATH.tmp")
    if [ -z "$DIFF" ]; then
        echo "VERIFICATION SUCCESS: All files are in perfect 12D alignment."
    else
        echo "ALERT: Structural Drift Detected! Check changes below:"
        echo "$DIFF"
    fi
else
    echo "Initial Blueprint anchored."
fi

# 3. Finalize the new Manifest
mv "$MANIFEST_PATH.tmp" "$MANIFEST_PATH"
chmod 400 "$MANIFEST_PATH" # Make the manifest Read-Only
echo "Integrity Mirror refreshed and locked."
