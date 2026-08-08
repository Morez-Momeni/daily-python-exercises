"""
# Problem 24: Atbash Cipher (Simple Implementation)

## Problem
Write a function that implements the **Atbash cipher** a simple substitution cipher where each letter is
replaced by its reverse in the alphabet (A↔Z, B↔Y, C↔X, …).  
The function should take a string and return the encoded string.
If the input contains any character that is not an uppercase English letter, the function should return `"False input"`.



"""



def atbash(user_input):

    first_half = "ABCDEFGHIJKLM"
    second_half = "ZYXWVUTSRQPON"
    result = ""

    for char in user_input:
        if char in first_half:
            index = first_half.find(char)
            result += second_half[index]
        elif char in second_half:
            index = second_half.find(char)
            result += first_half[index]

        else:
            return f"False input"
    
    return result


if __name__ == "__main__":
    
    test_inputs = ["HELLO", "WORLD", "ABC", "ZYX"]
    for s in test_inputs:
        print(f"{s} --> {atbash(s)}")