class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        arr=[]
        p=[]
        if n<=1:
            return 0
        for i in range(2,n+1):
            arr.append(i)
        
        while arr!=[]:
            i=0
            t=arr[0]
	    print arr
            while len(arr)>0 and arr[i]!=arr[-1]:
		print i
                p.append(t)
                if arr[i]%t==0:
                    del arr[i]
                i+=1
	    print t,arr,p
            if arr[-1]%t==0:
                del arr[-1]
	print p
        return len(p)

s=Solution()
print s.countPrimes(3)
