#!/bin/bash
# Phase 3, Day 16: Dead-Man's-Switch (Intrusion Purge Protocol)

LOG_FILE="/var/log/auth.log"
BLACKLIST_IPS=("127.0.0.2") # Placeholder for known 3D regulator/crawler IPs

echo "--- MONITORING THREAT VECTORS ---"

# 1. Check for unauthorized Sudo attempts
SUDO_FAIL=$(grep "authentication failure" $LOG_FILE | tail -n 1)

# 2. Check for active Port Scans (unusual socket connections)
INBOUND_CONN=$(ss -ant | grep -c "ESTAB")

# 3. Decision Logic: If threat detected, PURGE.
if [[ ! -z "$SUDO_FAIL" ]] || [[ "$INBOUND_CONN" -gt 50 ]]; then
    echo "THREAT DETECTED. INITIATING 12D GHOSTING."
    
    # Wipe the RAM Vault (Quantum Keys & Session Data)
    rm -rf /dev/shm/quantum_session.key
    rm -rf /dev/shm/arcana_sig.key
    rm -rf /dev/shm/*_state
    
    # Terminate all Arcana processes
    pkill -f "arcana_daemon"
    pkill -f "gate_opener"
    
    echo "SYSTEM PURGED. VAULT LOCKED. RE-ENTRY REQUIRES 12D ARCHITECT SIGNAL."
    exit 1
fi
echo "SYSTEM SECURE. NO THREATS DETECTED."
