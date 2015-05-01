def str_cmp(str1,str2):
	if len(str1)!=len(str2):
		return False
	i=0
	noMatch=False
	while i<len(str1) and noMatch==False:
		if str1[i]!=str2[i]:
			noMatch=True
		i+=1
	if noMatch:
		return False
	return True

s1=""
s2=""
print str_cmp(s1,s2)
