import prover_engine
import time

target = "arcana_test_prefix"
start = 0
end = 10_000_000

print(f"Testing engine with {end} iterations...")
start_time = time.time()
result = prover_engine.find_arcana_nonce(target, start, end)
duration = time.time() - start_time

if result:
    print(f"SUCCESS! Found nonce: {result}")
else:
    print("No nonce found in range, but engine executed correctly.")

print(f"Time taken: {duration:.4f} seconds")
print(f"Estimated Hashrate: {end/duration:,.0f} H/s")
