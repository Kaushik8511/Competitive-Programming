coin = [2,3,5,10]
change = 1
t = [[-1 for i in range(change+1)]for j in range(len(coin)+1)]

def makeChange(coin,change,n):
        for i in range(n+1):
                for j in range(change+1):
                        if j==0:
                                t[i][j]=1
                        elif i==0:
                                t[i][j]=0
                        elif coin[i-1]<=j:
                                t[i][j]=t[i][j-coin[i-1]]+t[i-1][j]
                        elif coin[i-1]>j:
                                t[i][j]=t[i-1][j]
        return t[n][change]
print(makeChange(coin,change,len(coin)))
