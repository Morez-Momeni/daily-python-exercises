"""
Problem #11: Check if String Contains All Letters of the Alphabet


Problem Statement:
Write a function that checks if a string contains every letter of the English alphabet at least once.
Case should be ignored. The function should return a boolean value.

Approach:
- Convert the string to lowercase.
- Iterate over each letter of the alphabet.
- If any letter is missing, immediately return False.
- If all letters are found, return True.
"""


import string


def check_char(str1):
    str1 = str1.lower()
    sample = "".join(string.ascii_lowercase)
    flag = False
    for ch in sample:
        if ch in str1:
            flag = True
        else:
            flag = False
            return flag
    return flag
print(check_char("The quick brown fox jumps over the lazy dog"))