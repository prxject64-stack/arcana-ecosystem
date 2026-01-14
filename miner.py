
import hashlib, time, json, os

from cryptography.fernet import Fernet



# CONFIGURATION

SECRET_KEY = b'ndPLwTx79HTmHY4XBZ9C44RzzFpM3CB8Zm4a_wgKgLk=' # Ensure you use your key from the last step

cipher = Fernet(SECRET_KEY)

L = "blockchain.enc"

BATCH_SIZE = 500  # Number of blocks to mine before writing to disk

TICK = 0.005      # 200 iterations per second potential



class ShadowBlockchain:

    def __init__(self):

        if os.path.exists(L):

            with open(L, "r") as f: self.chain = json.load(f)

        else:

            self.chain = []

            self.add_block(1, '0')



    def add_block(self, proof, prev_hash):

        # Generate and Encrypt instantly in RAM

        data = os.urandom(16).hex()

        enc_data = cipher.encrypt(data.encode()).decode()

        block = {

            'index': len(self.chain) + 1,

            'timestamp': time.time(),

            'proof': proof,

            'prev_hash': prev_hash,

            'data': enc_data

        }

        self.chain.append(block)



    def save(self):

        with open(L, "w") as f: json.dump(self.chain, f)



bc = ShadowBlockchain()

print("SHADOW VELOCITY: Maximum Private Throughput Active.")



while True:

    # High-Speed Batch Generation

    for _ in range(BATCH_SIZE):

        prev_hash = hashlib.sha256(json.dumps(bc.chain[-1], sort_keys=True).encode()).hexdigest()

        bc.add_block(proof=bc.chain[-1]['proof'] + 1, prev_hash=prev_hash)

        time.sleep(TICK) # 200/sec limit to prevent CPU Credit crash

    

    # Bulk write to disk

    bc.save()

    print(f">>> Private Wealth: {len(bc.chain) * 0.001:.3f} ARC | Blocks: {len(bc.chain)}")

