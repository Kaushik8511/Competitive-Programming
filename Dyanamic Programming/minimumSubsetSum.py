arr = [4,1,7]
sm = sum(arr)
t=[[-1 for i in range(sm+1)]for j in range(len(arr)+1)]

def subsetSum(arr,sm,n):
        for i in range(n+1):
                for j in range(sm+1):
                        if j==0:
                                t[i][j]=1
                        elif i==0:
                                t[i][j]=0
                        elif arr[i-1]<=j:
                                t[i][j]=t[i-1][j-arr[i-1]]|t[i-1][j]
                        elif arr[i-1]>j:
                                t[i][j]=t[i-1][j]
        for i in range(sm//2,-1,-1):
                if t[n][i]==1:
                        return i
s1 = subsetSum(arr,sm,len(arr))
print(sm-2*s1)
