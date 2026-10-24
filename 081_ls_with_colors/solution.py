"""
Problem #81: Implement `ls` with Colored Directories
Date: 2026-10-24

A simple replacement for the Unix `ls` command:
- Lists the entries of a given directory.
- Prints directories in green and files in the default color.
- Uses colorama for cross-platform ANSI colors.
"""

import os
from colorama import Fore, Style


def ls(path):
    result = os.listdir(path)

    for r in result:
        if os.path.isdir(f"{path}/{r}"):
            print(Fore.GREEN + f"{r}" + Style.RESET_ALL, end=" ")
        else:
            print(r, end=" ")