"""
Problem Statement:
Write a function that takes a nested list (a list that can contain other lists) 
and returns a flattened (one‑dimensional) list containing all the elements in order.

Example:
Input:  [1, [2, [3, 4], 5]]
Output: [1, 2, 3, 4, 5]

Approach:
- Iterate through the input list.
- If an element is a list, append its individual items to a new list.
- If it's not a list, append the element itself.
- After this first pass, check if the new list still contains any list.
  If yes, recursively call the function on that new list.
  If no, return the new list.
"""

def nested_to_flat(nested_list):
    flat_list = []
    for nl in nested_list:
        if type(nl) == list:
            for fl in nl:
                flat_list.append(fl)
        else:
            flat_list.append(nl)

    for ch in flat_list:
        if type(ch) == list:
            return nested_to_flat(flat_list)
    else:
        return flat_list



    
    
if __name__ == "__main__":
    test_cases = [
        ([1, [2, [3, 4], 5]], [1, 2, 3, 4, 5]),
        ([[[2, 3], 3]], [2, 3, 3]),
        ([1, [2, 3], [4, [5, 6]]], [1, 2, 3, 4, 5, 6]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
    ]       
    
for input , expected  in test_cases:
    result = nested_to_flat(input)
    if result == expected :
        print(f"[Pass] Input: {input}, expected: {expected}, Result: {result}")
    else:
        print(f"[Error] Input: {input}, expected: {expected}, Result: {result}")
