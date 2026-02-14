import boto3
import uuid
import time

TABLE_NAME = "TrustStack_Clients"
TEST_COUNT = 100 # We will start with a 100-batch burst

def run_stress():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table(TABLE_NAME)
    print(f"STARTING STRESS TEST: Injecting {TEST_COUNT} simulated swaps...")
    
    start_time = time.time()
    for i in range(TEST_COUNT):
        client_id = f"STRESS-{uuid.uuid4().hex[:8]}"
        try:
            table.put_item(Item={
                'client_id': client_id,
                'wallet_address': f"TestWallet_{i}",
                'referred_by': "VGVzdFdhbGxldDEyMw==",
                'referral_status': 'PENDING',
                'timestamp': str(time.time())
            })
        except Exception as e:
            print(f"FAIL at {i}: {e}")
            break
            
    end_time = time.time()
    total = end_time - start_time
    print(f"COMPLETE: 100 Swaps injected in {total:.2f} seconds.")
    print(f"THROUGHPUT: {100/total:.2f} swaps/sec.")

if __name__ == "__main__":
    run_stress()
