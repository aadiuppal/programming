def compressStr(string):
    curr=None
    new_str=""
    count=0
    for i in string:
        if not curr or curr==i:
            count+=1
            curr=i
        else:
            new_str+=curr+str(count)
            curr=i
            count=1
    new_str+=curr+str(count)
    if len(new_str)>=len(string):
        print new_str
        return string
    return new_str

print compressStr("adsasdfsafasfaaaaaaaaaaaaa")
print compressStr("aaaaaaaaaaaaaa")
