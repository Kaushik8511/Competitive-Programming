X = "kaushik"
Y = "prajapati"
m = len(X)
n = len(Y)

def printSCS(X,Y,m,n):
        t = [[-1 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
                for j in range(n+1):
                        if i==0 or j==0:
                                t[i][j]=0
                        elif X[i-1]==Y[j-1]:
                                t[i][j]=1+t[i-1][j-1]
                        else:
                                t[i][j]=max(t[i-1][j],t[i][j-1])
        i = m
        j = n
        s=""
        while(i>0 and j>0):
                if X[i-1]==Y[j-1]:
                        s+=X[i-1]
                        i-=1
                        j-=1
                elif t[i][j-1]>t[i-1][j]:
                        s+=Y[j-1]
                        j-=1
                else:
                        s+=X[i-1]
                        i-=1
        while i>0:
                s+=X[i-1]
                i-=1
        while j>0:
                s+=Y[j-1]
                j-=1
        return (s[::-1])

print(printSCS(X,Y,m,n))
                        
