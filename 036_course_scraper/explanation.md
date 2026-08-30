# Problem 36: Course Scraper with BeautifulSoup

## Problem
Write a script that scrapes course names and prices from the Mongard educational website (https://www.mongard.ir/courses/) using BeautifulSoup, and displays the data in a clean, formatted table.

## My Solution

I used **Requests** to fetch the page and **BeautifulSoup** to parse the HTML. The course names are extracted from `<h4>` tags and prices from `<b>` tags. The data is then displayed using the **Rich** library for a visually appealing table.