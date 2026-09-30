class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
a = Node(10)
b = Node(20)
a.next = b
head = a
new_node = Node(5)
new_node.next = head
head = new_node
temp = head
while temp:
    print(temp.data, end=" → ")
    temp = temp.next
    
    
    