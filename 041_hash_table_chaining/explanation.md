# Problem 42: Simple Hash Table with Chaining

## Problem
Implement a simple hash table with the following operations:
- `hash_function(value)` – returns an index (0–9) based on the sum of ASCII values of characters.
- `insert_to_hash_table(name)` – inserts a string into the hash table.
- `contains(name)` – checks if a string is present in the hash table.

The hash table uses **chaining** (a list of lists) to handle collisions.

---

## My Solution

I created a hash table as a list of 10 empty lists. The hash function sums the ASCII values of all characters in the string and computes the modulo 10 to get an index. Insertion appends the value to the list at that index. Lookup checks if the value exists in that list.