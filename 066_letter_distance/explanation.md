# Problem 66: Letter Distance Between Two Words

## Problem
Write a function `letter_distance(word1, word2)` that computes a numeric "distance" between two words based on their characters. The rule is:

1. For each position where both words have a character, add the **absolute difference of their ASCII codes**.
2. If one word is longer, add the **difference in length** (the number of extra characters).

**Examples:**
- `("sharp", "sharq")` → 1 (only the last letter differs: `p` vs `q`)
- `("abcde", "Abcde")` → 32 (`a` = 97, `A` = 65, difference = 32)
- `("house", "fly")` → 11 (5 chars vs 3 chars → 2 extra + character differences)
- `("abcde", "e")` → 8 (`a` vs `e` = 4, plus 4 extra characters)