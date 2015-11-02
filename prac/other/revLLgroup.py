from linkedList import LL
def revInGroup(head,n):
    temp = head
    start = temp
    prev = None
    while temp:
        end = temp
        for i in range(1,n):
            end = end.next
            if not end:
                return head
        n_start = end.next
        last = None
        node = reverse(temp,n-1,last)
        if prev:
            prev.next = node
        else:
            head = node
        prev = temp
        temp.next = n_start
        temp = temp.next
    return head

def reverse(start,n,last):
    if n==1:
        last = start.next
        last.next = start
        return last
    temp = start.next
    node = reverse(temp,n-1,last)
    temp.next = start
    return node



l = LL()
for i in range(1,17):
    l.insert(i)
l.print_list()
l1 = LL(revInGroup(l.head,4))
l1.print_list()
