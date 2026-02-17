"""
Problem #5: Check if Two Strings are Anagrams

Problem Statement:
Given two strings, write a function to determine if they are anagrams of each other.
Two strings are anagrams if they contain the same characters with the same frequencies,
ignoring case (optional) and considering only letters (if specified).

Approach:
- First compare lengths; if different, they cannot be anagrams.
- Define a helper function `count_char` that iterates over each character in the first string
  and compares its count in both strings using the `.count()` method.
- If all counts match, return True; otherwise, return False.
"""


def check_anagram(str1,str2):
    
    def count_char(s1,s2):
        for i in str1:
            if s1.count(i) != s2.count(i):
                return False
        else:
            return True
  
    if len(str1) == len(str2):
        if str1=="" and str2== "" :
            return f"strings are empty"
            if count_char(str1,str2) == True :  
                return True
            else:
                return False
        return False         
                
                

str1 = "silent"
str2 = "listen"

print(check_anagram(str1,str2))

str1 = "rat"
str2 = "car"

print(check_anagram(str1,str2))

str1 = ""
str2 = ""

print(check_anagram(str1,str2))
