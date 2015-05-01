class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_length=0
        length=0
        table=[]
        for i in range(0,256):
            table.append([0,0,0])
        for i in range(0,len(s)):
            if table[ord(s[i])][0]==1:
                if max_length<length:
                    max_length=length#update max_len
                if table[ord(s[i])][1]<length and length-table[ord(s[i])][1]<i-table[ord(s[i])][2]:
		    print table[ord(s[i])][1]
		    print s[i]
		    print length
                    length=length-table[ord(s[i])][1]#reset len
		else:
		    length=0
                for j in range(0,256):
                    table[j][0]=0#reset table
            table[ord(s[i])][0]+=1
            length+=1
            table[ord(s[i])][1]=length
	    table[ord(s[i])][2]=i
        if length>max_length:
            max_length=length
        return max_length

s=Solution()
a="vqblqcb"
print s.lengthOfLongestSubstring(a)
