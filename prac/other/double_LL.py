class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class doubleLL:
    def __init__(self,head = None):
        self.head = head
    def insert(self,val):
        if not self.head:
            self.head = Node(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        n = Node(val)
        temp.next = n
        n.prev = temp
    def print_list(self):
        temp = self.head
        while temp:
            if not temp.next:
                print temp.val
            else:
                print temp.val,"<->",
            temp = temp.next
    def print_back(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            if not temp.prev:
                print temp.val
            else:
                print temp.val,"<->",
            temp = temp.prev



#d= doubleLL()
#for i in range(5):
#    d.insert(i)
#d.print_list()
#d.print_back()
