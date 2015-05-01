class Solution:
	def ques1_1(self,str):
		set=[]
		for i in range(0,256):
			set.append(0)
		for i in str:
			if set[ord(i)] == 1:
				return 0
			set[ord(i)]=1
		return 1
	
	def ques1_2(self,str):
		rev_str=""
		for i in range(len(str)-1,-1,-1):
			rev_str=rev_str+str[i]
		return rev_str

	def ques1_3(self,str1,str2):
		if len(str1)!= len(str2):
			return 0
		str1=sorted(str1)
		str2=sorted(str2)
		if str1 != str2:
			return 0
		return 1

	def ques1_4(self,str):
		for i in range(0,len(str)):
			if str[i]==" ":
				temp=str[i+1:]
				str=str[:i]+"%20"+temp[:len(temp)-2]
		return str

	def ques1_5(self,str1):
		c_str=""
		count=0
		prev=""
		for i in str1:
			if prev and i!=prev:
				c_str=c_str+prev+ str(count)
				count=0
			count+=1
			prev=i
		c_str=c_str+prev+str(count)
		if len(c_str)<len(str1):
			return c_str
		return str1

	def ques1_6(self,A):
		N=len(A)
		B=[]
		for i in range(0,N):
			B.append([])
			for j in range(0,N):
				B[i].append(0)
		for j in range(0,N):
			for i in range(0,N):
				B[i][N-1-j]=A[j][i]
		return B

	def ques1_7(self,A):
		row=[]
		col=[]
		for i in range(0,len(A)):
			row.append(0)
		for i in range(0,len(A[0])):
			col.append(0)
		for i in range(0,len(A)):
			for j in range(0,len(A[0])):
				if A[i][j]==0:
					row[i]=1
					col[j]=1
		for i in range(0,len(A)):
			for j in range(0,len(A[0])):
				if row[i]==1 or col[j]==1:
					A[i][j]=0

	def ques1_8(self,s1,s2):
		if len(s1)==len(s2):
			s1s1=s1+s1
			return 1#isSubstring(s1s1,s2)     check this function not actually implemented
		return 0

s=Solution()
str4="Mr John Smith    "
str5="aabcccccaaa"
print s.ques1_4(str4)
print s.ques1_5(str5)
a=[[1,2],[3,4]]
print a
print s.ques1_6(a)
b=[[1,0,1],[1,1,1],[3,4,5],[0,9,8]]
s.ques1_7(b)
print b
