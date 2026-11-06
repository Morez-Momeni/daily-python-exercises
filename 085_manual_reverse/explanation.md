# Problem 85: Reverse a String Manually

## Problem
Read a number (as a string) from the user and print it reversed — **without** using Python's `[::-1]` slicing or the built-in `reversed()`.

**Example:**
- Input: `12345` → Output: `54321`
- Input: `hello` → Output: `olleh`

## My Solution

```python
number = input("Enter a number: ")

loop_count = 1
index = len(number) - 1
reversed_number = ""

while loop_count <= len(number):
    reversed_number += number[index]
    loop_count += 1
    index -= 1

print(reversed_number)