def replaceSpace(string,length):
    space=0
    for i in range(length):
        if string[i]==" ":
            space+=1
    newlen=length+(space*2)
    newlen-=1
    length-=1
    while newlen>=0:
        print string
        if string[length]!=" ":
            string=string[:newlen]+string[length]+string[newlen+1:]
            newlen-=1
            length-=1
        else:
            string=string[:newlen]+"0"+string[newlen+1:]
            string=string[:newlen-1]+"2"+string[newlen-1+1:]
            string=string[:newlen-2]+"%"+string[newlen-2+1:]
            newlen-=3
            length-=1
    return string

print replaceSpace("asd asd  fds      ",12)
