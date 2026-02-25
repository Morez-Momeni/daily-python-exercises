# Problem 14: Calculate Mean, Median, and Mode (Without Built-in Functions)

## Problem
Write a function that takes a list of numbers and returns its mean, median, and mode without using any dedicated statistics library.

- **Mean** – sum of all elements divided by count.
- **Median** – middle value when sorted (or average of two middle values for even length).
- **Mode** – most frequently occurring value(s). If multiple values share the highest frequency, return all of them.

---

## My Solution

I implemented a function `mean_mode_median(list1)` that returns a formatted string containing the three values. The logic is:

1. **Empty check** – if the list is empty, return `False` and a message.
2. **Sort** – sort the list (needed for median).
3. **Mean** – simply `sum(list1) / len(list1)`.
4. **Mode** – count occurrences by iterating and using `list1.count(i)` for each element, store in a dictionary, then collect keys with maximum count.
5. **Median** – use the sorted list and the standard even/odd rule.

> All calculations are done manually, without importing `statistics` or `numpy`.

