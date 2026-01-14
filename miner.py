import time, json, os
LEDGER_FILE = "ledger"
ITERATION_RATE = 1
def check_balance():
    try:
        if not os.path.exists(LEDGER_FILE): return 0.0
        with open(LEDGER_FILE, "r") as f:
            lines = sum(1 for line in f)
            return lines / 1000.0
    except: return 0.0
print("ARCANA AWS: 1s High-Speed Active.")
while True:
    entry = {"ts": time.time(), "id": os.urandom(8).hex()}
    with open(LEDGER_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    try:
        with open(LEDGER_FILE, "r") as f:
            current_lines = sum(1 for line in f)
        if current_lines % 10 == 0:
            print(f">>> Total Balance: {current_lines / 1000.0} ARC")
    except: pass
    time.sleep(ITERATION_RATE)
