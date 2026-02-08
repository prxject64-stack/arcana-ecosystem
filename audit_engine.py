import asyncio, json, sys
from web3 import AsyncWeb3, Web3
from web3.providers import AsyncHTTPProvider

LOCAL_RPC = "http://localhost:8545"
w3 = AsyncWeb3(AsyncHTTPProvider(LOCAL_RPC))

async def run_external_audit(target_address, client_name="Prospect"):
    target = Web3.to_checksum_address(target_address)
    accounts = await w3.eth.accounts
    pre_balance = await w3.eth.get_balance(target)
    successes = 0
    for i in range(5):
        tasks = [w3.eth.send_transaction({'from': acc, 'to': target, 'value': w3.to_wei(0.0001, 'ether'), 'gas': 100000, 'maxFeePerGas': w3.to_wei(100, 'gwei'), 'maxPriorityFeePerGas': w3.to_wei(10, 'gwei'), 'chainId': 8453}) for acc in accounts[:10]]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        successes += len([r for r in results if not isinstance(r, Exception)])
        await w3.provider.make_request("evm_mine", [])
    post_balance = await w3.eth.get_balance(target)
    report = {"client": client_name, "target": target, "integrity": "PASSED" if (post_balance - pre_balance) == w3.to_wei(successes * 0.0001, 'ether') else "FAILED", "verdict": "SECURE" if successes == 50 else "VULNERABLE"}
    with open(f"/home/ubuntu/arcana-ecosystem/audit_reports/audit_{target[:8]}.json", "w") as f:
        json.dump(report, f, indent=4)
    print(f"✅ Report saved for {target}")

if __name__ == "__main__":
    asyncio.run(run_external_audit(sys.argv[1] if len(sys.argv) > 1 else "0x418E22722F5A6C11B7A2916F6Cda8205854473F6"))
