# Problem 46: Manual Push and Pop Implementation

## Problem
Implement `push` and `pop` operations on a global list (`data_set`) without using the built‑in `list.append()` or `list.pop()` methods. Write tests to verify the behaviour.

## My Solution

I implemented:
- `push(data)` – extends the global list with the provided list. If the provided list is empty, it appends the empty list itself.
- `pop()` – returns the last element of the list and removes it using list slicing.
