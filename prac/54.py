def rotatestr(str,n):
	while n>=len(str):
		n=n-len(str)
	l=len(str)-1
	last=str[l-n]
	start=str[l-n+1:]
	mid=str[:l-n]
	return start+mid+last

str="abcde"
print rotatestr(str,10)
