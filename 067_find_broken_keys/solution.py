"""
Problem #67: Find Broken Keys (Keyboard Comparison)
Date: 2026-10-09

Given two strings of the same length — the correct text and the text typed
with a broken keyboard — find which keys are broken.

A key is considered broken if, at any position, its character in the correct
text differs from the character in the typed text. Duplicates are removed,
and the order of first appearance is preserved.
"""

def find_broken_keys(true_shape, false_shape):
    true_shape = list(true_shape)
    false_shape = list(false_shape)

    w = 0
    res = []
    while w < len(true_shape):
        if true_shape[w] != false_shape[w]:
            if true_shape[w] not in res:
                res.append(true_shape[w])
        w += 1
    return res


if __name__ == "__main__":
    test = [
        ("happy birthday", "hawwy birthday", ["p"]),
        ("starry night", "starrq light", ["y", "n"]),
        ("beethoven", "affthoif5", ["b", "e", "v", "n"]),
        ("mozart", "aiwgvx", ["m", "o", "z", "a", "r", "t"]),
        ("5678", "4678", ["5"]),
        ("!!??$$", "$$!!??", ["!", "?", "$"])
    ]

    for true_shape_word, false_shape_word, expected in test:
        result = find_broken_keys(true_shape_word, false_shape_word)
        if result == expected:
            print(f"[PASS] --> true-word-shape: [{true_shape_word}] and "
                  f"false-word-shape: [{false_shape_word}] our expected:[{expected}] --> result: [{result}] ")
        else:
            print(f"[FAILED] --> true-word-shape: [{true_shape_word}] and "
                  f"false_shape_word: [{false_shape_word}] our expected:[{expected}] --> result: [{result}] ")