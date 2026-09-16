"""
Terminal History Simulator
Date: 2026-09-16

A simple terminal history simulator that stores every command the user types
in a linked list. It supports three special commands:
- `-his`    : clear screen and display the full history.
- `-clear`  : clear the screen (and record the command in history).
- `-search` : search the history for a specific command.
Any other input is stored in history as a regular command.
"""

import os
import time


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

    def display(self):
        curr = self.head
        idx = 0
        while curr is not None:
            print(idx, curr.data)
            idx += 1
            curr = curr.next


def clean():
    os.system("cls" if os.name == "nt" else "clear")


link_list = LinkedList()


while True:
    try:
        command = input(">").strip()

        if "-his" == command:
            clean()
            link_list.display()
            link_list.append(Node(command))
        elif "-clear" == command:
            link_list.append(Node(command))
            clean()
        elif "-search" == command:
            clean()
            search_command = input("Enter Command to Search in History:")
            result = link_list.search(search_command)
            for idx in result:
                print(idx, search_command)
        else:
            link_list.append(Node(command))

    except KeyboardInterrupt:
        break