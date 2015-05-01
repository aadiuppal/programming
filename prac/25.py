def tower_of_hanoi(n,source,helper,target):

	if n>0:	
		tower_of_hanoi(n-1,source,target,helper)
	
		if source:
			target.append(source.pop())
		tower_of_hanoi(n-1,helper,source,target)


source=[4,3,2,1]
helper=[]
target=[]
tower_of_hanoi(len(source),source,helper,target)
print source,helper,target
