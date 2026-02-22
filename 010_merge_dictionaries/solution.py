"""
Problem #10: Merge Two Dictionaries

Problem Statement:
Write a function to merge two dictionaries. If both dictionaries have the same key,
prefer the second dictionary's value.

Approach:
- Iterate over the items of the second dictionary and assign each key-value pair
  to the first dictionary. This modifies the first dictionary in place.
- Finally, return the merged dictionary (the first one, now updated).

"""

def merge_dicts(dict1 : dict , dict2 : dict): 
 
    for key,value in dict2.items():
        dict1[key] = value
        
    return dict1
    

dict1 = {"a": 1, "b": 2, "d": 2}
dict2 = {"b": 3, "c": 4, "d": 8, "w": 0}

print(merge_dicts(dict1,dict2))