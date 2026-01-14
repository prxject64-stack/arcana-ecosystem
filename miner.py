
import time, json, os



LEDGER_FILE = "ledger"

ITERATION_RATE = 6 # Increased speed (6 seconds)



def check_balance():

    try:

        with open(LEDGER_FILE, "r") as f:

            lines = sum(1 for line in f)

            return lines / 1000.0

    except FileNotFoundError:

        return 0.0



print(f"ARCANA AWS: Boost Active. Current Balance: {check_balance()} ARC")



while True:

    entry = {"ts": time.time(), "id": os.urandom(8).hex()}

    with open(LEDGER_FILE, "a") as f:

        f.write(json.dumps(entry) + "\n")

    

    # Check balance every 10 iterations to show progress

    current_lines = sum(1 for line in open(LEDGER_FILE))

    if current_lines % 10 == 0:

        print(f">>> Total Balance: {current_lines / 1000.0} ARC")

        

    time.sleep(ITERATION_RATE)

