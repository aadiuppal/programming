class TreeNode():
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None

class BSTree():
	def __init__(self,root=None):
		self.root=root
		self.storage=[]

	def insert_list_as_tree(self,arr):
		arr=sorted(arr)
		self.root=self.insert_arr_as_tree(arr,0,len(arr)-1)

	def insert_arr_as_tree(self,arr,start,end):
		if start>end:
			return None
		mid=(start+end)/2
		node=TreeNode(arr[mid])
		node.left=self.insert_arr_as_tree(arr,start,mid-1)
		node.right=self.insert_arr_as_tree(arr,mid+1,end)
		return node

	def inorder(self,node):
		if node:
			if node.left:
				self.inorder(node.left)
			print node.val,
			if node.right:
				self.inorder(node.right)

	def preorder(self,node):
		if node:
			print node.val,
			if node.left:
				self.inorder(node.left)
			if node.right:
				self.inorder(node.right)

	def isBalanced(self,node):
		left=self.getHeight(node.left)
		right=self.getHeight(node.right)
		if abs(left-right)>1:
			return False
		if node.left:
			if not self.isBalanced(node.left):
				return False
		if node.right:
			if not self.isBalanced(node.right):
				return False
		return True

	def getHeight(self,node):
		if node:
			return max(self.getHeight(node.left),self.getHeight(node.right))+1
		return 0


t=BSTree()
arr=[1,2,3,4,5,6]
t.insert_list_as_tree(arr)
t.inorder(t.root)
print
t.preorder(t.root)
print t.isBalanced(t.root)
