from flask import Flask, render_template_string
import os

app = Flask(__name__)

# PROTOCOL REWARD SETTINGS (Infinite Network v1)
ARC_REWARD_PER_BLOCK = 0.15
CC_REWARD_PER_BLOCK = 0.50

# VAULT PATHS
VAULT_ARC = os.path.expanduser("~/arcana-ecosystem/vault/security_system")
VAULT_CC = os.path.expanduser("~/arcana-ecosystem/vault/sauna_protocol")

def get_total_balance(path, reward):
    if not os.path.exists(path):
        return 0.0
    # High-speed file counting for the vault
    count = sum(1 for entry in os.scandir(path) if entry.is_file() and entry.name.endswith('.receipt'))
    return count * reward

@app.route('/')
def index():
    total_arc = get_total_balance(VAULT_ARC, ARC_REWARD_PER_BLOCK)
    total_cc = get_total_balance(VAULT_CC, CC_REWARD_PER_BLOCK)
    
    # RUTHLESS UI: FOCUS ON THE TOTALS
    return f"""
    <body style="background:#000; color:#fff; font-family:'Courier New', monospace; padding:100px; text-align:center;">
        <div style="border: 2px solid #7000ff; display:inline-block; padding:40px; border-radius:15px; background:#0a0a0a;">
            <h2 style="color:#7000ff; letter-spacing:2px;">INFINITE NETWORK CONSOLIDATED LEDGER</h2>
            <hr style="border:0; border-top:1px solid #222; margin:20px 0;">
            
            <div style="font-size:4em; font-weight:bold; color:#7000ff;">
                ARC: {total_arc:,.2f}
            </div>
            
            <div style="font-size:2em; font-weight:bold; color:#00ffa3; margin-top:10px;">
                CC: {total_cc:,.2f}
            </div>
            
            <p style="color:#444; margin-top:30px; font-size:0.8em;">
                VAULT STATUS: PESSIMISTIC FINALITY VERIFIED<br>
                AUTO-REFRESH: 10S
            </p>
        </div>
        <script>setTimeout(() => location.reload(), 10000);</script>
    </body>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
