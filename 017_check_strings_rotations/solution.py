"""
Problem #17: Check if Two Strings are Rotations of Each Other


Write a function that takes two strings and returns True if one is a rotation of the other.
A rotation means shifting all characters circularly, e.g., "abcde" and "cdeab" are rotations.

Implementation:
- First, check if lengths are equal (if not, return False).
- If both are empty, return True.
- Then, repeatedly rotate the second string and compare with the first.
- If a match is found, return True; otherwise False.
"""



def check_string_rotation(s1,s2):
    if len(s1) == 0 and len(s2) == 0:
        return True
    if len(s1) == len(s2):
        n = 0
        while n < len(s2):
            ns = ""
            ns += s2[len(s2)-1]
            ns += s2[0:len(s2)-1]
            s2 = ns
            if s2 == s1:
                return True
            n+=1 
        return False
    else:
        return False    
    
if __name__ == "__main__":
    test_cases = [
        ("abcde", "cdeab", True),
        ("abcde", "abced", False),
        ("a", "a", True),
        ("", "", True),
        ("abc", "cab", True),
        ("abc", "acb", False),
        ("hello", "llohe", True),
        ("hello", "elloh", True),
        ("hello", "helol", False),
    ]

    for s1, s2, expected in test_cases:
        result = check_string_rotation(s1, s2)
        status = "P" if result == expected else "F"
        print(f"{status} {s1!r} vs {s2!r} → got {result}, expected {expected}")