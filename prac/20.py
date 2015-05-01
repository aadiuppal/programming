def permute_string(str):
	if len(str)==0:
		return ['']
	print str
	list1=permute_string(str[1:])
	list2=[]
	for i in range(0,len(list1)):
		for j in range(0,len(str)):
			str_new=list1[i][0:j]+str[0]+list1[i][j:]
			if str_new not in list2:
				list2.append(str_new)
	return list2

s="aabc"
print permute_string(s)
