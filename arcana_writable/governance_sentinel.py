import os, time, hashlib

VAULT = "/home/ubuntu/arcana-ecosystem/vault/sauna_protocol/"
GOV_LOG = "/home/ubuntu/arcana-ecosystem/governance_ledger.log"

def sign_governance_block():
    # Proof of Stake (Wealth) + Proof of Space (Disk)
    files = [f for f in os.listdir(VAULT) if f.endswith('.receipt')]
    weight = sum(os.path.getsize(os.path.join(VAULT, f)) for f in files) / (1024**3)
    wealth = len(files) * 10000000
    
    with open(GOV_LOG, "a") as f:
        timestamp = time.ctime()
        # Create a governance signature based on current state
        sig = hashlib.sha256(f"{timestamp}{weight}{wealth}".encode()).hexdigest()[:16]
        f.write(f"[{timestamp}] GOV_VOTE: Active | Weight: {weight:.2f}GB | Wealth: {wealth:,} CC | SIG: {sig}\n")
    print(f"Governance Vote Cast: {sig}")

if __name__ == "__main__":
    while True:
        sign_governance_block()
        time.sleep(300) # Vote every 5 minutes
