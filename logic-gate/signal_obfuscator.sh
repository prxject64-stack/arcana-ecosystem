#!/bin/bash
# Phase 2, Day 18: Signal-Obfuscator (Metadata Cloaking Protocol)

echo "--- APPLYING METADATA JITTER ---"

# 1. Randomize Timestamps for all GPG signals in the vault
# This makes it look like data was processed at different 3D times
find ~/arcana-ecosystem/vault-financial-records/ -name "*.gpg" | while read -r FILE; do
    # Generate a random date within the last 48 hours
    RND_OFFSET=$((RANDOM % 172800))
    RND_DATE=$(date -d "@$(($(date +%s) - RND_OFFSET))" "+%Y%m%d%H%M.%S")
    
    # Apply the fake timestamp
    touch -t "$RND_DATE" "$FILE"
    
    # 2. Inject Size Jitter (Add 1-10 random bytes to the file)
    # This prevents 'Identical Size' analysis
    JITTER_SIZE=$((1 + RANDOM % 10))
    truncate -s +"$JITTER_SIZE" "$FILE"
done

echo "SUCCESS: Vault metadata scrambled. Pattern recognition neutralized."
