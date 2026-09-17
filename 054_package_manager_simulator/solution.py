"""
Problem #54: Package Manager Simulator (MorezPkgManager)
Date: 2026-09-17

A simple package manager simulator built on top of a doubly linked list.
Each node represents a package (file) with a name, size, and a download status.
The manager supports:
- add    : append a new package to the list.
- delete : remove a package by name.
- complete : mark a package as downloaded (status = True).
- display : print all packages with their status.
"""


class Node:
    def __init__(self, file_name, size) -> None:

        self.filename = file_name
        self.size = size
        self.status = False
        self.next = None
        self.prev = None


class MorezPkgManager:

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

    def delete(self, val):

        if self.head is None:
            return

        curr = self.head

        while True:  # type: ignore

            if curr.filename == val:
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

    def complete(self, file_name):
        curr = self.head
        while curr is not None:  # type: ignore
            if curr.filename == file_name and curr.status == False:
                curr.status = True
                print(f"{file_name}, Downloaded.")
                return
            curr = curr.next  # type: ignore

    def display(self):
        if self.head is None:
            return
        curr = self.head
        while curr is not None:  # type: ignore
            print(f"Name: {curr.filename}, Status: {curr.status}")  # type: ignore
            curr = curr.next  # type: ignore


# Test
mpg = MorezPkgManager()

mpg.add(Node("ubuntu", 2))
mpg.add(Node("ubuntu", 2))

mpg.add(Node("kubuntu", 2))

mpg.complete("ubuntu")
mpg.complete("ubuntu")

mpg.display()