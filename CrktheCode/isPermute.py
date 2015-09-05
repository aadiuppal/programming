def isPermute(string1,string2):
    temp1=sorted(string1)
    temp2=sorted(string2)
    if temp1==temp2:
        return True
    return False

def isPermute1(string1,string2):
    if len(string1)!=len(string2):
        return False
    table=[0]*256
    for i in string1:
        table[ord(i)]+=1
    for i in string2:
        table[ord(i)]-=1
        if table[ord(i)]<0:
            return False
    return True


print isPermute("adad","ddaa")
print isPermute("adadadfad","adafdqqweq")
print isPermute1("adad","ddaa")
print isPermute1("adadadfad","adafdqqweq")
