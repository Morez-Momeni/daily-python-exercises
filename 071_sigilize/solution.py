"""
Problem #71: Sigilize - Magic Sigil Generator
Date: 2026-10-14

Removes vowels, spaces, and duplicate letters (keeping the last occurrence)
to produce a "magic sigil" from a phrase.
"""

def sigilize(text: str):
    text = text.strip().upper()
    seda_dar = "AEIOU"
    for char in text:
        if char in seda_dar:
            text = text.replace(char, "")
    text = text.replace(" ", "")
    listed_text = list(text)
    for i in listed_text[:]:
        char_numbers = listed_text.count(i)
        if char_numbers > 1:
            listed_text.remove(i)
    res = ""
    for ch in listed_text:
        res += ch
    return res