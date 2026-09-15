# Problem 51: Singly Linked List Implementation

## Problem
Implement a singly linked list from scratch with the following operations:
- `append(data)` – add a new node at the end.
- `prepend(data)` – add a new node at the beginning.
- `length()` – return the number of nodes.
- `search(data)` – return a list of indices where the value appears.
- `delete(data)` – remove the first occurrence of a value.
- `display()` – print all values in order.

## My Solution

I created two classes:
- **`Node`** – holds a `data` value and a `next` pointer.
- **`LinkedList`** – manages the chain of nodes starting from `head`.