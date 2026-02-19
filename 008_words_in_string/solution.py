"""
Problem #8: Find Words in a String
Difficulty: Medium
Date: 2026-02-19

Problem Statement:
Write a function that takes a string and returns/extracts the words from it.
A word is defined as a sequence of characters separated by spaces.
The function should:
- Ignore single‑character strings except for specific ones ('a', 'A', 'i', 'I').
- Exclude numbers (both integers and floats) from the result.
- Print the remaining words with an index.

Current implementation:
- Splits the string on whitespace after stripping leading/trailing spaces.
- Keeps multi‑character items unconditionally.
- For single‑character items, keeps only those in the `special_char` list.
- Then removes numbers (int or float) by trying conversions.
- Finally prints the filtered list with line numbers.
"""


def find_words(my_str: str):
    
    if len(my_str) == 0 :
        return "empty string"
    
    no_words = []
    words =[]
    special_char =['a','A','i','I']

    result = my_str.strip().split()

    for i in result:
        if len(i) <= 1 :
            for ch in special_char:
                if i == ch :
                    words.append(i)
        else:
            words.append(i)

    words_without_int = []
    number = []

    for nm in words:        
        try:
            if type(int(nm)) == int:
                number.append(nm)         
        except:
            try:
                if type(float(nm)) == float :
                    number.append(nm)
            except:
                words_without_int.append(nm)  
            
    def show_result():
        for i in range(len(words_without_int)):
            print(f"{i+1}){words_without_int[i]}")
    
    return show_result()


x = "i was born in 1383.1 "
find_words(x)