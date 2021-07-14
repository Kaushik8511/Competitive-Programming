def fun(petrol,sm):
    n = len(petrol)
    dp = [[None for _ in range(sm+1)]for i in range(n+1)]

    for i in range(n+1):
        for j in range(sm+1):
            if j==0:dp[i][j]=True
            elif i==0:dp[i][j]=False
            elif petrol[i-1]<=j:dp[i][j] = dp[i-1][j-petrol[i-1]] or dp[i-1][j]
            else:dp[i][j]=dp[i-1][j]
    for i in range(sm,-1,-1):
        if dp[-1][i]:return i


def solve(petrol):
    sm = sum(petrol)
    min_sum = fun(petrol,sm//2)
    print(sm-min_sum)


petrol_pump = list(map(int,input().split()))
solve(petrol_pump)
