"""
Problem #42: Simple Hash Table with Chaining
Date: 2026-09-07

A simple implementation of a hash table using a list of lists (chaining) to handle collisions.
The hash function sums the ASCII values of characters and takes the modulo 10.
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



def insert_to_hash_table(name):

    index = hash_function(name)
    my_list[index].append(name) # type: ignore


def contains(name):
    index = hash_function(name)
    return True if name in  my_list[index] else False



insert_to_hash_table("Stuart")
insert_to_hash_table("Lisa")
print(contains("Stuart"))   
print(contains("Lisa"))     
print(contains("Alex"))     