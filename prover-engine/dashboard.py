import os
import time
from rich.live import Live
from rich.table import Table
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_last_latency():
    try:
        with open("monitor.log", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                if "LATENCY" in last_line:
                    return last_line.split("LATENCY:")[1].strip()
    except:
        return "N/A"
    return "N/A"

def generate_table():
    table = Table(title="ARCANA 12D SOVEREIGNTY DASHBOARD")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Node Status", "[bold green]ONLINE[/bold green]")
    table.add_row("Active Engine", "RUST_PROVER_V1 (602 MH/s)")
    table.add_row("Current Latency", get_last_latency())
    table.add_row("Total Liquidity", "136,000,000,000 CC")
    table.add_row("Concurrent Swaps", "4,500 Max Capacity")
    table.add_row("Security Protocol", "Sauna-v1 (SHA256 Proof)")
    
    return table

with Live(generate_table(), refresh_per_second=1) as live:
    while True:
        time.sleep(1)
        live.update(generate_table())
