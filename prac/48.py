def pow(x, n):
	res=1
	if x<0 and n%2!=0:
		sign=-1
	else:
		sign=1
	if x<0:
		x=-x
	result=1
	prev_result=x
	while n!=0:
		if n%2!=0:
			print "n,rsult",n,result
			result=x*result
		print "n,x",n,x
		x=x*x
   		n=n/2
	
        return result


print pow(2,5)
