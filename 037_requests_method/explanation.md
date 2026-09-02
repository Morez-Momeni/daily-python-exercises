# Problem 37: Book Search with OpenLibrary API

## Problem
Write a script that allows users to search for books by topic using the OpenLibrary API, displays the results in a clean table, and provides a simple interactive command‑line interface.

## My Solution

I used the **OpenLibrary API** to fetch book data and **Rich** to format the output. The script:

1. Clears the terminal and shows a welcome panel.
2. Prompts the user for a topic (e.g., "python", "harry potter").
3. Sends a request to `https://openlibrary.org/search.json?q={topic}`.
4. Extracts book titles from the JSON response.
5. Displays the titles in a numbered table.
6. Allows the user to search again or exit.