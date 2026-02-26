"""
Atbash cipher implementation.
- Maps each letter to its reverse in the alphabet: A↔Z, B↔Y, etc.
- Uppercase and lowercase are handled separately.
- Non-letters remain unchanged.

"""


class Atbash:
    def __init__(self):
        self.__upper_char_first_half = "ABCDEFGHIJKLM"
        self.__upper_char_second_half = "ZYXWVUTSRQPON"
        self.__lower_char_first_half = "ABCDEFGHIJKLM".lower()
        self.__lower_char_second_half  = "ZYXWVUTSRQPON".lower()
        
    def encode(self,str1):
        result = ""
        for ch in str1:
            if ch.isupper():
                if ch in self.__upper_char_first_half :
                    index = self.__upper_char_first_half.find(ch)
                    result += self.__upper_char_second_half[index]
                elif ch in self.__upper_char_second_half :
                    index = self.__upper_char_second_half.find(ch)
                    result += self.__upper_char_first_half[index]
            elif ch.islower():
                if ch in self.__lower_char_first_half  :
                    index = self.__lower_char_first_half .find(ch)
                    result += self.__lower_char_second_half[index]
                elif ch in self.__lower_char_second_half :
                    index = self.__lower_char_second_half.find(ch)
                    result += self.__lower_char_first_half [index]
            else:
                result += ch
        return result
    
    def decode(self,str1):
        result = ""
        for ch in str1:
            if ch.isupper():
                if ch in self.__upper_char_first_half :
                    index = self.__upper_char_first_half.find(ch)
                    result += self.__upper_char_second_half[index]
                elif ch in self.__upper_char_second_half :
                    index = self.__upper_char_second_half.find(ch)
                    result += self.__upper_char_first_half[index]
            elif ch.islower():
                if ch in self.__lower_char_first_half  :
                    index = self.__lower_char_first_half .find(ch)
                    result += self.__lower_char_second_half[index]
                elif ch in self.__lower_char_second_half :
                    index = self.__lower_char_second_half.find(ch)
                    result += self.__lower_char_first_half [index]
            else:
                result += ch
        return result


