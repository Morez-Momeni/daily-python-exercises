"""
Problem #51: Singly Linked List Implementation
Date: 2026-09-15

A complete singly linked list implementation with the following operations:
- append (add to end)
- prepend (add to beginning)
- length (count nodes)
- search (find indices of a value)
- delete (remove first occurrence of a value)
- display (print all values)
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def length(self):
        curr = self.head
        length = 0

        while curr is not None:
            length += 1
            curr = curr.next

        return length

    def search(self, data):
        result = []
        counter = 0
        curr = self.head

        while curr is not None:
            if curr.data == data:
                result.append(counter)

            curr = curr.next
            counter += 1

        return result

    def delete(self, data):
        curr = self.head
        prev = None

        while curr is not None:

            if curr.data == data:

                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next

                return

            prev = curr
            curr = curr.next

    def display(self):
        curr = self.head

        while curr is not None:
            print(curr.data)
            curr = curr.next


# Tests

link_list = LinkedList()

link_list.append(Node(20))
link_list.append(Node(20))
link_list.append(Node(40))
link_list.append(Node(50))

link_list.prepend(Node(10))

link_list.display()

print("Length:", link_list.length())

print("Search:", link_list.search(20))

link_list.delete(20)

print("After delete:")
link_list.display()