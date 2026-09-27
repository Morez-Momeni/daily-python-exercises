# Problem 62: Build an Acronym from a Phrase

## Problem
Write a script that reads a phrase from the user and builds an acronym by taking the first letter of each word and converting it to uppercase.

**Example:**
- Input: `"portable network graphics"`
- Output: `"PNG"`

## My Solution

I used three simple steps:
1. Read the input with `input()`.
2. Split the phrase into words with `.strip().split()`.
3. Loop through each word, take `word[0]`, uppercase it, and append it to the result string.