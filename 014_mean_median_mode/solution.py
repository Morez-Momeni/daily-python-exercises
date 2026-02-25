"""
Problem #14: Calculate Mean, Median, and Mode (Without Built-in Functions)


Write a function that takes a list of numbers and returns its mean, median, and mode.
- Mean: average of all numbers.
- Median: middle value when sorted (average of two middle values for even length).
- Mode: most frequent value(s); if multiple, return all.
Do not use statistics module or numpy; implement manually.

"""



def mean_mode_median(list1 : list):
    if len(list1) == 0:
        return False,f"{list1} is empty "
    
    list1 = sorted(list1)
    
    def mean():
        mean = sum(list1) / len(list1)
        return mean
    
    def mode():
        number_count = {}
        mode_number = []
        for i in list1:
            x = list1.count(i)
            number_count[i]=x
        maximum = max(number_count.values())
        for key,value in number_count.items():
            if value == maximum:
                mode_number.append(key)
        return mode_number
    def median():
        
        if len(list1) % 2 == 0:
            half = len(list1) // 2
            result = (list1[half-1] + list1[half]) / 2
        else:
            half = len(list1) // 2
            result = list1[half]    
        return result
            
    return mean() , mode() ,median()
    

if __name__ == "__main__":
    
    test_data = [1, 2, 3, 4, 3, 7, 8, 8, 8, 8, 4, 6, 1]
    mean_val, mode_val, median_val = mean_mode_median(test_data)
    print(f"Data: {test_data}")
    print(f"Mean: {mean_val}")
    print(f"Mode: {mode_val}")
    print(f"Median: {median_val}")