# Problem 15: Fibonacci Number

## Problem
Write a function that takes an integer `n` and returns the `n`‑th number in the Fibonacci sequence.

**Definition used in this solution:**
- F(1) = 0
- F(2) = 1
- F(n) = F(n-1) + F(n-2) for n > 2

So the sequence starts: 0, 1, 1, 2, 3, 5, 8, ...

**Example:**  
For `n = 7`, the function returns `8` (the 7th number).

---

## My Solution

I implemented an iterative approach that uses two variables `i` and `j` to keep track of the last two numbers.

