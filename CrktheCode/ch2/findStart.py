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
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(val)
        return self.head
    def print_list(self):
        if not self.head:
            print "Empty List"
        else:
            temp=self.head
            while temp:
                if not temp.next:
                    print temp.val
                    temp=temp.next
                    continue
                print str(temp.val)+"->",
                temp=temp.next
    def loop_node_fromEnd(self,val):
        end=self.head
        node=self.getNode_fromVal(val)
        while end.next:
            end=end.next
        end.next=node
    def getNode_fromVal(self,val):
        temp=self.head
        while temp:
            if temp.val==val:
                return temp
            temp=temp.next
        return None
def findStart(head):
    slow=head
    fast=head
    start=True
    while slow!=fast or start:
        slow=slow.next
        fast=fast.next.next
        start=False
    slow=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow
def main():
    l=List()
    l.insert_val(1)
    l.insert_val(2)
    l.insert_val(3)
    l.insert_val(4)
    l.insert_val(5)
    l.insert_val(6)
    l.insert_val(7)
    l.print_list()
    l.loop_node_fromEnd(4)
    node=findStart(l.head)
    print node,node.val
if __name__=="__main__":
    main()
