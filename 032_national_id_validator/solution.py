"""
# Problem 33: Iranian National ID Validator

## Problem
Write a function that validates an Iranian National ID (کد ملی) using the official modulus-11 algorithm.

**Algorithm:**
1. The ID must be exactly 10 digits.
2. The last digit is the control digit.
3. Multiply each of the first 9 digits by weights 10 to 2 (from left to right).
4. Sum the products.
5. Compute the remainder of the sum divided by 11.
6. If the remainder is less than 2, the control digit must equal the remainder.
7. If the remainder is 2 or more, the control digit must equal (11 - remainder).

"""

def valid_national_id(n_id):
    control_number = ""
    place_number = 10 
    result = 0
    if len(n_id) == 10:
        control_number += n_id[-1]
        for num in n_id[0:-1]:
            result += int(num) * place_number  
            place_number -= 1
    else:
        extra_zeros = 10 -len(n_id)
        n_id = extra_zeros * '0' + n_id
        return valid_national_id(n_id) 
    answer = result % 11
    if answer >= 2 :
        answer = 11 - answer
        if answer == int(control_number):
            return True
    elif answer == int(control_number):
        return True
    return False   
print(valid_national_id("")) # replace your national id
