def sieve(n):
    dp = [True for i in range(n+1)]
    i=2
    while i*i<=n:
        if dp[i]:
            for j in range(i*i,n+1,i):dp[j]=False
        i+=1
    prime = []
    for i in range(2,n+1):
        if dp[i]:prime.append(i)
    return prime

print(sieve(100))
