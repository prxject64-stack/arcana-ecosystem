import asyncio
import time
from web3 import AsyncWeb3, Web3, AsyncIPCProvider
from eth_account import Account

# Connection to the Arcana Sovereign Node
w3 = AsyncWeb3(AsyncIPCProvider('./data/geth.ipc'))
sync_w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

PRIV_KEY = "0xfdfcd399e13c4f7e1612fd5e655159f899a4951ecf21d153a6adef68474271d2"
SENDER = sync_w3.to_checksum_address("0x14a3256052c02f9d87fe1cc3b712d4530061b25c")
RECIPIENT = sync_w3.to_checksum_address("0x179119B999F69006096333604931083916960E01")

# Limit concurrent requests to prevent ProviderConnectionError
SEM = asyncio.Semaphore(100)

async def send_tx(tx_hex):
    async with SEM:
        return await w3.eth.send_raw_transaction(tx_hex)

async def main():
    try:
        nonce = sync_w3.eth.get_transaction_count(SENDER)
        gas_price = sync_w3.eth.gas_price
    except Exception as e:
        print(f"Node Error: {e}")
        return

    print(f"Pre-signing 4,500 swaps for 136B CC-P liquidity...")
    signed_txs = []
    for i in range(4500):
        tx = {
            'nonce': nonce + i,
            'to': RECIPIENT,
            'value': sync_w3.to_wei(0.0001, 'ether'),
            'gas': 21000,
            'gasPrice': gas_price,
            'chainId': 1337
        }
        signed = Account.sign_transaction(tx, PRIV_KEY)
        signed_txs.append(signed.raw_transaction.hex())

    print("Launching Balanced Async Blast...")
    start_time = time.perf_counter()
    
    tasks = [send_tx(tx) for tx in signed_txs]
    await asyncio.gather(*tasks)
    
    end_time = time.perf_counter()
    latency = (end_time - start_time) * 1000
    print(f"Submission Latency: {latency:.2f}ms")

if __name__ == "__main__":
    asyncio.run(main())
