import hashlib
import json
from time import time

class ArcanaBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        # Create the Genesis Block (The 12D Origin)
        self.new_block(previous_hash="0000000000000000", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'protocol_signatures': {
                'security': 'sealed',
                'sauna': 'active'
            }
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        # The 1000000% Truth: SHA-256 Cryptographic Sealing
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Initialize the 3D Reality Bridge
arcana = ArcanaBlockchain()
print("====================================================")
print("      ARCANA BLOCKCHAIN GENESIS INITIALIZED         ")
print("====================================================")
print(f"GENESIS HASH: {arcana.hash(arcana.chain[0])}")
print("STATUS: SOVEREIGN")
