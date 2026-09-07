"""
Problem #43: Hash Table with Key-Value Support (Insert, Get, Contains, Delete)
Date: 2026-09-07

A simple hash table implementation with chaining. Each bucket stores tuples of (key, value).
Supports:
- Insert (with update if key exists)
- Get value by key
- Contains check
- Delete by key
"""

my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
] 

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10



def insert_to_hash_table(name, value):
    index = hash_function(name)
    for n in my_list[index]:
       if n[0] == name:
           print(f"find {name}")
           my_list[index].remove(n)
           
           
    my_list[index].append((name, value)) # type: ignore


def contains(name):
    result = get_value_by_key(name)
    if not result[0]: # type: ignore
       return False
    return True
        
def get_value_by_key(key_name):
   index = hash_function(key_name)
   for items in my_list[index]:
      if items[0] == key_name:
         return True , items[1]
   return False 


def delete_value_by_key(key_name):
   if contains(key_name):
      index = hash_function(key_name)
      for n in my_list[index]:
          if n[0] == key_name:
            my_list[index].remove(n)
            return True
   return False 
      
      

insert_to_hash_table("Stuart",4)
insert_to_hash_table("Lisa",5)
insert_to_hash_table("Lisa",0)
print(get_value_by_key("Stuarta"))
print(contains("Lisa"))
print(delete_value_by_key("Stuart"))
print(my_list)