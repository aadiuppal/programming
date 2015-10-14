import copy
class Nqueens:
    def __init__(self):
        self.cols = []
        self.rows = []
    def solve(self,n):
        for i in range(n):
            self.rows.append(i)
            self.cols.append(i)
        result = []
        self.solution(0,[],result)
        return self.printer(result)
    def solution(self,row,curr,result):
        for c in range(len(self.cols)):
            if self.check(row,c,curr):
                curr.append([row,c])
                if len(curr) == len(self.rows):
                    #result.append(copy.deepcopy(curr))
                    result += [tuple(curr)]
                else:
                    self.solution(row+1,curr,result)
                curr.pop()
    def check(self,r,c,curr):
        for i in curr:
            if i[0] == r:
                return False
            if i[1] == c:
                return False
            if abs(r-i[0]) == abs(c-i[1]):
                return False
        return True
    def printer(self,result):
        ans = []
        for r in result:
            res = ["" for x in range(len(r))]
            for i in r:
                for j in range(len(r)):
                    if j != i[1]:
                        res[i[0]] += "."
                    else:
                        res[i[0]] += "Q"
            ans.append(res)
        return ans
q=Nqueens()
print q.solve(4)
