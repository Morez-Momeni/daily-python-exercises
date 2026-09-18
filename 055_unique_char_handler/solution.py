"""
Problem #55: Count Duplicates and Extract Unique Characters
Date: 2026-09-18

This script:
1. Counts how many times each character appears in a string (ignoring spaces).
2. Extracts only the characters that appear exactly once.
3. Joins those unique characters into a new string.

Three functions are used:
- count_duplicated_char(string) : returns a dict {char: count}
- get_unique_chars(string)     : returns a list of characters with count == 1
- attach_chars(string)          : joins the list into a single string
"""

string = "Hello mohammad it is teest for reemove duplicaate char"


def count_duplicated_char(string):
    duplicate_count = {}
    for char in string:
        if char == ' ':
            continue
        if char in duplicate_count.keys():
            continue
        n = string.count(char)
        duplicate_count[char] = n
    return duplicate_count


def get_unique_chars(string):
    char_dict = count_duplicated_char(string)
    uniqe_char = []
    for key in char_dict.keys():
        if char_dict[key] == 1:
            uniqe_char.append(key)
    return uniqe_char


def attach_chars(string):
    chars = get_unique_chars(string)
    result = ""
    for char in chars:
        result += char
    return result


print(attach_chars(string))