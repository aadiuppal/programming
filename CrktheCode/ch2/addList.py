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
            print "Empty List"
            return
        temp=self.head
        while temp:
            if not temp.next:
                print temp.val
                temp=temp.next
                continue
            print str(temp.val)+"->",
            temp=temp.next
def addList(head1,head2):
    temp1=head1
    temp2=head2
    carry=0
    res_list=List()
    while temp1 or temp2:
        if temp1 and temp2:
            val=temp1.val+temp2.val+carry
            temp1=temp1.next
            temp2=temp2.next
        elif not temp1:
            val=temp2.val+carry
            temp2=temp2.next
        elif not temp2:
            val=temp1.val+carry
            temp1=temp1.next
        if val>=10:
            carry=1
            res_list.insert_val(val-10)
        else:
            carry=0
            res_list.insert_val(val)
    return res_list.head
def addRevList(head1,head2):
    if head1.next and head2.next:
        res,carr=addRevList(head1.next,head2.next)
    if not head1.next and not head2.next:
        res=None
        carr=0
    node_val=head1.val+head2.val+carr
    if node_val>=10:
        node=Node(node_val-10)
        node.next=res
        carr=1
    else:
        node=Node(node_val)
        node.next=res
        carr=0
    return node, carr
def pad_zeros(n,head):
    while n>0:
        node=Node(0)
        node.next=head
        head=node
        n-=1
    return head
def wrap_addRevList(head1,head2):
    temp1=head1
    temp2=head2
    c1=0
    c2=0
    while temp1:
        temp1=temp1.next
        c1+=1
    while temp2:
        temp2=temp2.next
        c2+=1
    if c1>c2:
        head2=pad_zeros(c1-c2,head2)
    elif c2>c1:
        head1=pad_zeros(c2-c1,head1)
    res,carr=addRevList(head1,head2)
    if carr==1:
        node=Node(1)
        node.next=res
        res=node
    return res
def main():
    l1=List()
    l2=List()
    l1.insert_val(6)
    l1.insert_val(1)
    l1.insert_val(7)
    l2.insert_val(2)
    l2.insert_val(9)
    l2.insert_val(5)
    l1.print_list()
    l2.print_list()
    l3=List(addList(l1.head,l2.head))
    l3.print_list()
    l4=List(wrap_addRevList(l1.head,l2.head))
    l4.print_list()
if __name__=="__main__":
    main()
