# Problem 1: Second Highest Number

## Problem
Write a function that takes a list of numbers and returns the second highest number.

## My Approach
I decided to implement a simple sorting algorithm (bubble sort) to arrange the numbers in descending order, then pick the second element. This approach is straightforward and helps me practice sorting algorithms.

### Step-by-step
1. Iterate through the list multiple times, swapping adjacent elements if they are out of order (smaller before larger for descending order).
2. After sorting, the largest number is at index 0, and the second largest at index 1.
3. Return the value at index 1.

## Edge Cases
- Duplicate numbers: The current solution may return the same number if duplicates exist. For example, `[5,5,5]` returns 5. Depending on requirements, we might need to find the second distinct highest. That can be fixed by converting to a set before sorting.
- List with less than 2 elements: Should return `None` or raise an exception. Not handled yet.

## What I Learned
- Bubble sort implementation.
