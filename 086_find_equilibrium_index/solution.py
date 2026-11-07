"""
Problem #86: Find Equilibrium Index
Date: 2026-11-07

The equilibrium index of a list is the index where the sum of elements
to its left equals the sum of elements to its right. Returns the first
such index, or -1 if none exists.
"""

def find_equilibrium_index(arr: list):
    index = 0
    for _ in range(len(arr)):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
        index += 1
    else:
        return -1


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3, 4, 6], 3),
        ([-7, 1, 5, 2, -4, 3, 0], 3),
        ([1, 2, 3], -1),
        ([0, 0, 0], 0),
        ([1, 3, 5, 2, 2], 2),
        ([2, 1, -1, 1, 2], 1),
        ([-1, -1, -1, -1], -1),
        ([10], 0),
        ([1, 2, 3, 4, 5, 6, 7], -1),
        ([1, 2, 3, 3, 2, 1], -1),
    ]
    for data, expected in test_cases:
        result = find_equilibrium_index(data)
        if result == expected:
            print(f"[PASS] Input:{data}, Expected:{expected} , result:{result}")
        else:
            print(f"[FAILED] Input:{data}, Expected:{expected} , result:{result}")