def table(n):
	for i in range(1,n+1):
		for j in range(1,n+1):
			print '{0:4}'.format(i*j),
		print

n=12
table(n)
