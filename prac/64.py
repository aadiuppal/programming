class Solution:
    # @param dividend, an integer
    # @param divisor, an integer
    # @return an integer
    def divide(self, dividend, divisor):
        count=1
        sign=1
        if divisor<0:
            sign=sign*-1
            divisor=divisor*-1
        if dividend<0:
            sign=sign*-1
            dividend=dividend*-1
	div=divisor
	if dividend<divisor:
		return 0
	if dividend==divisor:
		return 1*sign
	dividend-=divisor
        while dividend>divisor:
            count+=count
            dividend-=divisor
            divisor+=divisor
        count+=self.divide(dividend,div)
	return count*sign

s=Solution()
dividend=2147483648
divisor=-1
print s.divide(dividend,divisor)
