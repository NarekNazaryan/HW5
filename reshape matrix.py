 def matrixReshape(matrix, r, c):
        m = len(mat[0])
        n=len(matrix)
        if r*c != m*n:
            return matrix
        else:
            k = 0
            v = 0
            ans=[]

            for i in range(r):
                ans.append([])
                for j in range(c):
                    ans[i].append(0)
            for i in range(n):
                for j in range(m):
                    ans[k][v] = mat[i][j]
                    v += 1
                    if v == c:
                        v = 0
                        k += 1
        return ans