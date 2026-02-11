import jwt, requests, time

def rpc(m, p):
    with open("/home/ubuntu/arcana_node/jwt.hex", "r") as f:
        secret = bytes.fromhex(f.read().strip())
    token = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"jsonrpc": "2.0", "id": 1, "method": m, "params": p}
    return requests.post("http://127.0.0.1:8551", json=payload, headers=headers).json()

# Genesis hash for dev chain
PARENT = "0x683713729fcb72be6f3d8b88c8cda3e10569d73b9640d3bf6f5184d94bd97616"

print("Step 1: Preparing Payload for Block 1...")
attr = {
    "timestamp": hex(int(time.time())), 
    "prevRandao": "0x" + "0"*64, 
    "suggestedFeeRecipient": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    "withdrawals": [],
    "parentBeaconBlockRoot": "0x" + "0"*64
}
res = rpc("engine_forkchoiceUpdatedV3", [{"headBlockHash": PARENT, "safeBlockHash": PARENT, "finalizedBlockHash": PARENT}, attr])

if "result" in res and res["result"]["payloadId"]:
    p_id = res["result"]["payloadId"]
    print(f"Step 2: Retrieving and Executing Payload {p_id}...")
    payload = rpc("engine_getPayloadV3", [p_id])["result"]["executionPayload"]
    b_hash = payload["blockHash"]
    
    rpc("engine_newPayloadV3", [payload, [], "0x" + "0"*64])
    rpc("engine_forkchoiceUpdatedV3", [{"headBlockHash": b_hash, "safeBlockHash": b_hash, "finalizedBlockHash": b_hash}, None])
    print(f"SUCCESS: Block 1 is Live. Hash: {b_hash}")
else:
    print(f"FAILED: {res}")
