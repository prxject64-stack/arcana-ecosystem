import boto3
import time
import os

TABLE_NAME = "TrustStack_Clients"
LIMIT = 4500

def get_stats():
    client = boto3.client('dynamodb', region_name='us-east-1')
    # Efficiently get the count without downloading full items
    response = client.scan(TableName=TABLE_NAME, Select='COUNT')
    count = response.get('Count', 0)
    
    # Get table metadata for throughput status
    table_meta = client.describe_table(TableName=TABLE_NAME)['Table']
    status = table_meta['TableStatus']
    
    return count, status

def draw_dashboard():
    while True:
        try:
            count, status = get_stats()
            percent = (count / LIMIT) * 100
            
            os.system('clear')
            print("="*40)
            print(f" ARCANA SOVEREIGN - NETWORK PULSE ")
            print("="*40)
            print(f" NODE STATUS:   [{status}]")
            print(f" ACTIVE SWAPS:  {count} / {LIMIT}")
            print(f" CAPACITY:      [{'#' * int(percent/5)}{'-' * (20 - int(percent/5))}] {percent:.1f}%")
            print("="*40)
            print(f" LIQUIDITY:     136B CC (Sovereign Authority)")
            print(f" LAST UPDATED:  {time.strftime('%H:%M:%S')}")
            print("="*40)
            print(" Press Ctrl+C to exit monitor.")
            
            time.sleep(5) # Poll every 5 seconds
        except Exception as e:
            print(f"Monitor Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    draw_dashboard()
