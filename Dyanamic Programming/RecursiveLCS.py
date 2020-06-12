X = "acbcf"
Y = "abcdaf"
m = len(X)
n = len(Y)

def LCS(X,Y,m,n):
        if m==0 or n==0:
                return 0
        elif X[m-1]==Y[n-1]:
                return 1+LCS(X,Y,m-1,n-1)
        else:
                return max(LCS(X,Y,m,n-1),LCS(X,Y,m-1,n))

print(LCS(X,Y,m,n))
