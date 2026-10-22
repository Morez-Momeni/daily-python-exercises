# Problem 79: Count Word Occurrences in a Phrase

## Problem
Write a function that counts how many times a word appears (non‑overlapping) inside a phrase.

**Example:**
- `word = "incredible"`, `phrase = "increinincrincredibleediblecredibledible"` → `1`

## My Solution

```python
def count_word_occurrences(word: str, phrase: str) -> int:
    if word == phrase:
        return 1
    count = 0

    while True:
        start = phrase.find(word)
        if start == -1:
            return count
        end = len(word) + start
        x = phrase[start:end]
        if x == word:
            count += 1
        phrase = phrase[end:]