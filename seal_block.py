import jwt, requests, time
secret = bytes.fromhex(open("/home/ubuntu/arcana_node/jwt.hex").read().strip())
token = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
h = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
pid = "0x59824a7014fce017"
# 1. Get the payload
p = requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_getPayloadV3","params":[pid]}, headers=h).json()["result"]["executionPayload"]
# 2. Submit the payload
r1 = requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_newPayloadV3","params":[p, [], "0x"+"0"*64]}, headers=h).json()
bh = p["blockHash"]
# 3. Set as Canonical Head
r2 = requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_forkchoiceUpdatedV3","params":[{"headBlockHash": bh, "safeBlockHash": bh, "finalizedBlockHash": bh}, None]}, headers=h).json()
print(f"Block 1 Sealed: {bh}")
