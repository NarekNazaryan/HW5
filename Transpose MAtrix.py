def Transpose(matrix):
    row=len(matrix)
    col=len(matrix[0])
    A=[]
    for i in range(col):
        A.append([0 for k in range(row)])
    for i in range(col):
        for j in range(row):
            A[i][j]=matrix[j][i]
    return A
print(Transpose( [[1,2,3],[4,5,6],[7,8,9]]))