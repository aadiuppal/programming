class Solution:
    # @param s, a string
    # @return a string[]
    def findRepeatedDnaSequences(self, s):
        table={}
        l=[]
        #if len(s)<10:
        #        return []
        for i in range(0,len(s)-9):
            temp=s[i:i+10]
            if table.get(temp) is None:
                table[temp]=0
            else:
                if table[temp]==0:
                    l.append(temp)
                table[temp]+=1
        return l

s=Solution()
st="AAAAAAAAAAA"
print s.findRepeatedDnaSequences(st)
