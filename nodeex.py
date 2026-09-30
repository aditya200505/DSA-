class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
a = Node(10)
print(a)
print(a.data)
print(a.next)
b = Node(20)
a.next = b
print(a.next)
print(a.next.data)