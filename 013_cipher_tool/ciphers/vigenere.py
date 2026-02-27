"""
Vigenère cipher implementation.
- Handles both uppercase and lowercase letters.
- Preserves non-alphabetic characters.
- Key is repeated cyclically.
- Encode/decode with proper position arithmetic.
"""


import string

class Vigenere:
    
    def __init__(self):
        
        self.__letters_upper = "".join((string.ascii_uppercase))
        self.__letters_lower = "".join((string.ascii_lowercase))
        self.__key = "key"
        
    def encode(self,str1):
        new_str1 = ""
        result = "" 
        for index,char in enumerate(str1):         
                x = index % len(self.__key)
                new_str1 += self.__key[x]
        for i in range(len(new_str1)):
            if str1[i].isupper():
                if new_str1[i].isupper():
                    key_pos = ord(new_str1[i]) - ord('A')
                else:
                    key_pos = ord(new_str1[i]) - ord('a')
                pos = ord(str1[i]) - ord('A')
                y = (pos + key_pos) % 26
                result += self.__letters_upper[y]
            elif str1[i].islower():
                if new_str1[i].isupper():
                    key_pos = ord(new_str1[i]) - ord('A')
                else:
                    key_pos = ord(new_str1[i]) - ord('a')
                pos = ord(str1[i]) - ord('a')
                y = (pos + key_pos) % 26
                result += self.__letters_lower[y]
            else:
                result += str1[i] 
        return result
    
    def decode(self,str1):
        new_str1 = ""
        result = "" 
        for index,char in enumerate(str1):         
                x = index % len(self.__key)
                new_str1 += self.__key[x]
        for i in range(len(new_str1)):
            if str1[i].isupper():
                if new_str1[i].isupper():
                    key_pos = ord(new_str1[i]) - ord('A')
                else:
                    key_pos = ord(new_str1[i]) - ord('a')
                pos = ord(str1[i]) - ord('A')
                y = (pos - key_pos) % 26
                result += self.__letters_upper[y]
            elif str1[i].islower():
                if new_str1[i].isupper():
                    key_pos = ord(new_str1[i]) - ord('A')
                else:
                    key_pos = ord(new_str1[i]) - ord('a')
                pos = ord(str1[i]) - ord('a')
                y = (pos - key_pos) % 26
                result += self.__letters_lower[y]
            else:
                result += str1[i] 
        return result
   
    def change_key(self,key): 
        self.__key = key
        return self.__key
        
    
v = Vigenere()
print(v.encode("HELLO!"))
z = v.encode("hello!")
print(v.decode(z))
