import time
import subprocess

MAX_TPS = 4500
MIN_VAULT = 110_000_000_000

def monitor_and_protect():
    print("--- Obsidian Sentinel Active: Auto-Throttle Engaged ---")
    # Simulation mode: Check for 5 seconds then exit
    for i in range(10):
        current_tps = 4600  # Simulated breach
        current_vault = 136_000_000_000
        
        if current_tps > MAX_TPS or current_vault < MIN_VAULT:
            print(f"[CRITICAL] Threshold Breach! TPS: {current_tps}")
            # Try to run the throttle script
            try:
                subprocess.run(["./emergency_throttle.sh"], check=True)
            except Exception as e:
                print(f"Throttle failed: {e}. Check if emergency_throttle.sh exists.")
            break
            
        time.sleep(0.5)

if __name__ == "__main__":
    monitor_and_protect()
