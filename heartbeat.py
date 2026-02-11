import jwt, requests, time

JWT_SECRET_PATH = "./arcana_node/jwt.hex"
ENGINE_RPC_URL = "http://127.0.0.1:8551"
GENESIS_HASH = "0x683713729fcb72be6f3d8b88c8cda3e10569d73b9640d3bf6f5184d94bd97616"

with open(JWT_SECRET_PATH, "r") as f:
    secret_bytes = bytes.fromhex(f.read().strip())

def send_rpc(method, params):
    token = jwt.encode({"iat": int(time.time())}, secret_bytes, algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    return requests.post(ENGINE_RPC_URL, json=payload, headers=headers).json()

# 1. Prepare (fresh ID)
print("Preparing Payload...")
prep = send_rpc("engine_forkchoiceUpdatedV3", [
    {"headBlockHash": GENESIS_HASH, "safeBlockHash": GENESIS_HASH, "finalizedBlockHash": GENESIS_HASH},
    {"timestamp": hex(int(time.time())), "prevRandao": "0x"+"0"*64, "suggestedFeeRecipient": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266", "withdrawals": [], "parentBeaconBlockRoot": "0x"+"0"*64}
])
p_id = prep['result']['payloadId']

# 2. Get & Submit
print(f"Executing Payload {p_id}...")
exec_payload = send_rpc("engine_getPayloadV3", [p_id])['result']['executionPayload']
new_payload = send_rpc("engine_newPayloadV3", [exec_payload, [], "0x"+"0"*64])

# 3. Finalize
new_hash = exec_payload['blockHash']
final = send_rpc("engine_forkchoiceUpdatedV3", [
    {"headBlockHash": new_hash, "safeBlockHash": new_hash, "finalizedBlockHash": new_hash},
    None
])

print(f"Status: {final['result']['payloadStatus']['status']} | Block Hash: {new_hash}")
