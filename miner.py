
import time, json, os

LEDGER_FILE = "ledger"

print("ARCANA AWS: Generation Active...")

while True:

    entry = {"ts": time.time(), "id": os.urandom(8).hex()}

    with open(LEDGER_FILE, "a") as f:

        f.write(json.dumps(entry) + "\n")

    time.sleep(10)

