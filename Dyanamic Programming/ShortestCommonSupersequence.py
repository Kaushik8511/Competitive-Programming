X = "aggtab"
Y = "gxtxayb"
m = len(X)
n = len(Y)

def LCS(X,Y,m,n):
        t=[[-1 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
                for j in range(n+1):
                        if i==0 or j==0:
                                t[i][j]=0
                        elif X[i-1]==Y[j-1]:
                                t[i][j]=1+t[i-1][j-1]
                        else:
                                t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[m][n]

SCS = m+n-LCS(X,Y,m,n)
print(SCS)
