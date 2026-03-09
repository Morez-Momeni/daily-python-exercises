"""

rock-paper-siccors

"""
import random
from rich.panel import Panel
from rich import print
from rich.console import Console


console = Console()

def game():
    choises = ["rock","paper","siccors"]
    pc = 0
    human = 0
    
    while True:

        user_choise = console.input("Enter [i]your[/i] [bold red]choice[/]: ").strip().lower()
        computer_choise = random.choice(choises)
        
        if user_choise not in choises and user_choise != "exit":
            print(Panel("[red]Invalid choise",expand=False))
            continue
        
        if user_choise == "exit":
            print(Panel(f"[green]human[/]: {human}, [blue]pc:[/] {pc}",expand=False,title="[bold red]Result"))
            break
        
        if user_choise == computer_choise:
            print(Panel("[green]Equal",expand=False))
            continue
        
        elif user_choise == "rock":
            if computer_choise == "paper":
                print(Panel(f"[red]Lose",expand=False))
                pc+=1
            elif computer_choise == "siccors":
                print(Panel(f"[green]Win",expand=False))
                human+=1
        
        elif user_choise == "paper":
            if computer_choise == "rock":
                print(Panel(f"[green]Win",expand=False))
                human+=1
            elif computer_choise == "siccors":
                print(Panel(f"[red]Lose",expand=False))
                pc+=1
        
        elif user_choise == "siccors":
            if computer_choise == "rock":
                print(Panel(f"[red]Lose",expand=False))
                pc+=1
            elif computer_choise == "paper":
                print(Panel(f"[green]Win",expand=False))
                human+=1

game()
