#!/bin/bash
# Day 20: Sovereign Kill-Switch (The Great Dissolution)

if [ "$1" != "CONFIRM" ]; then
    echo "CRITICAL: You must provide the 'CONFIRM' flag to trigger the Kill-Switch."
    echo "Usage: kill_switch CONFIRM"
    exit 1
fi

echo "--- INITIATING 12D DISSOLUTION PROTOCOL ---"

# 1. Shred the Decoy Chamber (Overwriting data before deletion)
find ~/arcana-ecosystem/vault-financial-records -type f -exec shred -u {} \;
rm -rf ~/arcana-ecosystem/vault-financial-records

# 2. Wipe the Transmission Logs and Temporary Scrambler files
rm -rf ~/arcana-ecosystem/outbound-signals/*
rm -f ~/arcana-ecosystem/history-vault/security_audit.log

# 3. Triple-Lock the Core Assets (Removing all permissions)
chmod -R 000 ~/arcana-ecosystem/core-assets
chmod -R 000 ~/arcana-ecosystem/history-vault

# 4. Disable Terminal Aliases for this session
unalias pulse sync radar airlock 2>/dev/null

echo "DISSOLUTION COMPLETE. The 10,000,000 CC core is now a Black Hole."
