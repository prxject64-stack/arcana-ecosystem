import jwt, requests, time
secret = bytes.fromhex(open("/home/ubuntu/arcana_node/jwt.hex").read().strip())
token = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
h = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
bh = "0xeb85223ad5bade0c87f69eafd2978a68a5dadd41e3cef04b6226e77b16cc4511"
# Force transition config
requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_exchangeTransitionConfigurationV1","params":[{"terminalTotalDifficulty":"0x0","terminalBlockHash":"0x0000000000000000000000000000000000000000000000000000000000000000","terminalBlockNumber":"0x0"}]}, headers=h)
# Force forkchoice head
r = requests.post("http://127.0.0.1:8551", json={"jsonrpc":"2.0","id":1,"method":"engine_forkchoiceUpdatedV3","params":[{"headBlockHash": bh, "safeBlockHash": bh, "finalizedBlockHash": bh}, None]}, headers=h).json()
print(f"PIPELINE KICK RESULT: {r}")
