def atoi(num):
	mul=1
	if num[0]=='-':
		mul=-1
		num=num[1:]
	sum=0
	l=len(num)
	for i in range(0,l):
		sum+=(ord(num[i])-ord('0'))*(10**(l-1-i))
	return sum*mul

def merge_sort(arr):
	if len(arr)<=1:
		return arr
	mid=(len(arr))/2
	f_half=merge_sort(arr[:mid])
	s_half=merge_sort(arr[mid:])
	return merge(f_half,s_half)

def merge(arr1,arr2):
	i=0
	j=0
	new_arr=[]
	while i<len(arr1) and j<len(arr2):
		if arr1[i]<arr2[j]:
			new_arr.append(arr1[i])
			i+=1
		else:
			new_arr.append(arr2[j])
			j+=1
	if i>=len(arr1):
		if j<len(arr2):
			new_arr+=arr2[j:]
	if j>=len(arr2):
		if i<len(arr1):
			new_arr+=arr1[i:]
	return new_arr

num1="123"
num2="-123"
print atoi(num1)
print atoi(num2)
arr=[5,3,2,1,6]
print merge_sort(arr)
