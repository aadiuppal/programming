class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        tup=[]
        if len(num)<=2:
            return
        num=sorted(num)
	print num
        for i in range(0,len(num)):
            j=i+1
            k=len(num)-1
            while j<k:
       	        sum=num[i]+num[j]+num[k]
               	if sum ==0:
		      if num[i]!=num[i-1]:
		              tup.append([num[i],num[j],num[k]])
               	if sum <0:
                    j+=1	
                else:
                    k-=1
        return tup

a=[-1,0,1,2,-1,-4]
b=[0,0,0]
s=Solution()
print s.threeSum(b)
