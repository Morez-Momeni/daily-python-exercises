"""
Problem #13: Cipher Tool 
Date: 2026-02-25

A simple command-line tool for encryption/decryption using the Caesar cipher.
Built with modular design - the Caesar cipher logic is in a separate module.
Uses the `rich` library for a nicer terminal interface.

Current features:
- Caesar cipher with adjustable shift.
- Encode and decode operations.
- Interactive menu with submenus.
"""

from ciphers import caesar
from rich.pretty import pprint
from rich.panel import Panel
from rich.tree import Tree
from rich import print 
import os

c = caesar.Caesar()

while True:
    menu_tree = Tree("Tools")
    menu_tree.add("1.Caesar")
    menu_tree.add("2.Atbash")
    menu_tree.add("3.Vigenere")
    menu_tree.add("4.Exit")
    print(Panel(menu_tree))
    choise = int(input("Enter your choise: ").strip())
    match choise:
        case 1 :
            pprint("Caesar")
            caesar_tree = Tree("Algorithms")
            caesar_tree.add("1.Encode")
            caesar_tree.add("2.Decode")
            caesar_tree.add("3.Change shift")
            caesar_tree.add("4.Main Menu")
            print(Panel(caesar_tree))
            user_choise = int(input("Enter your choise: ").strip())
            if user_choise == 1:
                user_string = input("Enter string: ").strip()
                result = c.encode(user_string)
                print(f"{user_string} ---> {result}")
                
            elif user_choise == 2:
                user_string = input("Enter your encoded string: ").strip()
                result = c.decode(user_string)
                print(f"{user_string} ---> {result}")
                
            elif user_choise == 3:
                user_new_shift = int(input("Enter your new shift: ").strip())
                c.change_shift(user_new_shift)
                print(f"Shift now change to ---> {user_new_shift}")
                
            elif user_choise == 4:
                os.system("cls")
                continue
            
            else:
                pprint("Invalid")
        case 4 :
            exit()
        case _:
            continue