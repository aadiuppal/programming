class ListNode():
	def __init__(self,val):
		self.val=val
		self.next=None

class List():
	def __init__(self,head=None):
		self.head=head

	def insert_node_end(self,node):
		if not self.head:
			self.head=node
		else:
			temp=self.head
			while temp.next:
				temp=temp.next
			temp.next=node

	def insert_node_start(self,node):
		if not self.head:
			self.head=node
		else:
			node.next=self.head
			self.head=node
	def insert_val_end(self,val):
		node=ListNode(val)
		self.insert_node_end(node)

	def insert_val_start(self,val):
		node=ListNode(val)
		self.insert_node_start(node)

	def print_list(self):
		if not self.head:
			return
		else:
			temp=self.head
			while temp:
				print temp.val,
				temp=temp.next

	def make_it_circular_from_end(self,index):
		temp1=self.head
		temp2=self.head
		for i in range(0,index):
			temp1=temp1.next
		while temp2.next:
			temp2=temp2.next
		temp2.next=temp1
	def find_loop(self):
		temp1=self.head
		temp2=self.head.next
		while temp2 and temp2.next:
			if temp1.val==temp2.val:
				return 1
			temp1=temp1.next
			temp2=temp2.next.next
		return 0

	def print_list_circular(self,len):
		temp1=self.head
		for i in range(0,len):
			print temp1.val,
			temp1=temp1.next

l=List()
l.insert_val_start(5)
l.insert_val_start(6)
l.insert_val_end(7)
l.insert_val_end(8)
l.print_list()
print "Loop",
print l.find_loop()
l.make_it_circular_from_end(1)
l.print_list_circular(8)
print "Loop",
print l.find_loop()
