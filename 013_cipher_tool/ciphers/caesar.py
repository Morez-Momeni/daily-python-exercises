"""
Caesar cipher implementation.
- Uses two fixed alphabets (lowercase and uppercase).
- Shift can be changed at runtime.
- Encode and decode are symmetric.
"""

import string

class Caesar:
    
    def __init__(self):
        
        self.__shift = 3
        self.__letters_lower = "".join((string.ascii_lowercase))
        self.__letters_upper = "".join((string.ascii_uppercase))
    
    def encode(self,str1):
        result = ""
        for char in str1:
            if char.isupper() :
                x = (self.__letters_upper.find(char)+self.__shift) % 26
                result += self.__letters_upper[x]
            elif char.islower():
                x = (self.__letters_lower.find(char)+self.__shift) % 26
                result += self.__letters_lower[x]
            else:
                result += char
                    
        return result

    def decode(self,str1):
        result = ""        
        for char in str1:
            if char.isupper() :
                x = (self.__letters_upper.find(char)-self.__shift) % 26
                result += self.__letters_upper[x]
            elif char.islower():
                x = (self.__letters_lower.find(char)-self.__shift) % 26
                result += self.__letters_lower[x]
            else:
                result += char
                    
        return result
        

    def change_shift(self,shift):
        self.__shift = shift
        


