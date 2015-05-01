class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        max_sum=0
        sum=0
        start=-1
        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum<0:
                sum=0
            elif sum>max_sum:
                max_sum=sum
                start=i
        if start==-1:
            return max(nums)
        return max_sum

s=Solution()
n=[-2,1,-3,4,-1,2,1,-5,4]
print s.maxSubArray(n)
