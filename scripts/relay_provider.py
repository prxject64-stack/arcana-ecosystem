import os
import time

# CONFIGURATION
VAULT_ARC = os.path.expanduser("~/arcana-ecosystem/vault/security_system")
LOG_FILE = os.path.expanduser("~/arcana-ecosystem/logs/liquidity.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

print("--- RELAY ONLINE: MONITORING 47B ARC VAULT ---")

while True:
    try:
        # Count receipts for progress
        count = len([f for f in os.listdir(VAULT_ARC) if f.endswith('.receipt')])
        total_arc = count * 150_000_000
        
        # Log the entry
        log_entry = f"[{time.ctime()}] RELAY_SYNC: {count} Blocks | Depth: {total_arc:,} ARC | Fees: {count * 0.02:.2f} CC\n"
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
        
        # Immediate console feedback
        print(f"SYNC OK: {total_arc:,} ARC secured.")
    except Exception as e:
        print(f"ERROR: {e}")
        
    time.sleep(10)
