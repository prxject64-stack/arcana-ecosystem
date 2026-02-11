import jwt, requests, time

JWT_SECRET_PATH = "./arcana_node/jwt.hex"
RPC_URL = "http://127.0.0.1:8551"
# Replace this with the Block 1 hash from your previous output if different
BLOCK_HASH = "0x484c8e3c9656c59318caed53d1687682c6babe081e37ad085d3d18ec79742b2f" 

with open(JWT_SECRET_PATH, "r") as f:
    secret = bytes.fromhex(f.read().strip())

def rpc(m, p):
    t = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
    return requests.post(RPC_URL, json={"jsonrpc":"2.0","id":1,"method":m,"params":p}, headers={"Authorization":f"Bearer {t}"}).json()

print(f"Forcing Finalization of {BLOCK_HASH}...")
# We set Head, Safe, and Finalized all to the same hash to leave no room for 'Syncing'
res = rpc("engine_forkchoiceUpdatedV3", [
    {"headBlockHash": BLOCK_HASH, "safeBlockHash": BLOCK_HASH, "finalizedBlockHash": BLOCK_HASH}, 
    None
])

print(f"Status: {res['result']['payloadStatus']['status']}")
if res['result']['payloadStatus']['status'] == 'VALID':
    print("SUCCESS: Ledger is moving.")
