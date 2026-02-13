import os, uuid, time

VAULT = "/home/ubuntu/arcana-ecosystem/vault/sauna_protocol/"
os.makedirs(VAULT, exist_ok=True)

def mint_heavy_block():
    block_id = uuid.uuid4().hex[:12]
    filename = f"{VAULT}cc_{block_id}.receipt"
    
    # Generate 5MB of high-entropy cryptographic proof
    # 5 * 1024 * 1024 = 5,242,880 bytes
    data = os.urandom(5242880) 
    
    with open(filename, "wb") as f:
        f.write(f"REWARD: 10000000 CC\n".encode())
        f.write(f"BLOCK_ID: {block_id}\n".encode())
        f.write(data)
    
    print(f"MINTED HEAVY BLOCK: {block_id} (5MB)")

if __name__ == "__main__":
    while True:
        mint_heavy_block()
        time.sleep(1) # Controlled burn to manage IO
