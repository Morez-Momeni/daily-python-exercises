# Problem 33: Numeric Key Encryption

## Problem
Write a script that takes a text and a numeric key sequence (e.g., `1,2,3`) and encrypts the text by shifting each character’s ASCII code by the corresponding key number. If the key is shorter than the text, it should repeat cyclically. If the key is longer, an error message should be shown.

**Example:**
- Text: `"abc"`
- Key: `1,2,3`
- Encryption:
  - `a` (97) + 1 = 98 → `b`
  - `b` (98) + 2 = 100 → `d`
  - `c` (99) + 3 = 102 → `f`
- Result: `"bdf"`

---