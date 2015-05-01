def makeip(s,n):
	if not s:
		return []
	if n==1:
		if int(s)<=255:
			return [s]
		else:
			return []
        ip=""
        l=[]
        for i in range(0,3):
            for p in makeip(s[i+1:],n-1):
                ip=""
		if int(s[:i+1])>255:
			continue
		ip+=s[:i+1]+"."+p
                l.append(ip)
	return l

s="25525511135"
print makeip(s,4)
