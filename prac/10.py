def merge_sort(A):
	if len(A)==1:
		return A
	left=[]
	right=[]
	l=len(A)/2
	for i in range(0,l):
		left.append(A[i])
	left=merge_sort(left)
	for i in range(l,len(A)):
		right.append(A[i])
	right=merge_sort(right)
	return merge(left,right)
def merge(left,right):
	A=[]
	i=0
	j=0
	while 1:
		if i<len(left) or j<len(right):
			if i<len(left):
				if j<len(right):
					if  left[i]<right[j]:
						A.append(left[i])
						i+=1
					else:
						A.append(right[j])
						j+=1
				else:
					A.append(left[i])
					i+=1
			else:
				A.append(right[j])
				j+=1
		else:
			return A

def quick_sort(A,l,h):
	if l<h:
		p=partition(A,l,h)
		quick_sort(A,l,p-1)
		quick_sort(A,p+1,h)

def partition(A,l,h):
	pivot=h
	swap_i=l
	for i in range(0,len(A)):
		if A[i]<A[pivot]:
			temp=A[i]
			A[i]=A[swap_i]
			A[swap_i]=temp
			swap_i+=1
	temp=A[swap_i]
	A[swap_i]=A[pivot]
	A[pivot]=temp
	return swap_i


	

A=[2,1,4,3]
print A
print merge_sort(A)
print A
quick_sort(A,0,3)
print A 
