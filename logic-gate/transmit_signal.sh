#!/bin/bash
# 12D Transmission Protocol: Secure Mirroring & AES-256 Encryption

ASSET_NAME=$1
TARGET_DESTINATION=~/arcana-ecosystem/outbound-signals/
CORE_PATH=~/arcana-ecosystem/core-assets/$ASSET_NAME

if [ -f "$CORE_PATH" ]; then
    # Create an encrypted version in the outbound folder
    # This will prompt you to enter a password in the terminal
    gpg --output "${TARGET_DESTINATION}${ASSET_NAME}.gpg" --symmetric --cipher-algo AES256 "$CORE_PATH"
    
    echo "SUCCESS: $ASSET_NAME encrypted and moved to Outbound Signals."
    echo "$(date): Encrypted Signal Transmitted - ${ASSET_NAME}.gpg" >> ~/arcana-ecosystem/history-vault/transmission_log.md
else
    echo "ERROR: Asset $ASSET_NAME not found in Core. Check alignment."
fi
