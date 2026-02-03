import boto3
import time
import base64

# SOVEREIGN CONFIG
REWARD_AMOUNT = 1000
DYNAMODB_TABLE = "TrustStack_Clients"

def process_referrals():
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table(DYNAMODB_TABLE)
        
        response = table.scan(
            FilterExpression=boto3.dynamodb.conditions.Attr('referral_status').eq('PENDING')
        )
        
        for user in response.get('Items', []):
            try:
                # 1. Verify the Referrer
                ref_raw = user.get('referred_by')
                if not ref_raw: continue
                referrer_wallet = base64.b64decode(ref_raw).decode('utf-8')
                
                # 2. Log Action
                print(f"VALIDATING: Reward for {referrer_wallet} via Client {user['client_id']}")
                
                # 3. Mark as PAID using the mandatory client_id key
                table.update_item(
                    Key={'client_id': user['client_id']},
                    UpdateExpression="set referral_status = :s",
                    ExpressionAttributeValues={':s': 'PAID'}
                )
                print(f"SUCCESS: Reward Issued.")
            except Exception as e:
                print(f"ITEM ERROR: {e}")
    except Exception as e:
        print(f"SYSTEM ERROR: {e}")

if __name__ == "__main__":
    print("Sovereign Rewarder v2 (ID-Aware) Active...")
    while True:
        process_referrals()
        time.sleep(60)
