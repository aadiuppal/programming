class minStack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self,val):
        self.stack.append(val)
        if self.minstack!=[]:
            self.minstack.append(min(self.minstack[-1],val))
        else:
            self.minstack.append(val)
    def pop(self):
        self.minstack.pop()
        return self.stack.pop()
    def minval(self):
        return self.minstack[-1]
    def print_stack(self):
        for i in range(len(self.stack)):
            if i==len(self.stack)-1:
                print self.stack[i]
            else:
                print str(self.stack[i])+"<-",
s=minStack()
s.push(1)
s.push(2)
s.push(3)
print s.minval()
s.push(-11)
s.push(-1)
s.push(0)
print s.minval()
s.print_stack()
