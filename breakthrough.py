import jwt, requests, time

def rpc(m, p):
    with open("./arcana_node/jwt.hex", "r") as f:
        secret = bytes.fromhex(f.read().strip())
    token = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    return requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":m,"params":p}, headers=headers).json()

# The block that is currently "Syncing"
PARENT = "0x1a51269842f47413c0ca6db9e4ee2ae63e545bec8b4fd4f58c08201f6f916314"

print("Step 1: Forcing a New Payload on top of the Syncing Block...")
attr = {
    "timestamp": hex(int(time.time())), 
    "prevRandao": "0x" + "0"*64, 
    "suggestedFeeRecipient": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    "withdrawals": [],
    "parentBeaconBlockRoot": "0x" + "0"*64
}
r1 = rpc("engine_forkchoiceUpdatedV3", [{"headBlockHash": PARENT, "safeBlockHash": PARENT, "finalizedBlockHash": PARENT}, attr])

if "result" in r1 and r1["result"]["payloadId"]:
    p_id = r1["result"]["payloadId"]
    print(f"Step 2: Building Block 2 (ID: {p_id})...")
    payload = rpc("engine_getPayloadV3", [p_id])["result"]["executionPayload"]
    b_hash = payload["blockHash"]
    
    print(f"Step 3: Executing Block 2 ({b_hash})...")
    rpc("engine_newPayloadV3", [payload, [], "0x" + "0"*64])
    
    print("Step 4: Finalizing Chain at Block 2...")
    r2 = rpc("engine_forkchoiceUpdatedV3", [{"headBlockHash": b_hash, "safeBlockHash": b_hash, "finalizedBlockHash": b_hash}, None])
    print(f"FINAL STATUS: {r2['result']['payloadStatus']['status']}")
else:
    print(f"FAILED: {r1}")
