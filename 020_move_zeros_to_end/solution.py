"""

Given a list of integers, write a function to move all zeros to the end of the
list while maintaining the order of the other elements.


"""

def move_all_zeros_to_the_end(int_list):
    non_zero_list = []
    zero_list = []
    for i in int_list:
        if i == 0:
            zero_list.append(i)
        else:
            non_zero_list.append(i)
    return non_zero_list + zero_list

my_list = [0,1,4,6,2,0,345,0,11,7,34]
print(move_all_zeros_to_the_end(my_list))