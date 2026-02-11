import jwt, requests, time
secret = bytes.fromhex(open("/home/ubuntu/arcana_node/jwt.hex").read().strip())
token = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
h = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
# Genesis Hash
b = "0x683713729fcb72be6f3d8b88c8cda3e10569d73b9640d3bf6f5184d94bd97616"
attr = {"timestamp": hex(int(time.time())), "prevRandao": "0x"+"0"*64, "suggestedFeeRecipient": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266", "withdrawals": [], "parentBeaconBlockRoot": "0x"+"0"*64}
# 1. Start Payload
r1 = requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_forkchoiceUpdatedV3","params":[{"headBlockHash": b, "safeBlockHash": b, "finalizedBlockHash": b}, attr]}, headers=h).json()
pid = r1["result"]["payloadId"]
# 2. Get Payload
p = requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_getPayloadV3","params":[pid]}, headers=h).json()["result"]["executionPayload"]
# 3. Submit Payload
requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_newPayloadV3","params":[p, [], "0x"+"0"*64]}, headers=h)
bh = p["blockHash"]
# 4. Finalize
requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_forkchoiceUpdatedV3","params":[{"headBlockHash": bh, "safeBlockHash": bh, "finalizedBlockHash": bh}, None]}, headers=h)
print(f"Arcana Block 1 Atomic Seal Success: {bh}")
