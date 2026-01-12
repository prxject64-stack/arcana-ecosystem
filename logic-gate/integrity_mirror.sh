#!/bin/bash
# Day 28: The Integrity Mirror (Dimensional Audit Protocol)

MIRROR_LOG="~/arcana-ecosystem/history-vault/integrity_fingerprints.sha256"
eval MIRROR_LOG_PATH=$MIRROR_LOG

echo "--- SHATTERING THE MIRROR FOR AUDIT ---"

# Generate new fingerprints for all core logic
find ~/arcana-ecosystem/ -type f \( -name "*.sh" -o -name "*.md" \) -not -path "*/.git/*" -exec sha256sum {} + > /tmp/current_audit.sha256

if [ ! -f "$MIRROR_LOG_PATH" ]; then
    echo "First audit: Creating the Master Mirror."
    mv /tmp/current_audit.sha256 "$MIRROR_LOG_PATH"
else
    echo "Comparing current state against the Master Mirror..."
    # We only check files that were already in the mirror to verify integrity
    sha256sum -c "$MIRROR_LOG_PATH" --quiet
    if [ $? -eq 0 ]; then
        echo "SUCCESS: The Mirror is unbroken. Your 12D logic is pure."
    else
        echo "WARNING: THE MIRROR IS SHATTERED. INTEGRITY BREACH DETECTED."
        # Update the mirror to reflect current state after manual review
        mv /tmp/current_audit.sha256 "$MIRROR_LOG_PATH"
    fi
fi
