"""
Problem #87: Convert 2D Array Index to 1D Index
Date: 2026-11-18

Given a row and column in a 2D array, compute the corresponding
flat index (row-major order) using the formula:

    index = row * number_of_columns + col
"""

import numpy as np

array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


def index_2d_to_1d(row, col, array):
    array = np.array(array)
    arr_row, arr_col = array.shape
    number = (row * arr_col) + col
    return number


print(index_2d_to_1d(2, 3, array))