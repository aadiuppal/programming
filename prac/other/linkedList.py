class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LL:
    def __init__(self,head = None):
        self.head = head
    def insert(self,val):
        if not self.head:
            self.head = Node(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)
    def print_list(self):
        temp = self.head
        while temp:
            if not temp.next:
                print temp.val
            else:
                print temp.val,"->",
            temp = temp.next

"""
l= LL()
l.insert(1)
l.print_list()
l.insert(2)
l.print_list()
l.insert(3)
l.print_list()
l.insert(4)
l.print_list()
l.insert(5)
l.print_list()
l.insert(6)
l.print_list()
"""
