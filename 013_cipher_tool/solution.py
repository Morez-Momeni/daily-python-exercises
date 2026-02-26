"""
Problem #13: Cipher Tool (Caesar & Atbash)


A command-line tool for encryption/decryption using Caesar and Atbash ciphers.
Modular design with separate modules for each cipher.
Uses the `rich` library for a nicer terminal interface.
"""

from ciphers import caesar, atbash
from rich.pretty import pprint
from rich.panel import Panel
from rich.tree import Tree
from rich import print 
import os

c = caesar.Caesar()
a = atbash.Atbash()

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
            while True:
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
                    break
            
                else:
                    pprint("Invalid")
                
        case 2 :    
            while True:
                pprint("Atbash")
                atbash_tree = Tree("Algorithms")
                atbash_tree.add("1.Encode")
                atbash_tree.add("2.Decode")
                atbash_tree.add("3.Main Menu")
                print(Panel(atbash_tree))
                user_choise = int(input("Enter your choise: ").strip())
                if user_choise == 1:
                    user_string = input("Enter string: ").strip()
                    result = a.encode(user_string)
                    print(f"{user_string} ---> {result}")
                
                elif user_choise == 2:
                    user_string = input("Enter your encoded string: ").strip()
                    result = a.decode(user_string)
                    print(f"{user_string} ---> {result}")
                
                elif user_choise == 3:
                    os.system("cls")
                    break
        case 4 :
            exit()
        case _ :
            continue