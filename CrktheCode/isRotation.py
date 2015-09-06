def isRotation(s1,s2):
    s1+=s1
    return isSubstring(s1,s2)

def isSubstring(s1,s2):
    l_small=min(len(s1),len(s2))
    l_hi=max(len(s1),len(s2))
    if l_small==len(s1):
        s_small=s1
        s_hi=s2
    else:
        s_small=s2
        s_hi=s1
    for i in range(l_small,l_hi):
        if s_hi[i-l_small:i]==s_small:
            return True
    return False

s1="waterbottle"
s2="bottlewater"
print isRotation(s1,s2)
