class Caesar:
    
    def __init__(self):
        
        self.__shift = 3
    
    def caesar_encode(self,str1):
        result = ""
        for char in str1:
            result += chr(ord(char)+self.__shift)
            
        return result

    def caesar_decode(self,str1):
        result = ""
        for char in str1:
            result += chr(ord(char)-self.__shift)
            
        return result

    def change_shift(self,shift):
        self.__shift = shift
        
