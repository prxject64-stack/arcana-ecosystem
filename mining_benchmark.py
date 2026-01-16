import time
import hashlib
import prover_engine  # Your new Rust module
import statistics

def python_mining_logic(iterations=100000):
    """Pure Python mining simulation"""
    nonce = 0
    target_prefix = "0000"
    start = time.perf_counter()
    for _ in range(iterations):
        content = f"block_data_{nonce}"
        hash_result = hashlib.sha256(content.encode()).hexdigest()
        nonce += 1
    return time.perf_counter() - start

def rust_mining_logic(iterations=100000):
    """Rust-powered mining simulation"""
    # We call our compiled Rust function
    # Note: Our Rust function actually searches for a nonce, 
    # so we give it a difficult target to force it to work.
    start = time.perf_counter()
    # Difficulty 5 forces about 1M+ hashes usually
    prover_engine.find_arcana_nonce(1, "benchmark_data", "prev_hash", 5)
    return time.perf_counter() - start

if __name__ == "__main__":
    print("🚀 ARCANA PERFORMANCE BENCHMARK (2026)")
    print("-" * 40)
    
    # Test 1: Raw Python Hash Speed
    py_time = python_mining_logic(500000)
    print(f"[*] Python (500k hashes): {py_time:.4f} seconds")
    
    # Test 2: Rust Nonce Search
    # We time the Rust engine finding a block
    rust_start = time.perf_counter()
    hash_result, nonce = prover_engine.find_arcana_nonce(1, "tx_data", "0000", 5)
    rust_time = time.perf_counter() - rust_start
    
    print(f"[✔] Rust Found Block in:  {rust_time:.4f} seconds")
    print(f"[*] Nonces Checked:       {nonce:,}")
    
    hashes_per_sec = nonce / rust_time
    print(f"[*] Rust Hashrate:        {hashes_per_sec:,.0f} H/s")
    print("-" * 40)
    print(f"STRATEGY: Use Rust for loops, Python for the UI.")
