import sys
coin = [2,3,5,10]
change = 11
t = [[-1 for i in range(change+1)]for j in range(len(coin)+1)]

def makeChange(coin,change,n):
        for i in range(n+1):
                for j in range(change+1):
                        if i==0:
                                t[i][j]=sys.maxsize-3
                        elif j==0:
                                t[i][j]=0
                        elif i==1:
                                if j%coin[0]==0:
                                        t[i][j]=j//coin[0]
                                else:
                                        t[i][j]=sys.maxsize-3
                        elif coin[i-1]<=j:
                                t[i][j]=min(t[i][j-coin[i-1]]+1,t[i-1][j])
                        elif coin[i-1]>j:
                                t[i][j]=t[i-1][j]
        return t[n][change]
print(makeChange(coin,change,len(coin)))
