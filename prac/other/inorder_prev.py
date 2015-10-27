from tree import Tree

def inorder_prev(root,node):
    if node.left:
        temp = node.left
        while temp.right:
            temp = temp.right
        return temp
    path = getpath(root,node)
    prev = path.pop()
    while path:
        temp = path.pop()
        if temp.left != prev:
            return temp
        prev = temp
    return None
def getpath(root,node):
    if not root.left and not root.right:
        if node == root:
            return [root]
        else:
            return []
    l = []
    r = []
    if root.left:
        l = getpath(root.left,node)
    if root.right:
        r = getpath(root.right,node)
    if l == [] and r == []:
        return []
    return [root] + l + r



t = Tree()
for i in range(15):
    t.insert(i)
print t.inorder(t.root)
for i in range(15):
    n = t.getNodeinstance(i)
    if inorder_prev(t.root,n) != None:
        print inorder_prev(t.root,n).val,"->",n.val
    else:
        print None,"->",n.val
