import hashlib
import json
import os
from time import time
from flask import Flask, jsonify

class ArcanaBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.ledger_file = "ledger.json"
        self.miner_address = "arcana_b8b59183c7cbd51eb577135fb48317888ee48282"
        self.load_chain()

    def load_chain(self):
        try:
            if os.path.exists(self.ledger_file):
                with open(self.ledger_file, 'r') as f:
                    content = f.read()
                    self.chain = json.loads(content) if content else []
            
            if not self.chain:
                # Create Genesis Block if chain is empty
                self.new_block(previous_hash="0000000000000000", proof=100)
        except Exception:
            self.new_block(previous_hash="0000000000000000", proof=100)

    def save_chain(self):
        with open(self.ledger_file, 'w') as f:
            json.dump(self.chain, f, indent=4)

    def new_block(self, proof, previous_hash=None):
        reward_tx = {
            'sender': "0",
            'recipient': self.miner_address,
            'amount': 50,
            'protocol': 'ARCANA_MINING_REWARD'
        }
        self.pending_transactions.append(reward_tx)
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        self.save_chain()
        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

app = Flask(__name__)
arcana = ArcanaBlockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify({'chain': arcana.chain, 'length': len(arcana.chain)}), 200

@app.route('/mine', methods=['GET'])
def mine_block():
    if not arcana.chain:
        return jsonify({'error': 'Chain not initialized'}), 500
    last_block = arcana.chain[-1]
    proof = last_block['proof'] + 1
    block = arcana.new_block(proof)
    return jsonify({
        'message': "New Block Mined",
        'index': block['index'],
        'transactions': block['transactions'],
        'hash': arcana.hash(block)
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
