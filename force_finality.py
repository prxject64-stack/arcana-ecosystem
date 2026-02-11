import jwt, requests, time

def rpc(m, p):
    with open("./arcana_node/jwt.hex", "r") as f:
        secret = bytes.fromhex(f.read().strip())
    token = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"jsonrpc": "2.0", "id": 1, "method": m, "params": p}
    return requests.post("http://127.0.0.1:8551", json=payload, headers=headers).json()

target = "0x1a51269842f47413c0ca6db9e4ee2ae63e545bec8b4fd4f58c08201f6f916314"
print(f"Pushing pointers to {target}...")

# Force Head, Safe, and Finalized to the same block
res = rpc("engine_forkchoiceUpdatedV3", [{"headBlockHash": target, "safeBlockHash": target, "finalizedBlockHash": target}, None])

if "result" in res:
    status = res["result"]["payloadStatus"]["status"]
    print(f"FORCED STATUS: {status}")
else:
    print(f"ERROR: {res}")
