def roatatImage(matrix):
    #1 2 3 4        temp- 1 2 3 4
    #5 6 7 8        1 2 3 4 -> 13 9 5 1
    #9 10 11 12
    #13 14 15 16
    #
    n=len(matrix)
    i=0
    i_end=n-1
    j=0
    j_end=n-1
    temp=matrix[0][:-1]
    temp_new=[]
    while i<i_end and j<j_end:#condition:
        #check val at prev iter
        #for 1st iter temp is already assigned
        temp=matrix[i][j:j_end]
        for i_iter in range(i,i_end):
            temp_new.append(matrix[i_iter][j_end])
            matrix[i_iter][j_end]=temp[i_iter-i]
        #now reload temp
        temp=temp_new
        temp_new=[]
        for j_iter in range(j_end,j,-1):
            temp_new.append(matrix[i_end][j_iter])
            matrix[i_end][j_iter]=temp[j_end-j_iter]
        temp=temp_new
        temp_new=[]
        for i_iter in range(i_end,i,-1):
            temp_new.append(matrix[i_iter][j])
            matrix[i_iter][j]=temp[i_end-i_iter]
        temp=temp_new
        temp_new=[]
        for j_iter in range(j,j_end):
            temp_new.append(matrix[i][j_iter])
            matrix[i][j_iter]=temp[j_iter-j]
        j+=1
        i+=1
        j_end-=1
        i_end-=1
        temp=temp_new[1:-1]
        temp_new=[]
    return matrix

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
m=roatatImage(matrix)
for i in range(len(m)):
    print m[i]
