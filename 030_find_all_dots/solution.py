"""
Problem #30: Find All Positions of a Character in a String
Date: 2026-08-17

Write a function that finds and prints all positions (indices) of a specific character
in a given string. This implementation finds all dots ('.') in the input string.

Uses the `str.find()` method in a loop to locate each occurrence.
"""

# Find all positions of '.' in the string
file = "a.sd.zs.d.sd"

index = -1
while True:
    index = file.find('.', index + 1)
    if index == -1:
        break
    print(index)
