def subsets(arr):
	list=[]
	if len(arr)==1:
		return [arr,[]]
	set=subsets(arr[1:])
	for i in range(0,len(set)):
		list.append(set[i])
		list.append(set[i]+[arr[0]])
	for i in range(0,len(list)):
		list[i]=sorted(list[i])
	return list

arr=[1,2,3]
s=subsets(arr)
print s
print len(s)
