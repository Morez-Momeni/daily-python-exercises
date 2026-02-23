# Problem 11: Check if String Contains All Letters of the Alphabet

## Problem
Write a function that takes a string and returns `True` if the string contains every letter of the English alphabet at least once, otherwise `False`. The check should be case‑insensitive.

**Example:**  
`"The quick brown fox jumps over the lazy dog"` → `True` (it is a pangram).  
`"Hello World"` → `False` (missing many letters).

---

## My Solution

I wrote a function that iterates through all lowercase letters and returns `False` as soon as a missing letter is found. If the loop completes without finding any missing letter, it returns `True`.

## How it works

- Convert the input string to lowercase (so 'A' and 'a' are treated the same).

- Use string.ascii_lowercase to get the alphabet string 'abcdefghijklmnopqrstuvwxyz'.

- Loop over each character in the alphabet.

- If the character is not found in the string, return False immediately.

- If the loop finishes (meaning all letters were found), return True.