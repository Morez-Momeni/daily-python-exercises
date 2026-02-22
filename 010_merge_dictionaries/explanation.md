# Problem 10: Merge Two Dictionaries

## Problem
Write a Python function to merge two dictionaries. If both dictionaries have the same key, the second dictionary's value should be preferred (i.e., it overrides the first).

**Example:**  
`dict1 = {"a": 1, "b": 2, "d": 2}`  
`dict2 = {"b": 3, "c": 4, "d": 8, "w": 0}`  
Merged result should be: `{"a": 1, "b": 3, "c": 4, "d": 8, "w": 0}`

---

## My Solution

I implemented a simple loop that iterates over the second dictionary and assigns each key‑value pair to the first dictionary. This approach modifies the first dictionary **in place**. The function also returns the modified dictionary for convenience.
