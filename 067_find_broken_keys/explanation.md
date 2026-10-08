# Problem 67: Find Broken Keys (Keyboard Comparison)

## Problem
Two strings are given, both with the **same length**:
- `true_shape` – the text that was meant to be typed.
- `false_shape` – the text actually produced with a broken keyboard.

A key is considered **broken** if, at any position, the character in `true_shape` differs from the character in `false_shape`. Return the list of broken keys, **without duplicates**, in the order they first appear.

**Examples:**
- `("happy birthday", "hawwy birthday")` → `["p"]`
- `("beethoven", "affthoif5")` → `["b", "e", "v", "n"]`
- `("5678", "4678")` → `["5"]`

## My Solution

I used a single `while` loop over the character positions, comparing the two strings character by character