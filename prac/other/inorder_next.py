from tree import Tree

def inorder_next(root,node):
    stack = [root]
    res = []
    path = getpath(root,node)
    if node.right:
        return left_most(node.right)
    prev = node
    path.pop()
    while path:
        temp = path.pop()
        if temp.right != prev:
            return temp
        prev = temp
    return None
def getpath(root,node):
    l =[]
    r = []
    if root == node:
        return [root]
    if root.left:
        l = getpath(root.left,node)
    if root.right:
        r = getpath(root.right,node)
    if l != [] or r != []:
        return [root] + l + r
    return []

def left_most(root):
    temp = root
    while temp.left:
        temp = temp.left
    return temp

t = Tree()
for i in range(15):
    t.insert(i)
print t.inorder(t.root)
for i in range(15):
    n = t.getNodeinstance(i)
    if inorder_next(t.root,n) != None:
        print n.val,"->",inorder_next(t.root,n).val
    else:
        print n.val,"->",None
