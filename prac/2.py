class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.storage=[]
        self.st_min=[]
    def push(self, x):
        self.storage.append(x)
        if not self.st_min or self.st_min[len(self.st_min)-1]>=x:
            self.st_min.append(x)
        return x

    # @return nothing
    def pop(self):
        #del self.storage[-1]
        if self.top() <= self.st_min[len(self.st_min)-1]:
            self.st_min.pop()
        self.storage.pop()

    # @return an integer
    def top(self):
        return self.storage[len(self.storage)-1]

    # @return an integer
    def getMin(self):
        return self.st_min[len(self.st_min)-1]

m=MinStack()
m.push(-2)
print m.storage
m.push(0)
m.push(-1)
print m.storage
print m.getMin()
print m.top()
m.pop()
print m.storage
print m.getMin()
