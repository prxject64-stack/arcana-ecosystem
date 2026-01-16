import prover_engine
import time
import sys

TARGET_PREFIX = "arcana_"
BATCH_SIZE = 25_000_000  # Lowered slightly to ensure stability on small RAM

print(f"--- Arcana Industrial Prover Starting ---")
print(f"Targeting: {TARGET_PREFIX}")

try:
    total_hashes = 0
    while True:
        batch_start = time.time()
        # The engine we built earlier
        result = prover_engine.find_arcana_nonce(TARGET_PREFIX, total_hashes, total_hashes + BATCH_SIZE)
        
        duration = time.time() - batch_start
        total_hashes += BATCH_SIZE
        
        hashrate = BATCH_SIZE / duration
        print(f"Batch Complete | {hashrate/1_000_000:.2f} MH/s | Total: {total_hashes:,}")

        if result:
            print(f"\n[!!!] NONCE FOUND: {result}")
            # Optional: Submit to network here
            break

except KeyboardInterrupt:
    print("\nManual shutdown initiated.")
    sys.exit(0)
