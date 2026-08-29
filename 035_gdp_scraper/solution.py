"""
Problem #35: GDP Data Scraper with BeautifulSoup
Date: 2026-08-29

This script scrapes GDP data by country from Worldometer using BeautifulSoup,
parses the HTML table, and displays the data in a rich table format.
"""


import requests
from bs4 import BeautifulSoup
from rich.table import Table
from rich.console import Console

console = Console() 

url = "https://www.worldometers.info/gdp/gdp-by-country/"


page_data = requests.get(url)

soup = BeautifulSoup(page_data.text , "html.parser")

data = []

td_data = iter(soup.find_all('td'))

while True:
    try:
        id = next(td_data).text
        country = next(td_data).text
        gdp_us = next(td_data).text
        gdp_full = next(td_data).text
        gdp_growth = next(td_data).text
        gdp_per_capita = next(td_data).text 

        data.append((id,country,gdp_us,gdp_full,gdp_growth,gdp_per_capita))

    except StopIteration:
        break

table = Table(title="GDP_BY_COUNTRY", style="bright_blue")
table.add_column("id", style="bold blue")
table.add_column("country", style="bold red")
table.add_column("gdp_us", style="bold green")
table.add_column("gdp_full", style="white")
table.add_column("gdp_growth", style="bold black")
table.add_column("gdp_per_capita", style="bold yellow")

for id,country,gdp_us,gdp_full,gdp_growth,gdp_per_capita in data:
    table.add_row(str(id),str(country),str(gdp_us),
                  str(gdp_full),str(gdp_growth),str(gdp_per_capita))
console.print(table)



