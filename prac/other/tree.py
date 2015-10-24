class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self,root = None):
        self.root = root
    def insert(self,val):
        if not self.root:
            self.root = Node(val)
            return
        qu = [self.root]
        while qu:
            temp = qu[0]
            qu = qu[1:]
            if not temp.left:
                temp.left = Node(val)
                return
            else:
                qu.append(temp.left)
            if not temp.right:
                temp.right = Node(val)
                return
            else:
                qu.append(temp.right)

    def inorder(self,root):
        if not root:
            return []
        l = []
        r = []
        if root.left:
            l = self.inorder(root.left)
        if root.right:
            r = self.inorder(root.right)
        return l + [root.val] + r
    def getNodeinstance(self,val):
        stack = [self.root]
        while stack:
            temp = stack.pop()
            if temp.val == val:
                return temp
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return None
