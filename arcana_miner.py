import hashlib
import json
import time
import os
import multiprocessing as mp

LEDGER_PATH = os.path.expanduser("~/arcana-ecosystem/ledger.json")
VAULT_BASE = os.path.expanduser("~/arcana-ecosystem/vault")

def solve(target_prefix, prev_hash, start_nonce, step, result_queue):
    nonce = start_nonce
    timestamp = time.time()
    work_duration, sleep_duration = 0.003, 0.001 # 75% CPU load
    while True:
        cycle_start = time.time()
        while time.time() - cycle_start < work_duration:
            block_data = f"{prev_hash}{timestamp}{nonce}".encode()
            h = hashlib.sha256(block_data).hexdigest()
            if h.startswith(target_prefix):
                result_queue.put((h, nonce, timestamp))
                return
            nonce += step
        time.sleep(sleep_duration)

def mine_manager():
    with open(LEDGER_PATH, 'r') as f:
        ledger = json.load(f)
    
    difficulty = ledger.get('difficulty', 5)
    prev_hash = ledger.get('last_block_hash', '0'*64)
    result_queue = mp.Queue()
    cores = mp.cpu_count()
    
    processes = [mp.Process(target=solve, args=('0'*difficulty, prev_hash, i, cores, result_queue)) for i in range(cores)]
    for p in processes: p.start()
    h, nonce, timestamp = result_queue.get()
    for p in processes: p.terminate()

    # Fee Calculations
    gross = 50.0
    sauna_fee = gross * 0.025
    sec_fee = gross * 0.015
    net = gross - (sauna_fee + sec_fee)

    # Sovereign Vault Deposit (Physical Receipts)
    block_id = h[:12]
    with open(f"{VAULT_BASE}/sauna_protocol/block_{block_id}.receipt", "w") as f:
        f.write(f"TX: {h}\nFee: {sauna_fee} ARC\nStatus: Vaulted")
    with open(f"{VAULT_BASE}/security_system/block_{block_id}.receipt", "w") as f:
        f.write(f"TX: {h}\nFee: {sec_fee} ARC\nStatus: Vaulted")

    # Update Ledger
    ledger['balance'] = round(ledger.get('balance', 0) + net, 2)
    ledger['fees_paid'] = round(ledger.get('fees_paid', 0) + sauna_fee + sec_fee, 2)
    ledger['last_block_hash'] = h
    
    with open(LEDGER_PATH, 'w') as f:
        json.dump(ledger, f, indent=4)
    
    print(f"[!] BLOCK {block_id} VAULTED | Net: +{net} ARC")

if __name__ == "__main__":
    while True:
        mine_manager()
