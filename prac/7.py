class Solution:
	def number_freq(self,A,n):
		list=[]
		for i in range(0,max(A)+1):
			list.append([])
		max_a=max(A)+1
		for i in A:
			list[self.hash(i,max_a)].append(i)
		out=[]
		for i in list:
			if len(i)>=n:
				out.append(i[0])
		return out
		
	def hash(self,num,max_num):
		return num%max_num

A=[0,0,100,3,5,4,6,4,2,100,2,100]
s=Solution()
print s.number_freq(A,2)
