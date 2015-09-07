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
        while temp.next!=None:
            temp=temp.next
        new_node=Node(val)
        temp.next=new_node
        return self.head

    def print_list(self):
        if not self.head:
            print "Empty List"
            return
        else:
            temp=self.head
            while temp:
                if not temp.next:
                    print str(temp.val)
                    temp=temp.next
                    continue
                print str(temp.val)+"->",
                temp=temp.next

def deleteDups(head):
    table={}
    temp=head
    while temp:
        if temp.val in table:
            prev.next=temp.next
        else:
            table[temp.val]=1
            prev=temp
        temp=temp.next

def deleteDups_nostrore(head):
    temp=head
    prev=None
    while temp and temp.next:
        prev=temp
        l_iter=temp.next
        while l_iter:
            if temp.val==l_iter.val:
                if temp==prev:
                    temp.next=l_iter.next
                    prev=temp
                else:
                    prev.next=l_iter.next
            else:
                prev=l_iter
            l_iter=l_iter.next
        temp=temp.next

def main():
    l=List()
    l.insert_val(1)
    l.insert_val(1)
    l.insert_val(2)
    l.insert_val(3)
    l.insert_val(3)
    l.insert_val(3)
    l.insert_val(3)
    l.insert_val(1)
    l.insert_val(1)
    l.insert_val(1)
    l.insert_val(2)
    l.print_list()
    #deleteDups(l.head)
    deleteDups_nostrore(l.head)
    l.print_list()
    l.insert_val(2)
    l.print_list()
    #deleteDups(l.head)
    deleteDups_nostrore(l.head)
    l.print_list()
if __name__=="__main__":
    main()
