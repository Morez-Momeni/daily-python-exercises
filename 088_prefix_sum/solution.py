"""
Problem #88: Prefix Sum (Sum of First N Elements)
Date: 2026-11-21

Computes the sum of the first `prefix_index` elements of a list.
Returns False if prefix_index is larger than the list length.
"""

def prefix_sum(arr, prefix_index):
    counter = 0
    sum = 0
    if prefix_index > len(arr):
        return False
    while counter < prefix_index:
        sum += arr[counter]
        counter += 1

    return sum


arr = [1, 2, 3, 4, 5, 6]

print(prefix_sum(arr, 4))