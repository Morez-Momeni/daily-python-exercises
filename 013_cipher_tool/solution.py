"""
Problem #13: Cipher Tool (Caesar, Atbash, Vigenère)

A command-line tool for encryption/decryption using three classic ciphers.
Modular design with separate modules.
Uses the `rich` library for a polished terminal interface.

"""

from ciphers import caesar, atbash, vigenere
from rich.pretty import pprint
from rich.panel import Panel
from rich.tree import Tree
from rich import print
from rich.console import Console
import os

console = Console()

c = caesar.Caesar()
a = atbash.Atbash()
v = vigenere.Vigenere()

while True:
    menu_tree = Tree("Tools")
    menu_tree.add("1. Caesar")
    menu_tree.add("2. Atbash")
    menu_tree.add("3. Vigenère")
    menu_tree.add("4. Exit")
    print(Panel(menu_tree, title="[red]Menu"))
    choice = int(console.input("Enter [i]your[/i] [bold red]choice[/]: ").strip())
    
    match choice:
        case 1:  
            while True:
                caesar_tree = Tree("Caesar Options")
                caesar_tree.add("1. Encode")
                caesar_tree.add("2. Decode")
                caesar_tree.add("3. Change shift")
                caesar_tree.add("4. Main Menu")
                print(Panel(caesar_tree, title="[red]Caesar"))
                sub = int(console.input("Enter [i]your[/i] [bold red]choice[/]: ").strip())
                if sub == 1:
                    user_str = console.input("Enter [i]your[/i] [bold red]string[/]: ").strip()
                    result = c.encode(user_str)
                    print(Panel(f"[green]{user_str} [blue]--->[/] [red]{result}", title="Result"))
                elif sub == 2:
                    user_str = console.input("Enter [i]your[/i] [bold red]string[/]: ").strip()
                    result = c.decode(user_str)
                    print(Panel(f"[green]{user_str} [blue]--->[/] [red]{result}", title="Result"))
                elif sub == 3:
                    new_shift = int(console.input("Enter [i]your[/i] [bold red]shift[/]: ").strip())
                    c.change_shift(new_shift)
                    print(Panel(f"[green]Shift now changed to [blue]--->[/] [red]{new_shift}"))
                elif sub == 4:
                    os.system("cls")
                    break
                else:
                    pprint("Invalid option")
        
        case 2:  
            while True:
                atbash_tree = Tree("Atbash Options")
                atbash_tree.add("1. Encode")
                atbash_tree.add("2. Decode")
                atbash_tree.add("3. Main Menu")
                print(Panel(atbash_tree, title="[red]Atbash"))
                sub = int(console.input("Enter [i]your[/i] [bold red]choice[/]: ").strip())
                if sub == 1:
                    user_str = console.input("Enter [i]your[/i] [bold red]string[/]: ").strip()
                    result = a.encode(user_str)
                    print(Panel(f"[green]{user_str} [blue]--->[/] [red]{result}", title="Result"))
                elif sub == 2:
                    user_str = console.input("Enter [i]your[/i] [bold red]string[/]: ").strip()
                    result = a.decode(user_str)
                    print(Panel(f"[green]{user_str} [blue]--->[/] [red]{result}", title="Result"))
                elif sub == 3:
                    os.system("cls")
                    break
                else:
                    pprint("Invalid option")
        
        case 3:  
            while True:
                vig_tree = Tree("Vigenère Options")
                vig_tree.add("1. Encode")
                vig_tree.add("2. Decode")
                vig_tree.add("3. Change key")
                vig_tree.add("4. Main Menu")
                print(Panel(vig_tree, title="[red]Vigenère"))
                sub = int(console.input("Enter [i]your[/i] [bold red]choice[/]: ").strip())
                if sub == 1:
                    user_str = console.input("Enter [i]your[/i] [bold red]string[/]: ").strip()
                    result = v.encode(user_str)
                    print(Panel(f"[green]{user_str} [blue]--->[/] [red]{result}", title="Result"))
                elif sub == 2:
                    user_str = console.input("Enter [i]your[/i] [bold red]string[/]: ").strip()
                    result = v.decode(user_str)
                    print(Panel(f"[green]{user_str} [blue]--->[/] [red]{result}", title="Result"))
                elif sub == 3:
                    new_key = console.input("Enter [i]your[/i] [bold red]new key[/]: ").strip()
                    v.change_key(new_key)
                    print(Panel(f"[green]Key now changed to [blue]--->[/] [red]{new_key}"))
                elif sub == 4:
                    os.system("cls")
                    break
                else:
                    pprint("Invalid option")
        
        case 4:
            exit()
        
        case _:
            continue