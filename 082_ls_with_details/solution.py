"""
Problem #82: Implement `ls` with Optional Long Format (-l)
Date: 2026-10-25

A simple `ls` replacement that supports:
- Default mode: list entry names in one line, directories in green.
- Long mode (`l=True`): show name, size, creation time, and modification time.
"""

import os
from datetime import datetime
from colorama import Fore, Style


def ls(l=False):
    cwd = os.getcwd()
    result = os.listdir(cwd)
    info_list = []

    if not l:
        for r in result:
            full_path = os.path.join(cwd, r)

            if os.path.isdir(full_path):
                print(Fore.GREEN + f"{r}" + Style.RESET_ALL, end=" ")
            else:
                print(r, end=" ")

    else:
        for r in result:
            full_path = os.path.join(cwd, r)
            size = os.path.getsize(full_path)
            creation = datetime.fromtimestamp(os.path.getctime(full_path))
            modification = datetime.fromtimestamp(os.path.getmtime(full_path))
            info = {
                'name': r,
                'size': size,
                'creation': creation,
                'modification': modification
            }
            info_list.append(info)

        for inf in info_list:
            print(f"{inf['name']} {inf['size']} {inf['creation']} {inf['modification']}")


ls(l=True)