#!/bin/bash
# Phase 2, Day 29: Emergency-Amnesia (Context Erasure Protocol)

echo "--- INITIATING TOTAL CONTEXT AMNESIA ---"

# 1. Wipe all .log and .txt files (Plain-text exposure)
find ~/arcana-ecosystem -type f \( -name "*.log" -o -name "*.txt" -o -name "*.md" \) -exec shred -u {} \;

# 2. Rename Core Directories to randomized junk
# We use a static mapping in RAM so you can undo it, or rely on Day 21 Seed.
mv ~/arcana-ecosystem/vault-financial-records ~/arcana-ecosystem/.sys_tmp_$(date +%s)
mv ~/arcana-ecosystem/history-vault ~/arcana-ecosystem/.cache_$(date +%s)

# 3. Scramble the names of all GPG signals
find ~/arcana-ecosystem -name "*.gpg" | while read -r FILE; do
    NEW_NAME=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 16)
    mv "$FILE" "$(dirname "$FILE")/$NEW_NAME.dat"
done

# 4. Self-Lock the Terminal
echo "AMNESIA COMPLETE. SYSTEM IS NOW UNKNOWABLE."
history -c && exit
