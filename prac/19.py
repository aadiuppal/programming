class Solution:
    # @return a string
    def intToRoman(self, num):
        #1=I one
        #5=V fiv
        #10=X ten
        #50=L fif
        #100=C  hun
        #1000=M  tho
        str=""
        tho=num/1000
        num=num%1000
        hun=num/100
        num=num%100
        fif=num/50
        num=num%50
        ten=num/10
        num=num%10
        fiv=num/5
        one=num%5
        for i in range(0,tho):
            str=str+"M"
        for i in range(0,hun):
            str=str+"C"
        for i in range(0,fif):
            str=str+"L"
        for i in range(0,ten):
            str=str+"X"
        for i in range(0,fiv):
            str=str+"V"
        for i in range(0,one):
            str=str+"I"
        return str

s=Solution()
s.
