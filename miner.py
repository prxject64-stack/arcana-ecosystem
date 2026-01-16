import os, uuid, time, sys

VAULT_ARC = os.path.expanduser("~/arcana-ecosystem/vault/security_system")
VAULT_CC = os.path.expanduser("~/arcana-ecosystem/vault/sauna_protocol")
os.makedirs(VAULT_ARC, exist_ok=True)
os.makedirs(VAULT_CC, exist_ok=True)

# THE 10M OVERRIDE
CC_REWARD = 10_000_000 
ARC_REWARD = 150_000_000

print(f"MASTER MINT ACTIVE: REWARD = {CC_REWARD:,} CC PER BLOCK")

def master_mint():
    while True:
        block_id = uuid.uuid4().hex[:12]
        
        # 1. Mint 150M ARC
        with open(f"{VAULT_ARC}/arc_{block_id}.receipt", 'w') as f:
            f.write(f"PROVER_SIG: {block_id}\nVALUE: {ARC_REWARD}")
            f.flush(); os.fsync(f.fileno())
            
        # 2. Mint 10M CC
        with open(f"{VAULT_CC}/cc_{block_id}.receipt", 'w') as f:
            f.write(f"SAUNA_SIG: {block_id}\nVALUE: {CC_REWARD}")
            f.flush(); os.fsync(f.fileno())

        arc_c = len(os.listdir(VAULT_ARC))
        cc_c = len(os.listdir(VAULT_CC))
        
        sys.stdout.write(f"\r[MASTER-MINT] ARC: {arc_c * ARC_REWARD:,} | CC: {cc_c * CC_REWARD:,}")
        sys.stdout.flush()
        
        time.sleep(1) # Slowed to 1s to prevent disk flood with high-value files

if __name__ == '__main__':
    master_mint()
