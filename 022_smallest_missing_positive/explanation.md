# Problem 22: Find the Smallest Missing Positive Integer (Custom)

## Problem
Given an unsorted integer array, find the smallest positive integer that is missing, but **start the search from the smallest positive number that exists in the array**.

**Examples:**
- `[3, 4, 5]` → `2` (2 is missing, and 1 is ignored because it's not in the array)
- `[2, 3, 4]` → `1` (1 is missing before 2)
- `[1, 2, 3, 4]` → `5` (all numbers up to 4 exist, so 5 is missing)
- `[0, 5, 6]` → `4` (smallest positive is 5, 4 is missing)

---

## My Solution

I implemented the following steps:
1. If the array is empty, return `1`.
2. Sort the array.
3. Extract only the positive numbers into a new list.
4. If there are no positive numbers, return `1`.
5. Find the smallest positive number (`minimum`).
6. If `minimum - 1` is positive and not in the list, return `minimum - 1`.
7. Otherwise, start from `minimum` and check each consecutive number; return the first one that is missing.

