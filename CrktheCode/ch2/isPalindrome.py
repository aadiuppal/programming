class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class List:
    def __init__(self,head=None):
        self.head=head
    def insert_val(self,val):
        if not self.head:
            self.head=Node(val)
            return self.head
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(val)
        return temp
    def print_list(self):
        if not self.head:
            print "Empty List"
        else:
            temp=self.head
            while temp:
                if not temp.next:
                    print temp.val
                else:
                    print str(temp.val)+"->",
                temp=temp.next
def isPalindrome(head):
    temp=head
    rev_list=reverse_list_new(temp)
    while temp or rev_list:
        if temp.val!=rev_list.val:
            return False
        temp=temp.next
        rev_list=rev_list.next
    return True
def reverse_list(head):
    temp=head.next
    prev=head
    prev.next=None
    while temp:
        nex=temp.next
        temp.next=prev
        prev=temp
        temp=nex
    return prev
def reverse_list_new(head):
    temp=head
    prev=None
    while temp:
        node=Node(temp.val)
        node.next=prev
        temp=temp.next
        prev=node
    return prev
def isPalindrome_iter(head):
    stack=[]
    fast=head
    slow=head
    while fast and fast.next:
        stack.append(slow.val)
        slow=slow.next
        fast=fast.next.next
    if fast:
        slow=slow.next
    while slow:
        if slow.val!=stack.pop():
            return False
        slow=slow.next
    return True
def main():
    l=List()
    l.insert_val(1)
    l.insert_val(2)
    l.insert_val(3)
    l.insert_val(4)
    l.insert_val(3)
    l.insert_val(2)
    l.insert_val(1)
    l.print_list()
    #l1=List(reverse_list(l.head))
    #l1.print_list()
    print isPalindrome(l.head)
    print isPalindrome_iter(l.head)
if __name__=="__main__":
    main()
