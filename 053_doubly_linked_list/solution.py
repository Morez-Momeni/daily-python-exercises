"""
Problem #53: Doubly Linked List Implementation
Date: 2026-09-17

A doubly linked list implementation where each node has both `next` and `prev` pointers.
Supports:
- add (append to end)
- return_as_list
- delete (by value)
- display (forward)
- display_reverse (backward)
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkList:

    def __init__(self) -> None:
        self.head = None

    def add(self, new_node):

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def return_as_list(self):
        items = []
        if self.head is None:
            return
        curr = self.head
        while curr is not None:  # type: ignore
            items.append(curr.data)  # type: ignore
            curr = curr.next  # type: ignore
        return items

    def delete(self, val):

        if self.head is None:
            return

        curr = self.head

        while True:  # type: ignore

            if curr.data == val:
                if curr.prev is None and curr.next is None:
                    self.head = None
                    return

                if curr.prev is None:
                    curr = curr.next
                    curr.prev = None
                    self.head = curr
                    return

                elif curr.next is None:
                    curr = curr.prev
                    curr.next = None
                    return

                else:
                    x = curr.next
                    y = curr.prev
                    y.next = x  # type: ignore
                    x.prev = y
                    return
            curr = curr.next  # type: ignore
            if curr is None:
                return

    def display(self):
        if self.head is None:
            return
        curr = self.head
        while curr is not None:  # type: ignore
            print(curr.data)  # type: ignore
            curr = curr.next  # type: ignore

    def display_reverse(self):
        if self.head is None:
            return
        curr = self.head
        while curr.next is not None:  # type: ignore
            curr = curr.next  # type: ignore

        last_item = curr
        while last_item is not None:  # type: ignore
            print(last_item.data)  # type: ignore
            last_item = last_item.prev  # type: ignore



link_list = LinkList()
link_list.add(Node(12))

print(link_list.delete(12))

link_list.display()
print("-" * 50)
link_list.display_reverse()