# Problem 73: Check Registration Rules

## Problem
Write a function `check_registration_rules(**kwargs)` that receives usernames and passwords as keyword arguments and returns a list of usernames allowed to register.

**Rules:**
1. Usernames `"quera"` and `"codecup"` are reserved — not allowed.
2. Username must be at least **4 characters** long.
3. Password must be at least **6 characters** long.
4. Password must **not** consist only of digits.

The order of the returned list does not matter.