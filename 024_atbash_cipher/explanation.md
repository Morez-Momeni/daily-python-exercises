# Problem 24: Atbash Cipher (Simple Implementation)

## Problem
Write a function that implements the **Atbash cipher** – a simple substitution cipher where each letter is replaced by its reverse in the alphabet (A↔Z, B↔Y, C↔X, …).  
The function should take a string and return the encoded string. If the input contains any character that is not an uppercase English letter, the function should return `"False input"`.

**Examples:**
- `"HELLO"` --> `"SVOOL"`
- `"ABC"`--> `"ZYX"`
- `"ZYX"` --> `"ABC"`