class ListNode():
	def __init__(self,val):
		self.val=val
		self.next=None
		self.prev=None

class DList():
	def __init__(self,head=None):
		self.head=head

	def insert_node(self,node):
		if not self.head:
			self.head=node
		else:
			temp=self.head
			while temp and temp.next:
				temp=temp.next
			temp.next=node
			node.prev=temp
	def insert_val(self,val):
		node=ListNode(val)
		self.insert_node(node)
	def print_list_f(self):
		temp=self.head
		while temp:
			print temp.val,
			temp=temp.next
		print
	def print_list_b(self):
		temp=self.head
		while temp and temp.next:
			temp=temp.next
		while temp:
			print temp.val,
			temp=temp.prev
		print
	def del_val(self,val):
		temp=self.head
		while temp.val!=val:
			temp=temp.next
		if not temp.prev and not temp.next:
			self.head=None
		elif not temp.prev:
			self.head=temp.next
			temp=temp.next
			temp.prev=None
		elif not temp.next:
			temp=temp.prev
			temp.next=None
		else:
			tem_prev=temp.prev
			tem_next=temp.next
			tem_prev.next=tem_next
			tem_next.prev=tem_prev

l=DList()
l.insert_val(1)
l.insert_val(3)
l.insert_val(2)
l.insert_val(6)
l.insert_val(5)
l.insert_val(4)
l.print_list_f()
l.print_list_b()

l.del_val(4)
l.print_list_f()
l.print_list_b()
l.del_val(1)
l.print_list_f()
l.print_list_b()
l.del_val(2)
l.print_list_f()
l.print_list_b()
l.del_val(5)
l.print_list_f()
l.print_list_b()
l.del_val(6)
l.print_list_f()
l.print_list_b()
l.del_val(3)
l.print_list_f()
l.print_list_b()
