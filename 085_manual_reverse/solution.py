"""
Problem #85: Reverse a String Manually
Date: 2026-11-06

Reverses an input string (or number) using a manual index loop,
without using slicing ([::-1]) or the built-in reversed() function.
"""

number = input("Enter a number: ")

loop_count = 1
index = len(number) - 1
reversed_number = ""

while loop_count <= len(number):
    reversed_number += number[index]
    loop_count += 1
    index -= 1

print(reversed_number)