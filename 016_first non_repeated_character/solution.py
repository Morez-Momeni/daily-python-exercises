"""
Problem #18: Find the First Non-Repeated Character in a String


Write a function that returns the first character that appears only once.
If no such character exists, return None.

Implementation:
- Loop through the string in order.
- For each character, count its occurrences using str.count().
- If count is 1, return that character immediately.
- If loop finishes, return None.
"""



def first_non_repeated_char(str1):
    
    if len(str1) == 0:
        return None
    
    for i in str1:
        counter = str1.count(i)
        if counter > 1:
            continue
        else:
            return i
            



if __name__ == "__main__":
    
    test_case = (
        
        ["aabbcc",None],
        ["abc",'a'],
        ["",None],
        ['a','a'],
        ["mohammad reza momeni",'h'],
        ["swiss", 'w'],
        ["teeter", 'r'],
            
    )
    
    for Input,Expected in test_case:
        result = first_non_repeated_char(Input)
        if result == Expected :
            print(f"[PASS]: Input: {Input} ---> Expected: {Expected} ---> Output: {result}")
        else:
            print(f"[FAIL]: Input: {Input} ---> Expected: {Expected} ---> Output: {result}")