def fib(n):
	val=1
	prev_val=0
	i=1

	while i<=n:
		print val,
		temp=val
		val+=prev_val
		i+=1
		prev_val=temp

def fib_rec(n):
	if n<=1:
		return 1
	return fib_rec(n-1)+fib_rec(n-2)

fib(5)
print 
for i in range(0,5):
	print fib_rec(i),

