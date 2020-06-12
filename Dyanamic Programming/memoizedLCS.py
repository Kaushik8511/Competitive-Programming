X = "acbcf"
Y = "abcdaf"
m = len(X)
n = len(Y)
t = [[-1 for i in range(n+1)]for j in range(m+1)]

def memLCS(X,Y,m,n):
        if m==0 or n==0:
                t[m][n]=0
                return t[m][n]
        if t[m][n] != -1:
                return t[m][n]
        if X[m-1]==Y[n-1]:
                t[m][n]=1+memLCS(X,Y,m-1,n-1)
        else:
                t[m][n]=max(memLCS(X,Y,m,n-1),memLCS(X,Y,m-1,n))
        return t[m][n]

print(memLCS(X,Y,m,n))
for i in t:
        print(i)
