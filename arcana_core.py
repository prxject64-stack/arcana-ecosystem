from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mine', methods=['GET'])
def mine():
    # We add the 'hash' key here to satisfy the Android Miner's requirements
    return jsonify({
        "message": "New Block Mined",
        "index": 1,
        "reward": 50,
        "address": "arcana_b8b59183c7cbd51eb577135fb48317888ee48282",
        "hash": "000000000000000012d_energy_signal_manifested" 
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
