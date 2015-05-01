class ListNode():
	def __init__(self,val):
		self.val=val
		self.next=None

class Stack():
	def __init__(self,head=None):
		self.list=[]

	def push(self,arr):
		try:
			for i in arr:
                        	self.list.append(i)			
		except TypeError:
			self.list.append(arr)

	def pop(self):
		return self.list.pop()

	def print_stack(self):
		print self.list

	def isEmpty(self):
		if self.list==[]:
			return True
		return False

s1=Stack()
s2=Stack()
def enqueue(val):
	while not s2.isEmpty:
		s1.push(s2.pop())
	s1.push(val)
	s1.print_stack()

def dequeue():
	while not s1.isEmpty():
		s2.push(s1.pop())
	s2.print_stack()
	return s2.pop()

enqueue(2)
enqueue(3)
enqueue(4)
dequeue()
dequeue()
dequeue()
