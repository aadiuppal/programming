# Definition for singly-linked list.
class ListNode:
     def __init__(self, val):
         self.val = val
         self.next = None
class List:
     def __init__(self,head=None):
	self.head = head
     def insert(self,node):
	if not self.head:
		self.head=node
	else:
		node.next=self.head
		self.head=node
     def insert_value(self,val):
	node=ListNode(val)
	self.insert(node)
     def print_list(self):
	node=self.head
	while node:
		print node.val
		node=node.next

     def insert_end(self,node):
	if not self.head:
		self.head=node
	else:
		temp=self.head
		while temp:
			prev=temp
			temp=temp.next
		prev.next=node

     def insert_value_end(self,val):
	node=ListNode(val)
	self.insert_end(node)
"""
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
	if head.next:
	        node=head
        	temp=node.next
		node.next=temp.next
		temp.next=node
		head=temp
	else:
		return head
	node=head.next
        while node.next:
		temp1=node.next
		temp2=temp1.next
		temp1.next=temp2.next
		temp2.next=temp1
		node.next=temp2
		node=temp1
	return head
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry=0
        if l1 and l2:
            sum=l1.val+l2.val
            if sum>9:
                sum=sum-10
                carry=1
            head_s=ListNode(sum)

            l1=l1.next
            l2=l2.next
        if l1 or l2:
            if not l1:
                l1=ListNode(0)
            if not l2:
                l2=ListNode(0)
            sum=carry+l1.val+l2.val
            if sum>9:
                sum=sum-10
                carry=1
            else:
                carry=0
            s=ListNode(sum)
            head_s.next=s
	    head=head_s
            while l1.next or l2.next:
            	if not l1.next:
                    l1.val=0
	        else:
	            l1=l1.next
        	if not l2.next:
                    l2.val=0
	        else:
	            l2=l2.next
        	sum=carry+l1.val+l2.val
	        if sum>9:
	            sum=sum-10
	            carry=1
        	else:
 	            carry=0
        	tmp=ListNode(sum)
	        head_s.next=tmp
	        head_s=head_s.next
        if carry!=0:
            t=ListNode(carry)
            head_s.next=t
        return head



l1=List()
l2=List()
#l1.insert_value(8)
l1.insert_value(9)
#l1.insert_value_end(6)
#l1.insert_value(3)
l1.print_list()
l2.insert_value(9)
l2.insert_value(9)
l2.insert_value(9)
l2.insert_value(9)
l2.insert_value(9)
l2.insert_value(9)
l2.insert_value(9)
l2.insert_value(9)
l2.insert_value(9)
l2.insert_value(1)

l2.print_list()
s=Solution()
l=s.addTwoNumbers(l1.head,l2.head)
print "_______________"
while l:
	print l.val
	l=l.next
