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
    def get_last_node(self):
        if not self.head:
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        return temp
def partitionList(head,val):
    s_list=List()
    h_list=List()
    c_list=List()
    temp=head
    while temp:
        if temp.val<val:
            s_list.insert_val(temp.val)
        if temp.val>val:
            h_list.insert_val(temp.val)
        if temp.val==val:
            c_list.insert_val(temp.val)
        temp=temp.next
    s_last=s_list.get_last_node()
    c_last=c_list.get_last_node()
    if c_last:
        s_last.next=c_list.head
        c_last.next=h_list.head
    else:
        s_last.next=h_list.head
    return s_list.head

def main():
    l=List()
    l.insert_val(9)
    l.insert_val(2)
    l.insert_val(8)
    l.insert_val(29)
    l.insert_val(9)
    l.insert_val(1)
    l.insert_val(3)
    l.insert_val(62)
    l.insert_val(5)
    l.insert_val(5)
    l.print_list()
    l1=List(partitionList(l.head,5))
    l1.print_list()
if __name__=="__main__":
    main()
