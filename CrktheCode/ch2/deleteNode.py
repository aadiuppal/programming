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
        return self.head
    def print_list(self):
        if not self.head:
            print "Empty list"
            return
        temp=self.head
        while temp:
            if not temp.next:
                print temp.val
                temp=temp.next
                continue
            print str(temp.val)+"->",
            temp=temp.next
    def getNodefromVal(self,val):
        if not self.head:
            return
        temp=self.head
        while temp:
            if temp.val==val:
                return temp
            temp=temp.next
        return
def deleteNode(node):
    temp=node.next
    node.val=temp.val
    node.next=temp.next

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
    deleteNode(l.getNodefromVal(5))
    l.print_list()
if __name__=="__main__":
    main()
