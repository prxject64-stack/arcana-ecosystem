import hashlib
import json
from time import time
from flask import Flask, jsonify

class ArcanaBlockchain:
    def __init__(self):
        self.chain = []
        self.new_block(previous_hash="0000000000000000", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'contracts': ['Security_v1', 'Sauna_v1', 'Miner_v1']
        }
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Initialize Flask App
app = Flask(__name__)
arcana = ArcanaBlockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    response = {
        'chain': arcana.chain,
        'length': len(arcana.chain),
        'status': '12D_SOVEREIGN_ACTIVE'
    }
    return jsonify(response), 200

@app.route('/mine', methods=['GET'])
def mine_block():
    last_block = arcana.chain[-1]
    proof = last_block['proof'] + 1
    block = arcana.new_block(proof)
    return jsonify(block), 200

if __name__ == '__main__':
    print("Arcana Explorer Live at http://127.0.0.1:5000/chain")
    app.run(host='0.0.0.0', port=5000)
