# Problem 5: Check if Two Strings are Anagrams

## Problem
Write a function that takes two strings and returns `True` if they are anagrams of each other, otherwise `False`.

**Anagram definition:** Two strings are anagrams if they contain exactly the same characters with the same frequencies. Order does not matter.

**Examples:**
- `"listen"` and `"silent"` → `True`
- `"hello"` and `"billion"` → `False` (different lengths)
- `"rat"` and `"car"` → `False` (different character sets)

---

## My Solution

I wrote a function `check_anagram(str1, str2)` that follows these steps:

1. **Check lengths** – If the strings have different lengths, they cannot be anagrams. Return `False` immediately.
2. **Define a helper** `count_char(s1, s2)` – This helper iterates over each character in the first string and compares its count in both strings using Python's built‑in `.count()` method.
   - If any character appears a different number of times, the helper returns `False`.
   - If all characters pass, the helper returns `True`.
3. **Call the helper** – If lengths are equal and the helper returns `True`, the function returns `True`; otherwise, it returns `False`.

