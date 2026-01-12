import hashlib
import json
from time import time
from flask import Flask, jsonify, request

class ArcanaBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        # Architect Wallet Address
        self.miner_address = "arcana_b8b59183c7cbd51eb577135fb48317888ee48282"
        self.new_block(previous_hash="0000000000000000", proof=100)

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
        return block

    def add_transaction(self, sender, recipient, amount, protocol, signature=None):
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'protocol': protocol,
            'signature': signature
        })
        return self.chain[-1]['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

app = Flask(__name__)
arcana = ArcanaBlockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount', 'protocol']
    if not all(k in values for k in required):
        return 'Missing values', 400
    index = arcana.add_transaction(values['sender'], values['recipient'], values['amount'], values['protocol'], values.get('signature'))
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify({'chain': arcana.chain, 'length': len(arcana.chain)}), 200

@app.route('/mine', methods=['GET'])
def mine_block():
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
