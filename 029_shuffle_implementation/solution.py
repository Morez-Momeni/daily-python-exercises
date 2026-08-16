"""
Problem #26: Implement Shuffle (Without Using random.shuffle)
Date: 2026-08-17

Write a function that shuffles a list (or any sequence) randomly without using
the built‑in `random.shuffle()` function. The output should be a new list with
the same elements in a random order.

Implementation:
- Generate a list of indices.
- Randomly pick an unused index and append the corresponding element to the result.
- Continue until all indices are used.
"""

import random

def shuffle(sequence):
    index = []
    index_used = []
    final_list = []
    for i in range(len(sequence)):
        index.append(i)

    while len(index_used) < len(index):
        number = random.choice(index)
        if number in index_used:
            continue
        index_used.append(number)
        final_list.append(sequence[number])
        
    return final_list


if __name__ == "__main__":
    x = [1, 2, 3, 3, 2, 1, 3, 444, 5]
    x2 = [1, 2]
    print("Original:", x)
    print("Shuffled:", shuffle(x))
    print("Original:", x2)
    print("Shuffled:", shuffle(x2))
