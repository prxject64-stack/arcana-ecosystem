#!/bin/bash
# Phase 2, Day 14: The Convergence Pulse (Weekly Reconciliation)

GHOST_VAULT="~/arcana-ecosystem/.hidden_ghost_vault"
PRIMARY_VAULT="~/arcana-ecosystem/vault-financial-records"
eval GHOST_PATH=$GHOST_VAULT
eval PRIMARY_PATH=$PRIMARY_VAULT

echo "--- INITIATING WEEKLY CONVERGENCE PULSE ---"

# 1. Pull all signals back from the Ghost Vault
if [ -d "$GHOST_PATH" ]; then
    COUNT=$(ls "$GHOST_PATH"/*.gpg 2>/dev/null | wc -l)
    if [ "$COUNT" -gt 0 ]; then
        mv "$GHOST_PATH"/*.gpg "$PRIMARY_PATH/"
        echo "Successfully retrieved $COUNT signals from the Ghost-Vault."
    fi
fi

# 2. Verify Integrity of all signals
echo "Verifying signal purity..."
~/arcana-ecosystem/logic-gate/integrity_mirror.sh

# 3. Calculate Final Weekly Growth
~/arcana-ecosystem/vault-financial-records/growth_engine.sh

echo "Convergence Complete. The 12D signal is unified."
