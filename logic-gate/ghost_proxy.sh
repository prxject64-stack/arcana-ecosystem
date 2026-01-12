#!/bin/bash
# Day 27: The Ghost-Image Proxy (Camouflage Protocol)

echo "--- DEPLOYING GHOST METADATA ---"

# Target decoy directories
TARGETS=("~/arcana-ecosystem/decoy-data" "~/arcana-ecosystem/expansion-temp")

# Realistic fake filenames
GHOST_FILES=("package-lock.json" "requirements.txt" "setup.py" ".env.example" "README_INTERNAL.md" "webpack.config.js")

for DIR in "${TARGETS[@]}"; do
    eval FULL_DIR=$DIR
    mkdir -p "$FULL_DIR"
    for FILE in "${GHOST_FILES[@]}"; do
        # Create empty file with a random past timestamp
        touch -t $(date -d "$((RANDOM%30)) days ago" +%Y%m%d%H%M) "$FULL_DIR/$FILE"
    done
done

echo "SUCCESS: Ghost-Image Proxy active. 3D Scanners will see standard dev-logs."
