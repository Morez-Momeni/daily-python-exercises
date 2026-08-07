def prime_number(number):
    result = 0
    for num in range(1,number):
        if  number % num == 0:
            result += num
    if result == number:
        return True
    else:
        return False

if __name__ == "__main__":
    
    test = [

        (6,True),
        (28,True),
        (496,True),
        (10,False),
        (43,False)
    ]

for input_number,excepted in test:
    result = prime_number(input_number)
    if result == excepted:
        print(f"(Pass) Input --> {input_number}, Excepted --> {excepted}, Result --> {result}")
    else:
        print(f"(Failed) Input --> {input_number}, Excepted --> {excepted}, Result --> {result}")