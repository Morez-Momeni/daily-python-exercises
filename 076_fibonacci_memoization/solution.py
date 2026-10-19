"""
Problem #76: Fibonacci with Memoization (Class-Based)
Date: 2026-10-19

Computes the n-th Fibonacci number using recursion with memoization
to avoid redundant calculations. The cache is stored in a private
instance attribute of the Fib class.
"""

class Fib:

    def __init__(self) -> None:
        self.__cache = {}

    def calc(self, n):
        if n == 1 or n == 2:
            return 1
        if n in self.__cache:
            return self.__cache[n]
        res = self.calc(n - 1) + self.calc(n - 2)
        self.__cache[n] = res
        return res


f = Fib()
print(f.calc(40))