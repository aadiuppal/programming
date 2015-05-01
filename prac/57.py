class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        p=""
        i=0
        temp=""
        j=[0]
        while i<len(path):
            temp+=path[i]
            if path[i]=="/" or i==len(path)-1:
		if i!=len(path)-1:
	                temp=temp[:-1]
                if temp==".." :
                   if len(j)<2:
                       p=p[:j[-1]]
                   else:
                       p=p[:j[-2]]
                       j.pop()
                   i+=1
                elif temp==".":
                    i+=1
                    temp=""
                    continue
                else:
                    if i==len(path)-1 or temp=="":
                        p+=temp
                        i+=1
                    else:
                        p+=temp+"/"
                        j.append(len(p))
                        i+=1
                temp=""
            else:
                i+=1
        if len(p)<1 or p[0]!='/':
            p="/"+p
        return p

s=Solution()
p="/..."#/a/../b/c/d/.././" 
print s.simplifyPath(p)
