arr = [4,8]

def subsetsum(arr,sm,n):
        t = [[-1 for i in range(sm+1)]for j in range(n+1)]
        for i in range(n+1):
                for j in range(sm+1):
                        if j==0:
                                t[i][j]=1
                        elif i==0:
                                t[i][j]=0
                        elif arr[i-1]<=j:
                                t[i][j]=t[i-1][j-arr[i-1]] | t[i-1][j]
                        elif arr[i-1]>j:
                                t[i][j]=t[i-1][j]
        if t[n][sm]==1:
                return True
        return False

def equalSum(arr):
        sm = sum(arr)
        if (sm & 1) == 1:
                return False
        else:
                return subsetsum(arr,sm//2,len(arr))

print(equalSum(arr))
