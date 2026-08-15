"""
Problem #27: Password Generator
Date: 2026-08-15

A simple password generator that creates a random password of a given length
using a combination of uppercase letters, lowercase letters, digits, and special characters.

"""

import string
from numpy import random

class GEN_PASS:

    def __init__(self):

        self.chars = string.ascii_letters + string.digits + "~!@#$%^&*()_-+=><"

    def generate(self,lenght):
        password = ""
        
        for _ in range(lenght):
            password += random.choice(list(self.chars))

        return password




p = GEN_PASS()
print(p.generate(66))

