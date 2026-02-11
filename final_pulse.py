import jwt, requests, time

def rpc(m, p):
    try:
        with open("./arcana_node/jwt.hex", "r") as f:
            secret = bytes.fromhex(f.read().strip())
        t = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
        r = requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":m,"params":p}, headers={"Authorization":f"Bearer {t}"}).json()
        return r
    except Exception as e:
        return {"error": str(e)}

GEN = "0x683713729fcb72be6f3d8b88c8cda3e10569d73b9640d3bf6f5184d94bd97616"

print("Step 1: Requesting New Payload...")
attr = {
    "timestamp": hex(int(time.time())), 
    "prevRandao": "0x" + "0"*64, 
    "suggestedFeeRecipient": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    "withdrawals": [],
    "parentBeaconBlockRoot": "0x" + "0"*64
}
r1 = rpc("engine_forkchoiceUpdatedV3", [{"headBlockHash": GEN, "safeBlockHash": GEN, "finalizedBlockHash": GEN}, attr])

if "result" in r1:
    p_id = r1["result"]["payloadId"]
    print(f"Step 2: Retrieving Payload {p_id}...")
    payload = rpc("engine_getPayloadV3", [p_id])["result"]["executionPayload"]
    b_hash = payload["blockHash"]
    
    print(f"Step 3: Executing Block {b_hash}...")
    rpc("engine_newPayloadV3", [payload, [], "0x" + "0"*64])
    
    print("Step 4: Finalizing...")
    r2 = rpc("engine_forkchoiceUpdatedV3", [{"headBlockHash": b_hash, "safeBlockHash": b_hash, "finalizedBlockHash": b_hash}, None])
    print(f"FINAL STATUS: {r2['result']['payloadStatus']['status']}")
else:
    print(f"FAILED: {r1}")
