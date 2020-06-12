from sys import maxsize
s = "kaushik"
t = [[-1 for i in range(len(s))]for j in range(len(s))]

def ispalindrom(s,i,j):
        while (i<j):
                if s[i]!=s[j]:
                        return False
                i+=1
                j-=1
        return True

def MPP(s,i,j):
        if i>=j:
                t[i][j]=0
                return 0
        if ispalindrom(s,i,j):
                return 0
        if t[i][j]!=-1:
                return t[i][j]
        mn = maxsize
        for k in range(i,j):
                temp = MPP(s,i,k)+MPP(s,k+1,j)+1
                if temp<mn:
                        mn=temp
        t[i][j]=mn
        return t[i][j]

print(MPP(s,0,len(s)-1))
