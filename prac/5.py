# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
        if l1 and l2:
            sum=carry+l1.val+l2.val
            if sum>9:
                sum=sum-10
                carry=1
            s=ListNode(sum)
            head_s.next=s
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
                s.next=tmp
        if carry!=0:
                s=ListNode(carry)
                head_s.next=s
        return head_s
