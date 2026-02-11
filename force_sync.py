import jwt, requests, time

JWT_SECRET_PATH = "./arcana_node/jwt.hex"
RPC_URL = "http://127.0.0.1:8551"
BLOCK_HASH = "0x132409cd7fc54873a87e2fb5e1b764ee4ed8e71f021262ebe1a4c6f645b8f4c3"

with open(JWT_SECRET_PATH, "r") as f:
    secret = bytes.fromhex(f.read().strip())

def rpc(m, p):
    t = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
    return requests.post(RPC_URL, json={"jsonrpc":"2.0","id":1,"method":m,"params":p}, headers={"Authorization":f"Bearer {t}"}).json()

print(f"Forcing Finalization of {BLOCK_HASH}...")
# Setting all pointers to Block 1 to break the SYNCING loop
res = rpc("engine_forkchoiceUpdatedV3", [
    {"headBlockHash": BLOCK_HASH, "safeBlockHash": BLOCK_HASH, "finalizedBlockHash": BLOCK_HASH},
    None
])

print(f"Final Status: {res['result']['payloadStatus']['status']}")
