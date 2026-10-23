def lcm(num1: int,num2: int) -> int:
    if num1 == 0 or num2 == 0:
        return 0
    if num1 > num2:
        num2 , num1 = num1 , num2
    zarb = 1
    z1 = []
    z2 = []
    while True:
        x = num1 * zarb
        y = num2 * zarb
        z1.append(x)
        z2.append(y)
        if x in z2:
            return x
        zarb += 1

        

