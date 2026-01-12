#!/bin/bash
# Phase 2, Day 16: Signal-Synthesizer (Data Fusion Protocol)

PRIMARY_VAULT="~/arcana-ecosystem/vault-financial-records"
eval VAULT_PATH=$PRIMARY_VAULT

# Pull current secret for processing
ROTATING_KEY=$(date +%Y%m%d%H$(($(date +%M)/10)))
SECRET="12D_ARCANA_${ROTATING_KEY}"

echo "--- INITIATING SIGNAL FUSION ---"

# 1. Check for batches of 10 signals
SIGNAL_COUNT=$(ls $VAULT_PATH/signal_*.gpg 2>/dev/null | wc -l)

if [ "$SIGNAL_COUNT" -ge 10 ]; then
    echo "Resonance detected for $SIGNAL_COUNT signals. Synthesizing..."
    
    TMP_FUSION="/dev/shm/fusion_$(date +%s)"
    mkdir -p $TMP_FUSION
    
    # 2. Decrypt and aggregate the first 10 signals
    ls $VAULT_PATH/signal_*.gpg | head -n 10 | while read -r FILE; do
        gpg --batch --quiet --yes --passphrase "$SECRET" --decrypt "$FILE" >> $TMP_FUSION/batch.txt 2>/dev/null
        rm "$FILE" # Dissolve the original 3D component
    done
    
    # 3. Encrypt the Super-Signal
    SUPER_NAME="supersignal_$(date +%s).gpg"
    gpg --batch --yes --passphrase "$SECRET" --symmetric --cipher-algo AES256 -o "$VAULT_PATH/$SUPER_NAME" $TMP_FUSION/batch.txt
    
    echo "SUCCESS: 10 signals fused into $SUPER_NAME."
    rm -rf $TMP_FUSION
else
    echo "Wait: Only $SIGNAL_COUNT signals found. 10 required for stable synthesis."
fi
