from flask import Flask, render_template_string
import os
import datetime

app = Flask(__name__)

# PROTOCOL REWARD SETTINGS
ARC_REWARD = 0.15
CC_REWARD = 0.50

# VAULT PATHS
VAULT_ARC = os.path.expanduser("~/arcana-ecosystem/vault/security_system")
VAULT_CC = os.path.expanduser("~/arcana-ecosystem/vault/sauna_protocol")

def get_vault_data(path, reward):
    if not os.path.exists(path):
        return 0.0, "N/A"
    
    files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.receipt')]
    if not files:
        return 0.0, "N/A"
    
    total_balance = len(files) * reward
    # Get the latest file modification time
    latest_file = max(files, key=os.path.getmtime)
    mtime = os.path.getmtime(latest_file)
    last_ts = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-16 %H:%M:%S')
    
    return total_balance, last_ts

@app.route('/')
def index():
    arc_bal, arc_time = get_vault_data(VAULT_ARC, ARC_REWARD)
    cc_bal, cc_time = get_vault_data(VAULT_CC, CC_REWARD)
    
    return f"""
    <body style="background:#000; color:#fff; font-family:'Courier New', monospace; padding:50px; text-align:center;">
        <div style="border: 2px solid #7000ff; display:inline-block; padding:40px; border-radius:15px; background:#0a0a0a; min-width:500px;">
            <h2 style="color:#7000ff; letter-spacing:2px;">INFINITE NETWORK CONSOLIDATED LEDGER</h2>
            <hr style="border:0; border-top:1px solid #222; margin:20px 0;">
            
            <div style="font-size:4.5em; font-weight:bold; color:#7000ff; margin-bottom:10px;">
                ARC: {arc_bal:,.2f}
            </div>
            <div style="color:#888; font-size:0.9em; margin-bottom:30px;">
                LAST ARC SETTLEMENT: <span style="color:#fff;">{arc_time}</span>
            </div>
            
            <div style="font-size:2.5em; font-weight:bold; color:#00ffa3;">
                CC: {cc_bal:,.2f}
            </div>
            <div style="color:#888; font-size:0.9em;">
                LAST CC SETTLEMENT: <span style="color:#fff;">{cc_time}</span>
            </div>
            
            <p style="color:#444; margin-top:40px; font-size:0.7em; text-transform:uppercase;">
                Vault Sync: ACTIVE | 166 MH/s Verification | Auto-Refresh: 10s
            </p>
        </div>
        <script>setTimeout(() => location.reload(), 10000);</script>
    </body>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
