import time, json, os
L="ledger"
R=0.2 # 5 iterations per second
while True:
 entry={"ts":time.time(),"id":os.urandom(8).hex()}
 with open(L,"a") as f:
  f.write(json.dumps(entry)+"\n")
 # Balance check every 50 iterations (every 10 seconds at this speed)
 try:
  if time.time() % 10 < 0.2:
   with open(L,"r") as f:
    c=sum(1 for _ in f)
   print(f">>> Total Balance: {c/1000.0} ARC")
 except:pass
 time.sleep(R)
