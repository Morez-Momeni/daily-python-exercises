# Problem 17: Check if Two Strings are Rotations of Each Other

## Problem
Write a function that takes two strings and returns `True` if one string is a rotation of the other.  
A rotation means that by moving some number of characters from the beginning to the end (or vice versa) you can obtain the other string.

**Examples:**
- `("abcde", "cdeab")` → `True` (rotate left by 2)
- `("abcde", "abced")` → `False`
- `("a", "a")` → `True`
- `("", "")` → `True`
- `("abc", "cab")` → `True`
- `("hello", "llohe")` → `True`

---

## My Solution

I implemented a function that:
1. Checks if both strings are empty → return `True`.
2. Compares lengths; if different → return `False`.
3. Repeatedly rotates the second string and compares with the first.
4. If a match is found, returns `True`; after all rotations, returns `False`.

