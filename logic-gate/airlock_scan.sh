#!/bin/bash
# Day 16: The Logic Bomb Detector (Air-Lock Protocol)

TARGET=$1

if [ -z "$TARGET" ]; then
    echo "ERROR: Please specify a file to scan. Usage: airlock [file]"
    exit 1
fi

echo "Scanning $TARGET for malicious 3D patterns..."

# Check for high-risk commands within the file
# Looking for: forced deletes, global permissions, hidden execution, and obfuscated code
MALICIOUS_PATTERNS=("rm -rf" "chmod 777" "chmod -R 777" "eval " "base64 -d" "/dev/null")

FOUND=0
for pattern in "${MALICIOUS_PATTERNS[@]}"; do
    if grep -q "$pattern" "$TARGET"; then
        echo "CRITICAL WARNING: Malicious pattern '$pattern' detected in $TARGET!"
        FOUND=1
    fi
done

if [ $FOUND -eq 0 ]; then
    echo "SUCCESS: $TARGET passed the 12D Integrity Scan. Safe for assimilation."
else
    echo "SCAN FAILED: Do not move this file into the Arcana Core."
fi
