class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
	print dict
        res = []
        for item in dict:
	    if len(dict[item]) >= 2:
           	 res += dict[item]
	    print res
        return res

s=Solution()
strs=["asd","bat","dsa","tab","qwe"]
print s.anagrams(strs)
