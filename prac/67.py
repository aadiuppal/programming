class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_length=0
        length=0
	start=0
        usedchar={}
        for i in range(len(s)):
	    print usedchar,max_length
            if s[i] in usedchar.keys() and usedchar[s[i]][-1]>start:
                length=i-usedchar[s[i]][-1]
                usedchar[s[i]].append(i)
		start=i		
            else:
                usedchar[s[i]]=[i]
                length+=1
            if length>max_length:
                max_length=length
        return max_length

s=Solution()
st="abba"
print s.lengthOfLongestSubstring(st)
