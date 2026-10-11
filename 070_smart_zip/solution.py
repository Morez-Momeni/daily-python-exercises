"""
Problem #70: smart_zip - Extended zip() Function
Date: 2026-10-12

A custom zip-like function with:
- Auto-swap so the first list is the longer one.
- Optional fill (pad the shorter list) or truncate.
- Optional sorting before zipping.
- Deduplication of the first list (keeps last occurrence).
- Returns a dictionary instead of a list of tuples.
"""

def smart_zip(arr1 : list, arr2 : list, fill=False, fill_char="", sort=False):
    uq_arr1 = []
    if len(arr1) != len(arr2):
        sort = False

    if len(arr1) < len(arr2):
        for i in arr1:
            if i not in uq_arr1:
                uq_arr1.append(i)
        arr1, arr2 = arr2, uq_arr1
    else:
        for i in arr1:
            if i not in uq_arr1:
                uq_arr1.append(i)
        arr1, arr2 = uq_arr1, arr2

    if fill:
        needed_none = len(arr1) - len(arr2)
        for _ in range(needed_none):
            arr2.append(fill_char)

    elif not fill:
        cutted = len(arr1) - len(arr2)
        for _ in range(cutted):
            arr1.pop()

    if sort:
        arr1.sort()
        arr2.sort()

    res = {}
    counter = 0
    while len(res) != len(uq_arr1):
        res[arr1[counter]] = arr2[counter]
        counter += 1
    return res