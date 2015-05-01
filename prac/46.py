class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        list=[]
        if len(num)==1:
                return [num]
        set=self.permute(num[1:])
        for i in range(0,len(set)):
	    l=len(set[i])
            for j in range(0,l):
		temp=set[i][j]
                set[i][j]=num[0]
		list.append(set[i]+[temp])
		set[i][j]=temp
	    list.append(set[i]+[num[0]])
        return list 

num=[6,3,2,7,4,-1]
s=Solution()
print s.permute(num)
