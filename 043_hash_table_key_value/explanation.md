# Problem 43: Hash Table with Key‑Value Support

## Problem
Implement a hash table that stores key‑value pairs. The table should support:
- `insert_to_hash_table(key, value)` – insert or update a key with a value.
- `get_value_by_key(key)` – return the value associated with the key.
- `contains(key)` – check if a key exists.
- `delete_value_by_key(key)` – remove the key‑value pair.

Use chaining to handle collisions. The hash function sums the ASCII codes of the key string and takes modulo 10.

## My Solution (Current Version)

I implemented a hash table as a list of 10 buckets, each bucket being a list of tuples `(key, value)`.