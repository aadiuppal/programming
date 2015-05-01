def print_matrix(A):
	n=len(A)
	i_min=0
	j_min=0
	i_max=n
	j_max=n
	while i_min<=i_max or j_min<=j_max:
		j=j_min
		for i in range(i_min,i_max):
			print A[j][i]
		i=i_max-1
		for j in range(j_min+1,j_max):
			print A[j][i]
		j=j_max-1
		for i in range(i_max-2,i_min-1,-1):
			print A[j][i]
		for j in range(j_max-2,j_min,-1):
			print A[j][i]
		i_min+=1
		j_min+=1
		i_max-=1
		j_max-=1

A=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print_matrix(A)
