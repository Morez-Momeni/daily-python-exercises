"""
Problem #3: Filter Out Palindromes
Difficulty: Easy


Problem Statement:
Given a list of strings, write a function that returns a new list containing only the strings that are NOT palindromes.
A palindrome is a string that reads the same forwards and backwards (e.g., "radar", "level").

Approaches:
1. Using string slicing (word[::-1]) clean and Pythonic.
2. Manual reversal building the reversed string character by character (no slicing).

"""

def filter_out_palindromes_without_list_slicing(words):
    not_palindromes = []
    palindromes = []
    while True:
        if len(words) > 0:
            word = words.pop()
            lenght = len(word)+1
            compare_string= ""
            for i in range(-1,-lenght,-1):
                compare_string+=word[i]
            if compare_string == word:
                palindromes.append(word)
            else:
                not_palindromes.append(word)
        else:
            break
    return not_palindromes




def filter_out_palindromes(words):
    not_palindromes = []
    for word in words:
        if word != word[::-1]:
            not_palindromes.append(word)
    return not_palindromes
    

def main():
    while True:
        print("1)filter_out_palindromes\n2)filter_out_palindromes_without_list_slicing\n3)exit")
        menu_option = int(input("Enter your number ::"))
        
        if menu_option == 1:
            number_of_word = int(input("number of words ::"))
            words = []
            print("Enter your words ::")
            for i in range(number_of_word):
                x = input(f"{i+1}) ")
                words.append(x)
            print(filter_out_palindromes(words))
            
        elif menu_option == 2:
            number_of_word = int(input("number of words ::"))
            words = []
            print("Enter your words ::")
            for i in range(number_of_word):
                x = input(f"{i+1}) ")
                words.append(x)
            print(filter_out_palindromes_without_list_slicing(words))
            
        elif menu_option == 3:
            break
        
        else:
            continue
main()