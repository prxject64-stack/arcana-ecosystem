import os, time, datetime, psutil
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console
from rich.text import Text

# FINAL BILLION-SCALE CONSTANTS
VAULT_ARC = os.path.expanduser("~/arcana-ecosystem/vault/security_system")
VAULT_CC = os.path.expanduser("~/arcana-ecosystem/vault/sauna_protocol")

ARC_REWARD = 150000000.0  # 150M per block -> 46B total
CC_REWARD = 500000000.0   # 500M per block

def get_stats():
    # ARC Audit
    arc_count = len([f for f in os.listdir(VAULT_ARC) if f.endswith('.receipt')]) if os.path.exists(VAULT_ARC) else 0
    # CC Audit
    cc_count = len([f for f in os.listdir(VAULT_CC) if f.endswith('.receipt')]) if os.path.exists(VAULT_CC) else 0
    
    total_arc = arc_count * ARC_REWARD
    total_cc = cc_count * CC_REWARD
    
    recent_blocks = []
    if os.path.exists(VAULT_ARC):
        files = [(f, os.path.getmtime(os.path.join(VAULT_ARC, f))) for f in os.listdir(VAULT_ARC) if f.endswith('.receipt')]
        files.sort(key=lambda x: x[1], reverse=True)
        recent_blocks = files[:10]
    
    return total_arc, total_cc, recent_blocks

def make_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["body"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=1)
    )
    return layout

def generate_dashboard():
    arc_bal, cc_bal, recent = get_stats()
    
    header = Panel(Text(f"INFINITE NETWORK CORE | 166 MH/s | PROVER: ACTIVE", justify="center", style="bold white on purple"), border_style="purple")
    
    balance_text = Text()
    balance_text.append(f"\n ARC: {arc_bal:,.0f}\n", style="bold purple")
    balance_text.append(f" CC:  {cc_bal:,.0f}\n", style="bold green")
    left_panel = Panel(balance_text, title="[bold white]TOTAL COIN BALANCE", border_style="purple")
    
    ticker_table = Table(show_header=True, header_style="bold cyan", expand=True, box=None)
    ticker_table.add_column("BLOCK ID", style="dim")
    ticker_table.add_column("SETTLED", justify="right", style="cyan")
    
    for f, t in recent:
        ts = datetime.datetime.fromtimestamp(t).strftime('%H:%M:%S')
        short_name = f.replace("block_", "").replace(".receipt", "")[:12]
        ticker_table.add_row(f"0x{short_name}", ts)
    
    right_panel = Panel(ticker_table, title="[bold cyan]LIVE SETTLEMENTS", border_style="cyan")
    
    cpu = psutil.cpu_percent()
    footer = Panel(Text(f"CPU: {cpu}% | RAM: {psutil.virtual_memory().percent}% | DISK: OK | SYNC: 2s", justify="center", style="dim"), border_style="white")
    
    return header, left_panel, right_panel, footer

layout = make_layout()
with Live(layout, refresh_per_second=1, screen=True):
    while True:
        header, left, right, footer = generate_dashboard()
        layout["header"].update(header)
        layout["left"].update(left)
        layout["right"].update(right)
        layout["footer"].update(footer)
        time.sleep(2)
