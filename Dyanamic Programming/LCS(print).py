X = "kaushik"
Y = "kuaushiiaaaaaaak"
m = len(X)
n = len(Y)

def printLCS(X,Y,m,n):
        t = [[-1 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
                for j in range(n+1):
                        if i==0 or j==0:
                                t[i][j]=0
                        elif X[i-1]==Y[j-1]:
                                t[i][j]=1+t[i-1][j-1]
                        else:
                                t[i][j]=max(t[i][j-1],t[i-1][j])
        i=m
        j=n
        s=""
        while(i>0 and j>0):
                if X[i-1]==Y[j-1]:
                        s += X[i-1]
                        i-=1
                        j-=1
                elif t[i][j-1]>t[i-1][j]:
                        j-=1
                else:
                        i-=1
        return (s[::-1])
print(printLCS(X,Y,m,n))
