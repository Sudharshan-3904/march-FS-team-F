class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self,head):
        self.head = None

    def add(self,data):
        if self.head == None:
            self.head=Node(data)

        else:
            itr = 0
            while itr:
                print(self.data)
                itr = itr.next
