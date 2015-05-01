class Solution:
    # @param n, an integer
    # @return a string[]
    def __init__(self):
        self.p=[]
        self.s=""
    def generateParenthesis(self, n):
        if n>0:
            self.gen(n,0,0,0)
        return self.p
        
    def gen(self,n,start,close,pos):
        if close==n:
            self.p.append(self.s)
            self.s=""
	    return
	else:
	        if start>close:
	            m=len(self.s)
		    self.s+=")"
	            self.gen(n,start,close+1,pos+1)
		    self.s=self.s[:m]
		  
	        if start<n:
	            self.s+="("
	            self.gen(n,start+1,close,pos+1)

s=Solution()
n=2
print s.generateParenthesis(n)
