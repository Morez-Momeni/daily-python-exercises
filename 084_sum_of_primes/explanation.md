# Problem 84: Sum of Prime Numbers Below 51

## Problem
Compute the sum of all prime numbers below 51.

**Expected output:** `328`

## My Solution

```python
number = 2
sum = 0
while number < 51:
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            break
        elif number == 1:
            continue
    else:
        sum += number
    number += 1
print(sum)