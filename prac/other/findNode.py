class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BST:
    def __init__(self,root = None):
        self.root = root
    def insert_val(self,val):
        if not self.root:
            self.root = Node(val)
            return
        self.insert_node(self.root,val)
    def insert_node(self,node,val):
        if val > node.val:
            if node.right:
                self.insert_node(node.right,val)
            else:
                node.right = Node(val)
        else:
            if node.left:
                self.insert_node(node.left, val)
            else:
                node.left = Node(val)
    def print_tree(self):
        qu = [[self.root,0]]
        result = []
        l_max = -1
        while qu:
            temp,lev = qu[0]
            qu = qu[1:]
            result.append([temp,lev])
            if temp.left:
                qu.append([temp.left,lev+1])
            if temp.right:
                qu.append([temp.right,lev+1])
            l_max = max(l_max,lev)
        printer = [[] for i in range(l_max+1)]
        for i in result:
            printer[i[1]].append(i[0].val)
        for i in printer:
            for j in i:
                print j,
            print

def findNode(root,val):
    if not root:
        print "not found"
        return False
    if root.val == val:
        print "Found"
        return True
    if val > root.val:
        findNode(root.right,val)
    else:
        findNode(root.left,val)

t = BST()
t.insert_val(5)
t.insert_val(2)
t.insert_val(6)
t.insert_val(4)
t.insert_val(1)
t.insert_val(3)
t.insert_val(8)
t.insert_val(7)
t.print_tree()
findNode(t.root,5)
findNode(t.root,1)
findNode(t.root,2)
findNode(t.root,3)
findNode(t.root,4)
findNode(t.root,6)
findNode(t.root,7)
findNode(t.root,8)
findNode(t.root,9)
findNode(t.root,10)
findNode(t.root,-1)
findNode(t.root,-2)
