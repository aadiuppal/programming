def largestNumber(num):
    return str(int("".join(sorted(map(str,num), key=lambda x:1-float(x)/(10**len(x)-1)))))

n=[1,2,3,9,30,22,991]
print largestNumber(n)
