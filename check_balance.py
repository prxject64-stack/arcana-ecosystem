import requests

# Your Architect Address
ADDRESS = "arcana_b8b59183c7cbd51eb577135fb48317888ee48282"
URL = "http://127.0.0.1:5000/chain"

def get_balance():
    try:
        response = requests.get(URL)
        chain = response.json()['chain']
        balance = 0
        
        for block in chain:
            for tx in block['transactions']:
                if tx['recipient'] == ADDRESS:
                    balance += tx['amount']
                if tx['sender'] == ADDRESS:
                    balance -= tx['amount']
        
        print("====================================================")
        print("           ARCANA SOVEREIGN LEDGER REPORT           ")
        print("====================================================")
        print(f"ADDRESS: {ADDRESS}")
        print(f"TOTAL BALANCE: {balance} Arcana")
        print("====================================================")
    except Exception as e:
        print(f"Error connecting to Node: {e}")

if __name__ == "__main__":
    get_balance()
