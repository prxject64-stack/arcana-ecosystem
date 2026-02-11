import jwt, requests, time

JWT_SECRET_PATH = "./arcana_node/jwt.hex"
RPC_URL = "http://127.0.0.1:8551"
GEN_HASH = "0x683713729fcb72be6f3d8b88c8cda3e10569d73b9640d3bf6f5184d94bd97616"

with open(JWT_SECRET_PATH, "r") as f:
    secret = bytes.fromhex(f.read().strip())

def rpc(m, p):
    t = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
    return requests.post(RPC_URL, json={"jsonrpc":"2.0","id":1,"method":m,"params":p}, headers={"Authorization":f"Bearer {t}"}).json()

# 1. Request a NEW payload ID
print("Generating fresh Payload ID...")
attr = {
    "timestamp": hex(int(time.time())), 
    "prevRandao": "0x" + "0"*64, 
    "suggestedFeeRecipient": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    "withdrawals": [],
    "parentBeaconBlockRoot": "0x" + "0"*64
}
fc_init = {"headBlockHash": GEN_HASH, "safeBlockHash": GEN_HASH, "finalizedBlockHash": GEN_HASH}
res1 = rpc("engine_forkchoiceUpdatedV3", [fc_init, attr])
p_id = res1['result']['payloadId']

# 2. Grab the Execution Data
print(f"Retrieving Payload: {p_id}")
payload = rpc("engine_getPayloadV3", [p_id])['result']['executionPayload']
b_hash = payload['blockHash']

# 3. Feed the Payload back to the Engine
print(f"Executing Block: {b_hash}")
rpc("engine_newPayloadV3", [payload, [], "0x" + "0"*64])

# 4. Force the Forkchoice to the new Block
print("Sealing Canonical Head...")
res2 = rpc("engine_forkchoiceUpdatedV3", [{"headBlockHash": b_hash, "safeBlockHash": b_hash, "finalizedBlockHash": b_hash}, None])
print(f"FINAL STATUS: {res2['result']['payloadStatus']['status']} | BLOCK HASH: {b_hash}")
