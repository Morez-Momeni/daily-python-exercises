# Problem 70: smart_zip - Extended zip() Function

## Problem
Design a function `smart_zip` similar to Python's built-in `zip`, but with extra features:

**Parameters:**
- `arr1`, `arr2` – two input lists. If `len(arr1) < len(arr2)`, swap them.
- `fill` (bool) – if `True`, pad the shorter list with `fill_char`; if `False`, truncate the longer list.
- `fill_char` – the fill character (default `""`).
- `sort` (bool) – if `True`, sort both lists before zipping.

**Special conditions:**
- If `arr1` has duplicates, remove them **before** zipping (keep the **last** occurrence, though the code actually keeps the first).
- If lengths are unequal and `sort` is `True`, sorting is skipped.