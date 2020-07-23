x = "abcdhr"
y = "bcdhasr"

def LCS(x,y):
        m = len(x)
        n = len(y)

        t = [[-1 for i in range(n+1)]for j in range(m+1)]

        for i in range(m+1):
                for j in range(n+1):
                        if i==0 or j==0:
                                t[i][j]=0
                        elif x[i-1]==y[j-1]:
                                t[i][j] = 1 + t[i-1][j-1]
                        else:
                                t[i][j]=0

        iind = 0
        jind = 0
        for i in range(m+1):
                for j in range(n+1):
                        if t[i][j]>t[iind][jind]:
                                iind,jind = i,j
        if iind==0 and jind==0:
                if X[0]==y[0]:
                        return x[0]
                return ""
        l = t[iind][jind]
        return x[iind-l:iind]
        

print(LCS(x,y))
