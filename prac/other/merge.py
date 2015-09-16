def merge_sort(x):
    l=len(x)
    if l==1:
        return x
    s1=merge_sort(x[:l/2])
    s2=merge_sort(x[l/2:])
    t=merge(s1,s2)
    print t
    return t

def merge(s1,s2):
    i,j=0,0
    s=[]
    while i<len(s1) and j<len(s2):
        if s1[i]<s2[j]:
            s.append(s1[i])
            i+=1
        else:
            s.append(s2[j])
            j+=1
    if i!=len(s1):
        s+=s1[i:]
    if j!=len(s2):
        s+=s2[j:]
    return s

print merge_sort([2,1,2,7,6,8,3,4,5])

