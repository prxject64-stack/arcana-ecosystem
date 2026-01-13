import json
import os
from flask import Flask, jsonify

app = Flask(__name__)
LEDGER_FILE = "ledger.json"

# Function to load the ledger from disk
def load_ledger():
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, 'r') as f:
            return json.load(f)
    return {"arcana_b8b59183c7cbd51eb577135fb48317888ee48282": 1000}

# Function to save the ledger to disk
def save_ledger(data):
    with open(LEDGER_FILE, 'w') as f:
        json.dump(data, f)

ledger = load_ledger()

@app.route('/mine', methods=['GET'])
def mine():
    addr = "arcana_b8b59183c7cbd51eb577135fb48317888ee48282"
    ledger[addr] = ledger.get(addr, 0) + 50
    save_ledger(ledger) # PERSISTENCE
    return jsonify({
        "message": "Block Mined!",
        "new_balance": ledger[addr],
        "hash": "0000_immortal_persistence_signal"
    }), 200

@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    current_ledger = load_ledger()
    balance = current_ledger.get(address, 0)
    return jsonify({"address": address, "balance": balance, "currency": "Arcana"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
