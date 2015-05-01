class Node():
	def __init__(self,val):
		self.val=val
		self.next=None

class List():
	def __init__(self,head=None):
		self.head=head
	def insert(self,node):
		if not self.head:
			self.head=node
		else:
			node.next=self.head
			self.head=node

	def insert_val(self,val):
		node=Node(val)
		self.insert(node)

	def print_list(self):
		node=self.head
		while node:
			print node.val
			node=node.next

class TreeNode():
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None

class Tree():
	def __init__(self,root=None):
		self.root=root
		self.storage=[]
	def check_node(self,node):
		if node.left and node.right:
			return False
		return True

	def insert(self,node):
		if not self.root:
			self.root=node
		else:
			tmp=self.root
			self.storage.append(tmp)
			while self.storage!=[]:
				tmp=self.storage[0]
				if self.check_node(tmp):
					new_node=tmp
					self.storage=[]
				if self.storage!=[]:
					if tmp.left:
						self.storage.append(tmp.left)
					if tmp.right:
						self.storage.append(tmp.right)
					del(self.storage[0])
			
			if not new_node.left:
				new_node.left=node
			else:
				new_node.right=node

	def insert_val(self,val):
		node=TreeNode(val)
		self.insert(node)


			
class Sol1():
	def __init__(self):
		self.stack=[]
		self.sum=0
	def tree_check(self,node,val):
		self.stack.append(node)
		self.sum=self.sum+node.val
		while self.stack!=[]:
			if  self.stack[-1].left or self.stack[-1].right:
				if self.stack[-1].left:
					if self.tree_check(self.stack[-1].left,val):
						return 1
				if self.stack[-1].right:
					if self.tree_check(self.stack[-1].right,val):
						return 1
			else:
				if self.sum == val:
					return 1
			self.sum=self.sum-self.stack[-1].val
			self.stack.pop()
			return 0 
		
class Sol2():
	def max_depth(self,node):
		if not node:
			return 0
		return 1+max(self.max_depth(node.left),self.max_depth(node.right))
	def min_depth(self,node):
		if not node:
			return 0
		return 1+min(self.min_depth(node.left),self.min_depth(node.right))
	def is_balanced(self,node):
		return self.max_depth(node)-self.min_depth(node)<1

class Sol3():	
	def add_to_tree(self,arr,start,end):
		if start>end:
			return Null
		mid=(start+end)/2
		n=node_new(arr[mid])
		node.left=add_to_tree(arr,start,mid-1)
		node.right=add_to_tree(arr,mid+1,enf)
		return n 
	

class inorder():
	def __init__(self):
		self.stack=[]

	def traverse(self,node):
		if not node:
			return
		self.stack.append(node)
		if self.stack[-1].left:
			self.traverse(self.stack[-1].left)
		print self.stack[-1].val
		if self.stack[-1].right:
			self.traverse(self.stack[-1].right)
		self.stack.pop()
		return

class preorder():
	def __init__(self):
		self.stack=[]
	def traverse(self,node):
		if not node:
			return
		self.stack.append(node)
		print self.stack[-1].val
		if self.stack[-1].left:
			self.traverse(self.stack[-1].left)
		if self.stack[-1].right:
			self.traverse(self.stack[-1].right)
		self.stack.pop()
		return

class postorder():
	def __init__(self):
		self.stack=[]
	def traverse(self,node):
		if not node:
			return
		self.stack.append(node)
		if self.stack[-1].left:
			self.traverse(self.stack[-1].left)
		if self.stack[-1].right:
			self.traverse(self.stack[-1].right)
		print self.stack[-1].val
		self.stack.pop()
		return



class  Bfs():
	def __init__(self,node):
		self.queue=[node]
	def bfs(self):
		#self.queue.append(node)
		while self.queue!=[]:
			print self.queue[0].val
			if self.queue[0].left:
				self.queue.append(self.queue[0].left)
			if self.queue[0].right:
				self.queue.append(self.queue[0].right)
			del(self.queue[0])
			
		
		
class Dfs():
	def __init__(self):
		self.stack=[]
	def dfs(self,node):
		self.stack.append(node)
		while self.stack!=[]:
			print self.stack[-1].val
			if self.stack[-1].left!=None:
				self.dfs(self.stack[-1].left)
			if self.stack[-1].right!=None:
				self.dfs(self.stack[-1].right)

			self.stack.pop()
			return

class Sol4():
	def __init__(self):
		self.queue=[]
		self.bfs=[]
		self.lists=[]
	def bfs_list(self,node):
		self.queue.append(node)
		while self.queue!=[]:
			self.bfs.append(self.queue[0].val)
			if self.queue[0].left:
				self.queue.append(self.queue[0].left)
			if self.queue[0].right:
				self.queue.append(self.queue[0].right)
			del(self.queue[0])
		i=1
		while self.bfs!=[]:
			l=List()
			for j in range(0,i):
				l.insert_val(self.bfs[0])
				del(self.bfs[0])
			self.lists.append(l)
			i=i*2

class Sol5():
	def bst_check(self,node):
		if node.left:
			if node.val<self.bst_check(node.left):
				return 0
		if node.right:
			if node.val>=self.bst_check(node.right):
				return 0
		if node.left or node.right:
			if not node.left:
				return max(node.val,self.bst_check(node.right))
			if not node.right:
				return max(node.val,self.bst_check(node.left))
			return max(node.val,self.bst_check(node.left),self.bst_check(node.right))
		return node.val
	def tree_check(self,node):
		if node.val<=self.bst_check(node):
			return 1
		return 0

l=List()
l.insert_val(1)
l.insert_val(1)
l.insert_val(1)
#l.print_list()
l.insert_val(2)
l.insert_val(3)
#l.print_list()
t=Tree()
t.insert_val(1)
t.insert_val(2)
t.insert_val(3)
t.insert_val(4)
t.insert_val(5)
t.insert_val(6)
b=Bfs(t.root)
b.bfs()
d=Dfs()
print "___"
d.dfs(t.root)
s1=Sol1()
s2=Sol1()
s3=Sol1()
s4=Sol1()
s5=Sol1()
print "___"
print s1.tree_check(t.root,7)
print "___"
print s2.tree_check(t.root,8)
print "___"
print s3.tree_check(t.root,10)
print "___"
print s4.tree_check(t.root,11)
s6=Sol2()
print "___"
print s6.is_balanced(t.root)
t.insert_val(7)
print s6.is_balanced(t.root)
print "___"
i=inorder()
i.traverse(t.root)
print "___"
p1=preorder()
p1.traverse(t.root)
print "___"
p2=postorder()
p2.traverse(t.root)
s7=Sol4()
s7.bfs_list(t.root)
for i in s7.lists:
	print "********"
	i.print_list()
s8=Sol5()
print s8.bst_check(t.root)
t1=Tree()
t1.insert_val(5)
t1.insert_val(4)
t1.insert_val(6)
t1.insert_val(3)
t1.insert_val(7)
print "___"
print s8.tree_check(t1.root)
