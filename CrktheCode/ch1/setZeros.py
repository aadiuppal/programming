def setZeroes(matrix):
    m=len(matrix)
    n=len(matrix[0])
    rows=[]
    cols=[]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rows.append(i)
                cols.append(j)
    for i in rows:
        matrix[i]=[0]*n
    for j in cols:
        for i in range(m):
            matrix[i][j]=0
    return matrix



matrix=[[1,2,3,4],
        [5,0,6,7],
        [8,9,0,10],
        [11,12,13,14]]
m = setZeroes(matrix)
for i in m:
    print i
