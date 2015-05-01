class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words=[]
        temp=""
        for i in range(0,len(s)):
            if s[i]==" ":
                if temp:
                    words.append(temp)
		temp=""
            else:
                temp+=s[i]
	if not temp.isspace():
		if temp:
			words.append(temp)
	print words
        st=""
        for i in range(len(words)-1,-1,-1):
            st+=words[i]+" "
        if len(s)>0:
            st=st[:-1]
        return st

s=Solution()
st="1 "
t= s.reverseWords(st)
print t,len(t)
