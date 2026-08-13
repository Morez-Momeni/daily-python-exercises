"""

bingo game 

"""
import random

MAX_NUM = 20 
MIN_NUM = 1 


def get_number():
   while True:
        try:
            user_input = int(input("Enter number:"))
            if user_input > MAX_NUM or user_input < MIN_NUM:
                print("your number should between 1,20")
                continue
        except ValueError:
            print("Error: invalid number")

        else:
            return user_input
           
       
def compare(user_number, random_number):
    print(user_number,random_number)
    if user_number == random_number:
        return True
    return False

def main():
    number = random.randint(MIN_NUM,MAX_NUM)
    
    i = 1
    while i <= 3:
        user_number = get_number()
        if compare(user_number , number):
            return True
        print("False try again")
        i+=1 
    return False

if __name__ == "__main__":
    print(main())

