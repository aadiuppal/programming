class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num1,num2=self.check_sum(num,target)
        tup=()
	i=0
        while i<len(num):
            if num[i]==num1:
                tup=tup+(i+1,)
		i+=1
            elif num[i]==num2 :
                tup=tup+(i+1,)
		i+=1
            elif len(tup)==2:
                return tuple(sorted(tup))
	    else:
		i+=1
	return tuple(sorted(tup))  
        
    def check_sum(self,num,target):
        num1=sorted(num)
        l=len(num1)
        i=0
        j=l-1
        while i<j:
            sum=num1[i]+num1[j]
            if sum==target:
                return num1[i],num1[j]
            if sum<target:
                i+=1
            else:
                j-=1
s=Solution()
num=[0,2,4,0]
target=0
print s.twoSum(num,target)
