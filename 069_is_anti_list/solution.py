"""
Problem #69: Anti-List Checker
Date: 2026-10-11

Check if two lists are exactly opposite:
- Both lists consist of exactly two different elements.
- The positions of these elements are reversed between the two lists
  (wherever list1 has element a, list2 has element b, and vice versa).
"""

def is_anti_list(list1, list2):
    test_list1, test_list2 = set(list1), set(list2)
    if not test_list2.issubset(test_list1):
        return False
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            return False
    return True