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

def inorder_rec(root):
    l = []
    r = []
    if root.left:
        l = inorder_rec(root.left)
    if root.right:
        r = inorder_rec(root.right)
    return l + [root.val] + r

def inorder(root):
    curr = root
    res = []
    stack = []
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if not stack:
                break
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
            while curr == None:
                if not stack:
                    break
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
    return res

t = Tree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)
print "Now inorder"
print inorder_rec(t.root)
print inorder(t.root)
