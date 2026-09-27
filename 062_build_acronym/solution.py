"""
Problem #62: Build an Acronym from a Phrase
Date: 2026-09-27

Reads a phrase from the user and builds an acronym by taking the first
letter of each word and converting it to uppercase.
"""

phrase = input("Input phrase:").strip().split()

result = ""

for word in phrase:
    result += word[0].upper()

print(result)