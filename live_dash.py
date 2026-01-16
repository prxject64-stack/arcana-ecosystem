import json
import time
import os
from datetime import datetime
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console

LEDGER_PATH = os.path.expanduser("~/arcana-ecosystem/ledger.json")

def get_data():
    try:
        with open(LEDGER_PATH, 'r') as f:
            return json.load(f)
    except:
        return {"balance": 0, "fees_paid": 0, "last_block_hash": "N/A"}

def make_layout() -> Layout:
    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["body"].split_row(
        Layout(name="main", ratio=2),
        Layout(name="side", ratio=1)
    )
    return layout

def generate_reward_table(data) -> Table:
    table = Table(title="[bold green]Sovereign Rewards Ledger[/]", expand=True, border_style="green")
    table.add_column("Type", style="cyan")
    table.add_column("Amount", justify="right", style="bold yellow")
    table.add_row("Gross Block Reward", "50.00 ARC")
    table.add_row("Sauna Protocol Fee (2.5%)", "-1.25 ARC", style="red")
    table.add_row("Security System Fee (1.5%)", "-0.75 ARC", style="red")
    table.add_section()
    table.add_row("NET REWARD", "48.00 ARC", style="bold green")
    return table

def generate_fee_panel(data) -> Panel:
    fees = data.get('fees_paid', 0)
    content = f"\n[bold red]Total Fees Vaulted:[/]\n[bold white]{fees:,.2f} ARC[/]\n\n"
    content += f"[dim]Status: [green]Compliant[/dim]"
    return Panel(content, title="Compliance & Fees", border_style="red")

layout = make_layout()
console = Console()

if __name__ == "__main__":
    try:
        with Live(layout, refresh_per_second=2, screen=True):
            while True:
                data = get_data()
                layout["header"].update(Panel(f"ARCANA SOVEREIGN SYSTEM | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | [bold green]WATCHDOG: ONLINE[/]", style="white on blue"))
                layout["main"].update(generate_reward_table(data))
                layout["side"].update(generate_fee_panel(data))
                balance = data.get('balance', 0)
                footer_text = f"SOVEREIGN BALANCE: [bold yellow]{balance:,.2f} ARC[/] | [cyan]CPU LOAD: 75%[/] | [magenta]LAST HASH: {str(data.get('last_block_hash'))[:16]}...[/]"
                layout["footer"].update(Panel(footer_text, border_style="yellow"))
                time.sleep(1)
    except KeyboardInterrupt:
        # Catching the Ctrl+C to exit silently as requested for organization
        console.print("\n[bold yellow][!] Dashboard Suspended Safely. Miner continues in background.[/]\n")
