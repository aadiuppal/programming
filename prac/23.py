class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        if not version1 and not version2:
            return 0
        num1=""
        num2=""
        for i in range(0,len(version1)):
            if version1[i]==".":
                num1=version1[:i]
                v1=version1[i+1:]
                break
        for j in range(0,len(version2)):
            if version2[j]==".":
                num2=version2[:j]
                v2=version2[j+1:]
                break
        if not version1:
            if num2:
                if num2==0 and v2=="":
                    return 0
            if not num2:
                if str(version2)==0:
                    return 0
            return -1
        if not version2:
            if num1:
                if num1==0 and v1=="":
                    return 0
                if not num1:
                    if str(version1)==0:
                        return 0
            return 1
        if not num1 or not num2:
            if not num1:
                num1=version1
                v1=""
            if not num2:
                num2=version2
                v2=""
        if int(num2) >int(num1):
            return -1
        elif int(num1)>int(num2):
            return 1
        elif num1!=version1 or num2!=version2:
            return self.compareVersion(v1,v2)
        else:
            return 0

s=Solution()
v1="1.0"
v2="1"
print s.compareVersion(v1,v2)
