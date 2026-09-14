"""
simple linked-list

"""

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None



current = Node(100)
node2 = Node(200)
node3 = Node(300)

current.next = node2 # type: ignore
node2.next = node3 # type: ignore


while current is not None:
    print(current.data)
    current = current.next