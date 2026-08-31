import requests
import argparse
from bs4 import BeautifulSoup
from rich.table import Table
from rich.console import Console

console = Console()
parser = argparse.ArgumentParser()

parser.add_argument("-p")

args = parser.parse_args()

if args.p:

    url = f"https://www.mongard.ir/courses/?page={args.p}"

    data = requests.get(url)
    data.raise_for_status()
    soup = BeautifulSoup(data.text , "html.parser")

    all_h4_tags = soup.find_all('h4')
    all_b_tags = soup.find_all('b')

    course_name = []
    prices = []
    for h4 in all_h4_tags:
        course_name.append(h4.get_text(strip=True))
    
    for b in all_b_tags:
        prices.append(b.get_text(strip=True))

    courses = zip(course_name,prices)

    table = Table(title="mongard course price".title() , style= "bright_blue")

    table.add_column("ID" , style="bold yellow")
    table.add_column("Name" , style="bold green")
    table.add_column("Price", style="bold red")

    counter = 1
    for name , price in courses:
        table.add_row(str(counter) , name, price)
        counter +=1

    console.print(table)
