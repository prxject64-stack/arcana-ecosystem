import time, json, os
L="ledger"
BATCH_SIZE = 200 
R = 0.05 # 20 units per second

print("ARCANA AWS: Velocity Build Active.")
while True:
    batch = []
    # Generate the batch in memory to save CPU credits
    for _ in range(BATCH_SIZE):
        batch.append(json.dumps({"ts":time.time(),"id":os.urandom(8).hex()}) + "\n")
        time.sleep(R)
    
    # Write the batch in one single disk operation
    try:
        with open(L, "a") as f:
            f.writelines(batch)
        
        # Balance Check: Scans the file to confirm actual disk state
        with open(L, "r") as f:
            c = sum(1 for _ in f)
        print(f">>> Velocity Balance: {c/1000.0} ARC")
    except Exception as e:
        print(f"Error: {e}")
