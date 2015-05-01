class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        tup=[]
        num=sorted(num)
        if len(num)<4:
            return []
        for i in range(0,len(num)):
            if num[i]>target/4.0:
                break
            if i>0 and num[i]==num[i-1]:
                continue
            for j in range(i+1,len(num)):
                p=j+1
                q=len(num)-1
                while p<q:
                    if num[i]+num[j]+num[p]+num[q]==target:
                        #if num[i]+num[j]+num[p]+num[q] not in tup:
                        tup.append([num[i],num[j],num[p],num[q]])
                    if num[p]+num[q]+num[i]+num[j]>target:
                        q-=1
                    else:
                        p+=1
        return tup

s=Solution()
num=[0,0,0,0]
tar=0
print s.fourSum(num,tar)
