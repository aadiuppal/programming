class Solution:
    # @param digits, a string
    # @return a string[]
    def letterCombinations(self, digits):
        l={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        ans=[]
        if len(digits)<1:
            return 
        s=l[int(digits[0])]
        if len(digits)==1:
            for i in range(0,len(s)):
                ans.append(s[i])
            return ans
        for i in range(0,len(s)):
            temp=self.letterCombinations(digits[1:])
            for j in range(0,len(temp)):
                ans.append(s[i]+temp[j])
        return ans

s=Solution()
d="23"
print s.letterCombinations(d)
