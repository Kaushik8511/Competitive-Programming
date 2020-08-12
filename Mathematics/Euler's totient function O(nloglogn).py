n = 20
dp = [i for i in range(n+1)]
for i in range(2,n+1):
    if dp[i]==i:
        for j in range(i,n+1,i):
            dp[j]-=(dp[j]//i)
for i in range(1,n+1):print(dp[i],end=" ")
