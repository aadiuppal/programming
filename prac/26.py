class Solution:
	def __init__(self):
		self.count=0
		self.sum=0
		self.avg=0
	def averg(self,val):
		self.count+=1
		self.sum=self.sum+val
		self.avg=float(self.sum)/self.count
		return self.avg

s=Solution()
a=[1,2,3,4,5,-1,-2,-3,-4,-5]
for i in a:
	print s.averg(i)
