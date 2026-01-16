import prover_engine
import time
import sys

TARGET_PREFIX = "arcana_"
BATCH_SIZE = 50_000_000 

print(f"--- Arcana Industrial Prover: CONTINUOUS MODE ---")

try:
    total_hashes = 0
    while True:
        batch_start = time.time()
        result = prover_engine.find_arcana_nonce(TARGET_PREFIX, total_hashes, total_hashes + BATCH_SIZE)
        duration = time.time() - batch_start
        total_hashes += BATCH_SIZE
        
        print(f"Batch Complete | {BATCH_SIZE/duration/1_000_000:.2f} MH/s | Total: {total_hashes:,}")

        if result:
            print(f"\n[!!!] NONCE FOUND: {result}")
            # Log the win to a file
            with open("found_nonces.txt", "a") as f:
                f.write(f"Nonce: {result} | Total Hashes: {total_hashes}\n")
            # We removed the 'break' here to keep mining
            
except KeyboardInterrupt:
    print("\nManual shutdown.")
    sys.exit(0)
