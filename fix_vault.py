from eth_account import Account
import requests
import json

# HARDCODED - NO SHELL VARIABLES
priv = '43016dd610573795ce706b5a9a4f6ff0aaca60cb049b69de95c18612337e0d73'
god_addr = '0x3f1Eae7D46d88F08fc2F8ed27FCb2AB183EB2d0E'
vault = '0xDB2D15a3EB70C347E0D2C2c7861cAFb946baAb48'
rpc_url = 'http://localhost:8547'

acc = Account.from_key(priv)
print(f"Signing with: {acc.address}")

if acc.address.lower() != god_addr.lower():
    print(f"CRITICAL ERROR: Derived {acc.address} but need {god_addr}")
    exit(1)

tx = {
    'nonce': 27,
    'gasPrice': 100000000,
    'gas': 1000000,
    'to': vault,
    'value': 0,
    'data': '0x847fd5bf0000000000000000000000003f1eae7d46d88f08fc2f8ed27fcb2ab183eb2d0e',
    'chainId': 412346
}

signed = acc.sign_transaction(tx)
payload = {
    "jsonrpc": "2.0",
    "method": "eth_sendRawTransaction",
    "params": [signed.raw_transaction.hex()],
    "id": 1
}

resp = requests.post(rpc_url, json=payload)
print(f"Node Response: {resp.text}")
