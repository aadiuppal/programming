class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        tup=[]
        if len(num)<=2:
            return
        num=sorted(num)
	print num
        i=0
        j=len(num)-1
        for i in range(0,len(num)):
	   p=i+1
	   j=len(num)-1
	   while p<j:
	   	print [num[i],num[p],num[j]]
                if num[i]+num[j]+num[p]==0:
			 if [num[i],num[p],num[j]] not in tup:
	        	 	tup.append([num[i],num[p],num[j]])

	        if num[p]+num[j]+num[i]<0:
          	      p+=1
	  	else:
		      j-=1
		
        return tup

s=Solution()
arr=[-1,0,1,2,-1,-4]
arr1=[-2,0,1,1,2]
print s.threeSum(arr)
