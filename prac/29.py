def permute_check1(str1,str2):
	if len(str1)!=len(str2):
		return False
	str1=sorted(str1)
	str2=sorted(str2)
	i=0
	noMatch=False
	while i<len(str1):
		if str1[i]!=str2[i]:
			noMatch=True
			break
		i+=1
	if noMatch:
		return False
	return True

def permute_check2(str1,str2):
	table=[]
	noMatch=False
	for i in range(0,256):
		table.append(0)
	for i in range(0,len(str1)):
		table[ord(str1[i])]+=1
	new_table=[]
	for i in range(0,256):
		new_table.append(0)
	for i in range(0,len(str2)):
		new_table[ord(str2[i])]+=1
	for i in range(0,256):
		if table[i]!=new_table[i]:
			noMatch=True
			break
	if noMatch:
		return False
	return True

s1="asd"
s2="daa"
print permute_check1(s1,s2)
print permute_check2(s1,s2)
