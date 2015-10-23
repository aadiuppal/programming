class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class List:
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
    def cycleto(self,n):
        end = self.head
        temp = self.head
        while end.next:
            end = end.next
        for i in range(n-1):
            temp = temp.next
        end.next = temp

def cyc(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

l = List()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
print cyc(l.head)
l.cycleto(2)
print cyc(l.head)
