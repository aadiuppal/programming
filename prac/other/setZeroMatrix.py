def setzero(matrix):
    n = len(matrix)
    m = len(matrix[0])
    fst = False
    lst = False
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i == 0:
                    fst = True
                    continue
                if j == 0:
                    lst= True
                    continue
                matrix[i][0] = 0
                matrix[0][j] = 0
    #fst = False
    for i in range(n):
        if matrix[i][0] == 0:
            if i == 0:
                fst = True
                continue
            for j in range(m):
                matrix[i][j] = 0
    for j in range(m):
        if matrix[0][j] == 0:
            for i in range(n):
                matrix[i][j] = 0
    if fst:
        for j in range(m):
            matrix[0][j] = 0
    if lst:
        for i in range(n):
            matrix[i][0] = 0

arr = [ [1,0,3,4],
        [6,8,0,9],
        [7,1,1,1],
        [5,5,3,4]]
setzero(arr)
for i in arr:
    print i
