class Solution:
    # @param {string} s
    # @return {string}
    def __init__(self):
        self.table={}
        self.max=0
	self.max_table={}
    def longestPalindrome(self, s):
	if len(s)<=2:
		return s
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                self.check(s[i:j])
	self.max=max(self.max_table.keys())
        return self.max_table[self.max]
    
    def check(self,s):
        if len(s)<1:
            return
        i=0
        j=len(s)-1
        if i==j:
            return True
        if j-i==2:
            if s[i]==s[j]:
		self.table[s[i:j+1]]=True
		self.max_table[len(s[i:j+1])]=s[i:j+1]
                return True
            self.table[s[i:j+1]]= False
	    return False
        if j-i==1:
            return False
        if i<j:
            if s[i]==s[j]:
		if s[i:j+1] not in self.table.keys():
			self.table[s[i:j+1]]=self.check(s[i+1:j])
			if self.table[s[i:j+1]]==True:
				self.max_table[len(s[i:j+1])]=s[i:j+1]
		return self.table[s[i:j+1]]
            else:
		if s[i+1:j+1] not in self.table.keys():
	                self.table[s[i+1:j+1]]=self.check(s[i+1:j+1])
		if s[i:j] not in self.table.keys():
	                self.table[s[i:j]]=self.check(s[i:j])
	return False
s=Solution()
ss=["a","bb"]
for i in ss:
	print s.check(i)
	print s.longestPalindrome(i)
print s.table
print
print
print s.max_table

print s.longestPalindrome("ccc")
