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

    def print_list(self):
        if not self.head:
            print "Empty list"
        else:
            temp=self.head
            while temp:
                if not temp.next:
                    print temp.val
                    temp=temp.next
                    continue
                print str(temp.val),"->",
                temp=temp.next

def nthToLast(k,head):
    temp=head
    count=0
    while temp:
        count+=1
        temp=temp.next
    if count<k:
        return None
    temp=head
    for i in range(count-k):
        temp=temp.next
    return temp,temp.val


def main():
    l=List()
    l.insert_val(1)
    l.insert_val(2)
    l.insert_val(3)
    l.print_list()
    node,val=nthToLast(1,l.head)
    print node.val,val
if __name__=="__main__":
    main()
