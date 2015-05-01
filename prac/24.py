class Solution:
# @return a string
	def fractionToDecimal(self, numerator, denominator):
	    res=""
	    if numerator/denominator<0:
	        res+="-"
	    elif numerator%denominator==0:
	        return str(numerator/denominator)
	    numerator=abs(numerator)
	    denominator=abs(denominator)
	    res+=str(numerator/denominator)
	    res+="."
	    numerator%=denominator
	    i=len(res)
	
	    table={}
	    while numerator!=0:
        	if numerator not in table.keys():
	            table[numerator]=i
	        else:
		    print table
	            i=table[numerator]
	            res=res[:i]+"("+res[i:]+")"
	            return res
	        numerator=numerator*10
	        res+=str(numerator/denominator)
		print res
	        numerator%=denominator
	        i+=1
	    if i==len(res):
		return res[:-1]
	    return res

s=Solution()
num=1
den=5
print s.fractionToDecimal(num,den)
