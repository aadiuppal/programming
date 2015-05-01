def str_sub(str1,str2):
	for i in range(0,len(str1)):
		noMatch=False
		for j in range(0,len(str2)):
			if i+j>=len(str1):
				noMatch=True
				break
			if str1[i+j]!=str2[j]:
				noMatch=True
				break
		if not noMatch:
			return True
	return False

s2="ateaa"
s1="abatea"
print str_sub(s1,s2)
