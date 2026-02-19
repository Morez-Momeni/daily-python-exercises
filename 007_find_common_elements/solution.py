"""
Problem #7: Find Common Elements Between Two Lists

Problem Statement:
Write a function that takes two lists and returns a list of elements that appear in both lists.
The order of elements in the result should follow the order of the first list.
If an element appears multiple times in the first list and also exists in the second list,
it will appear multiple times in the result (duplicates preserved).

Approach:
- Use nested loops: for each element in the first list, iterate through the second list.
- If a match is found, append the element to the result list.
- This preserves duplicates and order from the first list.
 
"""

def find_common(list1,list2):
    common = []
    for i in list1:
        for j in list2:
            if i == j:
                common.append(i) 
        
    return common

if __name__ == "__main__":
    
    test_case = (
        [[1,2,3,4,5,[]],[1,2,3,4,5,[]],[1,2,3,4,5,[]]],
        [[1,2,3,4,5,[]],[1,8,7,6,5],[1,5]],
        [[],[],[]],
        [["a","b"],["c","d"],[]],      
    )
    
    for input1,input2,expected in test_case:
        result = find_common(input1,input2)
        if result == expected :
            print(f"[Pass] -> Result: {result}, expected: {expected}")
        else:
            print(f"[Error] -> Result: {result}, expected {expected}")