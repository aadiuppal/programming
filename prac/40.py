class TreeNode():
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None

class Tree():
	def __init__(self,root=None):
		self.root=root

	def insert_arr_as_tree(self,arr):
		if len(arr)==1:
			node=TreeNode(arr[0])
			return node
		if len(arr)>1:
			mid=len(arr)/2
			node=TreeNode(arr[mid])
			node.left=self.insert_arr_as_tree(arr[:mid])
			node.right=self.insert_arr_as_tree(arr[mid+1:])
			return node
		return None

	def insert_arr(self,arr):
		self.root=self.insert_arr_as_tree(arr)

	def inorder(self,node):
		if node:
			if node.left:
				self.inorder(node.left)
			print node.val,
			if node.right:
				self.inorder(node.right)

	def common_ancestor(self,node1,node2,node):
		if self.tree_contains(node.left,node1) and self.tree_contains(node.right,node2):
			return node.val
		if self.tree_contains(node.right,node1) and self.tree_contains(node.left,node2):
			return node.val
		if self.tree_contains(node.left,node1) and self.tree_contains(node.left,node2):
			return self.common_ancestor(node1,node2,node.left)
		if self.tree_contains(node.right,node1) and self.tree_contains(node.right,node2):
			return self.common_ancestor(node1,node2,node.right)
		if self.tree_contains(node,node1) and self.tree_contains(node,node2):
			return node.val
		return None

	def tree_contains(self,node,node_find):
		if node:
			if node.val==node_find.val:
				return True
			if self.tree_contains(node.left,node_find):
				return True
			if self.tree_contains(node.right,node_find):
				return True
		return False

	def return_node(self,val,node):
		if node:
			if node.val==val:
				return node
			if self.return_node(val,node.left):
				return self.return_node(val,node.left)
			if self.return_node(val,node.right):
				return self.return_node(val,node.right)
		return None

t=Tree()
arr=[1,2,3,4,5,6,7]
t.insert_arr(arr)
t.inorder(t.root)
node1= t.return_node(1,t.root)
node2= t.return_node(2,t.root)
node3= t.return_node(3,t.root)
node4= t.return_node(4,t.root)
node5= t.return_node(5,t.root)
node6= t.return_node(6,t.root)
node7= t.return_node(7,t.root)
print
print t.common_ancestor(node3,node1,t.root)
