import requests
import jwt
import time
import json
import sys
import re

# Configuration
JWT_PATH = "/home/ubuntu/arcana_node/jwt.hex"
ENGINE_URL = "http://127.0.0.1:8551"

# Load JWT
try:
    with open(JWT_PATH, "r") as f:
        secret_hex = f.read().strip()
    secret = bytes.fromhex(secret_hex)
    token = jwt.encode({"iat": int(time.time())}, secret, algorithm="HS256")
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
except Exception as e:
    print(f"FATAL: Could not load JWT: {e}")
    sys.exit(1)

def rpc_call(method, params):
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    try:
        response = requests.post(ENGINE_URL, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        print(f"RPC ERROR {method}: {e}")
        return None

print(">>> STARTING HASH-PATCH SEQUENCE <<<")

# 1. Trigger Build
print("[1] Triggering new block build (Time - 5s)...")
genesis_hash = "0x683713729fcb72be6f3d8b88c8cda3e10569d73b9640d3bf6f5184d94bd97616"
timestamp = hex(int(time.time()) - 5)

fc_params = [
    {
        "headBlockHash": genesis_hash,
        "safeBlockHash": genesis_hash,
        "finalizedBlockHash": genesis_hash
    },
    {
        "timestamp": timestamp,
        "prevRandao": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "suggestedFeeRecipient": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
        "withdrawals": [],
        "parentBeaconBlockRoot": "0x0000000000000000000000000000000000000000000000000000000000000000"
    }
]

r1 = rpc_call("engine_forkchoiceUpdatedV3", fc_params)
if "error" in r1:
    print(f"FATAL ERROR in Step 1: {r1['error']}")
    sys.exit(1)

payload_id = r1["result"]["payloadId"]
print(f"    SUCCESS! New Payload ID: {payload_id}")

# 2. Fetch Payload
print(f"[2] Fetching payload execution data...")
r2 = rpc_call("engine_getPayloadV3", [payload_id])
execution_payload = r2["result"]["executionPayload"]
original_hash = execution_payload["blockHash"]
print(f"    Got Payload. Original Hash: {original_hash}")

# 3. Submit (First Attempt)
print("[3] Submitting payload (Attempt 1)...")
beacon_root = execution_payload.get("parentBeaconBlockRoot", "0x0000000000000000000000000000000000000000000000000000000000000000")

r3 = rpc_call("engine_newPayloadV3", [execution_payload, [], beacon_root])
status_data = r3.get("result", {})
error_data = r3.get("error", {})

# 4. Handle "Hash Mismatch" Loop
if "message" in error_data and "block hash mismatch" in error_data["message"]:
    print(f"    MISMATCH DETECTED: {error_data['message']}")
    
    # Extract the hash the node *wants* (the one it calculated)
    # Looking for: "got 0x[hex]..."
    match = re.search(r"got (0x[a-fA-F0-9]{64})", error_data["message"])
    if match:
        calculated_hash = match.group(1)
        print(f"    PATCHING: Replacing {original_hash} with calculated hash {calculated_hash}")
        
        # Patch the payload
        execution_payload["blockHash"] = calculated_hash
        
        # Retry Submit
        print("[3b] Resubmitting Patched Payload...")
        r3_retry = rpc_call("engine_newPayloadV3", [execution_payload, [], beacon_root])
        
        if "result" in r3_retry:
            print(f"    RETRY STATUS: {r3_retry['result']['status']}")
            if r3_retry['result']['status'] == "VALID":
                # Update the hash variable for Step 4
                original_hash = calculated_hash 
                status_data = r3_retry['result']
            else:
                print("FATAL: Retry failed.")
                sys.exit(1)
        else:
             print(f"FATAL: Retry Error: {r3_retry}")
             sys.exit(1)
    else:
        print("FATAL: Could not extract calculated hash from error message.")
        sys.exit(1)
elif "result" in r3 and r3["result"]["status"] == "INVALID":
    # Sometimes it returns INVALID status instead of RPC error
    print(f"    INVALID STATUS: {r3['result']}")
    validation_err = r3['result'].get('validationError', '')
    if "block hash mismatch" in validation_err:
        match = re.search(r"got (0x[a-fA-F0-9]{64})", validation_err)
        if match:
            calculated_hash = match.group(1)
            print(f"    PATCHING via Validation Error: {calculated_hash}")
            execution_payload["blockHash"] = calculated_hash
            r3_retry = rpc_call("engine_newPayloadV3", [execution_payload, [], beacon_root])
            print(f"    RETRY STATUS: {r3_retry['result']['status']}")
            original_hash = calculated_hash

# 5. Finalize
print(f"[4] Finalizing Block {original_hash}...")
r4 = rpc_call("engine_forkchoiceUpdatedV3", [
    {
        "headBlockHash": original_hash,
        "safeBlockHash": original_hash,
        "finalizedBlockHash": original_hash
    },
    None
])

print(">>> SEQUENCE COMPLETE <<<")
print("Check height with: cast block-number --rpc-url http://127.0.0.1:8545")
