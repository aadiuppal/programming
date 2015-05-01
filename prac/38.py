class Solution:
    # @param x, an integer
    # @return an integer
    def reverse(self, x):
        x=str(x)
        mul=1
        new_x=""
        if x[0]=="-":
            x=x[1:]
            mul=-1
        for i in range(len(x)-1,-1,-1):
            new_x+=x[i]
        result=int(new_x)*mul
        if (result>2147483647) or (result < -2147483648):
	    print result 
            return 0
        return result

s=Solution()
n=1
print s.reverse(n)
