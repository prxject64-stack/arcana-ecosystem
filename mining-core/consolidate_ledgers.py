import subprocess
import os
import csv

WORKERS_FILE = "workers.txt"
MASTER_CSV = "master_ledger.csv"

def get_remote_logs():
    all_data = []
    
    if not os.path.exists(WORKERS_FILE):
        print("Error: workers.txt not found.")
        return

    with open(WORKERS_FILE, "r") as f:
        workers = f.read().splitlines()

    for ip in workers:
        print(f"Pulling logs from {ip}...")
        # Securely grab the miner.log from each worker via SSH
        try:
            cmd = f"ssh -o StrictHostKeyChecking=no ubuntu@{ip} 'cat ~/arcana-ecosystem/mining-core/miner.log'"
            result = subprocess.check_output(cmd, shell=True).decode('utf-8')
            
            for line in result.splitlines():
                if "SUCCESS" in line:
                    # Parse the log line: [Timestamp] - SUCCESS - Mined X ARC | Fee: Y ARC
                    parts = line.split(" - ")
                    timestamp = parts[0].strip("[]")
                    stats = parts[2].split(" | ")
                    mined = stats[0].split("Mined ")[1].split(" ARC")[0]
                    fee = stats[1].split("Fee: ")[1].split(" ARC")[0]
                    all_data.append([timestamp, ip, mined, fee])
        except Exception as e:
            print(f"Failed to reach {ip}: {e}")

    # Write to Master CSV
    with open(MASTER_CSV, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Node_IP", "Net_ARC", "Infinite_Fee_0.5"])
        writer.writerows(all_data)
    
    print(f"Consolidation Complete. Master file saved: {MASTER_CSV}")

if __name__ == "__main__":
    get_remote_logs()
