class Solution:
    # @param s, a string
    # @return an integer
    def __init__(self):
	self.table={}
    def numDecodings(self, s):
        if self.numDec(s)<0:
            return 0
        else:
            return self.numDec(s)
    
    def numDec(self, s):
        count=0
        if len(s)<1:
            return 1
        if len(s)==1 and int(s)>0:
            return 1
        elif len(s)==1:
            return -1
        for i in range(0,2):
	    print s[:i+1]
            if int(s[:i+1])>26:
                continue
	    if s[i+1:] not in self.table.keys():
	            temp=self.numDec(s[i+1:])
		    self.table[s[i+1:]]=temp
            temp= self.table[s[i+1:]]
	    if temp!=-1:
                count+=temp
	print self.table
        return count

s=Solution()
s1="11"
st="4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
print s.numDec(s1)
