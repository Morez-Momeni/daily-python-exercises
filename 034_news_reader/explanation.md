# Problem 34: News Reader with Text‑to‑Speech

## Problem
Write a script that fetches the latest news headlines from an online API (News API) and reads them aloud using text‑to‑speech. This combines API interaction, JSON parsing, and TTS.

## My Solution

I used the **News API** to fetch articles and **pyttsx3** for speech. The script:

1. Requests news articles for a given query (default: `"apple"`).
2. Parses the JSON response.
3. For each article, prints the title and speaks it using `pyttsx3`.
4. Handles `KeyboardInterrupt` to stop speech gracefully.