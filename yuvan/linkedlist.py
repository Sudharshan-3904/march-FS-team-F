class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.head = new_node

    def add(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

l1=Linkedlist()            
l1.add(10)
l1.add(20)
l1.add(30)
l1.add_beg(1)
l1.display()
            
        
