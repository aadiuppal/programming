class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        prev_max=0
        sum=0
        for i in range(0,len(A)):
            qty=max(A[i],prev_max)
            if qty-A[i]>0:
                sum=sum+qty-A[i]
            prev_max=qty
        prev_max=0
        sum_back=0
        for i in range(len(A)-1,-1,-1):
            qty=max(A[i],prev_max)
            if qty-A[i]>0:
                sum_back=sum_back+qty-A[i]
            prev_max=qty
        sum_max=0
        if A:
            m=max(A)
        else:
            return 0
        for i in range(0,len(A)):
            sum_max=sum_max+m-A[i]
	    print sum_max
	print "----"
	print m
	print sum
	print sum_back
	print sum_max
        return abs(sum_back+sum-sum_max)



A=[0,1,0,2,1,0,1,3,2,1,2,1]
#B=[1,2,1,2,3,1,0,1,2,0,1,0]
#A=[0,2,0]
#B=[0,2,0]
s=Solution()
print s.trap(A)
