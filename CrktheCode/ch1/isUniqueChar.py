def isUniqueChar(string):
    table=[0]*256
    for i in string:
        if table[ord(i)]>0:
            return False
        table[ord(i)]+=1
    return True


def isUniqueChar1(string):
    for i in range(len(string)-1):
        for j in range(i+1,len(string)):
            if string[i]==string[j]:
                return False
    return True

print isUniqueChar("asdasdfafd")
print isUniqueChar("asdqwruoim zx")
print isUniqueChar("asdlkjhfgoiuqweymnmzq")
print isUniqueChar1("asdasdfafd")
print isUniqueChar1("asdqwruoim zx")
print isUniqueChar1("asdlkjhfgoiuqweymnmzq")
