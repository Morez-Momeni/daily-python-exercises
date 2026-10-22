"""
Problem #79: Count Word Occurrences in a Phrase
Date: 2026-10-22

Counts how many times `word` appears (non-overlapping) in `phrase`.
"""

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


print(count_word_occurrences("incredible", "increinincrincredibleediblecredibledible"))