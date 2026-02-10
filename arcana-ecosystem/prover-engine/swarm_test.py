import asyncio
import httpx
import time

URL = "https://declare-cartridges-request-trek.trycloudflare.com/verify/0x11dB4806a640989fA44874051DFA4889c09534B4"
HEADERS = {"X-API-Key": "arcana_pro_001"}
CONCURRENT_REQUESTS = 50  # Let's start with 50 simultaneous hits

async def send_request(client, i):
    try:
        start = time.perf_counter()
        resp = await client.get(URL, headers=HEADERS)
        end = time.perf_counter()
        return end - start, resp.status_code
    except Exception as e:
        return None, str(e)

async def main():
    async with httpx.AsyncClient(timeout=10.0) as client:
        print(f"--- Swarming Node with {CONCURRENT_REQUESTS} Concurrent Swaps ---")
        tasks = [send_request(client, i) for i in range(CONCURRENT_REQUESTS)]
        results = await asyncio.gather(*tasks)
        
        latencies = [r[0] for r in results if r[0] is not None]
        statuses = [r[1] for r in results]
        
        if latencies:
            avg = sum(latencies) / len(latencies)
            print(f"AVERAGE LATENCY: {avg:.4f}s")
            print(f"MAX LATENCY: {max(latencies):.4f}s")
            print(f"SUCCESS RATE: {statuses.count(200)/len(statuses)*100}%")
        else:
            print("CRITICAL FAILURE: No requests completed.")

if __name__ == "__main__":
    asyncio.run(main())
