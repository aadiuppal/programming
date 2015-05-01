class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        j=[]
        n=len(s)-1
        for i in range(0,len(s)/2):
            temp=s[i]
            s=s[:i]+s[n-i]+s[i+1:]
            s=s[:n-i]+temp+s[n-i+1:]
	print s
        for i in range(0,len(s)):
            if s[i]==" ":
                j.append(i)
        for i in range(0,len(j)):
            if i==0:
                s=self.reverseWords(s[:j[i]])+s[j[i]:]
            else:
                s=s[:j[i-1]+1]+self.reverseWords(s[j[i-1]+1:j[i]])+s[j[i]:]
	if j!=[]:
		s=s[:j[-1]+1]+self.reverseWords(s[j[-1]+1:])
	if len(s)>0:
		if s[-1]==" ":
			s=s[:-1]
        return s

s=Solution()
st=" 1"
t= s.reverseWords(st)
print t,len(t)
