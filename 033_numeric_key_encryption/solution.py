text = "i am mohammad"

key_sequence = input("Enter your key sep with (,):").split(',')

key_iter = 0
result = ""

if len(text) > len(key_sequence):
    for char in range(len(text)):
        try:
            new_char = ord(text[char]) + int(key_sequence[key_iter])
            key_iter += 1
            result += chr(new_char)
        except IndexError:
            key_iter = 0
            new_char = ord(text[char]) + int(key_sequence[key_iter])
            key_iter += 1
            result += chr(new_char)

elif len(text) == len(key_sequence):
    for char in range(len(text)):

        new_char = ord(text[char]) + int(key_sequence[key_iter])
        key_iter += 1
        result += chr(new_char)

else:
    print("key cant be more than text lenght")
        
print(result)