"""
Problem #74: Camel Case to Snake Case Converter
Date: 2026-10-17

Converts a camelCase (or PascalCase) string to snake_case:
- Each uppercase letter (except the first character) is preceded by an underscore
  and converted to lowercase.
- The first character is lowercased without adding an underscore.
"""

def camel_to_snake(string):
    index = []

    res = ""
    for i in range(len(string)):
        if string[i].isupper():
            index.append(i)
    string = list(string.lower())
    for idx, c in enumerate(string):
        if idx in index and idx != 0:
            res += '_' + c
        else:
            res += c
    return res