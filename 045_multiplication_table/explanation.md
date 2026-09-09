# Problem 45: Multiplication Table Printer

## Problem
Write a script that prints a multiplication table (1–10) in a nicely formatted grid. Each cell should show `i x j = result`, aligned with consistent spacing. Separate columns with a pipe (`|`) character.

## My Solution (Current Version)

I used two nested loops: the outer loop iterates over `i` (1 to 10) for rows, and the inner loop iterates over `j` (1 to 10) for columns. The `print()` statement uses Python's string formatting to align the numbers, and `end='|'` to separate columns.