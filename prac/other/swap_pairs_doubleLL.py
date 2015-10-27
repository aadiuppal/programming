from double_LL import doubleLL

def swapPairs(head):
    if not head or not head.next:
        return head
    temp = head
    temp_n = head.next
    trav = temp_n.next

    temp.next = trav
    temp_n.next = temp
    head = temp_n

    prev = temp
    temp = trav
    while temp and temp.next:
        temp_n = temp.next
        trav = temp_n.next

        prev.next = temp_n
        temp.next = trav
        temp_n.next = temp

        prev = temp
        temp = trav
    temp = head
    temp.prev = None
    prev = temp
    temp = temp.next
    while temp:
        temp.prev = prev
        prev = temp
        temp = temp.next
    return head


d = doubleLL()
for i in range(10):
    d.insert(i)

d.print_list()
d.print_back()
d1 = doubleLL(swapPairs(d.head))
d1.print_list()
d1.print_back()
