class Solution:
	def __init__(self):
		self.table=[]
	def makechange(self,n,coins,index):
		if index>len(coins)-1:
			return 1
		ways=0
		#if len(coins)==1:
		#	return 1
		l=n/coins[index]
		for i in range(0,l+1):
			ways+=self.makechange(n-(i*coins[index]),coins,index+1)
		return ways
	def change(self,cent):
		denoms=[3,2,1]
		return self.makechange(cent,denoms,0)

s=Solution()
print "4: ",s.change(4)
print "100: ",s.change(100)
