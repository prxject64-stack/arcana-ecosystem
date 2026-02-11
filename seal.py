import jwt, requests, time

JWT_SECRET_PATH = "./arcana_node/jwt.hex"
ENGINE_RPC_URL = "http://127.0.0.1:8551"
BLOCK_HASH = "0xd5981791068a80f041c883b02e11258eaa0bddf705d9161e8c08d32c824dcb9b"

with open(JWT_SECRET_PATH, "r") as f:
    secret_bytes = bytes.fromhex(f.read().strip())

def send_rpc(method, params):
    token = jwt.encode({"iat": int(time.time())}, secret_bytes, algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    return requests.post(ENGINE_RPC_URL, json=payload, headers=headers).json()

# Force the Forkchoice to stick to the new hash
print(f"Forcing Finalization of {BLOCK_HASH}...")
final = send_rpc("engine_forkchoiceUpdatedV3", [
    {"headBlockHash": BLOCK_HASH, "safeBlockHash": BLOCK_HASH, "finalizedBlockHash": BLOCK_HASH},
    None
])
print(f"Final Status: {final['result']['payloadStatus']['status']}")
