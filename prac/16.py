class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        m=3*max(num)+1
        val=0
        num=sorted(num)
        for i in range(0,len(num)):
            j=i+1
            k=len(num)-1
            while j<k:
                sum=num[i]+num[j]+num[k]
		print sum
                if sum-target==0:
                    return sum
                diff=abs(sum-target)
		print "!!!"
		print m
		print diff
	        if m>diff:
                        m=diff
                        val=sum
                if sum <=target:
                    j+=1
                else:
                    k-=1
        return val

s=Solution()
a=[1,1,1,1]
print s.threeSumClosest(a,-100)
