class setOfStacks:
    def __init__(self):
        self.stack_arr=[]
    def push(self,val):
        if self.stack_arr==[]:
            s=Stack()
            s.push(val)
            self.stack_arr.append(s)
        else:
            curr=self.stack_arr[-1]
            if len(curr.stack)==curr.max_len:
                s=Stack()
                s.push(val)
                self.stack_arr.append(s)
            else:
                curr.push(val)
    def pop(self):
        if self.stack_arr==[]:
            return None
        else:
            curr=self.stack_arr[-1]
            if len(curr.stack)>1:
                val=curr.pop()
                self.stack_arr=self.stack_arr[:-1]+[curr]
            else:
                val=curr.pop()
                self.stack_arr=self.stack_arr[:-1]
        return val
    def print_set(self):
        for i in self.stack_arr:
            print i.stack
class Stack:
    def __init__(self,lenmax=3):
        self.stack=[]
        self.max_len=lenmax
    def push(self,val):
        if len(self.stack)<self.max_len:
            self.stack.append(val)
        else:
            print "stack Full"
    def pop(self):
        return self.stack.pop()
def popAt(index,set_stack):
    return shifter(index,set_stack)
def shifter(index,set_stack):
    curr,st_index,el_index=set_stack.getStack(index)
    if curr==set_stack[-1]:
        if el_index<len(curr.stack)-1:
            set_stack=set_stack[:-1]+[set_stack[-1][:el_index]]+[set_stack[-1][el_index+1:]]
        else:
            set_stack=set_stack[:-1]+[set_stack[-1][:-1]]
    else:
        set_stack.stack_arr[st_index][:el_index]+set_stack.stack_arr[st_index][el_index+1:]
s1=setOfStacks()
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)
s1.push(7)
s1.push(8)
s1.push(9)
s1.print_set()
print s1.pop()
s1.print_set()
print s1.pop()
s1.print_set()
print s1.pop()
s1.print_set()
print s1.pop()
s1.print_set()
print s1.pop()
s1.print_set()

