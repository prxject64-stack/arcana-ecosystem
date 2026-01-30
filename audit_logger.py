import datetime

def log_interaction():
    auditor = input("Enter Auditor Name/ID: ")
    method = input("Method (Email/Phone/Portal): ")
    topic = input("Topic (e.g., 136B CC Liquidity, 4,500 Slots, Grant Gas): ")
    notes = input("Summary of Discussion: ")
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"\n[{timestamp}] | AUDITOR: {auditor} | METHOD: {method}\nTOPIC: {topic}\nNOTES: {notes}\n{'-'*50}"
    
    with open("AUDIT_INTERACTION_LOG.txt", "a") as f:
        f.write(log_entry)
    print("\nInteraction Logged Successfully.")

if __name__ == "__main__":
    log_interaction()
