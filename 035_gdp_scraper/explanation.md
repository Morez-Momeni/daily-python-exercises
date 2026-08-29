# Problem 35: GDP Data Scraper with BeautifulSoup

## Problem
Write a script that scrapes GDP data by country from Worldometer (or a similar site) using BeautifulSoup, parses the HTML table, and displays the data in a clean, formatted table.

## My Solution

I used **Requests** to fetch the page and **BeautifulSoup** to parse the HTML. The data is extracted from `<td>` tags and displayed using the **Rich** library for a visually appealing table.