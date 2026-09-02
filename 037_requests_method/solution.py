"""
Problem #37: Book Search with OpenLibrary API
Date: 2026-09-02

This script searches for books by topic using the OpenLibrary API,
displays the results in a formatted table, and includes a clean
command-line interface with screen clearing and user prompts.

"""

import os
import time
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def clean():
    os.system("cls" if os.name == "nt" else "clear")

def search(user_book):
    books = []
    
    url = f"https://openlibrary.org/search.json?q={user_book}"
    headers = {"User-Agent": "MyBookApp/1.0"}
    r = requests.get(url, headers=headers, timeout=10).json()
    docs = r.get("docs", [])
    for book in docs:
        if book["title"]:
            books.append(book["title"])
    return books

def createTable(books:list):
    table = Table(title="Books" , style="bold cyan")
    table.add_column("ID")
    table.add_column("NAME")
    for idx , title in enumerate(books, start=1):
        table.add_row(str(idx) , title )
    console.print(table)

clean()

while True:

    console.print(Panel.fit("Search Books" , style= "bold cyan"))
    time.sleep(3)
    clean()
    user_book = Prompt.ask("Enter your topic")
    result = search(user_book)
    createTable(result) # type: ignore
    Prompt.ask("Enter any key to continiue")
    clean()
