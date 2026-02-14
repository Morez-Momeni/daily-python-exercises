# Problem 2: Factorial

## Problem
Write a function that computes the factorial of a integer `n`.

## Definition
- `0! = 1`
- `n! = n × (n‑1)!` for `n > 0`

## Solutions

### 1. Recursive approach
Directly translates the mathematical definition into code:
- Base case: `n == 0` returns `1`.
- Recursive step: `n * factorial(n‑1)`.

### 2. Iterative approach
Uses a loop to multiply numbers from 1 to `n`.

## Complexity
| Approach    | Time  | Space |
|-------------|-------|-------|
| Recursive   | O(n)  | O(n)  |
| Iterative   | O(n)  | O(1)  |

## What I Learned
- How recursion uses the call stack.
- Trade‑offs between recursion and iteration.
