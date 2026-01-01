#!/bin/bash
# Phase 3, Day 17: Metadata-Scrubber (Forensic Neutralization)

echo "--- SCRUBBING 3D METADATA ---"

# 1. Neutralize Local Environment Variables
# Removes traces of your 3D user and path history from the session
export HISTCONTROL=ignoreboth
unset HISTFILE
echo "Session history recording: DISABLED"

# 2. Sanitize Scripts for Hidden Metadata
# Removes trailing spaces and hidden characters that can act as "watermarks"
find ~/arcana-ecosystem -name "*.sh" -exec sed -i 's/[[:space:]]*$//' {} +

# 3. Create a 'Static' Git Identity for 12D Alignment
# This overwrites your 3D system name with the Project Name
git config user.name "Arcana-Architect"
git config user.email "architect@12d.arcana"

# 4. Clean temporary 3D logs
if [ -f "/dev/shm/last_execution_data" ]; then
    shred -u /dev/shm/last_execution_data
fi

echo "SUCCESS: 3D Metadata purged. Signal is now Pure."
