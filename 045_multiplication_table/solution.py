"""
Problem #45: Multiplication Table Printer
Date: 2026-09-09

This script prints a formatted multiplication table from 1 to 10
using nested loops and string formatting.
"""

for i in range(1, 11):
    for j in range(1, 11):
        print("{:>2d}x{:<2d}={:>4d}".format(i, j, i * j), end='|')
    print()