class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        result=str(float(numerator)/float(denominator))
	for i in range(0,len(result)):
            if result[i]=='.':
                str_before=result[:i]
                str_after=result[i+1:]
        for i in range(0,len(str_after)):
            if i>0:
                if rep==str_after[i]:
                    count+=1
                if count==4:
                    return str_before+".("+str_after[i]+")"
            rep=str_after[i]
        return result

s=Solution()
print s.fractionToDecimal(1,5)
