"""

Write a function to determine if a string has all unique characters (i.e., no
character is repeated)

"""


def check_unique(str1):
    
    if len(str1) == 0 :
        return False , f"Empty string"
    for ch in str1:
        if str1.count(ch) > 1:
            return False
    return True


print(check_unique("abc"))



if __name__ == "__main__":
    
    test_case = [
        
        ("abcde",True),
        ('a',True),
        ("aabb",False),
        ("admin",True),
        ("hello",False),
               
    ]
    
    for Input , expected in test_case:
        result = check_unique(Input)
        status = "P" if result == expected else "F"
        print(f"{status} Input: {Input} --> expected: {expected} --> got : {result}")