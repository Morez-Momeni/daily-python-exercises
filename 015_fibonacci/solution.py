"""
Problem #15: Fibonacci Number

Write a function that takes an integer n and returns the  number in the Fibonacci sequence.
The sequence is defined as:
- F(1) = 0
- F(2) = 1
- F(n) = F(n-1) + F(n-2) for n > 2
"""

def fibonaci(n):
    i = 0
    j = 1
    if n == 1:
        return 0
    for z in range(n-1):
        i, j = j, j + i
    return i

if __name__ == "__main__":
    
    test_values = [1, 2, 3, 4, 5, 6, 7]
    for num in test_values:
        print(f"F({num}) = {fibonaci(num)}")