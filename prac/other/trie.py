class Node:
    def __init__(self,val):
        self.val = val
        self.next = {}

class Trie:
    def __init__(self,head=None):
        self.head = head
    def insert(self,val):
        if not self.head:
            self.head = Node("")
        temp = self.head
        prev = temp
        for i in range(len(val)+1):
            try:
                if val[i] in temp.next:
                    prev = temp
                    temp = temp.next[val[i]]
                else:
                    break
            except:
                break
        prev = temp
        if i == len(val):
            return
        for j in range(i,len(val)):
            prev.next[val[j]] = Node(val[j])
            prev = prev.next[val[j]]
    def print_trie(self):
        stack = [self.head]
        while stack:
            print [i.val for i in stack]
            temp = stack.pop()
            print temp.val
            for i in temp.next:
                stack.append(temp.next[i])

t= Trie()
t.insert("asd")
t.insert("ase")
t.insert("asq")
t.print_trie()
