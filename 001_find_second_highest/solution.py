"""
Problem #001: Find the Second Highest Number
Difficulty: Easy

Problem Statement:
Given a list of numbers, return the second highest distinct number.

Approach:
- Sort the list in descending order (using bubble sort for learning purposes, though inefficient).
- Return the element at index 1.

"""

def second_highest_number(arr):
    
    it_num = len(arr)
    for i in range(it_num):
        for j in range(it_num):
            if arr[i] > arr[j]:
                temp = arr[j]
                arr[j]= arr[i]
                arr[i]= temp
                
    return arr[1]


print(second_highest_number([-10, -20, -30, -5]))