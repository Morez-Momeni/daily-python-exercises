"""
Problem #9: Most Repeated Character in a String

Problem Statement:
Write a function that takes a string and returns the character(s) that appear most frequently.
Spaces should be ignored.
If there are multiple characters with the same highest frequency, return them all as a list.

Approach:
- Strip leading/trailing spaces (optional, but helps clean input).
- Initialize an empty dictionary to store character counts.
- Iterate over each character in the string:
    - Skip spaces.
    - Count occurrences of the character using the built‑in `str.count()` method.
    - Store the count in the dictionary.
- Find the maximum count among the dictionary values.
- Collect all characters whose count equals that maximum.
- Return the list of most frequent characters.

"""

def most_reapeted_char(str1 : str):

    str1 = str1.strip()

    d = {}
    for i in str1:
        if i == " ":
            continue
        counter = str1.count(i)
        d[i] = counter
    
    most = max(d.values())
    most_char = []

    for j in d.keys():
        if d[j] == most:
            most_char.append(j)
    return most_char
    

if __name__ == "__main__":

    test_case = [

        ("Hello",['l']),
        ("mohammad",['m']),
        ("momo",['m','o']),
        ("zzzzzzzzzzz",['z']),
        ("i am mohammad reza momeni",['m']),
        ("ali",['a','l','i']),

    ]

    for input,expected in test_case:
        
        result = most_reapeted_char(input)

        if result == expected:
            print(f"[Pass] -> Result: {result}, expected: {expected}")
        else:
            print(f"[Error] -> Result: {result}, expected {expected}")