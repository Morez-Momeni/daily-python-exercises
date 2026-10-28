"""
Problem #83: Generate 3x3 Matrices of Prime Numbers
Date: 2026-10-29

Builds 3x3 matrices, each containing 3 consecutive prime numbers per row.
Collects 3 such rows to form a 3x3 matrix, then repeats for a total of 3 matrices.
"""

matrix = []
current_group = []
number = 2

while len(matrix) < 3:
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            break
    else:
        current_group.append(number)

        if len(current_group) == 3:
            matrix.append(list(current_group))
            current_group.clear()

    number += 1

print(matrix)
