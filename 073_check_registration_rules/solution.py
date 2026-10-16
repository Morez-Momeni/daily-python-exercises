"""
Problem #73: Check Registration Rules
Date: 2026-10-16

Validates usernames and passwords based on registration rules:
- Usernames "quera" and "codecup" are reserved.
- Username must be at least 4 characters long.
- Password must be at least 6 characters long and not consist only of digits.
Returns a list of allowed usernames.
"""

def check_registration_rules(**kwargs):
    user = []

    for key, val in kwargs.items():
        if len(key) < 4 or len(val) < 6 or val.isdigit() or key == "quera" or key == "codecup":
            continue
        else:
            user.append(key)

    return user


print(check_registration_rules(queraa='s1212ass2', ali='88'))