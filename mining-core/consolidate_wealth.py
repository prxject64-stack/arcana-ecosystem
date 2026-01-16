import pandas as pd
import os
import subprocess
from datetime import datetime

MASTER_CSV = "master_ledger.csv"
WORKERS_FILE = "workers.txt"

def get_remote_data(ip):
    # Command to pull the last mining entry from the worker
    cmd = f"ssh -o StrictHostKeyChecking=no ubuntu@{ip} 'tail -n 1 ~/arcana-ecosystem/mining-core/miner.log'"
    try:
        result = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        # Expecting format: Timestamp,Hashes,ARC_Minted
        return result.split(',')
    except:
        return None

def update_ledger():
    if not os.path.exists(WORKERS_FILE):
        print("[!] Error: workers.txt not found.")
        return

    with open(WORKERS_FILE, 'r') as f:
        workers = [line.strip() for line in f if line.strip()]

    new_entries = []
    for ip in workers:
        data = get_remote_data(ip)
        if data and len(data) == 3:
            new_entries.append({'IP': ip, 'Timestamp': data[0], 'Hashes': data[1], 'ARC': float(data[2])})
    
    if new_entries:
        df_new = pd.DataFrame(new_entries)
        if os.path.exists(MASTER_CSV):
            df_master = pd.read_csv(MASTER_CSV)
            df_master = pd.concat([df_master, df_new], ignore_index=True)
        else:
            df_master = df_new
        
        df_master.to_csv(MASTER_CSV, index=False)
        total_arc = df_master['ARC'].sum()
        print(f"[*] Ledger Updated. Total ARC Minted: {total_arc:,.2f}")

if __name__ == "__main__":
    update_ledger()
