def fraction(num,den):
	res=""
	if num/den<0:
		res+="-"
	if num%den==0:
		return str(num/den)
	res+=str(num/den)
	res+="."
	num%=den
	i=len(res)
	j=len(res)
	table={}
	while num!=0:
		if num not in table.keys():
			table[num]=i
		else:
			i=table[num]
			res=res[:i]+"("+res[i:]+")"
			return res
		num*=10
		res+=str(num/den)
		num%=den
		i+=1
	if j==len(res):
		return res[:-1]
	return res
