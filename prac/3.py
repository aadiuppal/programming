class Solution:
    # @param A, a list of integer
    # @return an integer
    def __init__(self):
        self.storage=[]
    def singleNumber(self, A):
        for i in range(0,len(A)):
            self.storage.append([])
        for i in A:
            val=self.hash(i,len(A))
            self.storage[val].append(i)
            
        for i in range(0,len(self.storage)):
            if len(self.storage[i])%2!=0:
                index=i
        prev=[]
        count=0
        j=0
        l= len(self.storage[index])
        list =sorted(self.storage[index])
	print list
        for i in range(0,l):
            prev.append(list[i])
            count+=1
	    print prev
            if prev:
                if prev[0]!= prev[-1] and j == 1:
                    	print "Here"
			return prev[0]
            if i==l-1:
                return list[i]
	    j=count%2
	    if prev and j==0:
		prev=[]
        

    def hash(self,x,l):
        return x%l




a=[10,186,-49,176,118,167,-61,189,6,-24,7,-93,71,112,187,45,-36,38,82,108,-46,112,51,165,-37,159,1,-53,7,38,90,181,-23,91,-42,172,-95,130,84,149,-47,68,126,-67,175,22,121,131,84,114,60,64,182,-75,-17,-71,69,-92,103,-91,-91,86,126,166,33,-36,-80,-37,118,-80,-18,127,36,-71,-82,-82,144,12,57,149,71,91,-83,-100,-30,45,186,16,-51,-72,-83,107,140,-97,-93,1,12,189,-61,-50,180,98,96,-29,193,167,57,-45,16,6,-76,4,109,-23,22,144,190,-97,193,-51,-99,-79,-47,142,107,175,109,121,190,90,34,32,63,-24,41,-53,41,89,130,-18,-99,103,86,127,-30,102,32,-49,181,-60,114,60,-29,182,-75,168,96,51,33,142,108,69,10,-57,166,48,82,161,-17,-50,102,63,-45,140,180,176,-95,36,-46,168,187,161,-72,-100,-42,165,-76,-67,89,159,64,34,98,4,-60,172,-79,68,48,131,-57]
s=Solution()
print s.singleNumber(a)
