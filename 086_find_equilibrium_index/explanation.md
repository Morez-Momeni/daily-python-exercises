# Problem 86: Find Equilibrium Index

## Problem
The **equilibrium index** of a list is the index where the sum of all elements to its left equals the sum of all elements to its right.

Find the first such index. If no equilibrium index exists, return `-1`.

**Examples:**
- `[1, 2, 3, 4, 6]` → `3` (left sum of index 3 = 1+2+3 = 6, right sum = 6)
- `[1, 2, 3]` → `-1`
- `[10]` → `0` (empty left and right sums both equal 0)

## My Solution

```python
def find_equilibrium_index(arr: list):
    index = 0
    for _ in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
        index += 1
    else:
        return -1