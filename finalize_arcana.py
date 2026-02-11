import jwt, requests, time

def rpc(m, p):
    with open("/home/ubuntu/arcana_node/jwt.hex", "r") as f:
        secret = bytes.fromhex(f.read().strip())
    token = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    return requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":m,"params":p}, headers=headers).json()

# The hash the engine previously confirmed
BLOCK_HASH = "0x9a856480cc23991a16e254266ee9c537eb8da333f491212b5c9442bd37ed7f4a"

print(f"Forcing pivot to {BLOCK_HASH}...")
# We update the forkchoice and explicitly mark Block 1 as SAFE and FINALIZED
res = rpc("engine_forkchoiceUpdatedV3", [{
    "headBlockHash": BLOCK_HASH, 
    "safeBlockHash": BLOCK_HASH, 
    "finalizedBlockHash": BLOCK_HASH
}, None])

print(f"Result: {res}")
