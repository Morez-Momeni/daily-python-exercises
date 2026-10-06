"""
Problem #66: Letter Distance Between Two Words
Date: 2026-10-07

Compute the "letter distance" between two words:
- For each position, add the absolute difference of ASCII codes.
- For the extra characters in the longer word, add the length difference.
"""

def letter_distance(word1, word2):

    result = 0
    if len(word1) == len(word2):
        for idx in range(len(word1)):
            result += abs(ord(word1[idx]) - ord(word2[idx]))

        return result

    elif len(word1) > len(word2):
        for idx in range(len(word2)):
            result += abs(ord(word1[idx]) - ord(word2[idx]))
        result += abs(len(word1) - len(word2))

        return result
    elif len(word2) > len(word1):
        for idx in range(len(word1)):
            result += abs(ord(word2[idx]) - ord(word1[idx]))
        result += abs(len(word2) - len(word1))

        return result


if __name__ == "__main__":

    test = [

        ("sharp", "sharq", 1),
        ("abcde", "Abcde", 32),
        ("abcde", "bcdef", 5),
        ("house", "fly", 11),
        ("very", "fragile", 67),
        ("abcde", 'A', 36),
        ("abcde", 'e', 8)

    ]

    for fword, sword, expected in test:
        result = letter_distance(fword, sword)
        if result == expected:
            print(f"[PASS] --> first-word: [{fword}] and "
                  f"seccond-word: [{sword}] our expected:[{expected}] --> result: [{result}] ")
        else:
            print(f"[FAILED] --> first-word: [{fword}] and "
                  f"seccond-word: [{sword}] our expected:[{expected}] --> result: [{result}] ")