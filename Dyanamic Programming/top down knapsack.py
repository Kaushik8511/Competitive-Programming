wt = [2,4,4,5]
val = [3,5,5,6]
W = 7
t = [[-1 for i in range(W+1)]for j in range(len(wt)+1)]
def max(a,b):
        if a>b:
                return a
        return b

def topdownKS(wt,val,W,n):
        for i in range(n+1):
                for j in range(W+1):
                        if i==0 or j==0:
                                t[i][j]=0
                        elif wt[i-1]<=j:
                                t[i][j]=max(t[i-1][j],t[i-1][j-wt[i-1]]+val[i-1])
                        elif wt[i-1]>j:
                                t[i][j]=t[i-1][j]
        return t[n][W]

print(topdownKS(wt,val,W,len(wt)))
for i in t:
        print(i)
