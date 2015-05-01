class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if len(num1) ==0 or len(num2)==0:
            return
        powr=10
        sum=0
        for i in range(len(num1)-1,-1,-1):
	    mul_fac_i=powr**(len(num1)-1-i)
            for j in range(len(num2)-1,-1,-1):
		mul_fac_j=powr**(len(num2)-1-j)
                sum=sum+mul_fac_i*mul_fac_j*(ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
        return sum

s=Solution()
a="12"
b="5"
print s.multiply(a,b)
