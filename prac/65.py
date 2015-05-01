class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        l=[]
        if len(candidates)<1:
            return l
        candidates=sorted(candidates)
        if candidates[0]>target:
            return l
	if candidates[0]==target:
		return [candidates[0]]
        if self.combinationSum(candidates[1:],target):
            l+=self.combinationSum(candidates[1:],target)
	if self.combinationSum(candidates,target-candidates[0]):
	    l+=[candidates[0]]+self.combinationSum(candidates,target-candidates[0])
        return l

s=Solution()
can=[48,22,49,24,26,47,33,40,37,39,31,46,36,43,45,34,28,20,29,25,41,32,23]
can1=[2,3,6,7]
tar=69
tar1=7
print s.combinationSum(can1,tar1)
