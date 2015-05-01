class Solution:
    # @param n, an integer
    # @return a string[]
    def generateParenthesis(self, n):
        if n<1:
            return []
        if n==1:
            return ["()"]
        p=[]
        temp=self.generateParenthesis(n-1)
        for i in range(0,len(temp)):
            p.append("("+temp[i]+")")
            p.append("()"+temp[i])
            if temp[i]+"()" not  in p:
                p.append(temp[i]+"()")
        return p

s=Solution()
n=4
print s.generateParenthesis(n)
