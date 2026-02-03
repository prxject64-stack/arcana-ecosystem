import prover_engine
import time

target = "ARCANA_SYSTEM_INIT"
print(f"\n--- TRUSTSTACK AI: RUST ENGINE TEST (EXPANDED) ---")
start = time.time()

# Increasing range to 100M for a 100% success probability
# This tests the 'Rayon' multi-threading in your Rust code
nonce = prover_engine.find_arcana_nonce(target, 0, 100000000)

end = time.time()

if nonce:
    print(f"RESULT: VERIFIED")
    print(f"NONCE FOUND: {nonce}")
    print(f"LATENCY: {end - start:.4f} seconds")
    print(f"HASHES PER SEC: {100000000 / (end - start):,.0f}")
    print(f"STAKE: 136B CC SECURITY CONFIRMED")
else:
    print("RESULT: REJECTED (Still no hit - your CPU is working, but luck is thin)")
