cut = [2,5,7,9]
profit = [4,7,20,27]
length = 31
t = [[-1 for i in range(length+1)]for j in range(len(cut)+1)]

def rodCut(cut,profit,length,n):
    for i in range(n+1):
        for j in range(length+1):
            if i==0 or j==0:
                t[i][j]=0
            elif cut[i-1]<=j:
                t[i][j]=max(profit[i-1]+t[i][j-cut[i-1]],t[i-1][j])
            elif cut[i-1]>j:
                t[i][j]=t[i-1][j]
    return t[n][length]

print(rodCut(cut,profit,length,len(cut)))

