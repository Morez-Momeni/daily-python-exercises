# Problem 32: Iranian National ID Validator

## Problem
Write a function that validates an Iranian National ID (کد ملی) using the official modulus‑11 algorithm.

**Algorithm:**
1. The ID must be exactly 10 digits.
2. The last digit is the control digit.
3. Multiply each of the first 9 digits by weights 10 to 2 (from left to right).
4. Sum the products.
5. Compute the remainder of the sum divided by 11.
6. If the remainder is less than 2, the control digit must equal the remainder.
7. If the remainder is 2 or more, the control digit must equal (11 - remainder).

---