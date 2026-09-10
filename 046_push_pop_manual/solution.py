"""
push and pop methode
"""


data_set = []


def push(data : list) -> bool: 
    global data_set

    if not len(data):
        data_set += [data] 

    else:
        data_set += data
    return True

def pop():
    global data_set
    index_last_data = len(data_set)-1
    last_item = data_set[index_last_data]
    data_set = data_set[0:index_last_data]
    return last_item
         


# --------------------
# Tests
# --------------------



# Test 1: push with normal values
push(["A", "B", "C"])

assert data_set == ["A", "B", "C"]

# Test 2: push with empty list
push([])

assert data_set == ["A", "B", "C", []]

# Test 3: push with different data types
push([10, "hello", True, None])

assert data_set == ["A", "B", "C", [], 10, "hello", True, None]

# Test 4: push with duplicate values
push(["A", "A", "B"])

assert data_set == [
    "A", "B", "C", [], 10, "hello", True, None,
    "A", "A", "B"
]

# Test 5: pop last item
result = pop()

assert result == "B"

assert data_set == [
    "A", "B", "C", [], 10, "hello", True, None,
    "A", "A"
]

# Test 6: pop duplicate value
result = pop()

assert result == "A"

assert data_set == [
    "A", "B", "C", [], 10, "hello", True, None,
    "A"
]

# Test 7: pop until empty
while len(data_set) > 0:
    pop()

assert data_set == []

print("All tests passed!")