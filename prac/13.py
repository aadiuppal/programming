class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        tup=[]
        if len(num)<=2:
            return
        num=sorted(num)
        for i in range(0,len(num)):
            for j in range(len(num)-1,i,-1):
                if num[i]+num[j]<=0:
                    tup.append([num[i],num[j]])
	print tup
        tup_fin=[]
        for i in range(0,len(num)):
            for j in range(0,len(tup)):
                if num[i]+tup[j][0]+tup[j][1]==0:
                    tup_fin.append([num[i],tup[j][0],tup[j][1]])
	tup_f=[]
	for j in range(0,len(tup_fin)-1):
		if j==0:
			tup_f.append(tup_fin[j])
		if tup_fin[j][0]==tup_fin[j+1][0]:
			if tup_fin[j][1]==tup_fin[j+1][1]:
				if tup_fin[j][2]==tup_fin[j+1][2]:
					continue
				else:
					tup_f.append(tup_fin[j])
	return tup_f


a=[0,0,0]
s=Solution()
print s.threeSum(a)
