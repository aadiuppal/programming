class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n=len(matrix)
        for i in range(0,n/2):
            temp=[]
	    t=matrix[i][i]
            for j in range(i,n-i):
                temp.append(matrix[i][j])
                matrix[i][j]=matrix[n-j-1][i]
	    matrix[i][n-i-1]=t
	    temp1=[]
	    print "temp",temp
            for j in range(i+1,n-i):
                temp1.append(matrix[j][n-i-1])
                matrix[j][n-i-1]=temp[j-i]
	    temp=[]
	    print "temp1",temp1
            for j in range(i+1,n-i):
                temp.append(matrix[n-i-1][n-j-1])
                matrix[n-i-1][n-j-1]=temp1[j-i-1]
	    temp1=[]
	    print "temp",temp
            for j in range(i+1,n-i-1):
                temp1.append(matrix[n-j-1][i])
                matrix[n-j-1][i]=temp[j-i-1]
	    print "temp1",temp1
s=Solution()
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print mat
s.rotate(mat)
print mat
