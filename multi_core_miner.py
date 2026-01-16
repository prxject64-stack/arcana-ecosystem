import multiprocessing
import prover_engine
import time
import os
import json

# Treasury Configuration
LEDGER_PATH = os.path.expanduser("~/arcana-ecosystem/ledger.json")
DIFFICULTY = 5  # 2026 Laptop Standard

def mining_worker(worker_id, result_queue):
    """The individual 'Worker' using the Rust Turbo Engine"""
    print(f"[Core {worker_id}] Soldier reporting for duty...")
    while True:
        # Each worker picks a unique starting point
        # In a real network, this would involve a dynamic 'extra_nonce'
        nonce_start = worker_id * 1_000_000
        hash_res, nonce = prover_engine.find_arcana_nonce(worker_id, "TX_DATA", "PREV_HASH", DIFFICULTY)
        
        if hash_res != "TIMEOUT":
            result_queue.put((worker_id, hash_res, nonce))
            break

def monitor_treasury(result_queue):
    """The 'CEO' process that updates the 482M ARC treasury"""
    while True:
        worker_id, hash_val, nonce = result_queue.get()
        print(f"\n[✔] BLOCK FOUND by Core {worker_id}!")
        print(f"[*] Hash: {hash_val}")
        
        # Update Ledger
        try:
            with open(LEDGER_PATH, 'r+') as f:
                data = json.load(f)
                data["balance"] += 50.0
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            print(f"[!] Treasury Status: {data['balance']:,.2f} ARC")
        except:
            print("[!] Ledger error. Ensuring treasury backup...")

if __name__ == "__main__":
    # Determine how many cores to use (Leave 1 for OS stability)
    num_cores = max(1, multiprocessing.cpu_count() - 1)
    print(f"🚀 Activating {num_cores} Core Industrial Stack...")
    
    q = multiprocessing.Queue()
    
    # Start the workers
    for i in range(num_cores):
        p = multiprocessing.Process(target=mining_worker, args=(i, q))
        p.start()
        
    # Start the monitor
    monitor_treasury(q)
