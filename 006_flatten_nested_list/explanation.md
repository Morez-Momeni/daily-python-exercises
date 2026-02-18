# Problem 6: Flatten a Nested List

## Problem
Write a function that takes a list which may contain other lists (nested lists) and returns a single flat list containing all the elements in the original order.

**Example:**  
`[1, [2, [3, 4], 5]]` → `[1, 2, 3, 4, 5]`

---

## My Solution

I implemented a recursive function `nested_to_flat(nested_list)` that works in two steps:

1. **First pass** – Build a temporary list `flat_list` by iterating over the input:
   - If an element is a list, append each of its items individually.
   - If it's not a list, append the element itself.
2. **Second pass** – Scan `flat_list` to see if any element is still a list:
   - If **any** list is found, call the function recursively on the current `flat_list`.
   - If no lists remain, return `flat_list`.

## Future Improvements

- Implement an iterative version using a stack to avoid recursion depth issues.

