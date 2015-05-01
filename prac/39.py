class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if not num:
            return num
        if len(num)<=2:
            return max(num)
        return max(self.rob(num[1:]),self.rob(num[2:])+num[0])

    def rob_new(self,num):
	if not num:
		return 0
	mid = len(num)/2
	if len(num)<=2:
		return max(num)
	return max(self.rob_new(num[:mid])+self.rob_new(num[mid+1:]),self.rob_new(num[:mid-1])+self.rob_new(num[mid+2:])+num[mid])

s=Solution()
num=[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
print s.rob_new(num)
print s.rob(num)

