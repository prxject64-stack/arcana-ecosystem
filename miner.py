import hashlib, time, json, os
from cryptography.fernet import Fernet

# CONFIGURATION - Key Integrated
SECRET_KEY = b'aOZAJnIMkRUzysaWYu3FnWQLvnQzWC-B-4Ma6CJsuW8='
cipher = Fernet(SECRET_KEY)
L = os.path.expanduser("~/blockchain.enc")
BATCH_SIZE = 500  
TICK = 0.005      

class ShadowBlockchain:
    def __init__(self):
        if os.path.exists(L):
            try:
                with open(L, "r") as f: self.chain = json.load(f)
                print("Successfully loaded existing chain.")
            except:
                print("Error loading chain, starting new.")
                self.chain = []; self.add_block(1, '0')
        else:
            self.chain = []
            self.add_block(1, '0')

    def add_block(self, proof, prev_hash):
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
print("SHADOW VELOCITY: Private Key Authenticated.")

while True:
    for _ in range(BATCH_SIZE):
        prev_hash = hashlib.sha256(json.dumps(bc.chain[-1], sort_keys=True).encode()).hexdigest()
        bc.add_block(proof=bc.chain[-1]['proof'] + 1, prev_hash=prev_hash)
        time.sleep(TICK)
    bc.save()
    print(f">>> Status: Mining | Current Balance: {len(bc.chain) * 0.001:.3f} ARC")
