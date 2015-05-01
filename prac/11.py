class Solution():
	def ques11_1(self,A,B):
		a=len(A)-len(B)-1
		b=len(B)-1
		i=len(A)-1
		while a>=0 and b>=0:
			if A[a]>B[b]:
				A[i]=A[a]
				i-=1
				a-=1
			else:
				A[i]=B[b]
				i-=1
				b-=1
		while b>=0:
			A[i]=B[b]
			b-=1
			i-=1

	def ques11_2(self,arr):
		store=[]
		for i in range(0,10):
			store.append([])
		for i in arr:
			val=self.hash(i)
			print val
			store[val].append(i)
		arr_index=0
		for i in range(0,10):
			if store[i]!=[]:
				for j in range(0,len(store[i])):
					arr[arr_index]=store[i][j]
					arr_index+=1
	def hash(self,str):
		sum=0
		for i in str:
			sum=sum+ord(i)
		return sum%10

s=Solution()
A=[3,21,32,45,0,0,0]
B=[1,12,25]
s.ques11_1(A,B)
print A
arr=["asd","bca","dsa"]
s.ques11_2(arr)
print arr
