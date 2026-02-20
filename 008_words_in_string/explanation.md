# Problem 8: Find Words in a String

## Problem
Write a function that takes a string and extracts the words from it.  
The definition of a "word" is flexible, but this implementation follows these rules:
- Words are separated by whitespace.
- Single‑character items are **only** kept if they are one of: `'a'`, `'A'`, `'i'`, `'I'`.
- Numbers (integers and floats) are **excluded** from the final list.
- The remaining words are printed with an index.

---

## My Solution

I wrote a function `find_words(my_str)` that works in three main steps:

### 1. Splitting and initial filtering
- First, the input string is stripped of leading/trailing spaces and split on whitespace using `.split()`.
- Each resulting piece is examined:
  - If its length is **1** or less, it is only added to the `words` list if it matches one of the allowed single‑character strings (`special_char` list).
  - If its length is **greater than 1**, it is added unconditionally.

### 2. Separating numbers from real words
- I iterate over the `words` list and try to convert each element to an `int`.
  - If successful, the element is appended to a separate `number` list (discarded later).
- If `int()` fails, I try converting to a `float`.
  - If successful, the element is also appended to `number`.
- If both conversions fail, the element is considered a real word and is appended to `words_without_int`.

### 3. Displaying the result
- A nested function `show_result()` prints each word in `words_without_int` with a line number.
