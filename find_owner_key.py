import re
import os
from eth_account import Account

target_address = "0x7bfbfcaceda78a54fa0c6cad236ab5a6c11b7a29".lower()
hex_pattern = re.compile(r'[a-fA-F0-9]{64}')

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith((".env", ".txt", ".json", ".toml", ".sh", ".log")):
            path = os.path.join(root, file)
            with open(path, 'r', errors='ignore') as f:
                content = f.read()
                matches = hex_pattern.findall(content)
                for m in matches:
                    try:
                        if Account.from_key(m).address.lower() == target_address:
                            print(f"\n[!!!] OWNER KEY FOUND [!!!]")
                            print(f"File: {path}")
                            print(f"Key: {m}")
                            exit(0)
                    except: continue
print("Owner key not found in files.")
