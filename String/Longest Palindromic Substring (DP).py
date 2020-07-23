x = "adsffxfxcdfccccaaacacacacacacaa"

def LCS(x,y):
    m = len(x)
    dp = [[None for i in range(m+1)]for j in range(m+1)]

    for i in range(m+1):
        for j in range(m+1):
            if i==0 or j==0:dp[i][j]=0
            elif x[i-1]==y[j-1]:dp[i][j]=1+dp[i-1][j-1]
            else:dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    i_=j_=0
    for i in range(m+1):
        for j in range(m+1):
            if dp[i][j]>dp[i_][j_]:i_,j_=i,j
    print(i_-dp[i_][j_]+2,i_+1)
    return x[i_-dp[i_][j_]+2:i_+1]
print(LCS(x,x[::-1]))
