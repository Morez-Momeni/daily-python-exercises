# Problem 3: Filter Out Palindromes

## Problem
Write a function that takes a list of strings and returns a new list containing only the strings that are **not** palindromes.

A palindrome is a string that reads the same forwards and backwards (e.g., `"radar"`, `"level"`, `"a"`).

---

## Solutions

### 1. Using string slicing (`word[::-1]`) – `filter_out_palindromes`
This is the most Pythonic approach. For each word, we compare it with its reverse created by slicing.
### 2.  Manual reversal (without slicing) – filter_out_palindromes_without_list_slicing
This approach builds the reversed string character by character using a loop. It demonstrates understanding of string indexing and avoids relying on Python’s slicing syntax.

## Edge Cases
-Empty string "" – it is considered a palindrome (reads the same forwards and backwards). It will be filtered out (not included in output).
-Single‑character strings – always palindromes, so they are removed.
-Case sensitivity – comparisons are case‑sensitive. If case‑insensitive filtering is desired, convert both sides to lowercase first (e.g., word.lower() != word[::-1].lower()).
-Empty input list – returns an empty list.
-Strings with spaces – spaces are treated like any other character; "race car" reversed is "rac ecar", so it is not a palindrome unless symmetric.

## What I Learned
-How to reverse a string both with slicing and manually using negative indices.
-The importance of not modifying a list while iterating over it – the slicing method avoids this issue, while the manual method uses pop() in a controlled way but consumes the list.





