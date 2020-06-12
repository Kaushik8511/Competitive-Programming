wt = [2,7,10,20]
val = [4,15,23,50]
W = 59
t = [[-1 for i in range(W+1)]for j in range(len(wt)+1)]

def UnboundedKnapsack(wt,val,W,n):
        for i in range(n+1):
                for j in range(W+1):
                        if i==0 or j==0:
                                t[i][j]=0
                        elif wt[i-1]<=j:
                                t[i][j]=max(t[i][j-wt[i-1]]+val[i-1],t[i-1][j])
                        elif wt[i-1]>j:
                                t[i][j]=t[i-1][j]
        return t[n][W]

print(UnboundedKnapsack(wt,val,W,len(wt)))
