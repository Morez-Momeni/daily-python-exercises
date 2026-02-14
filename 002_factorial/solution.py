"""
Problem #2: Factorial of a Number (Recursive & Iterative)
Difficulty: Easy


Problem Statement:
Write a function to compute the factorial of a non-negative integer n.
Factorial of n (n!) is the product of all positive integers from 1 to n.
By definition, 0! = 1.

Approaches shown:
1. Recursive (follows mathematical definition)
2. Iterative (using a loop)

"""
def factor_recursion(num):
    if num == 0:
        return 1
    return num * factor(num-1)
        
print(factor_recursion(5))

print('-'*40)

def factor(num):
    result = 1
    for i in range(1,num+1):
        result*=i 
    return result

print(factor(5))

