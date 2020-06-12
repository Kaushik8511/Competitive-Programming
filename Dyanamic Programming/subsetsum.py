arr = [2,3,5,7,8,10]
sm = 11
t = [[-1 for i in range(sm+1)]for j in range(len(arr)+1)]

def subsetsum(arr,sm,n):
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
        if t[n][sm]==1:
                return True
        return False

print(subsetsum(arr,sm,len(arr)))
for i in t:
        print(i)
