wt = [2,3,4,5]
val = [3,4,5,7]
W = 7
t = [[-1 for i in range(W+1)]for j in range(len(wt)+1)]


def memoized(wt,val,W,n):
        if n==0 or W==0:
                t[n][W]=0
                return t[n][W]
        if t[n][W] != -1:
                return t[n][W]
        if (wt[n-1]<=W):
                t[n][W]=max(memoized(wt,val,W-wt[n-1],n-1)+val[n-1],memoized(wt,val,W,n-1))
                return t[n][W]
        if (wt[n-1]>W):
                t[n][W]=memoized(wt,val,W,n-1)
                return t[n][W]
print(memoized(wt,val,W,len(wt)))
for i in t:
        print(i)

    
