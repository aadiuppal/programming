def nearest(x,y,n):
	list=[]
	list.append([x-n,y])
	list.append([x+n,y])
	list.append([x,y+n])
	list.append([x,y-n])
	for i in range(x-n+1,x+n):
		for j in range(y-n+1,y+n):
			if ((i-x)**2)+((j-y)**2)<=(n**2):
				list.append([i,j])
	return list

print nearest(0,0,3)
