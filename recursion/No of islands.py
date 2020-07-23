a = [[1,1,0,1],
     [0,0,1,0],
     [1,1,0,0],
     [0,0,1,1]]

def visit(A,i,j):
        if i<0 or j<0 or i>=len(A) or j>=len(A[0]) or A[i][j]==0:
                return 0

        A[i][j]=0
        visit(A,i,j+1)
        visit(A,i,j-1)
        visit(A,i+1,j)
        visit(A,i-1,j)

        return 1


def islands(A):
        res = 0
        n = len(A)
        m = len(A[0])
        for i in range(n):
                for j in range(m):
                        if A[i][j]==1:
                                res+=1
                                visit(A,i,j)
        return res

print(islands(a))
print(a)

