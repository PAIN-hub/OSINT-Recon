from rich.console import Console
from rich.table import Table

def print_table(data):
    console = Console()
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Key")
    table.add_column("Value", overflow="fold")
    for k, v in data.items():
        table.add_row(str(k), str(v))
    console.print(table)