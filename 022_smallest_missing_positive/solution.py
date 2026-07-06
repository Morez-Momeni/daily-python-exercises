"""
Problem #22: Find the Smallest Missing Positive Integer (Custom Definition)
Date: 2026-07-06

Given an unsorted integer array, find the smallest positive integer that is missing,
but start the search from the smallest positive number present in the array.

For example:
- [3,4,5] → 2 (because 2 is missing between the existing positives)
- [2,3,4] → 1 (because 1 is missing before 2)
- [1,2,3,4] → 5 (because 5 is missing after 4)
"""

def find_smallest_missing_positive_integer(array):
    if len(array) == 0:
        return 1   

    array.sort()
    
    positive_array = []
    for number in array:
        if number > 0:
            positive_array.append(number)
    
    if len(positive_array) == 0:
        return 1   
    
    minimum = min(positive_array)
    

    if minimum - 1 > 0:
        return minimum - 1
    
    current = minimum
    while True:
        if current not in positive_array:
            return current
        current += 1


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 5], 2),
        ([2, 3, 4], 1),
        ([1, 2, 3, 4], 5),
        ([0, 5, 6], 4),
        ([-1, -2, 0], 1),
        ([], 1),
        ([1, 2, 3], 4),
        ([10, 11, 12], 9),
    ]
    
    for inp, expected in test_cases:
        result = find_smallest_missing_positive_integer(inp)
        status = "Pass" if result == expected else "Reject"
        print(f"{status} Input: {inp} → Output: {result} (Expected: {expected})")