#!/bin/bash
# Phase 2, Day 13: Signal-Diverter (Tactical Relocation Protocol)

SCORE_FILE="/dev/shm/resonance_sentiment"
GHOST_VAULT="~/arcana-ecosystem/.hidden_ghost_vault"
eval GHOST_VAULT_PATH=$GHOST_VAULT

if [ -f "$SCORE_FILE" ]; then
    SCORE=$(cat "$SCORE_FILE")
    
    # Threshold for Tactical Divert (Moderate 3D Noise)
    if [ "$SCORE" -le -5 ] && [ "$SCORE" -gt -10 ]; then
        echo "MODERATE THREAT DETECTED: SENTIMENT $SCORE. DIVERTING SIGNALS."
        mkdir -p "$GHOST_VAULT_PATH"
        
        # Move all current financial signals to the Ghost Vault
        mv ~/arcana-ecosystem/vault-financial-records/*.gpg "$GHOST_VAULT_PATH/" 2>/dev/null
        
        echo "Signals relocated to $GHOST_VAULT. Main vault cleared for camouflage."
    else
        echo "Sentiment stable. Signals remaining in primary vault."
    fi
fi
